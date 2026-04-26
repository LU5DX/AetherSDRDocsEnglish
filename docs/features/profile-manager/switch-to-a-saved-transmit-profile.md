# Switch to a saved transmit profile

Use this page to apply a previously saved transmit profile to the radio. Loading a transmit profile restores the TX settings stored under that profile name.

## Before you start

- AetherSDR must be connected to the radio. Profile Manager requires an active radio connection.
- At least one transmit profile must already exist on the radio. If the profile list is empty, see [Save the current radio state as a new global profile](save-the-current-radio-state-as-a-new-global-profile.md) for how to create and save profiles.

## Steps

1. Click `Profiles > Profile Manager...` to open the Profile Manager dialog.
2. Click the `Transmit (tab)` tab.
3. In the profile list, click the profile you want to load. The active profile is highlighted.
4. Click `Load`.

Alternatively, double-click a profile name in the list to load it immediately without clicking `Load`.

5. Click `Close` when done.

## What each control does

| Control | Kind | Behavior | Persisted setting |
|---|---|---|---|
| `Transmit (tab)` | Tab | Shows all transmit profiles stored on the radio. | — |
| Profile list | List | Displays all transmit profiles; the currently active profile is highlighted. Click a name to select it. | — |
| Profile name | Text field | Populated automatically when you select a profile from the list. | — |
| `Load` | Button | Sends the selected profile to the radio, replacing current TX settings. Enabled only when a profile is selected. | — |
| `Save` | Button | Saves the current radio TX state under the name in the Profile name field. | — |
| `Delete` | Button | Deletes the selected profile after confirmation. Enabled only when a profile is selected. | — |
| `Close` | Button | Closes the Profile Manager dialog. | — |

## Tips

- Selecting a profile in the list populates the Profile name field with that profile's name. If you then click `Save`, the radio overwrites that profile with the current TX state.
- To have TX changes written back to the active profile automatically after loading it, enable `Auto-save profile changes` on the `Auto-Save (tab)` tab. This is controlled by the `AutoSaveTransmitProfile` setting.

## Related

- [Turn on auto-save so TX tweaks always persist](turn-on-auto-save-so-tx-tweaks-always-persist.md)
- [Profile Manager overview](overview.md)
- [Rename or delete a microphone profile](rename-or-delete-a-microphone-profile.md)
