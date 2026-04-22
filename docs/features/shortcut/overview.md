# Keyboard Shortcuts Overview

AetherSDR lets you assign keyboard shortcuts to application actions and edit those bindings at any time. Use the Keyboard Shortcuts dialog to view, reassign, clear, or reset bindings without restarting the application.

## Before you start

- No radio connection is required to open or use the shortcut editor.
- Keyboard shortcut processing must be enabled. Confirm that `View > Keyboard Shortcuts` is checked.

## How it works

Open the editor at `View > Configure Shortcuts...`. The dialog has two main areas: a visual keyboard map at the top, and a filterable action table below.

**Keyboard map** — A QWERTY layout showing all keys. Keys with assigned actions are color-coded by category. A legend below the map shows which color corresponds to which category. Click any key to select it; the panel below the map updates to show what is assigned to that key.

**Selected key panel** — Appears between the keyboard map and the action table. When a key is selected:

- `Key:` shows the selected key name. Default: `(none)` when nothing is selected.
- `Action:` is a combo box. Choose an action from the list to assign it to the selected key.
- `Category` shows the category of the currently assigned action.
- Click `Clear` to remove the assignment from the selected key.
- Click `Reset to Default` to restore the default key for the action assigned to the selected key.

If you assign a key that is already bound to a different action, AetherSDR prompts you to confirm the reassignment before making the change.

**Action table** — Lists every available action. Columns are Action, Category, Current Key, and Default Key. Click a row to select it and reflect that action in the selected key panel.

- `Filter:` narrows the table by typing any part of an action name or category name.
- `Category:` filters the table to a single category. Default selection is `All`.

**Bottom controls**

- `Reset All to Defaults` — Resets every binding to its default key. AetherSDR asks for confirmation before proceeding.
- `Close` — Closes the dialog.

## Tips

- The action table always shows both the current and default key for each action, so you can see at a glance what has been changed.
- Selecting a row in the action table and selecting a key on the keyboard map are independent operations. Assign a binding by selecting a key on the map first, then choosing the action from the `Action:` combo.

## Related

- [Rebind a keyboard shortcut](rebind-a-keyboard-shortcut.md)
- [Reset one shortcut to its default key](reset-one-shortcut-to-its-default-key.md)
- [Reset every shortcut back to defaults](reset-every-shortcut-back-to-defaults.md)
- [Find all actions in a category](find-all-actions-in-a-category.md)
- [See the default key for any action](see-the-default-key-for-any-action.md)
