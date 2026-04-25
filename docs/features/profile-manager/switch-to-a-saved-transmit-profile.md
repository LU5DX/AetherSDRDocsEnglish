# Switch to a saved transmit profile

Load a previously saved transmit profile onto the radio to restore a specific set of TX settings in one step.

## Before you start

- AetherSDR must be connected to the radio. Profile Manager requires an active radio connection.
- At least one transmit profile must already exist on the radio.

## Steps

1. Click `Profiles > Profile Manager...` to open the Profile Manager dialog.
2. Click the **Transmit (tab)** tab.
3. In the **Profile list**, click the profile you want to load to select it.
4. Click **Load**.

Alternatively, double-click the profile name in the **Profile list** to load it without clicking **Load**.

The active profile is highlighted in the **Profile list** after loading.

## What each control does

| Control | Description | Setting key |
|---|---|---|
| **Transmit (tab)** | Shows transmit profiles stored on the radio. | — |
| **Profile list** | All saved transmit profiles; the currently active profile is highlighted. | — |
| **Profile name** | Text field populated with the selected profile's name when you click an entry. Also used when saving a new profile. | — |
| **Load** | Sends the selected profile to the radio. Enabled only when a profile is selected. | — |
| **Save** | Saves the current radio TX state under the name in **Profile name**. | — |
| **Delete** | Deletes the selected profile after a confirmation prompt. | — |
| **Auto-save profile changes** | When checked, TX changes are written back to the active profile automatically. | `AutoSaveTransmitProfile` |

## Tips

- Selecting a profile in the **Profile list** fills the **Profile name** field with that profile's name. If you then click **Save**, the radio overwrites that profile with the current TX state.
- To keep TX changes from overwriting the profile you just loaded, leave **Auto-save profile changes** unchecked on the **Auto-Save (tab)** tab.

## Related

- [Profile Manager overview](overview.md)
- [Turn on auto-save so TX tweaks always persist](turn-on-auto-save-so-tx-tweaks-always-persist.md)
- [Save the current radio state as a new global profile](save-the-current-radio-state-as-a-new-global-profile.md)
