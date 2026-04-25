# Review the list of active global profiles

The Profile Manager shows all global profiles stored on the radio and highlights the one currently active. Use this when you want to confirm which profile is loaded or find the name of a profile before loading, saving, or deleting it.

## Before you start

- AetherSDR must be connected to the radio. Profile Manager requires an active radio connection.

## Steps

1. Click `Profiles > Profile Manager...` to open the Profile Manager dialog.
2. Click the **Global (tab)** tab if it is not already selected.
3. Read the **Profile list**. Every global profile stored on the radio appears here. The currently active profile is highlighted.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Global (tab)** | Tab | Shows global profile management. Contains the profile list for global profiles. |
| **Profile list** | List | Displays all global profiles on the radio. The active profile is highlighted. Selecting an entry enables Load and Delete and copies the name into the Profile name field. |
| **Profile name** | Text field | Shows the name of the selected profile. Used as the name when saving a new profile. |
| **Load** | Button | Loads the selected profile onto the radio. Disabled until a profile is selected. |
| **Save** | Button | Saves the current radio state under the name in the Profile name field. |
| **Delete** | Button | Deletes the selected profile after a confirmation prompt. Disabled until a profile is selected. |
| **Close** | Button | Closes the dialog. |

## Tips

- The profile list updates automatically if the radio reports a change while the dialog is open. You do not need to close and reopen the dialog to see additions or removals.
- Double-clicking a profile in the list loads it onto the radio immediately, the same as selecting it and clicking Load.
- To check which global profile is active without opening the dialog, click `Profiles` in the menu bar. The radio populates a checkable list of global profiles below the separator; the active one is checked.

## Related

- [Profile Manager overview](overview.md)
- [Save the current radio state as a new global profile](save-the-current-radio-state-as-a-new-global-profile.md)
- [Switch to a saved transmit profile](switch-to-a-saved-transmit-profile.md)
