# AetherSDR User Documentation (English)

Source for the AetherSDR user manual at
**https://lu5dx.github.io/AetherSDRDocsEnglish/**.

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
└── .github/workflows/      GitHub Pages deploy workflow
```

## Contributing

Open an issue or PR against `docs/`. For maintainer notes on how this
documentation is authored and kept in sync with AetherSDR releases, contact
the repo owner.
