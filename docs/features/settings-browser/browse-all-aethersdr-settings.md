# Browse all AetherSDR settings

Open the Settings Browser to inspect and edit every AetherSDR setting in one place, including app-wide keys, the station section, and per-radio feature documents. Use it to change configuration that has no dedicated dialog, and to understand what each stored value is set to.

## Before you start

- AetherSDR must be running. A radio connection is **not** required.
- Settings edited here apply immediately and bypass each feature's own validation. Prefer the feature's dedicated UI when one exists.

## Steps

1. In the main window, go to **Settings > Settings Browser...**.
2. In the left pane, select a scope:
   - App keys (application-wide settings)
   - The station section
   - Any listed radio, identified by its nickname or radio ID
3. In the **Filter** field at the top right, type to narrow the key/value table to matching rows. Matching is case-insensitive and checks both keys and values.
4. To change a value, double-click the **Value** cell (or press **Enter**). Booleans show a **True**/**False** dropdown; everything else is free text.
5. Edit the value, then press **Enter** or click away to commit.
6. To add a new key, click **Add Key…**, enter the key name, and set its value.
7. To remove a key, select its row and click **Delete**.
8. When finished, click **Close**.

## What each control does

| Control | Behavior | Default | Notes |
| --- | --- | --- | --- |
| **Filter** (text field) | Filters the settings table live as you type. Case-insensitive substring match over keys and values of the selected scope. | Empty | |
| **Add Key…** (button) | Adds a new key to the selected scope. | | |
| **Delete** (button) | Deletes the selected setting. | | |
| **Refresh** (button) | Reloads the tree from the settings store. | | |
| **Export Sanitized…** (button) | Exports a sanitized diagnostic text dump of the settings store. | | Diagnostic output only, not a backup; credential-shaped values are redacted. |
| **Close** (button) | Closes the dialog. | | |

## Tips

- The banner at the top warns that edits apply immediately and bypass validation. If a setting misbehaves, change it back or use the dedicated UI instead.
- Rows whose values contain credential-shaped data (for example, passwords or tokens) render partially redacted and are read-only. Editing them would overwrite the real secret with the redacted placeholder.
- Use **Refresh** after changing settings elsewhere in AetherSDR to make sure the browser shows the current store.

## Troubleshooting

- **A value shows `[REDACTED]` and won't let me edit** — The value contains credential-shaped data. AetherSDR masks it for safety and prevents accidental overwrite. Use the feature's own settings dialog to change it.
- **My edit appears to have no effect** — The setting may be read at startup or require a radio reconnect. Check the relevant feature's dialog for a note, or restart AetherSDR.

## Related

- [Edit a settings value from the Settings Browser](edit-a-settings-value-from-the-settings-browser.md)
- [Export a diagnostic settings dump](export-a-diagnostic-settings-dump.md)
- [Settings Browser overview](overview.md)
