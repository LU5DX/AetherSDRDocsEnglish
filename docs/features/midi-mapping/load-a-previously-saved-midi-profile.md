# Load a previously saved MIDI profile

Loading a saved profile replaces the current bindings with those stored under that profile name, letting you switch between controller configurations without re-learning every binding.

## Before you start

- A MIDI profile must already exist. If you have not saved one yet, see [Save the current mapping as a named profile](save-the-current-mapping-as-a-named-profile.md).
- Open the MIDI Controller Mapping dialog via `Settings > MIDI Mapping...`.

## Steps

1. In the **Profile:** combo box, select the name of the profile you want to load. If the list is empty, no profiles have been saved yet.
2. Click **Load**.

The current bindings are replaced with the bindings stored in the selected profile. The Bindings table updates immediately to show the loaded bindings.

## What each control does

| Control          | Kind                                                                                             | Behavior                                                                                                                                                                                                                                                                |
|------------------|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Port:            | Combo box                                                                                        | Selects the MIDI input device.                                                                                                                                                                                                                                          |
| Refresh          | Button                                                                                           | Rescans available MIDI ports.                                                                                                                                                                                                                                           |
| Connect          | Button                                                                                           | Opens or closes the selected MIDI port.                                                                                                                                                                                                                                 |
| Auto-connect on startup | Checkbox                                                                                   | Reopens the MIDI port on application launch.                                                                                                                                                                                                                            |
| Category         | Combo box                                                                                        | Filters the Parameter list to a control category.                                                                                                                                                                                                                       |
| Parameter        | Combo box                                                                                        | Chooses the target parameter for a new binding. In v26.8.4, three momentary (Gate) actions are available in the Phone/CW category: **Trigger straight key** (`cwkey`), **Trigger CW Left Paddle** (`cwdit`), **Trigger CW Right Paddle** (`cwdah`). Legacy dotted IDs (`cw.key`, `cw.dit`, `cw.dah`) are auto-migrated on read. |
| Learn            | Button                                                                                           | Starts listening for the next MIDI message and binds it to the selected parameter.                                                                                                                                                                                      |
| Manual…          | Button                                                                                           | Opens a dialog to type a binding's channel, message type and number instead of using Learn mode. New in v26.8.4 (#4760). Opens the same manual editor used by the per-row edit button.                                                                                  |
| Bindings table   | Shows existing bindings with per-row Invert, Relative, edit (✎) and delete controls.             | Columns: Parameter, MIDI Source, Channel, Invert, Relative, (edit), (delete).                                                                                                                                                                                           |
| ✎ (edit binding) | Button                                                                                           | Opens the manual editor to correct this binding's channel, type and number. New in v26.8.4 (#4760).                                                                                                                                                                     |
| Invert           | Checkbox                                                                                         | Reverses the control direction for the row.                                                                                                                                                                                                                             |
| Relative         | Checkbox                                                                                         | Treats the control as an endless encoder.                                                                                                                                                                                                                               |
| × (delete row)   | Button                                                                                           | Removes that binding.                                                                                                                                                                                                                                                   |
| Clear All        | Button                                                                                           | Removes every binding.                                                                                                                                                                                                                                                  |
| Profile:         | Combo box                                                                                        | Picks a saved MIDI mapping profile to load or save. Editable.                                                                                                                                                                                                           |
| Save             | Button                                                                                           | Saves the current bindings as a profile.                                                                                                                                                                                                                                |
| Load             | Button                                                                                           | Replaces current bindings with those from the selected profile.                                                                                                                                                                                                         |
| Import...        | Button                                                                                           | Imports a profile file into the store — AetherSDR profile XML or a SmartSDR ".map" file. New in v26.8.4. Reports how many bindings were imported and lets the user Load to apply.                                                                                         |
| Export...        | Button                                                                                           | Exports the current bindings as an AetherSDR profile XML file. New in v26.8.4. Remembered directory persisted under `MidiImportExportPath`.                                                                                                                             |
| Close            | Button                                                                                           | Closes the dialog.                                                                                                                                                                                                                                                      |

## Port status indicator

The **Port status** indicator shows whether the MIDI port is currently open:
- **Opened** — The MIDI port is active and receiving messages.
- **Closed** — The MIDI port is not open.

## Activity indicator

The **Activity indicator** shows the most recent MIDI message received, helping you confirm that the controller is sending data.

## Category filter options

The **Category** combo box filters the **Parameter** list to show only controls from a specific group. Available categories:

- All
- RX
- TX
- Phone/CW
- EQ
- Global
- Mode
- Band
- Filter
- Slice
- Display
- Frequency

Selecting a category limits the **Parameter** combo box to entries in that group, making it easier to find the control you want to bind.

## Parameter options

The **Parameter** combo box contains all available parameters for binding. In v26.8.4, three momentary (Gate) actions are available in the Phone/CW category:

- **Trigger straight key** (id: `cwkey`)
- **Trigger CW Left Paddle** (id: `cwdit`)
- **Trigger CW Right Paddle** (id: `cwdah`)

Legacy dotted IDs (`cw.key`, `cw.dit`, `cw.dah`) are automatically migrated to the new format when loading old profiles.

## Tips

- The **Profile:** combo box is editable. If you type a name that does not match a saved profile and click Load, nothing is loaded — no error is shown and the current bindings remain unchanged.
- After loading, the loaded bindings are immediately persisted as the active bindings. You do not need to click Save again to keep them active for the current session.
- Use **Import...** to bring in a SmartSDR `.map` file. After import, click Load to apply the imported bindings.
- The **Export...** dialog remembers the last directory you used, so subsequent exports start in the same folder.

## Troubleshooting

- **Load is clicked but the Bindings table does not change** — The profile name in the **Profile:** combo box does not match any saved profile, or the name field is empty. Select a name from the dropdown list rather than typing it manually.
- **Profile: list is empty** — No profiles have been saved. See [Save the current mapping as a named profile](save-the-current-mapping-as-a-named-profile.md).
- **MIDI port does not open** — Click Refresh to rescan available ports, then select the correct device from the **Port:** combo box and click Connect.

## Related

- [Save the current mapping as a named profile](save-the-current-mapping-as-a-named-profile.md)
- [Record a new binding with Learn mode](record-a-new-binding-with-learn-mode.md)
- [Connect a MIDI controller](../../getting-started/setup/connect-a-midi-controller.md)
- [MIDI Controller Mapping overview](overview.md)