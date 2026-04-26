# Create a separate mic profile per microphone

Use the Profile Manager to save a named microphone profile for each physical microphone you use. Switching mics then takes one load operation instead of manually adjusting mic settings each time.

## Before you start

- AetherSDR must be connected to the radio. Profile Manager requires an active radio connection.
- Configure the radio's mic settings (gain, EQ, etc.) for the microphone you want to capture before saving.

## Steps

1. Open `Profiles > Profile Manager...`.
2. Click the **Microphone** tab.
3. Adjust your radio's microphone settings to match the first microphone if you have not already done so.
4. Click the **Profile name** field and type a name for this microphone (for example, the microphone model or position).
5. Click **Save**. The new profile appears in the **Profile list**.
6. Repeat steps 3–5 for each additional microphone, using a distinct name each time.

To switch to a saved mic profile later, select it in the **Profile list** and click **Load**, or double-click the profile name directly.

## What each control does

| Control | Kind | Behavior | Setting key |
|---|---|---|---|
| **Microphone** tab | Tab | Shows the microphone profile list and controls. | — |
| **Profile name** | Text field | Name used when saving a new mic profile. Populated automatically when you select a profile from the list. | — |
| **Profile list** | List | All saved microphone profiles; the active one is highlighted. | — |
| **Load** | Button | Loads the selected mic profile onto the radio. Enabled only when a profile is selected. | — |
| **Save** | Button | Saves the current radio mic state under the name typed in **Profile name**. If **Profile name** is empty and a profile is selected, saves over that profile's name. | — |
| **Delete** | Button | Deletes the selected mic profile after a confirmation prompt. Enabled only when a profile is selected. | — |
| **Close** | Button | Closes the Profile Manager dialog. | — |

## Tips

- Selecting a profile from the **Profile list** copies its name into the **Profile name** field. Clear the field and type a new name before clicking **Save** to create a new profile rather than overwriting the existing one.
- The **Profile list** updates automatically if the radio pushes changes while the dialog is open.
- If you also use transmit profiles, consider enabling **Auto-save profile changes** on the **Auto-Save** tab so that mic adjustments made during a session are written back to the active profile automatically. This setting is persisted as `AutoSaveTransmitProfile`.

## Troubleshooting

- **Load and Delete are grayed out** — No profile is selected. Click a name in the **Profile list** to select it.
- **Clicking Save does nothing** — Both the **Profile name** field and the **Profile list** selection are empty. Type a name in **Profile name** before clicking **Save**.
- **Profile list is empty** — The radio has no saved microphone profiles yet. Create the first one using the steps above.

## Related

- [Profile Manager overview](overview.md)
- [Rename or delete a microphone profile](rename-or-delete-a-microphone-profile.md)
- [Turn on auto-save so TX tweaks always persist](turn-on-auto-save-so-tx-tweaks-always-persist.md)
- [Switch to a saved transmit profile](switch-to-a-saved-transmit-profile.md)
