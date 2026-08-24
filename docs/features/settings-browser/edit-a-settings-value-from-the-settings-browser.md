# Edit a settings value from the Settings Browser

This page explains how to edit any AetherSDR setting directly from the Settings Browser, useful for configuration that has no dedicated UI.

## Before you start

- AetherSDR must be running. The Settings Browser works without a radio connection.
- You have a specific AppSettings key in mind, or you can locate it by filtering.

## Steps

1. Open the Settings Browser: `Settings > Settings Browser...`.
2. In the left pane, select the scope containing the setting: application, station, or a specific radio (identified by nickname or serial number).
3. In the **Filter** field, type part of the key or value to narrow the list. The tree filters live as you type.
4. Locate the row you want to edit. The key is in the left column; the value is in the right column.
5. Double-click the value cell, or select the row and press **Enter** (or **Return**).
6. Edit the value:
   - Boolean values (shown as `True` or `False`) present a dropdown with only two choices.
   - All other values are free-text. Type the new value.
7. Press **Enter** or click elsewhere to commit the change.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| Scope tree (left pane) | Lists settings scopes: app keys, station section, and each radio's feature documents. | Radio scopes show the nickname when an Identity document exists. |
| **Filter** | Case-insensitive substring match over keys and values of the selected scope. | Not a persisted setting. |
| Value table | Shows key/value pairs for the selected scope. Editing is enabled. | Credential-shaped values are masked and read-only. |
| **Add Key…** | Adds a new key to the selected scope. | Use only when you know the exact key name and expected format. |
| **Delete** | Removes the selected setting. | Deletion is immediate. |
| **Refresh** | Reloads the settings tree from the store. | Use after external changes. |
| **Export Sanitized…** | Writes a secret-redacted diagnostic dump. | Not a restorable backup; credential-shaped values are redacted. |
| **Close** | Closes the dialog. | |

## Tips

- Edits apply immediately and bypass each feature's own validation. Prefer the feature's own UI when one exists.
- A yellow banner at the top of the dialog warns about this behavior. Heed it before changing values.
- Boolean values are stored as the literal strings `True` and `False`. The dropdown prevents typos like `Ture`.

## Troubleshooting

- **The value cell won't enter edit mode** — The row is read-only because the value is credential-shaped (contains a password, key, or token) or because it is a feature document. Feature documents open in a viewer instead; credential-shaped values cannot be edited here.
- **I changed a value and now a feature misbehaves** — The Settings Browser bypasses validation. Use **Refresh** (or reopen the dialog) to confirm the stored value, then correct it or restore the prior value from memory or a backup.

## Related

- [Settings Browser overview](overview.md)
- [Browse all AetherSDR settings](browse-all-aethersdr-settings.md)
- [Export a diagnostic settings dump](export-a-diagnostic-settings-dump.md)
