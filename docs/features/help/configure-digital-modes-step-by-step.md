# Configure digital modes step-by-step

This page explains how to open AetherSDR's bundled guide for configuring digital (data) modes. The guide is available offline and walks you through setup step-by-step.

## Before you start

- AetherSDR must be installed. No radio connection is required to read help topics.

## Steps

1. Click `Help` in the menu bar.
2. Click `Configuring Data Modes...`.
3. The HelpDialog opens, displaying the data modes guide in the Markdown viewer. The dialog header shows "AETHERSDR OFFLINE HELP" with the topic title and subtitle.
4. Read the guide. Scroll as needed.
5. To search within the guide, type a term into the `Find:` field and click `Next` to move forward through matches or `Previous` to move backward. Press Return to advance to the next match; press Shift+Return to go to the previous match.
6. Click `Close` when finished.

## What each control does

| Control         | Behavior                                                                                                                                          | Notes                                                                                                                                              |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| `Find:` field   | Enter a subject or term to search within the displayed topic. The field border turns red if no matches are found.                                 |                                                                                                                                                    |
| `Next`          | Moves to the next match in the document. Wraps to the top when the end is reached. Enabled only when the `Find:` field is not empty.              |                                                                                                                                                    |
| `Previous`      | Moves to the previous match in the document. Wraps to the bottom when the beginning is reached. Enabled only when the `Find:` field is not empty. |                                                                                                                                                    |
| `Close`         | Closes the help dialog.                                                                                                                           |                                                                                                                                                    |
| Find:           | Search field to find text in the help document. Enables the Next and Previous buttons when non-empty.                                             | Ctrl+F focuses the field. Enter jumps to next match; Shift+Enter jumps to previous. QLineEdit with clear button and placeholder 'Subject or term'. |
| Next (Find)     | Jumps to the next match of the search term.                                                                                                       | Disabled when search field is empty. Wraps around from end to top.                                                                                 |
| Previous (Find) | Jumps to the previous match of the search term.                                                                                                   | Disabled when search field is empty. Wraps around from top to end.                                                                                 |
| Find status     | Shows 'No matches' (red) or 'Wrapped to top/bottom' when no further matches are found in the current direction.                                   |                                                                                                                                                    |

## Tips

- Each help topic opens in its own dialog and remembers its own position and size independently. You can reopen `Help > Configuring Data Modes...` at any time without affecting other open help windows.
- The bundled help is available even when your station computer has no internet access.
- The dialog uses the current theme's color scheme for its background, text, and accent colors.

## Related

- [Open bundled getting-started guide](open-bundled-getting-started-guide.md)
- [Read the full AetherSDR help document](read-the-full-aethersdr-help-document.md)