# What's New — AetherSDR Overview

The What's New dialog shows release notes for versions you have not yet seen. It appears automatically after an upgrade and is also available on demand from the Help menu.

## How it works

When AetherSDR starts, it compares the current version against the version stored in `LastSeenVersion`. If the current version is newer, the dialog opens automatically and displays the release notes for each version between the last seen and the current one, up to a maximum of five releases. On a first install, where no `LastSeenVersion` has been recorded, the dialog shows only the notes for the current version with a welcome header instead of the standard "What's New" heading.

When you open the dialog manually via `Help > What's New...`, it shows all entries for the current version regardless of `LastSeenVersion`.

Release entries are rendered as styled HTML in a scrollable browser. Each entry can carry a version number, a release date, a short headline, and a list of individual changes. Changes are color-coded by category:

| Category | Indicator color |
|---|---|
| Feature | Blue |
| Bug Fix | Red-orange |
| Improvement | Green |
| Infrastructure | Gray |

Dismissing the dialog with "Got it — 73!" records the current version in `LastSeenVersion` so the dialog does not reappear for that version.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| Release notes browser | Scrollable HTML view | Displays the filtered release notes. Read-only; external links are not opened inline. |
| `Got it — 73!` | Button | Closes the dialog and marks the current version as seen by updating `LastSeenVersion`. |
| `Upgrade` | Button | Visible only when a newer build is available. Opens the AetherSDR releases page in your default browser and closes the dialog. |
| `Skip this version` | Button | Visible only when a newer build is available. Writes the current version to `LastSeenVersion` and closes the dialog without upgrading, suppressing the upgrade prompt for this version. |
| Hint | Footer indicator | Displays a short guidance line directing you to the lightbulb button in the title bar for bug reports and ideas. |

## Tips

- To re-read release notes after dismissing the dialog, use `Help > What's New...` at any time. This opens the dialog in show-all mode and does not modify `LastSeenVersion`.
- If you click `Skip this version`, the upgrade prompt will not appear again for that build, but you can still open the dialog manually via `Help > What's New...`.

## Related

- [Read what changed in the new version](read-what-changed-in-the-new-version.md)
- [Re-read release notes later via Help menu](re-read-release-notes-later-via-help-menu.md)
- [Open the upgrade flow for a newer build](open-the-upgrade-flow-for-a-newer-build.md)
- [Skip the current version's release notes](skip-the-current-version-s-release-notes.md)
