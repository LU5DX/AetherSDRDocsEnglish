# Read the full AetherSDR help document

The AetherSDR help system bundles several offline guides covering setup, noise cancellation, data modes, and more. Use the Help menu to open any topic without an internet connection.

## Before you start

- AetherSDR must be installed and running. No radio connection is required.

## Steps

1. Click `Help` in the menu bar.
2. Select any of the following items to open the corresponding guide:
   - `Help > Getting Started...`
   - `Help > AetherSDR Help...`
   - `Help > Understanding Noise Cancellation...`
   - `Help > Configuring AetherSDR Controls...`
   - `Help > Configuring Data Modes...`
   - `Help > Contributing to AetherSDR...`
3. Read the content in the Markdown viewer. Scroll as needed.
4. To search within the open topic, type a word or phrase in the `Find:` field.
5. Click `Next` to jump to the next match, or click `Previous` to go to the previous match. Search wraps around when it reaches the end or beginning of the document.
6. Click `Close` to dismiss the dialog.

## What each control does

| Control                            | Behavior                                                                                                                                              | Notes                                                                                                                                              |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| `AETHERSDR OFFLINE HELP` (eyebrow) | Brand header shown above the topic title. Read-only.                                                                                                  |                                                                                                                                                    |
| Title                              | Displays the name of the open help topic. Read-only.                                                                                                  |                                                                                                                                                    |
| Subtitle                           | One-line description: "Bundled help is available even when your station computer is offline." Read-only.                                              |                                                                                                                                                    |
| `Find:` field                      | Type a search term to locate text within the current topic. Placeholder text reads "Subject or term". The border turns red when there are no matches. |                                                                                                                                                    |
| `Next`                             | Finds the next occurrence of the search term. Enabled only when the `Find:` field contains text. Keyboard shortcut: Return.                           |                                                                                                                                                    |
| `Previous`                         | Finds the previous occurrence of the search term. Enabled only when the `Find:` field contains text. Keyboard shortcut: Shift+Return.                 |                                                                                                                                                    |
| Find status                        | Shows 'No matches' (red) or 'Wrapped to top/bottom' when no further matches are found in the current direction.                                      |                                                                                                                                                    |
| Markdown viewer                    | Renders the loaded help topic. External links open in your default browser.                                                                           |                                                                                                                                                    |
| Hint / footer                      | Reads: "Tip: The Help menu keeps each guide separate so you can reopen just the topic you need." Read-only.                                           |                                                                                                                                                    |
| `Close`                            | Closes the help dialog.                                                                                                                               |                                                                                                                                                    |

## Position and size persistence

Each help guide now remembers its own window position and size independently. If you open the "Getting Started" guide, move it to one area of your screen, and then open the "Understanding Noise Cancellation" guide, the second dialog will not stack on top of the first. AetherSDR restores each guide to its last-used position and size. This behavior applies to every help topic opened from the Help menu.

## Appearance and theming

The Help dialog now follows the active theme instead of using hard-coded colors. All header, separator, browser, and footer colors are driven by theme tokens. The dialog container is registered under `dialog/help` in the theme system. This ensures consistent visual styling when you switch between light and dark themes or use custom theme files.

## Tips

- Each Help menu item opens a separate dialog, so you can have more than one topic open at the same time, and each one will remember its own window position.
- Press the standard Find shortcut (Ctrl+F on Linux and Windows, Cmd+F on macOS) while the dialog is focused to move the cursor directly to the `Find:` field.
- If a search term is not found, the `Find:` field border turns red and the status area shows "No matches". Clearing the field resets the state.

## Related

- [Open bundled getting-started guide](open-bundled-getting-started-guide.md)
- [Learn the differences between NR2, NR4, DFNR and MNR](learn-the-differences-between-nr2-nr4-dfnr-and-mnr.md)
- [Configure digital modes step-by-step](configure-digital-modes-step-by-step.md)
- [Understand how to contribute bug reports and PRs](understand-how-to-contribute-bug-reports-and-prs.md)