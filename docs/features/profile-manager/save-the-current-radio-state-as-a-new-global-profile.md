# Profile Manager

Use the Profile Manager to create, rename, load, and delete Global, Transmit, and Microphone profiles on the radio, and to toggle auto-saving of transmit changes.

## Before you start

- AetherSDR must be connected to the radio. Profile Manager requires an active radio connection.
- Familiarise yourself with the profile categories: Global profiles store overall radio configuration; Transmit and Microphone profiles store transmission-specific settings.

## Opening the Profile Manager

Click `Profiles > Profile Manager...` to open the Profile Manager dialog.

## What each control does

| Control | Kind | Behavior | Setting key |
|---|---|---|---|
| `Global (tab)` | Tab | Manages global profiles. | — |
| `Transmit (tab)` | Tab | Manages transmit profiles. | — |
| `Microphone (tab)` | Tab | Manages microphone profiles. | — |
| `Auto-Save (tab)` | Tab | Controls automatic profile saving. | — |
| `Profile name` | Text field | Name used when saving a new profile. If left blank when Save is clicked and a profile is selected in the list, the selected profile's name is used instead. | — |
| `Profile list` | List | Shows all existing profiles for the selected category. The active profile is highlighted. | — |
| `Load` | Button | Loads the selected profile onto the radio. Enabled only when a profile is selected. | — |
| `Save` | Button | Saves the current radio state under the name typed in `Profile name`. | — |
| `Delete` | Button | Deletes the selected profile after a confirmation prompt. Enabled only when a profile is selected. | — |
| `Close` | Button | Closes the Profile Manager dialog. | — |
| `Auto-save profile changes` | Checkbox | When enabled, TX changes are written back to the active profile automatically. | `AutoSaveTransmitProfile` |

## Tab-specific behavior

### Global tab

- The `Save` button creates or overwrites a global profile. Enter a new name to create a profile, or select an existing one and click `Save` to overwrite it.

### Transmit and Microphone tabs

- The `Save` button is labelled **Create** instead of **Save**. The radio firmware does not support directly overwriting transmit or microphone profiles. Clicking `Create` always creates a new profile with a unique name.
- If a profile with the typed name already exists, a dialog appears offering to enable **Auto-Save**. Clicking the Enable Auto-Save button in this dialog sends the `profile autosave on` command to the radio. The Auto-Save checkbox on the Auto-Save tab updates automatically in response to the radio's confirmation.
- A note below the buttons explains: "Updates to existing profiles save automatically — enable Auto-Save (Auto-Save tab) so changes follow the active profile. Create makes a new profile; it does not overwrite an existing one."
- The `Load` button uses the firmware command `profile tx load` (on the Transmit tab) and `profile mic load` (on the Microphone tab) to load the selected profile.

### Auto-Save tab

- Check `Auto-save profile changes` to enable automatic saving of transmit and microphone profile changes.
- When enabled, any tweaks you make to an active transmit or microphone profile are written back to that profile immediately on the radio. You do not need to manually save.
- The checkbox stays in sync with the radio's actual auto-save state, even when auto-save is toggled by:
  - The Enable Auto-Save button in the Transmit or Microphone tab's duplicate-name dialog
  - TCI clients sending auto-save commands
  - Loading a profile that has auto-save enabled or disabled
  - Remote SmartSDR clients
- The checkbox ignores its own toggled signal when syncing from the radio, preventing feedback loops.

## Tips

- Clicking an existing profile in the `Profile list` populates the `Profile name` field with that profile's name. If you then click `Save` on the Global tab, the existing profile is overwritten with the current radio state.
- You can also double-click a profile in the `Profile list` to load it immediately without clicking `Load`.
- The `Profile list` updates automatically when the radio confirms the save. You do not need to close and reopen the dialog to see the new entry.
- For transmit and microphone profiles, enable Auto-Save before making adjustments so you do not lose your changes.

## Troubleshooting

- **Save has no effect and the profile does not appear in the list** — Confirm the radio is connected. Profile Manager requires an active radio connection; if the connection dropped, reconnect via `Settings > Connect to Radio...` and try again.
- **Clicking Save with an empty `Profile name` field does nothing** — Either type a name in `Profile name` or select an existing profile in the `Profile list` first (its name will fill the field automatically).
- **Cannot overwrite a transmit or microphone profile** — This is by design. Use `Create` to make a new profile, or enable Auto-Save so changes to the active profile are saved automatically.
- **The Auto-Save checkbox seems to change by itself** — This is normal. The checkbox reflects the radio's actual auto-save state. It may update when you enable Auto-Save from the Transmit or Microphone tab, or when another client toggles auto-save on the radio.

## Related

- [Profile Manager overview](overview.md)
- [Review the list of active global profiles](review-the-list-of-active-global-profiles.md)
- [Switch to a saved transmit profile](switch-to-a-saved-transmit-profile.md)
- [Turn on auto-save so TX tweaks always persist](turn-on-auto-save-so-tx-tweaks-always-persist.md)