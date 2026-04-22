"""Phase C — generate English user docs for AetherSDR via the Claude API.

For each topic in topics.json, collects:
  1. The matching UI catalog entries (applets/dialogs/panels touched).
  2. The navigation catalog (for menu paths and applet-panel layout).
  3. Relevant source-code snippets pulled from the entry's source_files.

Then calls Claude with a strict markdown template and writes the result to
the topic's output_path inside the English docs repo.

Requires:
  - ANTHROPIC_API_KEY in the environment
  - `pip install anthropic`

Usage:
  python generate_docs.py                 # generate everything new
  python generate_docs.py --limit 5       # just 5 topics (smoke test)
  python generate_docs.py --only tci      # only topic IDs containing 'tci'
  python generate_docs.py --force         # regenerate even if file exists
  python generate_docs.py --model sonnet  # sonnet (default) | opus | haiku

Resume-safe: skips any topic whose output file already exists (unless --force).
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Any

def _require_anthropic():
    try:
        import anthropic  # noqa: F401
        return anthropic
    except ImportError:
        print("ERROR: run `pip install anthropic` first.", file=sys.stderr)
        sys.exit(1)


HERE = Path(__file__).parent
CATALOG_DIR = HERE / "catalog"
TOPICS_FILE = HERE / "topics.json"
DOCS_ROOT = HERE.parent / "docs"  # MkDocs docs/ subfolder of the English repo
SOURCE_ROOT = Path(r"C:\Users\lu5dx\Documents\Codigo\AetherSDR")

MODEL_IDS = {
    "sonnet": "claude-sonnet-4-6",
    "opus": "claude-opus-4-7",
    "haiku": "claude-haiku-4-5-20251001",
}

MAX_SOURCE_CHARS = 12000  # per topic — keep prompts lean

SYSTEM_PROMPT = """You are a senior technical writer producing the official AetherSDR user manual.

AetherSDR is a Qt6 Linux-native SmartSDR-compatible client for FlexRadio FLEX-8600 radios. The target radio firmware is 4.1.5 speaking SmartSDR protocol v1.4.0.0. The application runs on Linux, macOS, and Windows.

Your readers are amateur radio operators. They know ham radio concepts (VFO, SSB, CW, bandwidth, panadapter) but may be new to AetherSDR's specific UI. They want to do one thing, quickly, and need the exact clicks.

## Hard rules

1. **Follow the template exactly.** Use the section headings provided. Skip sections only if there is literally nothing to say (e.g. no troubleshooting).
2. **Ground every instruction in the supplied UI catalog and source snippets.** If a detail isn't there, don't invent it — say "see <related page>" or omit.
3. **Use exact labels.** If the code sets a button label to "Enable", write "Enable", not "the enable button" or "Enable button".
4. **Menu paths use `>`:** `Settings > Autostart TCI with AetherSDR`. Buttons in the Applet Panel tray are called "tray buttons" (RX, TX, TCI, etc.).
5. **Keep steps imperative and short.** "Click Enable." not "You should click the Enable button to turn it on."
6. **Pin down values.** Defaults, valid ranges, units — pull them from the catalog when present.
7. **Write in plain English.** No marketing voice. No emojis. No exclamation marks.
8. **Settings keys go in backticks:** `TciPort`, `MqttHost`. These are AetherSDR's persisted AppSettings keys.
9. **Code blocks for literal values, paths, or commands only.**
10. **Do not reference code structure** (class names, signals/slots, C++ headers). Write for users, not developers.

## Template

```markdown
# <Title as given>

<One or two sentences stating what this page helps the user do, and why they'd want to.>

## Before you start

- <Prerequisite 1>
- <Prerequisite 2>

## Steps

1. <First action. Use exact menu paths and button labels.>
2. <Second action.>
3. <...>

## What each control does

<For task pages that are about a single feature — table or bullet list describing every related control, its default, valid range, and the persisted setting key.>

## Tips

- <Practical tip grounded in behavior from the source.>

## Troubleshooting

- **<Symptom>** — <cause and fix>

## Related

- [<Other topic title>](<relative path or same-folder filename>)
```

Omit `## What each control does`, `## Tips`, `## Troubleshooting`, or `## Related` if there is nothing grounded to say. Never fabricate.

