# Skip the current version's release notes

When AetherSDR finds a newer version available, the What's New dialog offers a way to stop the dialog from reappearing for that version without reading the full release notes.

## Before you start

- The What's New dialog must be open and showing an available upgrade. The "Skip this version" button appears only when an upgrade is available.

## Steps

1. Open `Help > What's New...` if the dialog is not already on screen.
2. Click `Skip this version`.

The dialog closes and `LastSeenVersion` is updated to the current version. AetherSDR will not show the release notes for this version again on future launches.

## What each control does

| Control | Behavior | Persisted setting |
|---|---|---|
| Release notes browser | Scrollable HTML view of release entries between your last seen version and the current version. | — |
| `Got it — 73!` | Dismisses the dialog and marks the current version as seen. | `LastSeenVersion` |
| `Upgrade` | Shown only when an upgrade is available. Opens the download page. | — |
| `Skip this version` | Shown only when an upgrade is available. Writes the current version to `LastSeenVersion` and closes the dialog, suppressing future nags for this version. | `LastSeenVersion` |
| Hint | Short footer line with guidance. Read-only. | — |

## Tips

- If you skip a version and later want to read its release notes, open `Help > What's New...` at any time. That path shows all entries for the current version regardless of the `LastSeenVersion` value.

## Related

- [Read what changed in the new version](read-what-changed-in-the-new-version.md)
- [Open the upgrade flow for a newer build](open-the-upgrade-flow-for-a-newer-build.md)
- [Re-read release notes later via Help menu](re-read-release-notes-later-via-help-menu.md)
