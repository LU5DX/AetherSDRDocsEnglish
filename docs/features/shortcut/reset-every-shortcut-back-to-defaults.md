# Keyboard Shortcuts (v26.7.4)

The Keyboard Shortcuts dialog lets you view, assign, reset, import, and export keyboard bindings for all actions in AetherSDR. Changes take effect immediately.

## Opening the dialog

- Open `View > Configure Shortcuts...`.

## Keyboard map

The upper portion of the dialog shows a visual QWERTY keyboard layout. Click any key to select it. The selected key is highlighted, and its label appears in the **Key:** indicator.

## Assigning a shortcut

1. Click a key on the keyboard map.
2. The **Key:** indicator shows the selected key.
3. In the **Action:** combo box, select the action you want to assign.
4. The **Category:** indicator shows the category of the selected action.

## Clearing a shortcut

1. Click the key on the keyboard map that has the assignment you want to remove.
2. Click **Clear**. The key becomes unbound.

## Resetting a single shortcut to its default

1. Select the key on the keyboard map.
2. Click **Reset to Default**. The key returns to its factory binding.

## Filtering the action table

The action table in the lower portion of the dialog lists all actions with columns for **Action**, **Category**, **Current Key**, and **Default Key**.

- Use the **Filter:** text field to filter actions by name.
- Use the **Category:** combo box to filter by action category.

Select a row in the table to edit its binding directly.

## Resetting all shortcuts to defaults

1. Click **Reset All to Defaults** in the bottom-left corner of the dialog.
2. When the confirmation prompt appears, click **Yes**.

## Importing shortcuts from a file

1. Click **Import...** in the bottom row of buttons.
2. In the file dialog, navigate to a CSV file containing AetherSDR keyboard shortcut definitions and click **Open**.
3. A summary dialog shows the number of imported shortcuts. If any actions in the file are not available in this AetherSDR release, they are skipped and listed in the dialog's details. If any imported shortcuts displace existing local bindings, those displaced actions are also listed.
4. The action table updates to reflect the imported bindings.

## Exporting shortcuts to a file

1. Click **Export...** in the bottom row of buttons.
2. In the file dialog, choose a location and filename for the CSV file and click **Save**.
3. A confirmation dialog shows the number of exported shortcuts and the file path.

The exported CSV file can be shared with other AetherSDR users or used as a personal backup. The file uses the `.csv` extension.

## Closing the dialog

- Click **Close**. Changes take effect immediately; there is no separate Save step.

## Indicator state

When the dialog is in key-capture mode (after clicking a key on the keyboard map), the next keypress is captured as the new binding. The **Key:** indicator updates to show the captured key.

## What each control does

| Control | Behavior |
|---|---|
| Keyboard map (visual QWERTY layout) | Click a key to select it for editing. |
| **Key:** indicator | Shows the selected key. |
| **Action:** combo box | Assigns an action to the selected key. |
| **Category:** indicator | Shows the category of the selected action. |
| **Clear** button | Removes the assignment from the selected key. |
| **Reset to Default** button | Restores the default key for the selected action. |
| **Filter:** text field | Filters the action table by text. |
| **Category:** combo box | Filters the action table by category. |
| Action table (list) | All actions with columns: Action, Category, Current Key, Default Key. Select a row to edit. |
| **Import...** button | Opens a file dialog to import keyboard shortcuts from a CSV backup file. |
| **Export...** button | Opens a file dialog to export keyboard shortcuts to a portable CSV backup file. |
| **Reset All to Defaults** button | Resets every binding to its default key. A confirmation prompt appears before any changes are applied. |
| **Close** button | Closes the dialog. |

## Tips

- To check what the default key for a specific action is before resetting, consult the **Default Key** column in the action table.
- If you only want to reset a single shortcut rather than all of them, use **Reset to Default** after selecting the relevant key on the keyboard map.
- Export your shortcuts regularly as a backup before making major changes.
- Import and export use the CSV format, making it easy to share or version-control your shortcuts.

## Related

- [Reset one shortcut to its default key](reset-one-shortcut-to-its-default-key.md)
- [Rebind a keyboard shortcut](rebind-a-keyboard-shortcut.md)
- [See the default key for any action](see-the-default-key-for-any-action.md)
- [Keyboard Shortcuts overview](overview.md)