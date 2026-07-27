# Understand How to Contribute Bug Reports and PRs

This page explains how to open the bundled contribution guide in AetherSDR. The guide covers how to file bug reports and submit pull requests without needing an internet connection.

## Before you start

- AetherSDR must be installed. No radio connection is required.

## Steps

1. Click `Help` in the menu bar.
2. Click `Contributing to AetherSDR...`.
3. The HelpDialog opens, displaying the contribution guide in the Markdown viewer. The dialog uses the current theme for all visual elements.
4. To search within the guide, type a term in the `Find:` field and click `Next` to advance through matches or `Previous` to go back. Press Return to find the next match. Press Shift+Return to find the previous match.
5. When you are finished, click `Close`.

## What each control does

| Control                            | Behavior                                                                                                                                      | Notes                                                                                                                                              |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| `AETHERSDR OFFLINE HELP` (eyebrow) | Brand header shown above the title.                                                                                                           |                                                                                                                                                    |
| `Title`                            | Displays the window title (topic name).                                                                                                       |                                                                                                                                                    |
| `Subtitle`                         | One-line topic description.                                                                                                                   |                                                                                                                                                    |
| `Markdown viewer`                  | Renders the loaded Markdown resource. Styled according to the current theme.                                                                  |                                                                                                                                                    |
| `Find:` field                      | Enter a subject or term to search within the displayed topic. The field border turns red when there are no matches.                           | Ctrl+F focuses the field. Enter jumps to next match; Shift+Enter jumps to previous. QLineEdit with clear button and placeholder 'Subject or term'. |
| `Next`                             | Moves to the next match in the document. Wraps to the top when the end is reached. Enabled only when the `Find:` field is non-empty.          | Disabled when search field is empty. Wraps around from end to top.                                                                                 |
| `Previous`                         | Moves to the previous match in the document. Wraps to the bottom when the start is reached. Enabled only when the `Find:` field is non-empty. | Disabled when search field is empty. Wraps around from top to end.                                                                                 |
| `Find status`                      | Shows 'No matches' (red) or 'Wrapped to top/bottom' when no further matches are found in the current direction.                               |                                                                                                                                                    |
| `Hint / footer`                    | Shows a short usage hint.                                                                                                                     |                                                                                                                                                    |

## Tips

- The Help menu keeps each guide in a separate dialog. Each dialog remembers its own window position and size independently. You can reopen just this topic at any time without disturbing other open help windows.
- The contribution guide is available offline. You do not need a network connection to read it.
- All HelpDialog colors, including the header background, text colors, scrollbar colors, and the separator, are controlled by the active theme. To change the appearance, select `Settings > Theme...`.

## Related

- [Open bundled getting-started guide](open-bundled-getting-started-guide.md)
- [Read the full AetherSDR help document](read-the-full-aethersdr-help-document.md)