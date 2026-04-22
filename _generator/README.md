# AetherSDR docs generator

Pipeline that turns the AetherSDR source code into user-facing Markdown docs.

## What's here

- `catalog/` — JSON catalog of every UI element (menus, applets, dialogs, panels, controls). Source of truth for the generator.
- `SCHEMA.md` — catalog entry schema.
- `build_topics.py` — Phase B. Reads the catalog and produces `topics.json` (one entry per user task).
- `topics.json` — the work list for the generator.
- `generate_docs.py` — Phase C. For each topic, calls Claude with the relevant catalog entries and source snippets, writes a Markdown file.
- `translate_docs.py` — Phase D. Mirrors the English `.md` tree into the Spanish docs repo, translating each file.

## Quick start

```bash
# 1. Install dependencies
pip install anthropic

# 2. Set your API key
export ANTHROPIC_API_KEY=sk-ant-...

# 3. Smoke test — generate 3 pages to check quality
cd _generator
python generate_docs.py --limit 3

# 4. Review output in ../features/..., ../getting-started/..., etc.

# 5. Generate everything
python generate_docs.py

# 6. Translate to Spanish
python translate_docs.py
```

## Useful flags

```bash
python generate_docs.py --only tci       # only TCI-related topics
python generate_docs.py --start 100      # resume from topic #100
python generate_docs.py --force          # regenerate even if the file exists
python generate_docs.py --model opus     # higher quality, higher cost
```

## When the source code changes

1. Rerun the four catalog agents (see project root history) or update catalog JSON by hand.
2. `python build_topics.py` to refresh the topic list.
3. `python generate_docs.py` — only missing pages regenerate; add `--force` if you want a full rebuild.
4. `python translate_docs.py` to refresh Spanish.

## Cost envelope (rough)

- Each page ≈ 8–12k input tokens (catalog + source snippets + nav), 1–2k output tokens.
- 366 topics × ~2k output with Sonnet 4.6 ≈ a small one-time bill.
- Prompt caching is enabled on the system prompt so repeated runs are cheaper.

## Notes

- The generator is resume-safe: it skips any topic whose output file already exists.
- `SOURCE_ROOT` in `generate_docs.py` is hard-coded to this machine. Change it if you move the AetherSDR clone.
