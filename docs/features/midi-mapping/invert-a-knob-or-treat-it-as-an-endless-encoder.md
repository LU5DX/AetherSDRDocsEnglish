# Invert a knob or treat it as an endless encoder

After creating a MIDI binding, you can reverse its direction with Invert or tell AetherSDR to treat the control as an endless encoder with Relative. Both options are set per binding in the Bindings table.

## Before you start

- A MIDI controller must be connected and at least one binding must already exist. See [Connect a MIDI controller](../../getting-started/setup/connect-a-midi-controller.md) and [Record a new binding with Learn mode](record-a-new-binding-with-learn-mode.md).
- Open `Settings > MIDI Mapping...` to reach the MIDI Controller Mapping dialog.

## Steps

1. Open `Settings > MIDI Mapping...`.
2. Locate the binding you want to change in the Bindings table.
3. To reverse the control direction, check the Invert checkbox in that binding's row.
4. To treat the control as an endless encoder, check the Relative checkbox in that binding's row.
5. Either checkbox can be checked or unchecked independently. Changes take effect immediately.
6. Click Close when finished.

## What each control does

| Control          | Column in Bindings table                                                                         | Behavior                                                                                                                                               |
|------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Invert           | Invert                                                                                           | Reverses the direction of the control for that binding. Turn clockwise to decrease, counter-clockwise to increase, or vice versa.                      |
| Relative         | Relative                                                                                         | Treats the control as an endless encoder. Use this when your hardware knob sends incremental (relative) values rather than absolute positions (0–127). |
| Manual…          | Opens a dialog to type a binding's channel, message type and number instead of using Learn mode. | New in v26.8.4 (#4760). Opens the same manual editor used by the per-row edit button.                                                                  |
| ✎ (edit binding) | Opens the manual editor to correct this binding's channel, type and number.                      | New in v26.8.4 (#4760).                                                                                                                                |
| Import...        | Imports a profile file into the store -- AetherSDR profile XML or a SmartSDR ".map" file.        | New in v26.8.4. Reports how many bindings were imported and lets the user Load to apply.                                                               |
| Export...        | Exports the current bindings as an AetherSDR profile XML file.                                   | New in v26.8.4. Remembered directory persisted under MidiImportExportPath.                                                                             |
| Port:            | Combo box                                                                                        | Selects MIDI input device.                                                                                                                              |
| Refresh          | Push button                                                                                      | Rescans available MIDI ports.                                                                                                                          |
| Connect          | Push button                                                                                      | Opens/closes selected MIDI port.                                                                                                                       |
| Auto-connect on startup | Checkbox                                                                                   | Reopens MIDI port on launch.                                                                                                                           |
| Category         | Combo box                                                                                        | Filters parameter combo to a control category.                                                                                                         |
| Parameter        | Combo box                                                                                        | Chooses the target parameter for a new binding. In v0.9.7, three new momentary (Gate) actions were added in the Phone/CW category: 'Trigger straight key' (id: cwkey), 'Trigger CW Left Paddle' (id: cwdit), 'Trigger CW Right Paddle' (id: cwdah). Legacy dotted IDs cw.key/cw.dit/cw.dah are auto-migrated on read. |
| Learn            | Push button                                                                                      | Starts listening for the next MIDI message and binds it to the selected parameter.                                                                     |
| Bindings table   | List                                                                                             | Shows existing bindings with per-row Invert, Relative, edit (✎) and delete controls. Columns: Parameter, MIDI Source, Channel, Invert, Relative, (edit), (delete). |
| × (delete row)   | Push button                                                                                      | Removes that binding.                                                                                                                                  |
| Clear All        | Push button                                                                                      | Removes every binding.                                                                                                                                 |
| Profile:         | Combo box                                                                                        | Picks a saved MIDI mapping profile.                                                                                                                    |
| Save             | Push button                                                                                      | Saves current bindings as a profile.                                                                                                                   |
| Load             | Push button                                                                                      | Loads the selected profile.                                                                                                                            |
| Close            | Push button                                                                                      | Closes the dialog.                                                                                                                                     |
| Port status      | Indicator                                                                                        | Shows whether the MIDI port is currently open (Opened/Closed).                                                                                         |
| Activity indicator | Indicator                                                                                      | Shows most recent MIDI message received.                                                                                                               |

## Category filter

The Category combo box above the Bindings table filters the Parameter combo box to a specific control category. In v26.6.1, the available categories are:

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

Select a category to narrow the list of parameters shown when creating a new binding.

## New momentary CW trigger actions

In v26.6.1, the Phone/CW category includes three new momentary (Gate) actions for CW keying:

- **Trigger straight key** (id: cwkey) — Emulates a straight key press.
- **Trigger CW Left Paddle** (id: cwdit) — Emulates a left paddle (dit) press.
- **Trigger CW Right Paddle** (id: cwdah) — Emulates a right paddle (dah) press.

Legacy dotted IDs (cw.key, cw.dit, cw.dah) are automatically migrated to the new format when loading older profiles.

## Tips

- Use Relative when your knob sends small increment/decrement values rather than an absolute position. If a knob jumps erratically when turned, enabling Relative usually corrects it.
- Invert and Relative can be combined on the same binding. For example, a Relative encoder that increments in the wrong direction can have both options checked.
- Changes to Invert and Relative are saved automatically when you save a profile. Use Save under Profile: to preserve them.
- The CW trigger actions are momentary — they activate while the MIDI control is held and deactivate when released.

## Troubleshooting

- **Checking Relative makes a knob stop responding** — The knob may be sending absolute values (0–127). Uncheck Relative and leave the binding in absolute mode.
- **Control still moves in the wrong direction after checking Invert** — Confirm you checked Invert on the correct row. Each binding row has its own Invert checkbox; scroll horizontally if the column is not visible.

## Related

- [Record a new binding with Learn mode](record-a-new-binding-with-learn-mode.md)
- [Delete a binding](delete-a-binding.md)
- [Save the current mapping as a named profile](save-the-current-mapping-as-a-named-profile.md)
- [Connect a MIDI controller](../../getting-started/setup/connect-a-midi-controller.md)