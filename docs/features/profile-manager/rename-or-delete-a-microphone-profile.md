# Profile Manager

The Profile Manager dialog creates, renames, loads, and deletes Global, Transmit, and Microphone profiles on the radio, and controls automatic saving of transmit changes.

## Before you start

- AetherSDR must be connected to the radio. The Profile Manager requires an active radio connection.
- Know which profile you want to rename or delete. The active profile is highlighted in the list.

## Opening the Profile Manager

Click `Profiles > Profile Manager...`.

## Working with profiles

### To rename a microphone profile

There is no in-place rename command. Renaming is a two-step process: create a new profile with the desired name, then delete the old one.

1. Click `Profiles > Profile Manager...`.
2. Click the **Microphone** tab.
3. Click the profile you want to rename in the **Profile list**. Its name appears in the **Profile name** field.
4. Clear the **Profile name** field and type the new name.
5. Click **Save**. The radio creates a new microphone profile under the new name and the list updates.
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

### To load or delete a transmit profile

1. Click `Profiles > Profile Manager...`.
2. Click the **Transmit** tab.
3. Click the profile you want to load or delete in the **Profile list**.
4. Click **Load** to apply the selected transmit profile to the radio.
5. Click **Delete** to remove the selected transmit profile after confirmation.

### To save a global profile

1. Click `Profiles > Profile Manager...`.
2. Click the **Global** tab.
3. Type a name in the **Profile name** field.
4. Click **Save**. The dialog displays a status message indicating the result. If the radio does not respond within 15 seconds, the status message is cleared.

### To enable or disable auto-save of transmit changes

1. Click `Profiles > Profile Manager...`.
2. Click the **Auto-Save** tab.
3. Check or uncheck **Auto-save profile changes**. The radio state updates immediately. The checkbox reads the radio's live auto-save status, not a local setting.

## What each control does

| Control                       | Kind       | Behavior                                                                                                                                                                                                                                                                                                                                          |
|-------------------------------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Global** tab                | Tab        | Switches the dialog to manage global profiles.                                                                                                                                                                                                                                                                                                    |
| **Transmit** tab              | Tab        | Switches the dialog to manage transmit profiles.                                                                                                                                                                                                                                                                                                  |
| **Microphone** tab            | Tab        | Switches the dialog to manage microphone profiles.                                                                                                                                                                                                                                                                                                |
| **Auto-Save** tab             | Tab        | Switches the dialog to control automatic profile saving.                                                                                                                                                                                                                                                                                          |
| **Profile name**              | Text field | Holds the name used when saving a new profile. Populated automatically when you select a profile from the list. The **Save** button is disabled when the field is empty. Retyping the name clears any status message from the previous save operation.                                                                                            |
| **Profile list**              | List       | Shows all profiles for the selected category on the radio. The active profile is highlighted. Double-clicking a profile loads it immediately.                                                                                                                                                                                                     |
| **Load**                      | Button     | Loads the selected profile onto the radio. Enabled only when a profile is selected. Disabled styling (greyed out) distinguishes the "no selection" state from an enabled button.                                                                                                                                                                 |
| **Save** (Global tab)         | Button     | Saves the current radio state under the name in **Profile name**. Disabled when the **Profile name** field is empty. After clicking, a status line appears below the buttons showing success or error information. The status line is hidden when you start typing a new name.                                                                   |
| **Save** (Transmit/Mic tab)   | Button     | Labeled **Create** on Transmit and Microphone tabs. Creates a new profile with the name in **Profile name**. Disabled when the **Profile name** field is empty. After clicking, a status line appears below the buttons showing success or error information. The status line is hidden when you start typing a new name.                          |
| **Delete**                    | Button     | Deletes the selected profile after confirmation. Enabled only when a profile is selected. Disabled styling (greyed out) distinguishes the "no selection" state from an enabled button.                                                                                                                                                           |
| **Auto-save profile changes** | Checkbox   | When enabled, transmit changes are written back to the active transmit profile automatically. The checkbox reads and writes the radio's live auto-save state directly. Setting is not persisted via `AutoSaveTransmitProfile` in AppSettings. Toggling sends `profile autosave on` or `profile autosave off` to the radio. New in v26.7.4. |
| **Close**                     | Button     | Closes the Profile Manager dialog.                                                                                                                                                                                                                                                                                                                |

## Status messages

After saving or creating a profile, a status line appears below the Save/Create and Delete buttons. The status line indicates whether the operation succeeded or failed:

- Success messages appear in a light blue color.
- Error messages appear in a light red color.

The status line disappears when you start typing in the **Profile name** field, or when 15 seconds have elapsed without a radio response after clicking Save on a global profile.

## Tips

- Selecting a profile in the **Profile list** automatically populates the **Profile name** field. For a rename, simply overwrite that text before clicking **Save**.
- Load, Delete, Save, and Create are disabled until a valid target exists. If a button is greyed out, check that a profile is selected (for Load/Delete) or that the **Profile name** field is not empty (for Save/Create).
- Double-click a profile in the list to load it immediately, bypassing the **Load** button.
- The list refreshes automatically when the radio reports a change. You do not need to reopen the dialog after creating or deleting.
- Microphone profiles cannot be overwritten directly. To update an existing microphone profile, enable **Auto-save profile changes** on the **Auto-Save** tab and then make your changes while the profile is active.
- The **Auto-save profile changes** checkbox stays in sync with the radio: if auto-save is toggled by another client or by the profile load process, the checkbox updates automatically.
- The **Load** button for transmit profiles uses the `profile tx load` command internally. This change is transparent and does not affect how you interact with the dialog.

## Troubleshooting

- **Delete is greyed out** — No profile is selected in the **Profile list**. Click a profile name to select it, then click **Delete**.
- **Save is greyed out** — The **Profile name** field is empty. Type a profile name to enable the button.
- **Save appears but the new profile does not show in the list** — The radio pushes list updates asynchronously. Wait a moment for the list to refresh. If it does not update, close and reopen the Profile Manager.
- **I get a "Profile already exists" dialog** — You attempted to create a microphone profile with a name that already exists. The radio cannot overwrite microphone profiles. Click **Enable Auto-Save** in the dialog to turn on automatic profile saving, then load the existing profile and make your changes to update it.
- **The old profile name is still present after deleting** — You may have clicked **No** at the confirmation prompt. Repeat steps 3–5 and click **Yes** to confirm.
- **Transmit profile load fails** — Ensure the radio is connected and the transmit profile name is valid. The dialog uses the `profile tx load` command for loading transmit profiles.
- **The status message stays on screen too long** — If the radio does not respond within 15 seconds to a global profile save, the status message is cleared automatically.

## Related

- [Profile Manager overview](overview.md)
- [Create a separate mic profile per microphone](create-a-separate-mic-profile-per-microphone.md)
- [Turn on auto-save so TX tweaks always persist](turn-on-auto-save-so-tx-tweaks-always-persist.md)