# Read what changed in the new version

The What's New dialog shows release notes for versions you have not yet seen. It appears automatically after an update and is also available on demand from the Help menu.

## Before you start

- AetherSDR must be installed and running. No radio connection is required.

## Steps

1. Click `Help > What's New...`.
2. Read the release notes in the scrollable **Release notes browser**.
3. Click `Got it — 73!` to dismiss the dialog. AetherSDR records the current version in `LastSeenVersion` so the dialog does not appear again for this version.

## What each control does

| Control | Behavior |
|---|---|
| Release notes browser | Scrollable HTML view of release entries for versions newer than the last seen version, capped at the five most recent releases. |
| `Got it — 73!` | Dismisses the dialog and marks the current version as seen in `LastSeenVersion`. |
| `Upgrade` | Visible only when a newer build is available. Opens the download page and closes the dialog. |
| `Skip this version` | Visible only when a newer build is available. Writes the current version to `LastSeenVersion` and closes the dialog without upgrading. |
| Hint | Footer line with brief guidance. Read-only. |

## Tips

- On first install, the dialog shows only the current version's notes. On subsequent updates it shows every version released since the last seen version, up to five releases.
- If no new changes are available, the browser displays "No new changes to report."
- To re-read notes at any time, use `Help > What's New...`. This path always shows the full notes for the current version regardless of `LastSeenVersion`.

## Related

- [Re-read release notes later via Help menu](re-read-release-notes-later-via-help-menu.md)
- [Skip the current version's release notes](skip-the-current-version-s-release-notes.md)
- [Open the upgrade flow for a newer build](open-the-upgrade-flow-for-a-newer-build.md)
