"""Phase D — translate the English docs tree into Spanish.

Mirrors the English docs directory into the Spanish repo. For each `.md`
file that is missing on the Spanish side (or whose English version is
newer, if --sync is passed), calls Claude to translate it and writes the
translated file to the same relative path.

Translation rules given to the model:
  - Preserve every heading, list, table, code block, and link path.
  - Do NOT translate: code/config (fenced blocks), AppSettings keys in
    backticks, menu paths (AetherSDR's UI is in English), file paths,
    URLs, shortcut strings (`Ctrl+Q`).
  - Translate prose, headings, and explanatory text into clear Spanish
    addressed to an amateur radio operator (voseo not required, neutral
    Spanish preferred).

Requires:
  - ANTHROPIC_API_KEY in the environment
  - `pip install anthropic`

Usage:
  python translate_docs.py                    # translate everything missing
  python translate_docs.py --limit 5          # smoke test
  python translate_docs.py --sync             # retranslate stale files
  python translate_docs.py --force            # retranslate everything
  python translate_docs.py --only tci         # only paths containing 'tci'
  python translate_docs.py --model sonnet     # sonnet | opus | haiku
"""

from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent
EN_REPO = HERE.parent
EN_ROOT = EN_REPO / "docs"   # MkDocs docs/ subfolder of the English repo
ES_REPO = Path(r"C:\Users\lu5dx\Documents\Codigo\AetherSDRDocsSpanish")
ES_ROOT = ES_REPO / "docs"   # MkDocs docs/ subfolder of the Spanish repo

MODEL_IDS = {
    "sonnet": "claude-sonnet-4-6",
    "opus": "claude-opus-4-7",
    "haiku": "claude-haiku-4-5-20251001",
}

# Folders under EN_ROOT that are NOT docs and should be skipped.
SKIP_DIRS = {"assets", "stylesheets", "javascripts"}  # MkDocs-only resources, no prose to translate

SYSTEM_PROMPT = """You are a professional technical translator. You translate
AetherSDR user-manual pages from English into neutral, clear Spanish for an
audience of amateur radio operators.

## Preserve exactly — DO NOT translate

- All Markdown structure: `#` headings, lists, tables, blockquotes, links,
  images.
- Fenced code blocks (anything inside ``` ``` or indented 4+ spaces).
- AppSettings keys in backticks: `TciPort`, `MqttHost`, `AutoStartTCI`.
- Menu paths: `Settings > Autostart TCI with AetherSDR`. The AetherSDR UI
  ships in English only — keep menu labels, button labels, tab names, and
  dialog titles in English, even when they appear in prose.
- Keyboard shortcuts: `Ctrl+Q`, `Ctrl+Shift+F`.
- File paths, URLs, version numbers, protocol names (TCI, DAX, MQTT,
  VITA-49, SmartSDR, NR2, NR4, DFNR, MNR, WSJT-X, FT8, RBN, POTA, SmartLink).
- Link destinations in `[text](target)`: only translate the `text`, leave
  `target` as-is.
- Numbers, units (dB, Hz, kHz, MHz, ms, W).

## Translate

- Prose sentences, including any English text around the preserved tokens.
- Heading content itself (but keep the `#` levels).
- `[link text]` content (the part in square brackets).

## Style

- Neutral (Latin American) Spanish. Use "usted"/"su" voice, or impersonal
  imperatives ("Haga clic en...", "Abra..."). No voseo. No regionalisms.
- Keep sentences short and imperative, matching the English source.
- Technical amateur-radio vocabulary: use Spanish terms where standard
  (banda, frecuencia, modo, filtro, ganancia, ruido), keep English for
  terms with no accepted translation (panadapter, waterfall, applet,
  slice — these may be loaned or briefly glossed the first time).
- "QSO" stays "QSO". "CW" stays "CW". "SSB" stays "SSB".

## Output

Respond with ONLY the translated Markdown — no preamble, no commentary,
no code fences wrapping the whole answer. Begin with the translated `#`
heading.
"""


def _require_anthropic():
    try:
        import anthropic  # noqa: F401
        return anthropic
    except ImportError:
        print("ERROR: run `pip install anthropic` first.", file=sys.stderr)
        sys.exit(1)


def iter_english_docs() -> list[Path]:
    """Every .md file under EN_ROOT, excluding SKIP_DIRS."""
    out: list[Path] = []
    for p in EN_ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in p.relative_to(EN_ROOT).parts):
            continue
        # Skip the repo-level README if present — those tend to be
        # English-only landing pages. They can still be translated if
        # the user insists, but we skip by default.
        out.append(p)
    out.sort()
    return out


def needs_translation(en_path: Path, es_path: Path, sync: bool) -> bool:
    if not es_path.exists():
        return True
    if sync:
        try:
            return en_path.stat().st_mtime > es_path.stat().st_mtime
        except OSError:
            return True
    return False


def translate_one(client, model: str, en_text: str) -> str:
    resp = client.messages.create(
        model=model,
        max_tokens=4000,
        system=[
            {"type": "text", "text": SYSTEM_PROMPT, "cache_control": {"type": "ephemeral"}},
        ],
        messages=[
            {"role": "user", "content": f"Translate this Markdown page to Spanish following the rules.\n\n---\n\n{en_text}"}
        ],
    )
    return "".join(block.text for block in resp.content if block.type == "text").strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--only", type=str, default="")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--sync", action="store_true", help="Retranslate if EN is newer than ES")
    ap.add_argument("--model", choices=MODEL_IDS.keys(), default="sonnet")
    args = ap.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: set ANTHROPIC_API_KEY first.", file=sys.stderr)
        sys.exit(1)

    if not ES_ROOT.exists():
        print(f"ERROR: Spanish docs repo missing at {ES_ROOT}", file=sys.stderr)
        sys.exit(1)

    anthropic = _require_anthropic()
    client = anthropic.Anthropic()
    model = MODEL_IDS[args.model]

    candidates = iter_english_docs()
    if args.only:
        candidates = [p for p in candidates if args.only.lower() in str(p).lower()]

    work: list[tuple[Path, Path]] = []
    for en_path in candidates:
        rel = en_path.relative_to(EN_ROOT)
        es_path = ES_ROOT / rel
        if args.force or needs_translation(en_path, es_path, args.sync):
            work.append((en_path, es_path))

    if args.limit:
        work = work[: args.limit]

    print(f"Translating {len(work)} file(s) with model={model}")
    print(f"English root: {EN_ROOT}")
    print(f"Spanish root: {ES_ROOT}\n")

    done = failed = 0
    t0 = time.time()
    for i, (en_path, es_path) in enumerate(work, 1):
        rel = en_path.relative_to(EN_ROOT)
        try:
            en_text = en_path.read_text(encoding="utf-8")
            es_text = translate_one(client, model, en_text)
        except Exception as e:
            failed += 1
            print(f"[{i}/{len(work)}] FAIL {rel}: {e}", flush=True)
            continue
        es_path.parent.mkdir(parents=True, exist_ok=True)
        es_path.write_text(es_text + "\n", encoding="utf-8")
        done += 1
        elapsed = time.time() - t0
        rate = done / elapsed if elapsed > 0 else 0
        print(f"[{i}/{len(work)}] {rel}  ({rate:.2f} pages/s)", flush=True)

    print(f"\nDone. Translated {done}, failed {failed} in {time.time()-t0:.1f}s.")


if __name__ == "__main__":
    main()
