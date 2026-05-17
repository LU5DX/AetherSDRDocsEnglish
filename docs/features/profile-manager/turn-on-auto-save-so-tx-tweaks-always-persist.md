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

| Control | Kind | Behavior | Setting key |
|---|---|---|---|
| **Global** | Tab | Manages global profiles. | — |
| **Transmit** | Tab | Manages transmit profiles. Note: the radio cannot overwrite existing transmit profiles directly — the Save/Create button is labelled "Create" and creates a new profile only. Updates to existing profiles are captured by Auto-Save while the profile is active. | — |
| **Microphone** | Tab | Manages microphone profiles. Note: the radio cannot overwrite existing microphone profiles directly — the Save/Create button is labelled "Create" and creates a new profile only. Updates to existing profiles are captured by Auto-Save while the profile is active. | — |
| **Auto-Save** | Tab | Controls automatic profile saving. | — |
| **Profile name** | Text field | Name used when saving a new profile. | — |
| **Profile list** | List | All profiles for this category; active one highlighted. | — |
| **Load** | Push button | Loads the selected profile onto the radio. | — |
| **Save** (Global tab) | Push button | Saves the current radio state under the typed name (creates or overwrites). | — |
| **Create** (Transmit and Microphone tabs) | Push button | Creates a new profile with the typed name. Does not overwrite an existing profile. | — |
| **Delete** | Push button | Deletes the selected profile (with confirmation). | — |
| **Auto-save profile changes** | Checkbox | When checked, TX and microphone setting changes are automatically saved to the active profile on the radio. When unchecked, changes are discarded unless you save manually. | `AutoSaveTransmitProfile` |
| **Close** | Push button | Closes the dialog. | — |

## Tips

- Auto-save applies to both TX and microphone settings, not just one category. If you want to experiment without overwriting your current profile, uncheck **Auto-save profile changes** first, make your changes, and evaluate before committing a manual save.
- The checkbox reflects the current state reported by the radio when the dialog opens. If another client changed the setting on the radio, the checkbox updates to match.
- On the Transmit and Microphone tabs, if you enter a name that already exists and click **Create**, a dialog explains the limitation and offers to enable Auto-Save so your changes to the existing profile are captured.

## Related

- [Switch to a saved transmit profile](switch-to-a-saved-transmit-profile.md)
- [Save the current radio state as a new global profile](save-the-current-radio-state-as-a-new-global-profile.md)
- [Profile Manager overview](overview.md)