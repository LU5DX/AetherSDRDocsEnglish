# Open the Upgrade Flow for a Newer Build

When a newer build of AetherSDR is available, the What's New dialog shows an "Upgrade" button that opens the download page in your browser. This page explains how to reach that button.

## Before you start

- The "Upgrade" button appears only when AetherSDR has detected that a newer build is available. If no upgrade is available, the button is not shown.
- No radio connection is required.

## Steps

1. Open `Help > What's New...`.
2. Review the release notes in the scrollable browser at the top of the dialog.
3. Click `Upgrade`.

AetherSDR opens the AetherSDR releases page in your default web browser and closes the dialog. The download page URL is obtained from the application's internal release page reference.

## What each control does

| Control                      | Kind                                                                                                                                                                             | Behavior                                                                                                                                                     |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Release notes browser        | Scrollable QTextBrowser rendering release notes as GitHub-flavored Markdown. Issue/PR numbers and @mentions are hyperlinked to GitHub. Clicking links opens the default browser. | Refactored in v26.5.3 (#2979) to fetch live notes from api.github.com. Shows 'Loading...' state, error state with suggestions, or the rendered release body. |
| `Got it — 73!`               | Push button                                                                                                                                                                      | Dismisses the dialog and marks the version as seen.                                                                                                          |
| `Upgrade`                    | Push button                                                                                                                                                                      | Visible only when an upgrade is available. Opens the download page.                                                                                          |
| `Skip this version`          | Push button                                                                                                                                                                      | Skips release nag for this version.                                                                                                                          |
| AETHERSDR V<version> eyebrow | Branded header showing the current AetherSDR version and either 'Welcome!' or 'What's New' heading.                                                                              | Rendered as styled HTML in a QLabel with padding.                                                                                                            |
| Status label                 | Under the header shows the GitHub release title and published date after fetch, or a loading message while fetching.                                                             | Multi-line status via <br/> insertion.                                                                                                                       |
| Find                         | Opens a QInputDialog to enter search text; highlights matches in the release notes and wraps around.                                                                             | New in v26.5.3 (#2979).                                                                                                                                      |
| Close                        | Primary action button that dismisses the dialog.                                                                                                                                 | Styled as primary blue button. Always visible.                                                                                                               |
## Tips

- If you close the dialog with `Got it — 73!` instead of `Upgrade`, AetherSDR records the current version in `LastSeenVersion` and will not prompt you again for this release. You can still return to the dialog via `Help > What's New...`.
- If you click `Skip this version`, `LastSeenVersion` is set to the current version and the nag for this release is suppressed, but the download page is not opened.

## Related

- [Re-read release notes later via Help menu](re-read-release-notes-later-via-help-menu.md)
- [Read what changed in the new version](read-what-changed-in-the-new-version.md)
- [Skip the current version's release notes](skip-the-current-version-s-release-notes.md)