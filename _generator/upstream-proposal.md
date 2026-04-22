# Proposal: host AetherSDR user documentation upstream

> **Status:** Draft. Paste into a GitHub Issue on `ten9876/AetherSDR` once the
> chatbot has been in real-user use for 2-4 weeks and the `<<FILL IN>>`
> placeholders below have real numbers. Do not submit before then — the ask
> is far more credible with evidence than without.

---

## TL;DR

I've been running a documentation pipeline that reads the AetherSDR source tree
and generates a 366-page user manual in English and Spanish, currently hosted
in two personal repos. It powers an AetherSDR help chatbot. After `<<N>>`
weeks of real-user questions, the manual holds up well. I'd like to offer the
pipeline as a PR against AetherSDR so the project owns its own user
documentation and docs regenerate automatically on each release. This issue
is to check whether that's something you'd accept before I open the PR.

## What exists today

- **[AetherSDRDocsEnglish](<<url>>)** — 367 Markdown pages covering every
  applet, dialog, panel, menu action, and ~20 cross-cutting guides (install,
  first QSO, noise reduction, digital modes). Grounded in source: every page
  was generated from the actual `.cpp/.h` files with exact labels, defaults,
  ranges, and AppSettings keys.
- **[AetherSDRDocsSpanish](<<url>>)** — 1:1 mirror in neutral Spanish. UI
  labels and settings keys stay in English; only prose is translated.
- **Pipeline** — catalog JSON + Python generator + translator. Resume-safe,
  diff-aware, ~90 min full run, ~$10 total cost at Sonnet 4.6.
- **Chatbot** — `<<chatbot URL or description>>`. Currently answering
  `<<N>>` queries/week. Top categories: `<<fill in from logs>>`.

## Evidence from the bake-in period

- Pages that needed hand-editing: `<<list>>` and why.
- Pages users quoted back in questions: `<<list>>`.
- Accuracy failures the chatbot surfaced: `<<list>>` (fixed in-place).
- Cost per full regeneration: `$<<actual>>`.
- Generation time: `<<actual>> min` on a full-source rescan.

## Proposed shape if you accept

A PR against AetherSDR `main` with three components:

### 1. `docs/user-manual/` (367 `.md` files)

One folder per feature, task-oriented pages. Readable on GitHub, mkdocs-ready,
suitable for your existing `docs/` sibling. I've kept paths stable so
cross-links survive rearrangement.

### 2. `docs/user-manual/_generator/`

- `catalog/` — structured JSON describing every UI element, source of truth.
- `build_topics.py` — derives the topic list from the catalog.
- `generate_docs.py` — calls Claude Sonnet 4.6 with per-topic source context.
- `translate_docs.py` — mirrors EN → ES (extensible to more languages).
- `SCHEMA.md` + `README.md` — how to run and extend.

### 3. `.github/workflows/regenerate-user-docs.yml`

Triggers on `release: published` and `workflow_dispatch`. Steps:

1. Rebuild catalog from current source (agents or incremental diff — TBD).
2. Run `build_topics.py`.
3. Run `generate_docs.py` + `translate_docs.py`.
4. **Open a PR**, not auto-commit to main. CODEOWNERS review required as
   usual. Labelled `docs:auto-regen` for easy filtering.

Uses `secrets.ANTHROPIC_API_KEY`. No other runtime dependencies beyond
`anthropic` Python SDK.

## What this would cost you

- **API budget:** `~$<<actual>>/release`. At `<<your release cadence>>`
  that's `$<<annual>>`/year.
- **Review load:** one auto-PR per release. Mostly diff noise when a
  control's label changes — reviewable in 5-10 minutes once you're used to
  the patterns. Skippable between releases.
- **Ownership:** I'd like to be CODEOWNER for `docs/user-manual/_generator/`
  so catalog/pipeline changes come through me, not you. You retain full
  authority over merged content. Nothing changes about the rest of the
  project.

## What this explicitly does not do

Per your CLAUDE.md rules, the pipeline never:

- Changes source code, behavior, defaults, or visual design.
- Runs without human review — every regen becomes a PR.
- Modifies existing hand-written `docs/` content. The user manual lives in
  a new `docs/user-manual/` subtree.

If you ever want to kill it, it's one folder + one workflow file to delete.
No deeper entanglement.

## Alternatives I considered

- **Keep in my personal repo forever.** Works, but drifts as AetherSDR
  evolves. Contributors don't know docs exist. Each release I play
  catch-up.
- **Fork + upstream merge occasionally.** Same drift problem, plus a fork
  maintenance burden.
- **Official AetherSDR-Docs sibling repo under ten9876/.** Cleaner than
  personal repos, but same CI/cost story as in-tree with worse discoverability.
  I'd be fine with this as a fallback if you prefer it over `docs/user-manual/`.

## The ask

1. In principle, would you host user documentation in-tree?
2. If yes: do you prefer the generator in-tree, or only the generated
   Markdown (with the generator living elsewhere and pushing results)?
3. Any opinion on AI-generated content policy I should follow when
   structuring the PR (footer attribution, per-page provenance comments,
   etc.)?

Happy to open the PR in whatever shape you'd actually merge — or to keep
hosting it myself if this isn't a direction you want to take. Either way,
the pipeline and the baseline docs stay available and I'll keep maintaining
them for my chatbot.

— `<<your name / callsign>>`
