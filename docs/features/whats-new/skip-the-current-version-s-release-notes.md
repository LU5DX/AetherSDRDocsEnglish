# Skip the current version's release notes

When AetherSDR detects a newer version is available, the What's New dialog includes an option to stop it from reappearing for that version. Use this if you have seen the notes and do not want the dialog shown again on next launch.

## Before you start

- The "Skip this version" button appears only when an upgrade is available. If no upgrade is detected, the button is not shown.
- The What's New dialog must be open. It opens automatically after a version change, or manually via `Help > What's New...`.

## Steps

1. Open the What's New dialog. If it is not already on screen, go to `Help > What's New...`.
2. Confirm that the "Skip this version" button is visible in the footer. If it is absent, no upgrade has been detected and skipping is not applicable.
3. Click "Skip this version".

The dialog closes. AetherSDR writes the current version string to `LastSeenVersion` and saves it. The What's New dialog will not appear automatically on the next launch for this version.

## What each control does

| Control | Kind | Behavior | Setting key |
|---|---|---|---|
| Release notes browser | Scrollable HTML view | Displays release entries between the last seen version and the current version. | — |
| "Got it — 73!" | Button | Dismisses the dialog and marks the version as seen. | `LastSeenVersion` |
| "Upgrade" | Button | Shown only when an upgrade is available. Opens the download page. | — |
| "Skip this version" | Button | Shown only when an upgrade is available. Saves the current version to `LastSeenVersion` and closes the dialog so the nag does not reappear. | `LastSeenVersion` |
| Hint | Indicator | Short footer line with guidance. | — |

## Tips

- "Skip this version" and "Got it — 73!" both write to `LastSeenVersion`. The practical difference is intent: "Got it — 73!" acknowledges the current release notes, while "Skip this version" dismisses the upgrade prompt without further action.
- To re-read release notes at any time, use `Help > What's New...`. This opens the dialog regardless of the saved `LastSeenVersion` value.

## Troubleshooting

- **"Skip this version" is not visible** — The button only appears when AetherSDR has detected that an upgrade is available. If no upgrade is detected, only "Got it — 73!" is shown. This is expected behavior.

## Related

- [Re-read release notes later via Help menu](re-read-release-notes-later-via-help-menu.md)
- [Open the upgrade flow for a newer build](open-the-upgrade-flow-for-a-newer-build.md)
- [Read what changed in the new version](read-what-changed-in-the-new-version.md)
