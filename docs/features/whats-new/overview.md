# What's New — AetherSDR overview

The What's New dialog shows release notes for versions of AetherSDR you have not yet seen. It appears automatically after an update and is also available on demand from the Help menu.

## How it works

When AetherSDR starts, it compares the current version against the value stored in `LastSeenVersion`. If the current version is newer, the dialog opens automatically and displays the release notes for every version between the last seen version and the current one, capped at the five most recent releases. On a first install, where `LastSeenVersion` has no stored value, the dialog shows only the current version's notes and greets you with a welcome header instead of a version-change header.

When you open the dialog via `Help > What's New...`, it shows all entries for the current version regardless of what `LastSeenVersion` contains.

Release entries are displayed as styled HTML in a scrollable browser. Each entry can include a version number, a release date, a short headline, and a list of individual changes. Changes are color-coded by category:

| Category | Indicator color |
|---|---|
| Feature | Blue |
| Bug Fix | Red-orange |
| Improvement | Green |
| Infrastructure | Grey |

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| Release notes browser | Scrollable text area | Displays styled HTML release notes for versions newer than `LastSeenVersion`, up to five releases. |
| `Got it — 73!` | Button | Dismisses the dialog and marks the current version as seen by updating `LastSeenVersion`. |
| `Upgrade` | Button | Visible only when an upgrade is available. Opens the AetherSDR releases download page and closes the dialog. |
| `Skip this version` | Button | Visible only when an upgrade is available. Writes the current version to `LastSeenVersion` and closes the dialog, suppressing the upgrade prompt for this version. |
| Hint | Footer indicator | Displays a short line of guidance below the header. |

The `Upgrade` and `Skip this version` buttons appear only when AetherSDR has detected that a newer build is available.

## Tips

- To re-read the release notes at any time without triggering an upgrade prompt, use `Help > What's New...`. This path always shows the current version's notes.
- The Hint footer points to the lightbulb button in the title bar for submitting bug reports or feature ideas.

## Related

- [Read what changed in the new version](read-what-changed-in-the-new-version.md)
- [Re-read release notes later via Help menu](re-read-release-notes-later-via-help-menu.md)
- [Open the upgrade flow for a newer build](open-the-upgrade-flow-for-a-newer-build.md)
- [Skip the current version's release notes](skip-the-current-version-s-release-notes.md)
