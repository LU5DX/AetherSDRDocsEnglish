# Read what changed in the new version via live GitHub release notes

View the release notes for your current AetherSDR version, fetched live from GitHub. The dialog also appears automatically on first launch after installing an update.

## Before you start

- A working internet connection is required to fetch release notes from GitHub's API.

## Steps

1. Open the **What's New** dialog: `Help > What's New...`

   The dialog shows a branded header with your current AetherSDR version and either "Welcome!" (first install) or "What's New".

2. The release notes load automatically from GitHub. A status label below the header shows the release title and published date.

3. (Optional) Click **Find** to search within the release notes. Enter your search text and press Enter; matches are highlighted and wrap around.

4. Click **Close** to dismiss the dialog.

## What each control does

| Control | Default | Behavior | Setting key |
|---|---|---|---|
| Header (AETHERSDR V&lt;version&gt;) | — | Shows current version and "Welcome!" or "What's New" heading | — |
| Status label | — | Shows GitHub release title and published date, or a loading/error message | — |
| Release notes browser | — | Scrollable view of GitHub-flavored Markdown. Issue/PR numbers and @mentions link to GitHub | — |
| Find | — | Opens a search dialog; highlights matching text in the release notes | — |
| Upgrade | — | (Only shown when an upgrade is available) Opens the latest release page on GitHub and closes the dialog | — |
| Skip this version | — | (Only shown when an upgrade is available) Marks the current version as seen so the dialog won't auto-open on next launch | `LastSeenVersion` |
| Close | — | Dismisses the dialog | — |

## Troubleshooting

- **"GitHub is rate-limiting requests from your network"** — GitHub's unauthenticated API is limited to 60 requests per hour per IP. Wait a few minutes and try again, or visit github.com/aethersdr/AetherSDR/releases directly.
- **"GitHub returned HTTP ..."** — The API request failed. Check your internet connection and try again later.

## Related

- [Re-read release notes later via Help menu](re-read-release-notes-later-via-help-menu.md)
- [Search within the release notes using the Find button](search-within-the-release-notes-using-the-find-button.md)
- [Skip the current version's release notes](skip-the-current-version-s-release-notes.md)
- [Open the upgrade flow for a newer build](open-the-upgrade-flow-for-a-newer-build.md)
