# Review the list of active global profiles

The Profile Manager shows all global profiles stored on the radio and highlights the one currently in use. Use this when you want to confirm which profiles exist or identify the active one before loading or deleting.

## Before you start

- AetherSDR must be connected to the radio. The Profile Manager requires an active radio connection.

## Steps

1. Click `Profiles > Profile Manager...` to open the Profile Manager dialog.
2. Click the **Global (tab)** tab if it is not already selected.
3. Review the **Profile list**. The active profile is highlighted.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Global (tab)** | Tab | Displays the global profiles list for the connected radio. |
| **Profile list** | List | Shows all global profiles stored on the radio. The currently active profile is highlighted. |
| **Profile name** | Text field | Populated automatically when you select a profile from the list. Used when saving. |
| **Load** | Button | Loads the selected profile onto the radio. Enabled only when a profile is selected. |
| **Save** | Button | Saves the current radio state under the name in **Profile name**. |
| **Delete** | Button | Deletes the selected profile after a confirmation prompt. Enabled only when a profile is selected. |
| **Close** | Button | Closes the dialog. |

## Tips

- The **Profile list** updates automatically if the radio pushes a new profile list while the dialog is open. You do not need to close and reopen the dialog to see changes.
- The active profile is shown highlighted in the list. If no item appears highlighted, no global profile is currently loaded on the radio.
- The `Profiles` menu also shows a dynamic checkable list of global profiles below the separator. You can see the active profile at a glance there without opening the Profile Manager.

## Related

- [Profile Manager overview](overview.md)
- [Save the current radio state as a new global profile](save-the-current-radio-state-as-a-new-global-profile.md)
- [Switch to a saved transmit profile](switch-to-a-saved-transmit-profile.md)
