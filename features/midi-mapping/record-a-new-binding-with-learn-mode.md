# Record a new binding with Learn mode

Use Learn mode to map a physical MIDI control — a knob, fader, or button — to an AetherSDR parameter by moving the control while AetherSDR listens. This is faster and more reliable than entering MIDI channel and number values by hand.

## Before you start

- A MIDI controller must be connected to your computer and visible to the OS.
- The MIDI port must be open in AetherSDR. If it is not, see [Connect a MIDI controller](../../getting-started/setup/connect-a-midi-controller.md).

## Steps

1. Open `Settings > MIDI Mapping...`.
2. In the **Category** combo box, select the category that contains the parameter you want to bind (for example, `RX`, `TX`, or `All`).
3. In the **Parameter** combo box, select the target parameter.
4. Click `Learn`. The button label changes to `Cancel Learn`, indicating AetherSDR is waiting for a MIDI message.
5. Move the knob, fader, or button on your controller that you want to assign.
6. AetherSDR captures the message and adds a new row to the **Bindings table**. The button label returns to `Learn`.
7. If you want to cancel without recording, click `Cancel Learn` instead of moving a control.
8. Repeat steps 2–6 for each additional binding.
9. Click `Close` when finished. Bindings are saved automatically when Learn completes.

## What each control does

| Control | Description |
|---|---|
| **Category** combo box | Filters the **Parameter** list by control category. Options include `All`, `RX`, `TX`, `Phone/CW`, `EQ`, and `Global`. |
| **Parameter** combo box | Selects the AetherSDR parameter the next Learn capture will be bound to. |
| `Learn` | Starts listening for the next incoming MIDI message and binds it to the selected parameter. Clicking again while listening cancels the operation. |
| **Bindings table** | Shows all recorded bindings. Columns: Parameter, MIDI Source, Channel, Invert, Relative, and a delete button. |
| **Invert** checkbox (per row) | Reverses the direction of the control for that binding. |
| **Relative** checkbox (per row) | Treats the control as an endless encoder rather than an absolute value source. |
| Activity indicator | Displays the most recent MIDI message received (channel, type, number, and value). Useful for confirming the controller is sending data before you click `Learn`. |

## Tips

- Watch the activity indicator while moving a control before clicking `Learn`. If nothing appears, the port is not open or the controller is not sending.
- If the wrong parameter is selected when you move the control, click `Cancel Learn`, correct the **Parameter** selection, and click `Learn` again.
- After recording several bindings, use `Save` with a name in the **Profile:** field to preserve the mapping. See [Save the current mapping as a named profile](save-the-current-mapping-as-a-named-profile.md).

## Troubleshooting

- **`Learn` times out or the button stays labeled `Cancel Learn` after moving a control** — The MIDI port may not be open. Check the port status indicator; if it shows `Closed`, click `Connect` and then retry Learn.
- **Activity indicator shows a message but no binding is created** — The parameter field may have been empty. Ensure a parameter is selected in the **Parameter** combo box before clicking `Learn`.
- **The controller sends data but the activity indicator is blank** — The selected port in the **Port:** combo box may not match the controller. Click `Refresh` to rescan, select the correct port, and click `Connect`.

## Related

- [Connect a MIDI controller](../../getting-started/setup/connect-a-midi-controller.md)
- [Invert a knob or treat it as an endless encoder](invert-a-knob-or-treat-it-as-an-endless-encoder.md)
- [Delete a binding](delete-a-binding.md)
- [Save the current mapping as a named profile](save-the-current-mapping-as-a-named-profile.md)
- [Load a previously saved MIDI profile](load-a-previously-saved-midi-profile.md)
- [Auto-connect MIDI controller on startup](../../getting-started/setup/auto-connect-midi-controller-on-startup.md)
