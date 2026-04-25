# Open bundled getting-started guide

AetherSDR ships a set of offline help topics that open without an internet connection. This page explains how to open the getting-started guide.

## Before you start

- AetherSDR must be running. A radio connection is not required.

## Steps

1. Click `Help` in the menu bar.
2. Click `Getting Started...`.
3. The help dialog opens, displaying the getting-started topic in the Markdown viewer.
4. To search within the topic, type a term in the `Find:` field and click `Next` to move forward through matches or `Previous` to move backward. Press Return to advance to the next match. Press Shift+Return to go to the previous match.
5. To close the dialog, click `Close`.

## What each control does

| Control | Behavior |
|---|---|
| `AETHERSDR OFFLINE HELP` (eyebrow) | Brand header shown above the topic title. Read-only. |
| Title | Displays the topic name passed to the dialog at open time. Read-only. |
| Subtitle | One-line description of the topic. Read-only. |
| Markdown viewer | Renders the bundled Markdown content for the selected topic. Read-only; external links open in your browser. |
| `Find:` field | Type a subject or term to search within the displayed topic. The `Next` and `Previous` buttons are disabled until you enter text. |
| `Next` | Finds the next occurrence of the search term. Wraps to the top when the end of the document is reached. |
| `Previous` | Finds the previous occurrence of the search term. Wraps to the bottom when the start of the document is reached. |
| Hint / footer | Shows a short usage tip. Read-only. |
| `Close` | Closes the help dialog. |

## Tips

- Each entry under the `Help` menu opens a separate dialog for that topic, so you can keep multiple topics open at the same time.
- The help content is bundled with the application and does not require a network connection.
- If a help file cannot be loaded, the viewer displays a notice asking you to reinstall AetherSDR or report the missing asset.

## Related

- [Read the full AetherSDR help document](read-the-full-aethersdr-help-document.md)
- [Learn the differences between NR2, NR4, DFNR and MNR](learn-the-differences-between-nr2-nr4-dfnr-and-mnr.md)
- [Configure digital modes step-by-step](configure-digital-modes-step-by-step.md)
- [Understand how to contribute bug reports and PRs](understand-how-to-contribute-bug-reports-and-prs.md)
