# Re-read Release Notes Later via Help Menu

The What's New — AetherSDR dialog opens automatically after an upgrade, but you can reopen it at any time from the Help menu to review release notes for the current version.

## Before you start

- AetherSDR must be running. No radio connection is required.

## Steps

1. Click `Help > What's New...` in the menu bar.
2. Scroll through the release notes browser to read the changes.
3. Click `Got it — 73!` to dismiss the dialog.

## What each control does

| Control                      | Kind     | Behavior                                                                                                                                                     |
|------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AETHERSDR V<version> eyebrow | indicator| Branded header showing the current AetherSDR version and either 'Welcome!' or 'What's New' heading. Rendered as styled HTML in a QLabel with padding.         |
| Status label                 | indicator| Under the header shows the GitHub release title and published date after fetch, or a loading message while fetching. Multi-line status via <br/> insertion. |
| Release notes browser        | text_field| Scrollable QTextBrowser rendering release notes as GitHub-flavored Markdown. Issue/PR numbers and @mentions are hyperlinked to GitHub. Clicking links opens the default browser. Shows 'Loading...' state, error state with suggestions, or the rendered release body. |
| Find                         | push_button| Opens a QInputDialog to enter search text; highlights matches in the release notes and wraps around.                                                          |
| Upgrade                      | push_button| Shown only when an upgrade is available. Opens the latest release page on GitHub and closes the dialog. Styled as secondary button.                            |
| Skip this version            | push_button| Shown only when an upgrade is available. Persists current version as seen so the dialog is not shown on next launch. Styled as secondary button.               |
| Close                        | push_button| Primary action button that dismisses the dialog. Styled as primary blue button. Always visible.                                                               |

## Tips

- Opening the dialog via `Help > What's New...` always shows the full notes for the current version, regardless of what `LastSeenVersion` is set to. The automatic on-launch version shows only entries newer than the last seen version, capped at five releases.
- The dialog fetches release notes from the GitHub API. If you see an error about rate limiting, try again in a few minutes, or visit `github.com/aethersdr/AetherSDR/releases` directly in your browser.
- The Upgrade button uses the `kReleasesPageUrl` constant from the UpdateChecker to open the releases page. This ensures consistent URL usage across the application.

## Related

- [Read what changed in the new version](read-what-changed-in-the-new-version.md)
- [Skip the current version's release notes](skip-the-current-version-s-release-notes.md)
- [Open the upgrade flow for a newer build](open-the-upgrade-flow-for-a-newer-build.md)