# Rename or delete a microphone profile

The Profile Manager lets you rename a microphone profile by saving the current radio state under a new name, then deleting the old one. Use this page to clean up outdated mic profiles or give them more descriptive names.

## Before you start

- AetherSDR must be connected to the radio. Profile Manager requires an active radio connection.
- Know the name of the profile you want to rename or delete. Open the Microphone tab to review the list if needed.

## Steps

### To rename a microphone profile

The radio does not provide a direct rename command. Rename by saving under a new name, then deleting the old one.

1. Click `Profiles > Profile Manager...`.
2. Click the **Microphone** tab.
3. In the **Profile list**, click the profile you want to rename. Its name appears in the **Profile name** field.
4. Clear the **Profile name** field and type the new name.
5. Click **Save**. The radio saves the current mic state under the new name and the **Profile list** updates.
6. In the **Profile list**, click the old profile name.
7. Click **Delete**.
8. When prompted "Delete profile "…"?", click **Yes**.
9. Click **Close**.

### To delete a microphone profile

1. Click `Profiles > Profile Manager...`.
2. Click the **Microphone** tab.
3. In the **Profile list**, click the profile you want to delete.
4. Click **Delete**.
5. When prompted "Delete profile "…"?", click **Yes**.
6. Click **Close**.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Microphone** tab | Tab | Shows all microphone profiles stored on the radio. |
| **Profile name** | Text field | Holds the name used when Save is clicked. Populated automatically when you select a profile from the list. |
| **Profile list** | List | All microphone profiles on the radio; the active profile is highlighted. |
| **Load** | Button | Loads the selected profile onto the radio. Enabled only when a profile is selected. |
| **Save** | Button | Saves the current radio mic state under the name in the **Profile name** field. |
| **Delete** | Button | Deletes the selected profile after confirmation. Enabled only when a profile is selected. |
| **Close** | Button | Closes the dialog. |

## Tips

- Selecting a profile in the **Profile list** automatically fills the **Profile name** field with that profile's name, which saves typing when renaming.
- Double-clicking a profile in the **Profile list** loads it immediately, the same as clicking **Load**.
- If `AutoSaveTransmitProfile` is enabled, mic setting changes are written back to the active profile automatically. Verify which profile is active before deleting to avoid losing recent changes. See [Turn on auto-save so TX tweaks always persist](turn-on-auto-save-so-tx-tweaks-always-persist.md).

## Troubleshooting

- **Delete is greyed out** — No profile is selected in the **Profile list**. Click a profile name to select it, then click **Delete**.
- **Profile list does not update after Save or Delete** — The radio pushes the updated list via status message. If the list does not refresh within a few seconds, close and reopen Profile Manager to force a reload.

## Related

- [Profile Manager overview](overview.md)
- [Create a separate mic profile per microphone](create-a-separate-mic-profile-per-microphone.md)
- [Turn on auto-save so TX tweaks always persist](turn-on-auto-save-so-tx-tweaks-always-persist.md)
