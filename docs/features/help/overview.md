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

Each entry opens a separate window pre-loaded with that topic. You can have multiple help windows open at the same time. Each window remembers its own position and size independently — closing and reopening a topic restores its previous geometry.

## What each control does

| Control                    | Description                                                                                                                                                                                                    | Notes                                                                                                                                              |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| **AETHERSDR OFFLINE HELP** | Brand header shown above the topic title. Read-only indicator.                                                                                                                                                 |                                                                                                                                                    |
| **Title**                  | Displays the topic name as the window title. Read-only.                                                                                                                                                        |                                                                                                                                                    |
| **Subtitle**               | One-line description: "Bundled help is available even when your station computer is offline." Read-only.                                                                                                       |                                                                                                                                                    |
| **Find:** field            | Type a subject or term to search within the current topic. The field border turns red when there are no matches. Activate with the standard Find keyboard shortcut or by clicking the field.                   | Ctrl+F focuses the field. Enter jumps to next match; Shift+Enter jumps to previous. QLineEdit with clear button and placeholder 'Subject or term'. |
| **Next**                   | Jumps to the next match of the search term. Enabled only when the Find field contains text. Press Return in the Find field for the same effect. Wraps around from end to top.                                  | Disabled when search field is empty.                                                                                                               |
| **Previous**               | Jumps to the previous match of the search term. Enabled only when the Find field contains text. Press Shift+Return in the Find field for the same effect. Wraps around from top to end.                        | Disabled when search field is empty.                                                                                                               |
| **Find status**            | Shows 'No matches' (red) or 'Wrapped to top/bottom' when no further matches are found in the current direction.                                                                                                |                                                                                                                                                    |
| **Markdown viewer**        | Renders the loaded help topic. Read-only. External links open in your system browser.                                                                                                                          |                                                                                                                                                    |
| **Hint / footer**          | Shows the tip: "The Help menu keeps each guide separate so you can reopen just the topic you need." Read-only.                                                                                                 |                                                                                                                                                    |
| **Close**                  | Closes the help window.                                                                                                                                                                                        |                                                                                                                                                    |

## Appearance

The Help dialog uses theme-aware colors. The header background, text colors, and scroll bar colors are styled based on the current AetherSDR theme. The overall layout includes theme tokens for the header background, accent color, primary and secondary text, and background layers for the main viewer and scroll bars.

## Tips

- The Find field searches only the currently open topic. To search a different guide, open it from the Help menu and use Find there.
- If a search term is not found from the current scroll position, the viewer wraps automatically and shows "Wrapped to top" or "Wrapped to bottom" as a status indicator next to the Find field. If there are no matches at all, it shows "No matches."
- Each help topic remembers its own window position and size. Open two different guides at once, move them to different screen locations, and close them. The next time you open each guide, it returns to its previous position.

## Related

- [Open bundled getting-started guide](open-bundled-getting-started-guide.md)
- [Read the full AetherSDR help document](read-the-full-aethersdr-help-document.md)
- [Learn the differences between NR2, NR4, DFNR and MNR](learn-the-differences-between-nr2-nr4-dfnr-and-mnr.md)
- [Configure digital modes step-by-step](configure-digital-modes-step-by-step.md)
- [Understand how to contribute bug reports and PRs](understand-how-to-contribute-bug-reports-and-prs.md)