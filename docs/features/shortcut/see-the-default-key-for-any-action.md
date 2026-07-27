# See the default key for any action

The action table in the Keyboard Shortcuts dialog shows the default key for every action alongside its current binding, so you can check what a shortcut was originally set to without changing anything.

## Before you start

- No radio connection is required.

## Steps

1. Click `View > Configure Shortcuts...` to open the Keyboard Shortcuts dialog.
2. In the action table, locate the action you want to check. Each row shows four columns: **Action**, **Category**, **Current Key**, and **Default Key**.
3. Read the value in the **Default Key** column for that action.

To narrow the list, type part of the action name into the `Filter:` field, or select a category from the `Category:` combo box above the table.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| `Keyboard map` | Indicator | Visual QWERTY layout; click a key to select it. |
| `Key:` | Indicator | Shows the selected key. |
| `Action:` | Combo box | Assigns an action to the selected key. |
| `Category` | Indicator | Shows the category of the selected action. |
| `Clear` | Push button | Removes the assignment from the selected key. |
| `Reset to Default` | Push button | Restores the default key for the selected action. |
| `Filter:` | Text field | Filters the action table to rows whose Action or Category text matches what you type. |
| `Category:` | Combo box | Filters the action table to a single category. Defaults to **All**. |
| Action table | List | Displays all actions with columns: Action, Category, Current Key, Default Key. Select a row to edit. |
| `Import...` | Push button | Imports keyboard shortcut bindings from a CSV file. |
| `Export...` | Push button | Exports current keyboard shortcut bindings to a CSV file. |
| `Reset All to Defaults` | Push button | Resets every binding to its default key. |
| `Close` | Push button | Closes the dialog. |

## Importing and exporting keyboard shortcuts

You can back up your customized keyboard shortcuts or transfer them to another instance of AetherSDR using CSV files.

### Import shortcuts from a CSV file

1. Click `Import...` at the bottom of the Keyboard Shortcuts dialog.
2. In the file dialog, navigate to the CSV file and select it.
3. Click **Open**. AetherSDR imports the bindings and updates the action table.
   - If any actions in the file are not available in this AetherSDR release, they are skipped and listed in the detailed error text.
   - If any imported bindings conflict with existing local bindings, those local bindings are cleared and listed in the information dialog.

### Export shortcuts to a CSV file

1. Click `Export...` at the bottom of the Keyboard Shortcuts dialog.
2. In the file dialog, choose a location and filename for the CSV file.
3. Click **Save**. AetherSDR writes all current keyboard shortcut bindings to the file.

The import/export dialog remembers the last directory you used for subsequent operations.

## Tips

- The **Default Key** column always reflects the factory default, even after you have rebound or cleared the action. Use it as a reference before deciding whether to restore a binding.
- To restore a single action to the value shown in **Default Key**, select its row, then click `Reset to Default`. See [Reset one shortcut to its default key](reset-one-shortcut-to-its-default-key.md).
- Export your shortcuts periodically as a backup before making extensive changes.

## Related

- [Keyboard Shortcuts overview](overview.md)
- [Find all actions in a category](find-all-actions-in-a-category.md)
- [Reset one shortcut to its default key](reset-one-shortcut-to-its-default-key.md)
- [Reset every shortcut back to defaults](reset-every-shortcut-back-to-defaults.md)