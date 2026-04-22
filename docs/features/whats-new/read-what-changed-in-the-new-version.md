# Read what changed in the new version

The What's New dialog shows release notes for versions you have not yet seen. It opens automatically after an upgrade and is also available on demand from the Help menu.

## Before you start

- AetherSDR must be installed and launched. No radio connection is required.

## Steps

1. Click `Help > What's New...`.
2. Read the release notes in the scrollable browser. Each entry is grouped by version and lists individual changes marked with colored dots (features, bug fixes, improvements, and infrastructure changes).
3. Click `Got it — 73!` to dismiss the dialog. AetherSDR records the current version in `LastSeenVersion` so the dialog will not reappear for this version automatically.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| Release notes browser | Scrollable view | Displays styled HTML release entries for versions newer than `LastSeenVersion`, up to the five most recent. |
| `Got it — 73!` | Button | Closes the dialog and marks the current version as seen in `LastSeenVersion`. |
| `Upgrade` | Button | Visible only when a newer build is available. Opens the AetherSDR releases download page and closes the dialog. |
| `Skip this version` | Button | Visible only when a newer build is available. Sets `LastSeenVersion` to the current version, suppressing the upgrade prompt for this release. |
| Hint | Footer indicator | Displays a short guidance message below the header. |

## Tips

- On first install, the dialog shows only the current version's notes. After an upgrade it shows all versions released since your last seen version, capped at five entries.
- If you closed the dialog before reading it, reopen it at any time via `Help > What's New...`. Using the menu always shows the full current version notes regardless of `LastSeenVersion`.

## Related

- [Re-read release notes later via Help menu](re-read-release-notes-later-via-help-menu.md)
- [Skip the current version's release notes](skip-the-current-version-s-release-notes.md)
- [Open the upgrade flow for a newer build](open-the-upgrade-flow-for-a-newer-build.md)
