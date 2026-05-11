# Save the Current Mapping as a Named Profile

Save your current MIDI bindings under a name so you can recall them later or switch between controller layouts without re-learning every binding.

## Before you start

- At least one binding must exist in the Bindings table. An empty mapping can be saved but is not useful.
- Open `Settings > MIDI Mapping...` to reach the MIDI Controller Mapping dialog.

## Steps

1. Open `Settings > MIDI Mapping...`.
2. Confirm that the Bindings table shows the bindings you want to save.
3. In the **Profile:** field, type a name for the profile. The field accepts free text; it also shows existing profile names in its drop-down if any have been saved before.
4. Click **Save**.

The profile is stored immediately. The **Profile:** drop-down is refreshed to include the new name.

## What each control does

| Control | What it does | Setting key |
|---|---|---|
| **Port:** | Selects MIDI input device. | `MidiPort` |
| **Refresh** | Rescans available MIDI ports. | — |
| **Connect** | Opens/closes selected MIDI port. | — |
| **Auto-connect on startup** | Reopens MIDI port on launch. | `MidiAutoConnect` |
| **Category** | Filters parameter combo to a control category. Available categories: All, RX, TX, Phone/CW, EQ, Global, Mode, Band, Filter, Slice, Display, Frequency. | — |
| **Parameter** | Chooses the target parameter for a new binding. In v26.5.1, three new momentary (Gate) actions are available in the Phone/CW category: "Trigger straight key" (id: cwkey), "Trigger CW Left Paddle" (id: cwdit), "Trigger CW Right Paddle" (id: cwdah). Legacy dotted IDs cw.key/cw.dit/cw.dah are auto-migrated on read. | — |
| **Learn** | Starts listening for the next MIDI message and binds it to the selected parameter. | — |
| **Bindings table** | Shows existing bindings with per-row Invert, Relative and delete controls. Columns: Parameter, MIDI Source, Channel, Invert, Relative, (delete). | — |
| **Invert** | Reverses the control direction for the row. | — |
| **Relative** | Treats the control as an endless encoder. | — |
| **× (delete row)** | Removes that binding. | — |
| **Clear All** | Removes every binding. | — |
| **Profile:** | Editable combo box. Type a new name to create a profile, or pick an existing name from the drop-down to overwrite it. | — |
| **Save** | Saves the current bindings under the name shown in **Profile:**. Does nothing if the field is empty. | — |
| **Load** | Replaces the current bindings with those stored under the selected profile name. | — |
| **Close** | Closes the dialog. | — |

## Indicators

| Indicator | Meaning |
|---|---|
| **Port status** | Shows "Opened" or "Closed" to indicate whether the MIDI port is currently open. |
| **Activity indicator** | Shows the most recent MIDI message received. |

## Tips

- Typing a name that already exists in **Profile:** and clicking **Save** overwrites that profile without a confirmation prompt.
- To keep bindings for different controllers separate, use a descriptive name such as the controller model or use case.

## Troubleshooting

- **Clicking Save does nothing** — The **Profile:** field is empty or contains only spaces. Type a name first.
- **A profile name does not appear in the drop-down after saving** — Click anywhere to dismiss the drop-down and reopen it; the list refreshes after each save.

## Related

- [Load a previously saved MIDI profile](load-a-previously-saved-midi-profile.md)
- [Record a new binding with Learn mode](record-a-new-binding-with-learn-mode.md)
- [Delete a binding](delete-a-binding.md)
- [MIDI Controller Mapping overview](overview.md)