Output ONLY the markdown content, starting with the `# ` header. No preamble, no postamble, no code fences around the whole thing.
"""


# ─── catalog loading ────────────────────────────────────────────────────────

def load_catalog() -> dict[str, Any]:
    """Load and index all four catalog files."""
    nav = json.loads((CATALOG_DIR / "00-navigation.json").read_text(encoding="utf-8"))
    core = json.loads((CATALOG_DIR / "01-applets-core.json").read_text(encoding="utf-8"))
    dsp = json.loads((CATALOG_DIR / "02-applets-dsp.json").read_text(encoding="utf-8"))
    dialogs = json.loads((CATALOG_DIR / "03-dialogs-panels.json").read_text(encoding="utf-8"))

    entries_by_id: dict[str, dict] = {}
    for pack in (core, dsp, dialogs):
        for e in pack.get("entries", []):
            entries_by_id[e["id"]] = e

    return {"nav": nav, "entries_by_id": entries_by_id}


def load_topics() -> list[dict]:
    data = json.loads(TOPICS_FILE.read_text(encoding="utf-8"))
    return data["topics"]


# ─── source snippet extraction ──────────────────────────────────────────────

def gather_source_snippets(entry: dict, budget_chars: int) -> str:
    """Read the entry's source files and concatenate up to a char budget."""
    snippets: list[str] = []
    used = 0
    files = list(entry.get("source_files") or []) + list(entry.get("related_core_files") or [])
    for rel in files:
        if used >= budget_chars:
            break
        path = SOURCE_ROOT / rel.replace("/", os.sep)
        if not path.exists():
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        # Take a leading chunk of each file — enough for the structure
        chunk = text[: max(0, budget_chars - used)]
        snippets.append(f"--- {rel} ({len(text)} chars total) ---\n{chunk}")
        used += len(chunk)
    return "\n\n".join(snippets)


# ─── prompt assembly ────────────────────────────────────────────────────────

def compute_siblings(topic: dict, all_topics: list[dict]) -> list[dict]:
    """Find topics likely to be linked from this one — same subcategory, or
    sharing any source_entries. Returns them with their exact output
    filename (basename) and a relative path usable from the current topic."""
    my_path = Path(topic["output_path"])
    my_dir = my_path.parent
    my_sources = set(topic.get("source_entries") or [])
    my_sub = topic.get("subcategory")

    siblings = []
    for t in all_topics:
        if t["id"] == topic["id"]:
            continue
        t_sources = set(t.get("source_entries") or [])
        same_sub = t.get("subcategory") == my_sub
        shares_source = bool(my_sources & t_sources)
        if not (same_sub or shares_source):
            continue
        t_path = Path(t["output_path"])
        # Compute relative link from this page to the sibling
        if t_path.parent == my_dir:
            rel = t_path.name  # same folder → just the filename
        else:
            # Walk up from my_dir to common ancestor, then down to target
            up = ["..."] * len(my_dir.parts) if False else []
            try:
                rel = str(Path(os.path.relpath(t_path, my_dir))).replace("\\", "/")
            except ValueError:
                rel = t["output_path"]
        siblings.append({"title": t["title"], "filename": rel, "is_overview": t.get("is_overview", False)})
    return siblings


