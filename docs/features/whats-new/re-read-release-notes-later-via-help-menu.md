# Re-read Release Notes Later via Help Menu

The What's New — AetherSDR dialog opens automatically after a version upgrade, but you can reopen it at any time from the Help menu to review release notes for the current version.

## Before you start

- AetherSDR must be running. No radio connection is required.

## Steps

1. Click `Help > What's New...` in the menu bar.
2. Scroll the release notes browser to read the entries.
3. Click `Got it — 73!` to close the dialog.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| Release notes browser | Scrollable view | Displays styled HTML release entries for the current version. |
| `Got it — 73!` | Button | Dismisses the dialog and marks the current version as seen in `LastSeenVersion`. |
| `Upgrade` | Button | Shown only when an upgrade is available. Opens the download page and closes the dialog. |
| `Skip this version` | Button | Shown only when an upgrade is available. Records the current version in `LastSeenVersion` and closes the dialog without upgrading. |
| Hint | Indicator | Short footer line with guidance text. |

## Tips

- When opened via `Help > What's New...`, the dialog shows all entries for the current installed version regardless of what `LastSeenVersion` is set to.
- The dialog shows at most five of the most recent release entries when opened automatically after an upgrade.

## Related

- [Read what changed in the new version](read-what-changed-in-the-new-version.md)
- [Open the upgrade flow for a newer build](open-the-upgrade-flow-for-a-newer-build.md)
- [Skip the current version's release notes](skip-the-current-version-s-release-notes.md)
