# Re-read Release Notes Later via Help Menu

The What's New — AetherSDR dialog opens automatically after an upgrade, but you can reopen it at any time from the Help menu to review release notes for the current version.

## Before you start

- AetherSDR must be running. No radio connection is required.

## Steps

1. Click `Help > What's New...` in the menu bar.
2. Scroll through the release notes browser to read the changes.
3. Click `Got it — 73!` to dismiss the dialog.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| Release notes browser | Scrollable view | Displays release entries as styled HTML. When opened via `Help > What's New...`, shows all entries for the current version. |
| `Got it — 73!` | Button | Dismisses the dialog and marks the current version as seen (persisted as `LastSeenVersion`). |
| `Upgrade` | Button | Shown only when an upgrade is available. Opens the download page. |
| `Skip this version` | Button | Shown only when an upgrade is available. Records the current version in `LastSeenVersion` and dismisses the dialog without upgrading. |
| Hint | Indicator | Footer line with brief guidance. |

## Tips

- Opening the dialog via `Help > What's New...` always shows the full notes for the current version, regardless of what `LastSeenVersion` is set to. The automatic on-launch version shows only entries newer than the last seen version, capped at five releases.

## Related

- [Read what changed in the new version](read-what-changed-in-the-new-version.md)
- [Skip the current version's release notes](skip-the-current-version-s-release-notes.md)
- [Open the upgrade flow for a newer build](open-the-upgrade-flow-for-a-newer-build.md)
