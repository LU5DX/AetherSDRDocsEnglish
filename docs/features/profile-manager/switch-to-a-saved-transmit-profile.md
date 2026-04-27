# Switch to a saved transmit profile

Load a previously saved transmit profile onto the radio. This applies a stored set of TX parameters in one step, replacing the current transmit settings.

## Before you start

- AetherSDR must be connected to the radio. Profile Manager requires an active radio connection.
- At least one transmit profile must already exist on the radio. If the profile list is empty, save a profile first.

## Steps

1. Click `Profiles > Profile Manager...` to open the Profile Manager dialog.
2. Click the **Transmit (tab)** to switch to the transmit profile list.
3. Click the profile you want to load in the **Profile list**. The active profile is highlighted.
4. Click **Load**.

Alternatively, double-click any entry in the **Profile list** to load it without clicking **Load**.

## What each control does

| Control | Kind | Behavior | Setting key |
|---|---|---|---|
| **Transmit (tab)** | Tab | Switches the dialog to the transmit profile view. | — |
| **Profile list** | List | Shows all transmit profiles stored on the radio. The currently active profile is highlighted. | — |
| **Profile name** | Text field | Populated automatically when you select an item in the list. Used when saving; not required for loading. | — |
| **Load** | Button | Sends the selected profile to the radio, replacing current TX settings. Enabled only when a profile is selected. | — |
| **Save** | Button | Saves the current radio TX state under the name in **Profile name**. | — |
| **Delete** | Button | Deletes the selected profile after confirmation. Enabled only when a profile is selected. | — |
| **Auto-save profile changes** | Checkbox | When checked, TX setting changes are written back to the active profile automatically. | `AutoSaveTransmitProfile` |

## Tips

- Selecting a profile in the list fills the **Profile name** field with that profile's name. If you then click **Save**, the current TX state overwrites that profile under the same name.
- If you want TX changes to persist to the active profile without manually clicking **Save** each time, enable **Auto-save profile changes** on the **Auto-Save (tab)**.

## Troubleshooting

- **Load is grayed out** — No profile is selected in the **Profile list**. Click a profile name to select it, then click **Load**.
- **Profile list is empty** — No transmit profiles exist on the radio yet. Use **Save** to create one first.

## Related

- [Turn on auto-save so TX tweaks always persist](turn-on-auto-save-so-tx-tweaks-always-persist.md)
- [Profile Manager overview](overview.md)
- [Save the current radio state as a new global profile](save-the-current-radio-state-as-a-new-global-profile.md)
