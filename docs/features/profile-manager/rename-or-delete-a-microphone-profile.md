# Rename or delete a microphone profile

The Profile Manager lets you rename a microphone profile by saving the current radio state under a new name, and delete profiles you no longer need. Use this when you want to clean up the mic profile list or correct a profile name.

## Before you start

- AetherSDR must be connected to the radio. Profile Manager requires an active radio connection.
- Know the name of the profile you want to rename or delete.

## Steps

### To rename a microphone profile

There is no dedicated rename command. Rename a profile by saving it under a new name and then deleting the old one.

1. Open `Profiles > Profile Manager...`.
2. Click the **Microphone** tab.
3. Click the profile you want to rename in the **Profile list**. The name appears in the **Profile name** field.
4. Clear the **Profile name** field and type the new name.
5. Click **Save**. The radio saves the current mic settings under the new name and the **Profile list** updates.
6. Click the old profile name in the **Profile list**.
7. Click **Delete**. A confirmation dialog appears asking "Delete profile "*name*"?".
8. Click **Yes**.

### To delete a microphone profile

1. Open `Profiles > Profile Manager...`.
2. Click the **Microphone** tab.
3. Click the profile you want to delete in the **Profile list**.
4. Click **Delete**. A confirmation dialog appears asking "Delete profile "*name*"?".
5. Click **Yes**.
6. Click **Close** when finished.

## What each control does

| Control | Kind | Behavior | Setting key |
|---|---|---|---|
| **Microphone** tab | Tab | Shows the mic profile list and controls. | — |
| **Profile name** | Text field | Name used when saving a profile. Populated automatically when you select a profile from the list. | — |
| **Profile list** | List | All mic profiles on the radio; the active profile is highlighted. | — |
| **Load** | Button | Loads the selected profile onto the radio. Enabled only when a profile is selected. | — |
| **Save** | Button | Saves the current radio mic state under the name in **Profile name**. Falls back to the selected list item if the field is empty. | — |
| **Delete** | Button | Deletes the selected profile after confirmation. Enabled only when a profile is selected. | — |
| **Close** | Button | Closes the Profile Manager dialog. | — |

## Tips

- Selecting a profile in the **Profile list** automatically fills in the **Profile name** field, which makes it easy to copy the name before editing it for a rename.
- Load and Delete are disabled until you select a profile in the **Profile list**.
- The profile list refreshes automatically when the radio pushes an updated list; you do not need to close and reopen the dialog.

## Troubleshooting

- **Delete is greyed out** — No profile is selected in the **Profile list**. Click a profile name to select it, then click **Delete**.
- **Profile list is empty** — No microphone profiles exist on the radio yet. See [Create a separate mic profile per microphone](create-a-separate-mic-profile-per-microphone.md).
- **Saved profile does not appear in the list** — The radio pushes the updated list asynchronously. Wait a moment; the list will refresh without closing the dialog.

## Related

- [Profile Manager overview](overview.md)
- [Create a separate mic profile per microphone](create-a-separate-mic-profile-per-microphone.md)
- [Turn on auto-save so TX tweaks always persist](turn-on-auto-save-so-tx-tweaks-always-persist.md)