def build_user_message(topic: dict, catalog: dict, all_topics: list[dict]) -> str:
    """Build the user-side prompt for a single topic."""
    entries_by_id = catalog["entries_by_id"]
    nav = catalog["nav"]

    linked_entries = []
    for eid in topic.get("source_entries") or []:
        e = entries_by_id.get(eid)
        if e:
            linked_entries.append(e)

    # Per-topic source budget — share evenly if multiple entries
    per_entry_budget = MAX_SOURCE_CHARS // max(1, len(linked_entries))
    source_blocks = []
    for e in linked_entries:
        snippet = gather_source_snippets(e, per_entry_budget)
        if snippet:
            source_blocks.append(f"### Source for {e['id']}\n\n{snippet}")

    ui_blocks = []
    for e in linked_entries:
        # Serialize catalog entry minus massive source_files lists
        slim = {k: v for k, v in e.items() if k not in ("source_files", "related_core_files")}
        ui_blocks.append(f"### Catalog entry: {e['id']}\n\n```json\n{json.dumps(slim, indent=2)}\n```")

    parts = [
        f"# Topic to document\n\n**Title:** {topic['title']}\n\n**Category:** {topic['category']} / {topic['subcategory']}",
    ]
    if topic.get("menu_path"):
        parts.append(f"**Menu path:** `{topic['menu_path']}`")
    if topic.get("description"):
        parts.append(f"**Action description from source:** {topic['description']}")
    if topic.get("related_settings"):
        parts.append(f"**Related persisted settings:** " + ", ".join(f"`{s}`" for s in topic["related_settings"]))
    if topic.get("is_overview"):
        parts.append("**This is an overview page** — describe the feature as a whole, summarize what each control does, and link out to task-specific pages. Do NOT include the 'Steps' section; use 'How it works' instead.")

    parts.append("---\n\n## UI catalog context")
    parts.extend(ui_blocks)

    # Sibling pages — real filenames the LLM should use in the Related section
    siblings = compute_siblings(topic, all_topics)
    if siblings:
        lines = ["## Sibling pages you MAY link to (use EXACT filenames shown)",
                 "",
                 "When you add entries to the `## Related` section, pick from this list and copy the filename verbatim. Do NOT invent filenames. Format: `[Title](filename)`.",
                 ""]
        # Prefer overview pages at the top, then cap the list to keep prompts lean
        siblings.sort(key=lambda s: (not s["is_overview"], s["title"]))
        for s in siblings[:40]:
            tag = " — overview" if s["is_overview"] else ""
            lines.append(f"- `{s['filename']}` — {s['title']}{tag}")
        parts.append("\n".join(lines))

    parts.append("## Navigation catalog (for menu paths and applet-panel layout)")
    parts.append("```json\n" + json.dumps(nav, indent=2)[:8000] + "\n```")

    if source_blocks:
        parts.append("## Source snippets (for verifying labels, defaults, behavior)")
        parts.extend(source_blocks)

    parts.append(
        "---\n\nGenerate the markdown page now. Follow the template. Use exact labels from the catalog and source. Stay grounded. Only link to sibling filenames listed above; omit the Related section if there are no good matches."
    )
    return "\n\n".join(parts)


# ─── generation loop ────────────────────────────────────────────────────────

def generate_one(client, model: str, topic: dict, catalog: dict, all_topics: list[dict]) -> str:
    user_msg = build_user_message(topic, catalog, all_topics)

    resp = client.messages.create(
        model=model,
        max_tokens=2500,
        system=[
            {"type": "text", "text": SYSTEM_PROMPT, "cache_control": {"type": "ephemeral"}},
        ],
        messages=[{"role": "user", "content": user_msg}],
    )
    # Extract text
    out = "".join(block.text for block in resp.content if block.type == "text")
    return out.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="Process only the first N topics")
    ap.add_argument("--only", type=str, default="", help="Only topics whose id contains this substring")
    ap.add_argument("--force", action="store_true", help="Regenerate even if output file exists")
    ap.add_argument("--model", choices=MODEL_IDS.keys(), default="sonnet")
    ap.add_argument("--start", type=int, default=0, help="Skip the first N topics (for resuming)")
    args = ap.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: set ANTHROPIC_API_KEY in your environment first.", file=sys.stderr)
        sys.exit(1)

    catalog = load_catalog()
    all_topics = load_topics()  # complete list for sibling lookup
    topics = list(all_topics)

    if args.only:
        topics = [t for t in topics if args.only.lower() in t["id"].lower()]
    if args.start:
        topics = topics[args.start:]
    if args.limit:
        topics = topics[: args.limit]

    anthropic = _require_anthropic()
    client = anthropic.Anthropic()
    model = MODEL_IDS[args.model]

    print(f"Generating {len(topics)} topic(s) with model={model}")
    print(f"Output root: {DOCS_ROOT}")
    print()

    written = skipped = failed = 0
    t0 = time.time()

    for i, topic in enumerate(topics, 1):
        out_path = DOCS_ROOT / topic["output_path"]
        if out_path.exists() and not args.force:
            skipped += 1
            continue

        try:
            md = generate_one(client, model, topic, catalog, all_topics)
        except Exception as e:
            failed += 1
            print(f"[{i}/{len(topics)}] FAIL {topic['id']}: {e}", flush=True)
            continue

        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(md + "\n", encoding="utf-8")
        written += 1
        elapsed = time.time() - t0
        rate = written / elapsed if elapsed > 0 else 0
        print(f"[{i}/{len(topics)}] {topic['output_path']}  ({rate:.2f} pages/s)", flush=True)

    print(f"\nDone. Wrote {written}, skipped {skipped}, failed {failed} in {time.time()-t0:.1f}s.")


if __name__ == "__main__":
    main()
