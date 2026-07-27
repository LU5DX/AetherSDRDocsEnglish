# Turn on auto-save so TX tweaks always persist

When auto-save is enabled, any changes you make to TX and microphone settings are written back to the active profile automatically, so you never lose a tweak by forgetting to save manually.

## Before you start

- AetherSDR must be connected to the radio. The Profile Manager requires an active radio connection.
- At least one transmit or microphone profile must already exist on the radio for auto-save to have a profile to write to.

## Steps

1. Click `Profiles > Profile Manager...` to open the Profile Manager dialog.
2. Click the **Auto-Save** tab.
3. Check **Auto-save profile changes**.
4. Click **Close**.

The setting takes effect immediately. AetherSDR sends the change to the radio; no restart is required.

To turn auto-save off, repeat the steps and uncheck **Auto-save profile changes**.

## What each control does

| Control                                   | Kind        | Behavior                                                                                                                                                                                                                                                                                     |
|-------------------------------------------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Global**                                | Tab         | Manages global profiles.                                                                                                                                                                                                                                                                     |
| **Transmit**                              | Tab         | Manages transmit profiles. Note: the radio cannot overwrite existing transmit profiles directly — the Save/Create button is labelled "Create" and creates a new profile only. Updates to existing profiles are captured by Auto-Save while the profile is active.                            |
| **Microphone**                            | Tab         | Manages microphone profiles. Note: the radio cannot overwrite existing microphone profiles directly — the Save/Create button is labelled "Create" and creates a new profile only. Updates to existing profiles are captured by Auto-Save while the profile is active.                        |
| **Auto-Save**                             | Tab         | Controls automatic profile saving.                                                                                                                                                                                                                                                           |
| **Profile name**                          | Text field  | Name used when saving a new profile. Empty field disables the Save/Create button. Typing or editing the field clears any status message shown on that tab.                                                                                                                                   |
| **Profile list**                          | List        | All profiles for this category; active one highlighted. Double-click loads the profile.                                                                                                                                                                                                      |
| **Load**                                  | Push button | Loads the selected profile onto the radio. Disabled when no profile is selected.                                                                                                                                                                                                             |
| **Save** (Global tab)                     | Push button | Saves the current radio state under the typed name (creates or overwrites). Disabled when the profile name field is empty. After clicking, shows a status message ("Saving...", "Saved", or an error) below the buttons. The timeout for a save response is 15 seconds.                      |
| **Create** (Transmit and Microphone tabs) | Push button | Creates a new profile with the typed name. Does not overwrite an existing profile. Disabled when the profile name field is empty. After clicking, shows a status message ("Saving...", "Saved", or an error) below the buttons. The timeout for a save response is 15 seconds.               |
| **Delete**                                | Push button | Deletes the selected profile (with confirmation). Disabled when no profile is selected.                                                                                                                                                                                                      |
| **Auto-save profile changes**             | Checkbox    | When enabled, TX changes are written back to the active profile automatically. State is read live from the radio model, not from local settings. When disabled, changes are discarded unless you save manually. Sends `profile autosave on/off` to the radio on toggle.                        |
| **Close**                                 | Push button | Closes the dialog.                                                                                                                                                                                                                                                                           |

## Tips

- The Save/Create button is disabled when the profile name field is empty, preventing accidental clicks on a button that would do nothing.
- After clicking Save or Create, a status message appears below the buttons showing "Saving...", "Saved" (in blue), or an error (in red). The status clears automatically when you type or edit the profile name field.
- Auto-save applies to both TX and microphone settings, not just one category. If you want to experiment without overwriting your current profile, uncheck **Auto-save profile changes** first, make your changes, and evaluate before committing a manual save.
- The checkbox reflects the current state reported by the radio when the dialog opens. If another client changed the setting on the radio, the checkbox updates to match. The checkbox also stays in sync with Auto-Save flips that originate outside AetherSDR, such as loading a profile, TCI clients, or remote SmartSDR clients.
- On the Transmit and Microphone tabs, if you enter a name that already exists and click **Create**, a dialog explains the limitation and offers to enable Auto-Save so your changes to the existing profile are captured. If you click **Enable Auto-Save**, the checkbox on the Auto-Save tab is updated automatically.

## Related

- [Switch to a saved transmit profile](switch-to-a-saved-transmit-profile.md)
- [Save the current radio state as a new global profile](save-the-current-radio-state-as-a-new-global-profile.md)
- [Profile Manager overview](overview.md)