# AetherSDR User Documentation (English)

User-facing documentation for [AetherSDR](https://github.com/ten9876/AetherSDR),
a Qt6 Linux-native SmartSDR-compatible client for FlexRadio FLEX-8600 radios.

## Structure

```
/
├── getting-started/   Install, first connect, first QSO, core concepts
├── features/          One folder per UI feature (applet, dialog, panel) with
│                      an overview page plus task-focused how-to pages
├── operating/         Cross-cutting operating guides (digital modes, remote
│                      operation, contesting)
├── reference/         Menu-action reference, AppSettings key reference
├── troubleshooting/   Common problems and fixes
└── _generator/        Build pipeline that turns the AetherSDR source tree
                       into these Markdown files. See _generator/README.md.
```

## Who this is for

- **Amateur radio operators** using AetherSDR — this is the user manual.
- **AetherSDR maintainers** — each doc is grounded in specific source files
  (listed in the page's front matter or footer). When the code changes, rerun
  the generator and only the affected pages update.
- **The AetherSDR help chatbot** — a separate project indexes these Markdown
  files into a vector store and answers user questions.

## Regenerating these docs

The full pipeline lives in `_generator/`. Short version:

```bash
cd _generator
pip install anthropic
export ANTHROPIC_API_KEY=sk-ant-...

python build_topics.py          # refresh topic list from the catalog
python generate_docs.py         # generate missing Markdown pages
```

See [`_generator/README.md`](_generator/README.md) for details, flags, and the
Spanish translation step.

## Spanish version

Translations of every page live in a sibling repository:
[AetherSDRDocsSpanish](../AetherSDRDocsSpanish). The `_generator/translate_docs.py`
script mirrors the English tree into that repo on demand.
