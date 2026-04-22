# Read the full AetherSDR help document

The HelpDialog is an offline Markdown reader built into AetherSDR. Use it to browse bundled reference guides without an internet connection.

## Before you start

- No radio connection is required to open help topics.
- AetherSDR must be installed with its bundled help assets intact. If a help file is missing, the viewer displays an error message instead of the topic content.

## Steps

1. Click `Help` in the menu bar.
2. Click `Help > AetherSDR Help...`.
3. The help window opens. The header shows the eyebrow label **AETHERSDR OFFLINE HELP** above the topic title and subtitle.
4. Scroll through the Markdown viewer to read the content.
5. Click `Close` when finished.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **AETHERSDR OFFLINE HELP** | Indicator | Brand eyebrow shown above the topic title. Not interactive. |
| Title | Indicator | Displays the name of the open help topic. |
| Subtitle | Indicator | One-line description: "Bundled help is available even when your station computer is offline." |
| Markdown viewer | Text area | Renders the bundled Markdown file for the topic. Read-only. External links open in your default browser. |
| Hint / footer | Indicator | Shows the tip: "The Help menu keeps each guide separate so you can reopen just the topic you need." |
| `Close` | Button | Closes the help window. |

## Tips

- Each help topic opens in its own window. You can open multiple topics side by side by choosing different items from the `Help` menu without closing the previous window.
- All six topics are available from the `Help` menu: `Help > Getting Started...`, `Help > AetherSDR Help...`, `Help > Understanding Noise Cancellation...`, `Help > Configuring AetherSDR Controls...`, `Help > Configuring Data Modes...`, and `Help > Contributing to AetherSDR...`.

## Troubleshooting

- **The viewer shows "Help file not available" instead of content** — A bundled help asset is missing from the installation. Reinstall AetherSDR and confirm all files are present, or report the missing asset to the project.

## Related

- [Open bundled getting-started guide](open-bundled-getting-started-guide.md)
- [Learn the differences between NR2, NR4, DFNR and MNR](learn-the-differences-between-nr2-nr4-dfnr-and-mnr.md)
- [Configure digital modes step-by-step](configure-digital-modes-step-by-step.md)
- [Understand how to contribute bug reports and PRs](understand-how-to-contribute-bug-reports-and-prs.md)
