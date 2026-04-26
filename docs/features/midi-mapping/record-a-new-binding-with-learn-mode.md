# Record a new binding with Learn mode

Use Learn mode to map a physical knob, fader, or button on your MIDI controller to a parameter in AetherSDR. After clicking Learn, move the control on your hardware and AetherSDR records the binding automatically.

## Before you start

- Your MIDI controller must be connected to the computer and visible as a MIDI input device.
- The MIDI port must be open in AetherSDR. If the port status shows "Disconnected", connect it first — see [Connect a MIDI controller](../../getting-started/setup/connect-a-midi-controller.md).

## Steps

1. Open `Settings > MIDI Mapping...`.
2. In the **Parameter Bindings** section, use the **Category** combo box to narrow the list — choose from All, RX, TX, Phone/CW, EQ, or Global.
3. Use the **Parameter** combo box to select the target parameter you want to control.
4. Click **Learn**. The button label changes to **Cancel Learn**.
5. Move the knob, fader, or press the button on your MIDI controller that you want to assign. AetherSDR detects the incoming MIDI message and records the binding.
6. The button returns to **Learn** automatically when the binding is captured. The new binding appears as a row in the **Bindings table**.
7. Click **Close** when finished, or continue adding bindings by repeating steps 2–6.

## What each control does

| Control | Description |
|---|---|
| **Category** | Filters the Parameter list to a specific control category (All, RX, TX, Phone/CW, EQ, Global). |
| **Parameter** | Selects the target parameter to bind. |
| **Learn** | Starts listening for the next MIDI message and binds it to the selected parameter. Click again (shown as **Cancel Learn**) to abort. |
| **Bindings table** | Displays all current bindings. Columns: Parameter, MIDI Source, Channel, Invert, Relative, and a delete button. |
| **Invert** | Reverses the control direction for that binding row. |
| **Relative** | Treats the assigned control as an endless encoder rather than an absolute value control. |
| **× (delete row)** | Removes that individual binding. |
| **Clear All** | Removes every binding at once. |

## Tips

- The **Activity indicator** in the MIDI Device section shows the most recent MIDI message received (channel, type, number, and value). Use it to confirm your controller is sending data before clicking Learn.
- If you select the wrong parameter before clicking Learn, click **Cancel Learn** to abort without creating a binding, then select the correct parameter and try again.
- Bindings are saved automatically when Learn completes. To keep your bindings across sessions, save them as a named profile — see [Save the current mapping as a named profile](save-the-current-mapping-as-a-named-profile.md).
- Check **Auto-connect on startup** (persisted as `MidiAutoConnect`) so the port reopens automatically next time. The selected port is persisted as `MidiPort`.

## Troubleshooting

- **Learn does not complete after moving a control** — Verify the port status shows "Connected" in the MIDI Device section. If it shows "Disconnected", select the correct port in the **Port:** combo box and click **Connect**. Use the Activity indicator to confirm incoming MIDI messages are being received.
- **Parameter combo box is empty** — The selected Category may have no mapped parameters. Set **Category** to All and check whether the Parameter list populates.
- **Learn captures the wrong control** — Click **Cancel Learn**, wait until no controls on the hardware are being moved, then click **Learn** again and move only the intended control.

## Related

- [Connect a MIDI controller](../../getting-started/setup/connect-a-midi-controller.md)
- [Auto-connect MIDI controller on startup](../../getting-started/setup/auto-connect-midi-controller-on-startup.md)
- [Invert a knob or treat it as an endless encoder](invert-a-knob-or-treat-it-as-an-endless-encoder.md)
- [Delete a binding](delete-a-binding.md)
- [Save the current mapping as a named profile](save-the-current-mapping-as-a-named-profile.md)
- [Load a previously saved MIDI profile](load-a-previously-saved-midi-profile.md)
