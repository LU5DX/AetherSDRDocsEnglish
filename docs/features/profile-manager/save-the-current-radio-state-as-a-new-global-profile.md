# Save the current radio state as a new global profile

Use this page to capture the radio's current state — frequencies, modes, and settings — as a named global profile you can reload later.

## Before you start

- AetherSDR must be connected to the radio. Profile Manager requires an active radio connection.
- Decide on a name for the new profile before you open the dialog.

## Steps

1. Click `Profiles > Profile Manager...`.
2. Click the **Global** tab.
3. In the **Profile name** field, type the name for the new profile.
4. Click **Save**.

The radio saves the current state under that name. The **Profile list** updates automatically when the radio confirms the new profile.

## What each control does

| Control | Kind | Behavior | Setting key |
|---|---|---|---|
| **Global (tab)** | Tab | Switches to the global profile view. | — |
| **Profile name** | Text field | Name used when saving a new profile. If left blank, Save uses the name of the currently selected item in the Profile list. | — |
| **Profile list** | List | Shows all existing global profiles. The active profile is highlighted. | — |
| **Load** | Button | Loads the selected profile onto the radio. Enabled only when a profile is selected. | — |
| **Save** | Button | Saves the current radio state under the name typed in Profile name. | — |
| **Delete** | Button | Deletes the selected profile after a confirmation prompt. Enabled only when a profile is selected. | — |
| **Close** | Button | Closes the Profile Manager dialog. | — |

## Tips

- If you select an existing profile in the **Profile list**, its name fills the **Profile name** field automatically. Clicking **Save** at that point overwrites that profile with the current radio state.
- You can also load a profile by double-clicking its entry in the **Profile list** instead of using **Load**.
- To have transmit changes written back to the active profile automatically, enable **Auto-save profile changes** on the **Auto-Save** tab. This setting is stored as `AutoSaveTransmitProfile`.

## Troubleshooting

- **Save does nothing** — Check that the **Profile name** field is not empty and no profile in the list is selected with a blank name field. At least one source of a name must be present for Save to act.
- **Profile list does not update after saving** — The list refreshes when the radio sends a status update. If it does not appear, verify the radio connection is still active via `Settings > Connect to Radio...`.

## Related

- [Profile Manager overview](overview.md)
- [Review the list of active global profiles](review-the-list-of-active-global-profiles.md)
- [Switch to a saved transmit profile](switch-to-a-saved-transmit-profile.md)
- [Turn on auto-save so TX tweaks always persist](turn-on-auto-save-so-tx-tweaks-always-persist.md)
