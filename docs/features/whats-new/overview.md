# What's New — AetherSDR overview

The What's New dialog shows release notes for versions of AetherSDR you have not yet seen. It appears automatically after an update and is also available on demand from the Help menu.

## How it works

When AetherSDR starts, it compares the current version against the value stored in `LastSeenVersion`. If the current version is newer, the dialog opens automatically and fetches the release notes from GitHub for every version between the last seen version and the current one, capped at the five most recent releases. On a first install, where `LastSeenVersion` has no stored value, the dialog shows only the current version's notes and greets you with a welcome header instead of a version-change header.

When you open the dialog via `Help > What's New...`, it shows all entries for the current version regardless of what `LastSeenVersion` contains.

Release notes are fetched from GitHub's Releases API and rendered as styled HTML in a scrollable browser. GitHub Markdown features such as issue references (e.g., `#1234`), user mentions (e.g., `@username`), and relative links are converted to clickable links automatically. The first heading is removed from each release note if it duplicates the release title or tag name.

If the GitHub API is rate-limited (HTTP 403 with a "rate limit" message), the dialog shows a friendly message suggesting you wait a few minutes or read the release notes directly at github.com/aethersdr/AetherSDR/releases.

## What each control does

| Control                      | Kind                                             | Behavior                                                                                                                                                               |
|------------------------------|--------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AETHERSDR V<version> eyebrow | indicator                                        | Branded header showing the current AetherSDR version and either 'Welcome!' or 'What's New' heading. Rendered as styled HTML in a QLabel with padding.                 |
| Status label                 | indicator                                        | Under the header shows the GitHub release title and published date after fetch, or a loading message while fetching. Multi-line status via `<br/>` insertion.          |
| Release notes browser        | text_field                                       | Scrollable QTextBrowser rendering release notes as GitHub-flavored Markdown. Issue/PR numbers and @mentions are hyperlinked to GitHub. Clicking links opens the default browser. Shows 'Loading...' state, error state with suggestions, or the rendered release body. |
| Find                         | push_button                                      | Opens a QInputDialog to enter search text; highlights matches in the release notes and wraps around. New in v26.5.3 (#2979).                                         |
| Upgrade                      | push_button                                      | Visible only when an upgrade is available. Opens the AetherSDR releases download page and closes the dialog.                                                          |
| Skip this version            | push_button                                      | Visible only when an upgrade is available. Writes the current version to `LastSeenVersion` and closes the dialog, suppressing the upgrade prompt for this version.     |
| Close                        | push_button                                      | Primary action button that dismisses the dialog. Styled as primary blue button. Always visible.                                                                        |

The `Upgrade` and `Skip this version` buttons appear only when AetherSDR has detected that a newer build is available.

## Tips

- To re-read the release notes at any time without triggering an upgrade prompt, use `Help > What's New...`. This path always shows the current version's notes.
- The Hint footer points to the lightbulb button in the title bar for submitting bug reports or feature ideas.
- If the release notes fail to load due to network issues or GitHub rate limiting, you can always read them directly at github.com/aethersdr/AetherSDR/releases.

## Related

- [Read what changed in the new version](read-what-changed-in-the-new-version.md)
- [Re-read release notes later via Help menu](re-read-release-notes-later-via-help-menu.md)
- [Open the upgrade flow for a newer build](open-the-upgrade-flow-for-a-newer-build.md)
- [Skip the current version's release notes](skip-the-current-version-s-release-notes.md)