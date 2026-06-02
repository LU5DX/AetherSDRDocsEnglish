# Switch to a saved transmit profile

Load a previously saved transmit profile onto the radio. This applies a stored set of TX parameters in one step, replacing the current transmit settings.

## Before you start

- AetherSDR must be connected to the radio. Profile Manager requires an active radio connection.
- At least one transmit profile must already exist on the radio. If the profile list is empty, create a profile first.

## Steps

1. Click `Profiles > Profile Manager...` to open the Profile Manager dialog.
2. Click the **Transmit (tab)** to switch to the transmit profile list.
3. Click the profile you want to load in the **Profile list**. The active profile is highlighted.
4. Click **Load**.

Alternatively, double-click any entry in the **Profile list** to load it without clicking **Load**.

## What each control does

| Control | Kind | Behavior | Setting key |
|---|---|---|---|
| **Global (tab)** | Tab | Switches the dialog to the global profile view. | — |
| **Transmit (tab)** | Tab | Switches the dialog to the transmit profile view. | — |
| **Microphone (tab)** | Tab | Switches the dialog to the microphone profile view. | — |
| **Auto-Save (tab)** | Tab | Switches the dialog to the auto-save settings view. | — |
| **Profile name** | Text field | Name used when saving a new profile. | — |
| **Profile list** | List | Shows all profiles of the selected category stored on the radio. The currently active profile is highlighted. | — |
| **Load** | Button | Loads the selected profile onto the radio. Enabled only when a profile is selected. | — |
| **Save** | Button | Saves the current radio state under the typed name. | — |
| **Delete** | Button | Deletes the selected profile after confirmation. Enabled only when a profile is selected. | — |
| **Auto-save profile changes** | Checkbox | When enabled, TX changes are written back to the active profile automatically. | `AutoSaveTransmitProfile` |
| **Close** | Button | Closes the dialog. | — |

## Notes

- The button for saving profiles is labeled **Save**, not **Create**. To update an existing profile, enable **Auto-save profile changes** on the **Auto-Save (tab)** — changes to the active profile are then captured automatically.
- The **Auto-save profile changes** checkbox syncs with the radio automatically. Changes made outside the dialog (by TCI clients, profile load, or remote SmartSDR clients) will update the checkbox state.
- If you attempt to save a profile with a name that already exists and Auto-Save is off, a dialog offers to enable Auto-Save so future changes to the profile are captured.

## Tips

- Selecting a profile in the list fills the **Profile name** field with that profile's name. If you enter a different name and click **Save**, a new profile is created with that name.
- To persist TX changes to the active transmit profile without manual saving, enable **Auto-save profile changes** on the **Auto-Save (tab)**.

## Troubleshooting

- **Load is grayed out** — No profile is selected in the **Profile list**. Click a profile name to select it, then click **Load**.
- **Profile list is empty** — No profiles exist for the selected category on the radio yet. Use **Save** to make one first.
- **Clicking Save does nothing for an existing name** — The radio cannot directly overwrite profiles. Enable Auto-Save so your changes are captured automatically, or manually make changes while the profile is active and Auto-Save is on.

## Related

- [Turn on auto-save so TX tweaks always persist](turn-on-auto-save-so-tx-tweaks-always-persist.md)
- [Profile Manager overview](overview.md)
- [Save the current radio state as a new global profile](save-the-current-radio-state-as-a-new-global-profile.md)