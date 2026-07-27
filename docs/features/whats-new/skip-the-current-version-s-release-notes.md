# What's New dialog

The What's New dialog displays release notes for the current version of AetherSDR. It appears automatically after a version change, or you can open it manually via `Help > What's New...`. The dialog fetches live release notes from the GitHub API and renders them as styled Markdown.

## Before you start

- A working internet connection is required to fetch live release notes from GitHub.
- The dialog appears automatically when AetherSDR detects a new version has been installed.
- You can open the dialog at any time from the Help menu.

## Steps

1. If the dialog does not open automatically, go to `Help > What's New...`.
2. Wait for the release notes to load. The status label shows "Loading..." while fetching.
3. Read the release notes in the browser area. Click any hyperlinked issue/PR numbers or @mentions to open them in your default browser.
4. To search within the release notes, click "Find", enter your search text, and press Enter. Matches are highlighted and the view wraps around.
5. When finished, click "Close" to dismiss the dialog.

## What each control does

| Control                      | Kind                                                                                                                                                                             | Behavior                                                                                                                                                      |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AETHERSDR V<version> eyebrow | Indicator                                                                                                                                                                        | Branded header showing the current AetherSDR version and either 'Welcome!' or 'What's New' heading. Rendered as styled HTML in a QLabel with padding.         |
| Status label                 | Indicator                                                                                                                                                                        | Under the header shows the GitHub release title and published date after fetch, or a loading message while fetching. Multi-line status via `<br/>` insertion. |
| Release notes browser        | Scrollable QTextBrowser rendering release notes as GitHub-flavored Markdown. Issue/PR numbers and @mentions are hyperlinked to GitHub. Clicking links opens the default browser. | Refactored in v26.5.3 (#2979) to fetch live notes from api.github.com. Shows 'Loading...' state, error state with suggestions, or the rendered release body.  |
| Find                         | Push button                                                                                                                                                                      | Opens a QInputDialog to enter search text; highlights matches in the release notes and wraps around. New in v26.5.3 (#2979).                                  |
| Upgrade                      | Shown only when showUpgrade is true; opens the latest release page on GitHub and closes the dialog.                                                                              | Styled as secondary button.                                                                                                                                   |
| Skip this version            | Shown only when showUpgrade is true; persists current version as seen so the dialog is not shown on next launch.                                                                 | Styled as secondary button.                                                                                                                                   |
| Close                        | Push button                                                                                                                                                                      | Primary action button that dismisses the dialog. Always visible. Styled as primary blue button.                                                               |
## Tips

- The "Skip this version" and "Upgrade" buttons appear only when an upgrade is available. If no upgrade is detected, only "Close" is shown.
- "Skip this version" writes the current version to `LastSeenVersion` and closes the dialog. The What's New dialog will not appear automatically on the next launch for this version.
- "Upgrade" opens the releases page on GitHub using the application's configured releases URL. Clicking it also closes the dialog.
- To re-read release notes at any time, use `Help > What's New...`. This opens the dialog regardless of the saved `LastSeenVersion` value.
- Release notes are fetched from `api.github.com`. If your network is rate-limited by GitHub (HTTP 403 with a "rate limit" message), the dialog shows a friendly message suggesting you try again later or read the notes directly at the releases page.
- The release notes browser renders Markdown from the GitHub release body. GitHub issue references (e.g., `#123`) and `@username` mentions are automatically converted to clickable links.

## Troubleshooting

- **"Skip this version" is not visible** — The button only appears when AetherSDR has detected that an upgrade is available. If no upgrade is detected, only "Close" is shown. This is expected behavior.
- **"Upgrade" is not visible** — Same condition as above. The button only appears when an upgrade is detected.
- **Release notes fail to load** — The dialog fetches release notes from `api.github.com`. If you see an error message, it may be due to network issues or GitHub rate limiting. Try again later or visit the release page directly.
- **Find dialog does not find matches** — The search is case-insensitive and searches the rendered release notes text. Ensure your search term is spelled correctly.

## Related

- [Re-read release notes later via Help menu](re-read-release-notes-later-via-help-menu.md)
- [Open the upgrade flow for a newer build](open-the-upgrade-flow-for-a-newer-build.md)
- [Read what changed in the new version](read-what-changed-in-the-new-version.md)