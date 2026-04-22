# Review the List of Active Global Profiles

The Profile Manager shows all global profiles stored on the radio, with the currently active one highlighted. Use this to see which profiles exist and which one is loaded.

## Before you start

- AetherSDR must be connected to the radio. The Profile Manager requires an active radio connection.

## Steps

1. Click `Profiles > Profile Manager...` to open the Profile Manager dialog.
2. Click the `Global (tab)` tab if it is not already selected.
3. Read the `Profile list`. All global profiles stored on the radio are shown here. The currently active profile is highlighted.

## What each control does

| Control | Description |
|---|---|
| `Global (tab)` | Switches the dialog to global profile management. |
| Profile list | Displays all global profiles on the radio. The active profile is highlighted. Selecting an entry populates the `Profile name` field and enables `Load` and `Delete`. |
| `Load` | Loads the selected profile onto the radio. Also triggered by double-clicking a profile in the list. |
| `Save` | Saves the current radio state under the name typed in `Profile name`. |
| `Delete` | Deletes the selected profile after a confirmation prompt. |
| `Profile name` | Text field used to name a profile before saving. Populated automatically when you select a profile from the list. |
| `Close` | Closes the dialog. |

## Tips

- The profile list updates automatically if the radio reports a change while the dialog is open. You do not need to close and reopen the dialog to see a fresh list.
- The `Profiles` menu also shows a dynamic list of global profiles below a separator. Each entry is checkable and indicates the currently loaded profile without opening the Profile Manager.

## Related

- [Profile Manager overview](overview.md)
- [Save the current radio state as a new global profile](save-the-current-radio-state-as-a-new-global-profile.md)
- [Switch to a saved transmit profile](switch-to-a-saved-transmit-profile.md)
