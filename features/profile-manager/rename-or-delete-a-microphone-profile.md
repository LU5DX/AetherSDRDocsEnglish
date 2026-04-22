# Rename or delete a microphone profile

The Profile Manager lets you rename a microphone profile by saving the current radio state under a new name, and delete profiles you no longer need. Use this to keep your mic profile list tidy when microphone setups change.

## Before you start

- AetherSDR must be connected to the radio. Profile Manager requires an active radio connection.
- Know the name of the profile you want to rename or delete.

## Steps

### To rename a microphone profile

The radio does not provide a direct rename command. Rename by saving under a new name, then deleting the old one.

1. Click `Profiles > Profile Manager...`.
2. Click the **Microphone** tab.
3. In the **Profile list**, click the profile you want to rename. Its name appears in the **Profile name** field.
4. Clear the **Profile name** field and type the new name.
5. Click **Save**. The radio saves the current microphone state under the new name and the **Profile list** updates.
6. In the **Profile list**, click the old profile name.
7. Click **Delete**. A confirmation dialog appears asking `Delete profile "<name>"?`.
8. Click **Yes**. The profile is removed from the **Profile list**.

### To delete a microphone profile

1. Click `Profiles > Profile Manager...`.
2. Click the **Microphone** tab.
3. In the **Profile list**, click the profile you want to delete.
4. Click **Delete**. A confirmation dialog appears asking `Delete profile "<name>"?`.
5. Click **Yes**. The profile is removed from the **Profile list**.
6. Click **Close** when finished.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Microphone** tab | Tab | Switches the dialog to show microphone profiles. |
| **Profile name** | Text field | Holds the name used when clicking Save. Populated automatically when you select a profile from the list. |
| **Profile list** | List | Shows all microphone profiles on the radio. The active profile is highlighted. |
| **Load** | Button | Loads the selected profile onto the radio. Enabled only when a profile is selected. |
| **Save** | Button | Saves the current radio microphone state under the name in **Profile name**. |
| **Delete** | Button | Deletes the selected profile after confirmation. Enabled only when a profile is selected. |
| **Close** | Button | Closes the dialog. |

## Tips

- Selecting a profile in the **Profile list** automatically copies its name into the **Profile name** field, so you only need to edit the part of the name you want to change before clicking **Save**.
- Load and Delete are disabled until you select a profile from the **Profile list**. If both buttons appear greyed out, click a profile name in the list first.
- The **Profile list** refreshes automatically when the radio confirms a change. You do not need to reopen the dialog.

## Troubleshooting

- **Delete is greyed out** — No profile is selected. Click a name in the **Profile list** to select it, then click **Delete**.
- **Save produces a duplicate rather than a rename** — This is expected. Save creates the new name first; then select and delete the old profile as described in the rename steps above.
- **Profile list does not update after Save or Delete** — The list refreshes when the radio sends a confirmation. If it does not update, check the radio connection and try reopening the dialog via `Profiles > Profile Manager...`.

## Related

- [Profile Manager overview](overview.md)
- [Create a separate mic profile per microphone](create-a-separate-mic-profile-per-microphone.md)
- [Turn on auto-save so TX tweaks always persist](turn-on-auto-save-so-tx-tweaks-always-persist.md)
