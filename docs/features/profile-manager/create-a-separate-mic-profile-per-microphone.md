# Create a separate mic profile per microphone

Use the Profile Manager to save a named microphone profile for each physical microphone you use. Switching profiles then restores the correct mic settings without manual adjustment.

## Before you start

- AetherSDR must be connected to the radio. Profile Manager requires an active radio connection.
- Configure the radio's mic settings (gain, EQ, etc.) for the first microphone before saving.

## Steps

1. Open `Profiles > Profile Manager...`.
2. Click the **Microphone** tab.
3. Type a name for this microphone in the **Profile name** field (for example, the microphone model or use case).
4. Click **Save**. The profile is created on the radio and appears in the **Profile list**.
5. Connect or select your second microphone and adjust the radio's mic settings for it.
6. Repeat steps 3–4 with a different name for the second microphone.
7. To switch between microphones, select the corresponding profile in the **Profile list** and click **Load**, or double-click the profile name. The radio loads those mic settings immediately.
8. Click **Close** when finished.

## What each control does

| Control | Kind | Behavior | Setting key |
|---|---|---|---|
| **Microphone** (tab) | Tab | Manages microphone profiles stored on the radio. | — |
| **Profile name** | Text field | Name used when saving a new profile. Populated automatically when you select an existing profile from the list. | — |
| **Profile list** | List | All microphone profiles on the radio; the active profile is highlighted. | — |
| **Load** | Button | Loads the selected profile onto the radio. Enabled only when a profile is selected. | — |
| **Save** | Button | Saves the current radio mic state under the name in **Profile name**. If the field is empty, saves over the selected profile. | — |
| **Delete** | Button | Deletes the selected profile after a confirmation prompt. Enabled only when a profile is selected. | — |
| **Close** | Button | Closes the Profile Manager dialog. | — |

## Tips

- Selecting a profile in the **Profile list** copies its name into the **Profile name** field. Edit that name before clicking **Save** to save as a new profile rather than overwriting.
- If you want mic changes to persist automatically to the active profile without a manual **Save**, enable **Auto-save profile changes** on the **Auto-Save** tab. This is controlled by the `AutoSaveTransmitProfile` setting.

## Related

- [Turn on auto-save so TX tweaks always persist](turn-on-auto-save-so-tx-tweaks-always-persist.md)
- [Rename or delete a microphone profile](rename-or-delete-a-microphone-profile.md)
- [Profile Manager overview](overview.md)
