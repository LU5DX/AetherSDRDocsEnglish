# Review the list of active global profiles

The Profile Manager shows all global profiles stored on the radio and highlights the one currently in use. Use this when you want to confirm which profiles exist or identify the active one before loading or deleting.

## Before you start

- AetherSDR must be connected to the radio. The Profile Manager requires an active radio connection.

## Steps

1. Click `Profiles > Profile Manager...` to open the Profile Manager dialog.
2. Click the **Global (tab)** tab if it is not already selected.
3. Review the **Profile list**. The active profile is highlighted.

## What each control does

| Control                       | Kind       | Behavior                                                                                                                                                                                                                                                                              |
|-------------------------------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Global (tab)**              | Tab        | Displays the global profiles list for the connected radio.                                                                                                                                                                                                                            |
| **Transmit (tab)**            | Tab        | Displays the transmit profiles list for the connected radio.                                                                                                                                                                                                                          |
| **Microphone (tab)**          | Tab        | Displays the microphone profiles list for the connected radio.                                                                                                                                                                                                                        |
| **Auto-Save (tab)**           | Tab        | Controls automatic profile saving for transmit and microphone profiles.                                                                                                                                                                                                               |
| **Profile list**              | List       | Shows all profiles for the selected tab. The currently active profile is highlighted.                                                                                                                                                                                                 |
| **Profile name**              | Text field | Name used when saving or creating a new profile. When empty, the Save/Create button is disabled to prevent accidental saves with no target.                                                                                                                                           |
| **Load**                      | Button     | Loads the selected profile onto the radio. Enabled only when a profile is selected.                                                                                                                                                                                                   |
| **Save** / **Create**         | Button     | On the **Global (tab)**, saves the current radio state under the name in **Profile name**. On the **Transmit (tab)** or **Microphone (tab)**, creates a new profile; it does not overwrite an existing one. Disabled when **Profile name** is empty.                                  |
| **Delete**                    | Button     | Deletes the selected profile after a confirmation prompt. Enabled only when a profile is selected.                                                                                                                                                                                    |
| **Auto-save profile changes** | Checkbox   | When enabled, TX and microphone changes are written back to the active profile automatically. Reads and writes the radio model directly. State reflects the live radio state, not local settings. On toggle, sends `profile autosave on/off` to the radio.                            |
| **Close**                     | Button     | Closes the dialog.                                                                                                                                                                                                                                                                    |
| **Status message**            | Label      | Shows a result message after each Save or Create operation. Displays the profile name and save status in blue on success, or an error message in red on failure. Hidden until a result is available. Automatically clears when you start typing a new profile name.                   |

## Status message behavior

- A **Save** or **Create** click shows a status line below the buttons.
- On success: displays the profile name with a confirmation message in blue text.
- On failure: displays an error description in red text.
- The status message clears automatically when you begin typing in the **Profile name** field.
- The status line is hidden when there is no message to display, so it does not add extra height to the dialog.

## Tips

- The **Profile list** updates automatically if the radio pushes a new profile list while the dialog is open. You do not need to close and reopen the dialog to see changes.
- The active profile is shown highlighted in the list. If no item appears highlighted, no profile of that type is currently loaded on the radio.
- On the **Transmit (tab)** and **Microphone (tab)**, the **Save** button is labelled **Create** because the radio cannot overwrite existing transmit or microphone profiles directly. Updates to existing profiles are captured by Auto-Save while the profile is active. Enable **Auto-save profile changes** on the **Auto-Save (tab)** so changes follow the active profile.
- If you try to create a transmit or microphone profile with a name that already exists and Auto-Save is off, AetherSDR will prompt you to enable Auto-Save so your changes to that profile are captured.
- The **Auto-save profile changes** checkbox stays synchronized with the radio's Auto-Save state even when that state changes from outside the dialog. For example, if you enable Auto-Save through the "Enable Auto-Save" prompt or if a remote SmartSDR client or TCI client changes it, the checkbox updates to match.
- The **Save** and **Create** buttons are disabled when the **Profile name** field is empty, preventing accidental saves with no target profile name.
- The `Profiles` menu also shows a dynamic checkable list of global profiles below the separator. You can see the active profile at a glance there without opening the Profile Manager.

## Related

- [Profile Manager overview](overview.md)
- [Save the current radio state as a new global profile](save-the-current-radio-state-as-a-new-global-profile.md)
- [Switch to a saved transmit profile](switch-to-a-saved-transmit-profile.md)