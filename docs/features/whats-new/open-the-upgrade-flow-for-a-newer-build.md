# Open the Upgrade Flow for a Newer Build

When a newer build of AetherSDR is available, the What's New dialog shows an "Upgrade" button that opens the download page in your browser. This page explains how to reach that button.

## Before you start

- The "Upgrade" button appears only when AetherSDR has detected that a newer build is available. If no upgrade is available, the button is not shown.
- No radio connection is required.

## Steps

1. Open `Help > What's New...`.
2. Review the release notes in the scrollable browser at the top of the dialog.
3. Click `Upgrade`.

AetherSDR opens the AetherSDR releases page in your default web browser and closes the dialog.

## What each control does

| Control | Kind | Behavior | Persisted setting |
|---|---|---|---|
| Release notes browser | Scrollable HTML view | Displays release entries between the last seen version and the current version. Shows at most 5 recent releases. | — |
| `Upgrade` | Button | Visible only when an upgrade is available. Opens the download page and closes the dialog. | — |
| `Got it — 73!` | Button | Dismisses the dialog and marks the current version as seen. | `LastSeenVersion` |
| `Skip this version` | Button | Suppresses the release reminder for this version and marks it as seen. | `LastSeenVersion` |
| Hint | Indicator | Short footer line with guidance. | — |

## Tips

- If you close the dialog with `Got it — 73!` instead of `Upgrade`, AetherSDR records the current version in `LastSeenVersion` and will not prompt you again for this release. You can still return to the dialog via `Help > What's New...`.
- If you click `Skip this version`, `LastSeenVersion` is set to the current version and the nag for this release is suppressed, but the download page is not opened.

## Related

- [Re-read release notes later via Help menu](re-read-release-notes-later-via-help-menu.md)
- [Read what changed in the new version](read-what-changed-in-the-new-version.md)
- [Skip the current version's release notes](skip-the-current-version-s-release-notes.md)
