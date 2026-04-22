# Reset one shortcut to its default key

Use this page to restore a single keyboard shortcut to the key it shipped with, without affecting any other bindings.

## Before you start

- Open `View > Configure Shortcuts...` to reach the Keyboard Shortcuts dialog.
- Identify the action whose binding you want to restore. If you are not sure what the default key is, check the **Default Key** column in the action table.

## Steps

1. Open `View > Configure Shortcuts...`.
2. In the action table, locate the action you want to reset. Use the **Filter:** field or the **Category:** combo box to narrow the list if needed.
3. Click the row in the action table to select the action.
4. On the keyboard map, confirm that the correct key is highlighted and shown in the **Key:** indicator.
5. Click **Reset to Default**.

The binding is immediately restored to the action's default key. The action table updates to show the change in the **Current Key** column.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| Keyboard map | Visual indicator | QWERTY layout; click a key to select it and populate the **Key:** indicator. |
| **Key:** | Indicator | Shows the currently selected key. Displays `(none)` when no key is selected. |
| **Action:** | Combo box | Shows the action assigned to the selected key. |
| **Category** | Indicator | Shows the category of the action assigned to the selected key. |
| **Reset to Default** | Button | Restores the default key for the action currently assigned to the selected key. |
| **Filter:** | Text field | Filters the action table by text. |
| **Category:** | Combo box | Filters the action table by category. |
| Action table | List | All actions with columns: Action, Category, Current Key, Default Key. |
| **Reset All to Defaults** | Button | Resets every binding to its default key — use with caution. |
| **Close** | Button | Closes the dialog. |

## Tips

- The **Default Key** column in the action table always shows the factory default, even after you have changed the binding. Use it to confirm what **Reset to Default** will restore before clicking.
- If the action you want is assigned to a key that conflicts with another binding, resetting one action may free up a key for another. Check the **Current Key** column after resetting.

## Related

- [Keyboard Shortcuts overview](overview.md)
- [Rebind a keyboard shortcut](rebind-a-keyboard-shortcut.md)
- [Reset every shortcut back to defaults](reset-every-shortcut-back-to-defaults.md)
- [See the default key for any action](see-the-default-key-for-any-action.md)
- [Find all actions in a category](find-all-actions-in-a-category.md)
