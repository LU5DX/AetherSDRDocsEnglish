# AetherSDR Offline Help Overview

AetherSDR includes a built-in help reader that displays bundled Markdown documentation without requiring an internet connection. Use it to read getting-started guides, learn about noise cancellation modes, configure data modes, and more.

## How it works

Each help topic opens in its own HelpDialog window. The window is independent of the radio connection — you can read help at any time, even when no radio is connected.

Open any topic from the Help menu:

- `Help > Getting Started...`
- `Help > AetherSDR Help...`
- `Help > Understanding Noise Cancellation...`
- `Help > Configuring AetherSDR Controls...`
- `Help > Configuring Data Modes...`
- `Help > Contributing to AetherSDR...`

Each entry opens a separate window pre-loaded with that topic. You can have multiple help windows open at the same time.

## What each control does

| Control | Description |
|---|---|
| **AETHERSDR OFFLINE HELP** | Brand header shown above the topic title. Read-only indicator. |
| **Title** | Displays the topic name as the window title. Read-only. |
| **Subtitle** | One-line description: "Bundled help is available even when your station computer is offline." Read-only. |
| **Find:** field | Type a subject or term to search within the current topic. The field border turns red when there are no matches. Activate with the standard Find keyboard shortcut or by clicking the field. |
| **Next** | Finds the next occurrence of the search term. Enabled only when the Find field contains text. Press Return in the Find field for the same effect. Wraps to the top of the document when the end is reached. |
| **Previous** | Finds the previous occurrence of the search term. Enabled only when the Find field contains text. Press Shift+Return in the Find field for the same effect. Wraps to the bottom when the beginning is reached. |
| **Markdown viewer** | Renders the loaded help topic. Read-only. External links open in your system browser. |
| **Hint / footer** | Shows the tip: "The Help menu keeps each guide separate so you can reopen just the topic you need." Read-only. |
| **Close** | Closes the help window. |

## Tips

- The Find field searches only the currently open topic. To search a different guide, open it from the Help menu and use Find there.
- If a search term is not found from the current scroll position, the viewer wraps automatically and shows "Wrapped to top" or "Wrapped to bottom" as a status indicator next to the Find field. If there are no matches at all, it shows "No matches."
- No persisted settings are associated with the help reader. Nothing is saved when you close it.

## Related

- [Open bundled getting-started guide](open-bundled-getting-started-guide.md)
- [Read the full AetherSDR help document](read-the-full-aethersdr-help-document.md)
- [Learn the differences between NR2, NR4, DFNR and MNR](learn-the-differences-between-nr2-nr4-dfnr-and-mnr.md)
- [Configure digital modes step-by-step](configure-digital-modes-step-by-step.md)
- [Understand how to contribute bug reports and PRs](understand-how-to-contribute-bug-reports-and-prs.md)
