# Save the current radio state as a new global profile

Use the Profile Manager to capture the radio's current state and store it as a named global profile. Global profiles record overall radio configuration and can be recalled at any time from the Profiles menu.

## Before you start

- AetherSDR must be connected to the radio. The Profile Manager requires an active radio connection.
- Decide on a name for the new profile before you begin.

## Steps

1. Click `Profiles > Profile Manager...` to open the Profile Manager dialog.
2. Click the **Global (tab)** tab.
3. In the **Profile name** field, type the name for the new profile.
4. Click **Save**.

The radio saves the current state under the name you entered. The **Profile name** field clears, and the radio pushes an updated list back to AetherSDR. The new profile appears in the **Profile list**.

## What each control does

| Control | Kind | Behavior | Setting key |
|---|---|---|---|
| **Global (tab)** | Tab | Switches to the global profile view. | — |
| **Profile name** | Text field | Name used when saving a new profile. If empty when you click Save, the name of the selected item in the Profile list is used instead. | — |
| **Profile list** | List | Shows all global profiles stored on the radio. The active profile is highlighted. | — |
| **Load** | Button | Loads the selected profile onto the radio. Enabled only when a profile is selected. | — |
| **Save** | Button | Saves the current radio state under the name typed in Profile name. | — |
| **Delete** | Button | Deletes the selected profile after a confirmation prompt. Enabled only when a profile is selected. | — |
| **Close** | Button | Closes the Profile Manager dialog. | — |

## Tips

- You can also load a profile by double-clicking its entry in the **Profile list** without clicking **Load**.
- If you select an existing profile from the **Profile list**, its name is copied into the **Profile name** field automatically. Clicking **Save** at that point overwrites that profile with the current radio state.
- Saved global profiles appear in the dynamic list under `Profiles` in the menu bar and can be loaded with a single click from there.

## Related

- [Profile Manager overview](overview.md)
- [Review the list of active global profiles](review-the-list-of-active-global-profiles.md)
- [Switch to a saved transmit profile](switch-to-a-saved-transmit-profile.md)
- [Turn on auto-save so TX tweaks always persist](turn-on-auto-save-so-tx-tweaks-always-persist.md)
