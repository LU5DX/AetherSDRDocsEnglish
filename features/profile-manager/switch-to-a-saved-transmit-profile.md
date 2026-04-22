# Switch to a saved transmit profile

Use the Profile Manager to recall a previously saved transmit profile and apply it to the radio. This replaces the radio's current transmit settings with those stored in the selected profile.

## Before you start

- AetherSDR must be connected to the radio. Profile Manager requires an active radio connection.
- At least one transmit profile must already exist on the radio. If the profile list is empty, save a profile first.

## Steps

1. Click `Profiles > Profile Manager...` to open the Profile Manager dialog.
2. Click the `Transmit (tab)` tab.
3. In the profile list, click the profile you want to load. The profile name appears highlighted and the `Profile name` field fills with its name.
4. Click `Load`. The selected profile is applied to the radio immediately.

Alternatively, double-click a profile in the profile list to load it without clicking `Load`.

5. Click `Close` to dismiss the dialog.

## What each control does

| Control | Description | Persisted setting |
|---|---|---|
| `Transmit (tab)` | Shows all transmit profiles stored on the radio. The currently active profile is highlighted. | — |
| `Profile name` | Displays the name of the selected profile. Editable when saving a new profile. | — |
| Profile list | Lists all available transmit profiles. Click a row to select it; the active profile is highlighted. | — |
| `Load` | Applies the selected profile to the radio. Disabled until a profile is selected. | — |
| `Save` | Saves the current radio transmit state under the name in `Profile name`. Does not load a profile. | — |
| `Delete` | Removes the selected profile after confirmation. Disabled until a profile is selected. | — |
| `Close` | Closes the Profile Manager dialog. | — |

## Tips

- Selecting a profile in the list automatically populates the `Profile name` field. If you then click `Save`, the current radio state overwrites that profile under the same name. Click `Load` instead if you only want to recall the profile without modifying it.
- To have transmit changes written back to the active profile automatically after loading, enable `Auto-save profile changes` on the `Auto-Save (tab)` tab. This controls the `AutoSaveTransmitProfile` setting.

## Related

- [Profile Manager overview](overview.md)
- [Save the current radio state as a new global profile](save-the-current-radio-state-as-a-new-global-profile.md)
- [Turn on auto-save so TX tweaks always persist](turn-on-auto-save-so-tx-tweaks-always-persist.md)
