# Open the upgrade flow for a newer build

When a newer build of AetherSDR is available, the What's New — AetherSDR dialog shows an Upgrade button that opens the download page directly. This page explains how to reach that button.

## Before you start

- The Upgrade button appears only when AetherSDR has detected that a newer build is available. If no upgrade is pending, the button is not shown.
- No radio connection is required.

## Steps

1. Open `Help > What's New...`.
2. In the What's New — AetherSDR dialog, review the release notes in the release notes browser.
3. Click `Upgrade`.

AetherSDR opens the AetherSDR releases page in your default browser and closes the dialog.

## What each control does

| Control | Kind | Behavior | Persisted setting |
|---|---|---|---|
| Release notes browser | Scrollable view | Displays styled HTML release notes for versions newer than `LastSeenVersion` up to the current version. Shows at most 5 releases. | — |
| `Got it — 73!` | Button | Dismisses the dialog and marks the current version as seen. | `LastSeenVersion` |
| `Upgrade` | Button | Visible only when an upgrade is available. Opens the download page and closes the dialog. | — |
| `Skip this version` | Button | Visible only when an upgrade is available. Suppresses the upgrade prompt for the current version and closes the dialog. | `LastSeenVersion` |
| Hint | Indicator | Displays a short footer line with guidance. | — |

## Tips

- If you click `Skip this version` instead of `Upgrade`, AetherSDR writes the current version to `LastSeenVersion` and will not prompt you about this release again. You can still return to the dialog later via `Help > What's New...`, but the Upgrade button will not reappear for the skipped version.
- Clicking `Got it — 73!` also marks the version as seen without opening the download page.

## Related

- [Re-read release notes later via Help menu](re-read-release-notes-later-via-help-menu.md)
- [Read what changed in the new version](read-what-changed-in-the-new-version.md)
- [Skip the current version's release notes](skip-the-current-version-s-release-notes.md)
