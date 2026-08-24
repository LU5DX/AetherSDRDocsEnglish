# Settings Browser overview

The Settings Browser gives you a complete, searchable view of every AetherSDR setting in one place — including scope-grouped trees for the app, the station, and each radio's feature documents. It's primarily a diagnostic and advanced-editing tool for settings that don't have a dedicated UI, letting you inspect and change values directly with live filtering and a sanitized export for support.

## How it works

The Settings Browser opens via **Settings > Settings Browser...** and presents a scope tree on the left (application settings, the station section, and each connected radio's feature documents), with a key-value table for the selected scope on the right.

It is an advanced tool:

- Edits apply immediately and bypass each feature's own validation.
- Prefer the feature's dedicated UI when one exists.
- Credential-shaped values (passwords, tokens) are masked and read-only, so you can't accidentally overwrite a secret with a redacted placeholder.

The dialog includes a warning banner at the top to remind you of this.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| **Filter** | Live, case-insensitive substring match over the keys and values of the selected scope. | Shown at the top of the right pane. |
| **Add Key…** | Adds a new settings key to the selected scope. | Empty values aren't allowed. |
| **Delete** | Deletes the selected setting. | Only enabled when a non-read-only row is selected. |
| **Refresh** | Rebuilds the scope tree to reflect any settings the radio or other processes have changed underneath the dialog. | Useful after external modifications. |
| **Export Sanitized…** | Writes a secret-redacted diagnostic text dump of the settings store to a file. | Diagnostic output only — not a restorable backup. |
| **Close** | Closes the dialog. | |

In the value table, boolean values (`True`/`False`) are edited with a two-entry dropdown to prevent typos like `Ture`. Double-click a value (or select a row and press **Enter**) to edit it; feature document rows open a viewer dialog instead of inline editing.

## Tips

- Use **Filter** to find a key quickly — it searches both keys and values, so you can type part of a value to locate the setting that holds it.
- Radios are shown by their **Identity** nickname when one is set; family-wide defaults appear as `(family-wide defaults)`.
- The dialog remembers its window size and position between sessions.
- If you fix a typo, press **Refresh** to re-read the current store state.

## Troubleshooting

- **I can't edit a setting I expected to change** — Credential-shaped values are intentionally read-only and masked. Make the change from the feature's own UI instead.
- **A feature document shows `(corrupt)`** — The stored JSON couldn't be parsed. The raw value is still shown for diagnosis; you can overwrite it with a valid document via **Add Key…**.

## Related

- [Browse all AetherSDR settings](browse-all-aethersdr-settings.md)
- [Edit a settings value from the Settings Browser](edit-a-settings-value-from-the-settings-browser.md)
- [Export a diagnostic settings dump](export-a-diagnostic-settings-dump.md)
