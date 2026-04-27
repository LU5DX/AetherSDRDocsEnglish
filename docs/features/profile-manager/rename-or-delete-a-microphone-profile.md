# Rename or delete a microphone profile

The Profile Manager lets you rename a microphone profile by saving the current radio state under a new name, and delete profiles you no longer need. Use this to keep your microphone profile list tidy as your setup changes.

## Before you start

- AetherSDR must be connected to the radio. The Profile Manager requires an active radio connection.
- Know which profile you want to rename or delete. The active profile is highlighted in the list.

## Steps

### To rename a microphone profile

There is no in-place rename command. Renaming is a two-step process: save under the new name, then delete the old one.

1. Click `Profiles > Profile Manager...`.
2. Click the **Microphone** tab.
3. Click the profile you want to rename in the **Profile list**. Its name appears in the **Profile name** field.
4. Clear the **Profile name** field and type the new name.
5. Click **Save**. The radio saves the current microphone state under the new name and the list updates.
6. Click the original profile name in the **Profile list**.
7. Click **Delete**. A confirmation dialog appears asking "Delete profile "*name*"?".
8. Click **Yes**. The profile is removed from the list.
9. Click **Close**.

### To delete a microphone profile

1. Click `Profiles > Profile Manager...`.
2. Click the **Microphone** tab.
3. Click the profile you want to delete in the **Profile list**.
4. Click **Delete**. A confirmation dialog appears asking "Delete profile "*name*"?".
5. Click **Yes**. The profile is removed from the list.
6. Click **Close**.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Microphone** tab | Tab | Switches the dialog to manage microphone profiles. |
| **Profile name** | Text field | Holds the name used when saving a new profile. Populated automatically when you select a profile from the list. |
| **Profile list** | List | Shows all microphone profiles on the radio. The active profile is highlighted. |
| **Load** | Button | Loads the selected profile onto the radio. Enabled only when a profile is selected. |
| **Save** | Button | Saves the current microphone state under the name in **Profile name**. Falls back to the selected list item if the field is empty. |
| **Delete** | Button | Deletes the selected profile after confirmation. Enabled only when a profile is selected. |
| **Close** | Button | Closes the Profile Manager dialog. |

## Tips

- Selecting a profile in the **Profile list** automatically populates the **Profile name** field. For a rename, simply overwrite that text before clicking **Save**.
- Load and Delete are disabled until you select a profile in the list. If either button is greyed out, click a profile name first.
- The list refreshes automatically when the radio reports a change. You do not need to reopen the dialog after saving or deleting.

## Troubleshooting

- **Delete is greyed out** — No profile is selected in the **Profile list**. Click a profile name to select it, then click **Delete**.
- **The renamed profile does not appear in the list** — The radio pushes list updates asynchronously. Wait a moment for the list to refresh. If it does not update, close and reopen the Profile Manager.
- **The old profile name is still present after deleting** — You may have clicked **No** at the confirmation prompt. Repeat steps 3–5 and click **Yes** to confirm.

## Related

- [Profile Manager overview](overview.md)
- [Create a separate mic profile per microphone](create-a-separate-mic-profile-per-microphone.md)
- [Turn on auto-save so TX tweaks always persist](turn-on-auto-save-so-tx-tweaks-always-persist.md)
