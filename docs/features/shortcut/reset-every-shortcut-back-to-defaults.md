# Keyboard Shortcuts (v26.6.1)

The Keyboard Shortcuts dialog lets you view, assign, and reset keyboard bindings for all actions in AetherSDR. Changes take effect immediately.

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
3. Click **Close**.

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
| **Reset All to Defaults** button | Resets every binding to its default key. A confirmation prompt appears before any changes are applied. |
| **Close** button | Closes the dialog. |

## Tips

- To check what the default key for a specific action is before resetting, consult the **Default Key** column in the action table.
- If you only want to reset a single shortcut rather than all of them, use **Reset to Default** after selecting the relevant key on the keyboard map.

## Related

- [Reset one shortcut to its default key](reset-one-shortcut-to-its-default-key.md)
- [Rebind a keyboard shortcut](rebind-a-keyboard-shortcut.md)
- [See the default key for any action](see-the-default-key-for-any-action.md)
- [Keyboard Shortcuts overview](overview.md)