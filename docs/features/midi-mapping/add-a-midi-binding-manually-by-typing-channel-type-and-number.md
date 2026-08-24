# Add a MIDI binding manually by typing channel, type and number

This page shows you how to create a MIDI binding in AetherSDR by typing the channel, message type, and number directly, instead of using Learn mode. This is useful when you know your controller's exact MIDI message details and want to add a binding without physically moving a knob or button.

## Before you start

- Your MIDI controller must be connected to your computer.
- Open the MIDI Controller Mapping dialog: `Settings > MIDI Mapping...`
- A port must be selected and connected (see [Connect a MIDI controller](../../getting-started/setup/connect-a-midi-controller.md)).

## Steps

1. In the **Parameter** combo box, select the target parameter for the new binding. Optionally, use the **Category** combo box to filter the list (e.g., `RX`, `TX`, `Phone/CW`).
2. Click **Manual…** . The same editor used by the per-row edit button (✎) opens.
3. Type the MIDI channel, message type, and number for the binding.
4. Confirm the dialog to add the binding to the table.

The new binding appears in the **Bindings table** with its parameter, MIDI source, and channel.

## What each control does

| Control | Description | Persisted setting |
|---|---|---|
| **Port:** | Selects the MIDI input device. | `MidiPort` |
| **Refresh** | Rescans available MIDI ports. | — |
| **Connect** | Opens or closes the selected MIDI port. | — |
| **Auto-connect on startup** | Reopens the MIDI port when AetherSDR starts. | `MidiAutoConnect` |
| **Category** | Filters the parameter list by control category. | — |
| **Parameter** | Chooses the target parameter for a new binding. | — |
| **Learn** | Starts listening for the next MIDI message and binds it to the selected parameter. | — |
| **Manual…** | Opens a dialog to type a binding's channel, message type, and number instead of using Learn mode. New in v26.8.4. | — |
| **Bindings table** | Shows existing bindings with per-row Invert, Relative, edit (✎), and delete (×) controls. Columns: Parameter, MIDI Source, Channel, Invert, Relative. | — |
| **Invert** | Reverses the control direction for the row. | — |
| **Relative** | Treats the control as an endless encoder. | — |
| **Clear All** | Removes every binding. | — |

## Tips

- The **Manual…** button is the same editor used by the per-row edit button (✎), so you can correct a binding the same way you created it.
- Manual entry is useful when you know the exact MIDI message your controller sends and don't want to risk a wrong Learn capture.

## Related

- [Connect a MIDI controller](../../getting-started/setup/connect-a-midi-controller.md)
- [Record a new binding with Learn mode](record-a-new-binding-with-learn-mode.md)
- [Edit an existing binding's channel, type and number](edit-an-existing-binding-s-channel-type-and-number.md)
- [Delete a binding](delete-a-binding.md)
- [Save the current mapping as a named profile](save-the-current-mapping-as-a-named-profile.md)
- [Load a previously saved MIDI profile](load-a-previously-saved-midi-profile.md)
