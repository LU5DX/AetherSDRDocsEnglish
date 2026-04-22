# Save the current radio state as a new global profile

Use this page to capture the radio's current state into a named global profile so you can recall it later. Global profiles store settings such as mode, frequency, and band configuration across the entire radio.

## Before you start

- AetherSDR must be connected to the radio. Profile Manager requires an active radio connection.
- Decide on a name for the new profile before you begin.

## Steps

1. Click `Profiles > Profile Manager...` to open the Profile Manager dialog.
2. Click the **Global** tab.
3. In the **Profile name** field, type the name for the new profile.
4. Click **Save**.

The radio saves its current state under the name you typed. The **Profile list** updates automatically when the radio confirms the save.

## What each control does

| Control | Kind | Behavior | Setting key |
|---|---|---|---|
| **Global (tab)** | Tab | Switches to global profile management. | — |
| **Profile name** | Text field | Name used when saving a new profile. If the field is empty when you click Save, the name of the currently selected list item is used instead. | — |
| **Profile list** | List | Shows all saved global profiles. The active profile is highlighted. | — |
| **Load** | Button | Loads the selected profile onto the radio. Enabled only when a profile is selected. | — |
| **Save** | Button | Saves the current radio state under the name in **Profile name**. | — |
| **Delete** | Button | Deletes the selected profile after a confirmation prompt. Enabled only when a profile is selected. | — |
| **Close** | Button | Closes the Profile Manager dialog. | — |

## Tips

- You can also load a profile by double-clicking its entry in the **Profile list** — no need to click **Load** separately.
- Selecting an existing profile in the **Profile list** copies its name into the **Profile name** field. Type a different name before clicking **Save** if you want to create a new profile instead of overwriting the existing one.
- To have transmit and microphone setting changes saved back to the active profile automatically, enable **Auto-save profile changes** on the **Auto-Save** tab. That setting is stored as `AutoSaveTransmitProfile`.

## Related

- [Profile Manager overview](overview.md)
- [Review the list of active global profiles](review-the-list-of-active-global-profiles.md)
- [Switch to a saved transmit profile](switch-to-a-saved-transmit-profile.md)
- [Turn on auto-save so TX tweaks always persist](turn-on-auto-save-so-tx-tweaks-always-persist.md)
