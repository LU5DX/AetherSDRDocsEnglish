# AetherSDR User Documentation (English)

Source for the AetherSDR user manual at
**https://lu5dx.github.io/AetherSDRDocsEnglish/** (once Pages is enabled).

Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).
Spanish mirror: [AetherSDRDocsSpanish](https://github.com/LU5DX/AetherSDRDocsSpanish).

## Repository layout

```
/
├── mkdocs.yml              MkDocs Material config
├── overrides/              Theme overrides (custom landing template)
├── docs/                   The documentation tree (MkDocs serves this)
│   ├── index.md            Landing page (uses overrides/home.html)
│   ├── stylesheets/        Custom CSS (parallax hero, polish)
│   ├── javascripts/        Parallax scroll
│   ├── assets/             Hero artwork (placeholder SVGs — see assets/README.md)
│   ├── getting-started/    Install, first connect, first QSO, core concepts
│   ├── features/           One folder per applet/dialog/panel
│   ├── operating/          Cross-cutting operating guides
│   ├── reference/          Menu actions, AppSettings reference
│   └── troubleshooting/    Common problems and fixes
├── _generator/             Pipeline that turns AetherSDR source into docs/
└── .github/workflows/      GitHub Pages deploy workflow
```

## Local preview

```bash
pip install mkdocs-material
mkdocs serve     # http://127.0.0.1:8000
```

## Regenerating the docs

When AetherSDR ships a new version:

```bash
cd _generator
python -m pip install anthropic
$env:ANTHROPIC_API_KEY="sk-ant-..."   # PowerShell
python build_topics.py                # refresh topic list from catalog
python generate_docs.py               # regenerates missing pages into docs/
python translate_docs.py --sync       # mirrors EN → ES
```

See [`_generator/README.md`](_generator/README.md) for full details.

## Hero artwork

The landing page uses three SVG layers (stars, alien silhouette, AetherSDR
UI mockup) for a parallax effect. The current SVGs are placeholders — see
[`docs/assets/README.md`](docs/assets/README.md) for the image-generation
prompt to swap in a higher-fidelity rendered scene.

## Hosting

The included GitHub Actions workflow (`.github/workflows/deploy-docs.yml`)
publishes to GitHub Pages on every push to `main`. **Note:** Pages on a
private repository requires GitHub Pro or higher. On the free tier, either
make this repo public or swap the deploy job for Cloudflare Pages / Netlify
/ Vercel — all of which build from private repos for free.
