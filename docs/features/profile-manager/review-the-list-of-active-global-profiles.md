# Review the list of active global profiles

Open the Profile Manager to see all global profiles stored on the radio and identify which one is currently active.

## Before you start

- AetherSDR must be connected to the radio. The Profile Manager requires an active radio connection.

## Steps

1. Click `Profiles > Profile Manager...` to open the Profile Manager dialog.
2. Click the **Global (tab)** if it is not already selected.
3. Read the **Profile list**. All global profiles stored on the radio appear here. The currently active profile is highlighted.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Global (tab)** | Tab | Shows global profiles. The active profile is highlighted in the **Profile list**. |
| **Profile list** | List | Displays all global profiles on the radio. The active profile is pre-selected when the dialog opens. |
| **Profile name** | Text field | Populated automatically when you select a profile in the list. Used when saving. |
| **Load** | Button | Loads the selected profile onto the radio. Enabled only when a profile is selected. |
| **Save** | Button | Saves the current radio state under the name typed in **Profile name**. |
| **Delete** | Button | Deletes the selected profile after confirmation. Enabled only when a profile is selected. |
| **Close** | Button | Closes the dialog. |

## Tips

- The **Profile list** updates automatically if the radio reports a change while the dialog is open. You do not need to reopen the dialog to see new profiles.
- Clicking a profile in the **Profile list** populates the **Profile name** field with that profile's name and enables the **Load** and **Delete** buttons.
- The active profile can also be loaded directly from the `Profiles` menu without opening the Profile Manager. Below the separator in that menu the radio populates a checkable list of global profiles; the currently active one is checked.

## Related

- [Profile Manager overview](overview.md)
- [Save the current radio state as a new global profile](save-the-current-radio-state-as-a-new-global-profile.md)
- [Switch to a saved transmit profile](switch-to-a-saved-transmit-profile.md)
