# Rebind a keyboard shortcut

Use the Keyboard Shortcuts dialog to assign a different key to any action, or to reassign a key that is already in use.

## Before you start

- No radio connection is required to edit shortcuts.
- Confirm that keyboard shortcut processing is enabled via `View > Keyboard Shortcuts` (checkable item).

## Steps

1. Open `View > Configure Shortcuts...`.
2. Find the action you want to rebind. Either:
   - Click the target key on the keyboard map to select it, or
   - Locate the action in the action table. The table columns are **Action**, **Category**, **Current Key**, and **Default Key**. Use the **Filter:** field or the **Category:** combo box to narrow the list.
3. Click the key on the keyboard map that you want to use as the new binding. The **Key:** indicator updates to show the selected key.
4. In the **Action:** combo box, select the action you want to assign to that key.
5. If the key is already bound to a different action, a conflict dialog appears: "Key [X] is currently bound to 'Y'. Reassign it?" Click **Yes** to proceed or **No** to cancel.
6. The action table refreshes automatically. Confirm the **Current Key** column shows your new binding.
7. Click **Close**.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| Keyboard map | Visual display | QWERTY layout. Click a key to select it. |
| **Key:** | Indicator | Shows the currently selected key. Default: `(none)`. |
| **Action:** | Combo box | Assigns an action to the selected key. |
| **Category** | Indicator | Shows the category of the action assigned to the selected key. |
| **Clear** | Button | Removes the action assignment from the selected key. |
| **Reset to Default** | Button | Restores the default key for the action on the selected key. |
| **Filter:** | Text field | Filters the action table by text. |
| **Category:** | Combo box | Filters the action table by category. |
| Action table | List | All actions with columns: Action, Category, Current Key, Default Key. |
| **Reset All to Defaults** | Button | Resets every binding to its default key. Prompts for confirmation. |
| **Close** | Button | Closes the dialog. |

## Tips

- Keys are color-coded on the keyboard map by category. A legend below the map identifies each category color.
- To remove a binding without assigning a replacement, select the key on the keyboard map and click **Clear**.
- To find what key an action uses by default without changing anything, check the **Default Key** column in the action table.

## Troubleshooting

- **The Action: combo box does not respond after selecting a key** — No key is selected. The **Key:** indicator must show a key name (not `(none)`) before the **Action:** combo box takes effect. Click a key on the keyboard map first.
- **A key cannot be reassigned and the conflict dialog keeps appearing** — Click **Yes** in the conflict dialog to confirm the reassignment. Clicking **No** cancels the change and leaves the original binding intact.

## Related

- [Keyboard Shortcuts overview](overview.md)
- [Reset one shortcut to its default key](reset-one-shortcut-to-its-default-key.md)
- [Reset every shortcut back to defaults](reset-every-shortcut-back-to-defaults.md)
- [Find all actions in a category](find-all-actions-in-a-category.md)
- [See the default key for any action](see-the-default-key-for-any-action.md)
