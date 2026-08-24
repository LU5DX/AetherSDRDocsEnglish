# Record a new binding with Learn mode

Use Learn mode to map a physical knob, fader, or button on your MIDI controller to a parameter in AetherSDR. After clicking Learn, move the control on your hardware and AetherSDR records the binding automatically.

## Before you start

- Your MIDI controller must be connected to the computer and visible as a MIDI input device.
- The MIDI port must be open in AetherSDR. If the port status shows "Disconnected", connect it first — see [Connect a MIDI controller](../../getting-started/setup/connect-a-midi-controller.md).

## Steps

1. Open `Settings > MIDI Mapping...`.
2. In the **Parameter Bindings** section, use the **Category** combo box to narrow the list — choose from All, RX, TX, Phone/CW, EQ, Global, Mode, Band, Filter, Slice, Display, or Frequency.
3. Use the **Parameter** combo box to select the target parameter you want to control.
4. Click **Learn**. The button label changes to **Cancel Learn**.
5. Move the knob, fader, or press the button on your MIDI controller that you want to assign. AetherSDR detects the incoming MIDI message and records the binding.
6. The button returns to **Learn** automatically when the binding is captured. The new binding appears as a row in the **Bindings table**.
7. Click **Close** when finished, or continue adding bindings by repeating steps 2–6.

## Add a binding manually without Learn mode

If you know the exact MIDI channel, message type, and number of the control you want to assign, you can enter it directly instead of using Learn mode.

1. Open `Settings > MIDI Mapping...`.
2. Select the target **Category** and **Parameter** for the binding.
3. Click **Manual…**.
4. In the dialog, type the binding's channel, message type, and number.
5. Click **OK** to add the binding to the table.

You can also edit an existing binding's channel, message type, or number by clicking the **✎ (edit binding)** button in that row and correcting the values in the same manual editor.

## What each control does

| Control                     | Description                                                                                                                                   | Notes                                                                                                                                                                                                                                     |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Port:**                   | Selects MIDI input device.                                                                                                                    | Persisted as `MidiPort`.                                                                                                                                                                                                                  |
| **Refresh**                 | Rescans available MIDI ports.                                                                                                                 |                                                                                                                                                                                                                                           |
| **Connect**                 | Opens/closes selected MIDI port. Port status is shown next to the button.                                                                     |                                                                                                                                                                                                                                           |
| **Auto-connect on startup** | Reopens MIDI port on launch.                                                                                                                  | Persisted as `MidiAutoConnect`.                                                                                                                                                                                                           |
| **Category**                | Filters the Parameter list to a specific control category (All, RX, TX, Phone/CW, EQ, Global, Mode, Band, Filter, Slice, Display, Frequency). |                                                                                                                                                                                                                                           |
| **Parameter**               | Selects the target parameter to bind.                                                                                                         | In v0.9.7, three new momentary (Gate) actions were added in the Phone/CW category: "Trigger straight key", "Trigger CW Left Paddle", "Trigger CW Right Paddle". Legacy dotted IDs `cw.key`, `cw.dit`, `cw.dah` are auto-migrated on read. |
| **Learn**                   | Starts listening for the next MIDI message and binds it to the selected parameter. Click again (shown as **Cancel Learn**) to abort.          |                                                                                                                                                                                                                                           |
| **Manual…**                 | Opens a dialog to type a binding's channel, message type and number instead of using Learn mode.                                             | New in v26.8.4. Opens the same manual editor used by the per-row edit button.                                                                                                                                                             |
| **Bindings table**          | Displays all current bindings. Columns: Parameter, MIDI Source, Channel, Invert, Relative, edit (✎) and delete buttons.                       |                                                                                                                                                                                                                                           |
| **✎ (edit binding)**        | Opens the manual editor to correct this binding's channel, type and number.                                                                   | New in v26.8.4.                                                                                                                                                                                                                           |
| **Invert**                  | Reverses the control direction for that binding row.                                                                                          |                                                                                                                                                                                                                                           |
| **Relative**                | Treats the assigned control as an endless encoder rather than an absolute value control.                                                      |                                                                                                                                                                                                                                           |
| **× (delete row)**          | Removes that individual binding.                                                                                                              |                                                                                                                                                                                                                                           |
| **Clear All**               | Removes every binding at once.                                                                                                                |                                                                                                                                                                                                                                           |
| **Profile:**                | Picks a saved MIDI mapping profile.                                                                                                           |                                                                                                                                                                                                                                           |
| **Save**                    | Saves current bindings as a profile.                                                                                                          |                                                                                                                                                                                                                                           |
| **Load**                    | Loads the selected profile.                                                                                                                   |                                                                                                                                                                                                                                           |
| **Import...**               | Imports a profile file into the store — AetherSDR profile XML or a SmartSDR ".map" file.                                                      | New in v26.8.4. Reports how many bindings were imported and lets the user Load to apply.                                                                                                                                                  |
| **Export...**               | Exports the current bindings as an AetherSDR profile XML file.                                                                                | New in v26.8.4. Remembered directory persisted under `MidiImportExportPath`.                                                                                                                                                             |
| **Close**                   | Closes the dialog.                                                                                                                            |                                                                                                                                                                                                                                           |

## Tips

- The **Activity indicator** in the MIDI Device section shows the most recent MIDI message received (channel, type, number, and value). Use it to confirm your controller is sending data before clicking Learn.
- If you select the wrong parameter before clicking Learn, click **Cancel Learn** to abort without creating a binding, then select the correct parameter and try again.
- Use the **Manual…** button or the row **✎** button to correct a binding when you know the exact MIDI message details — this is faster than deleting and re-learning the binding.
- Bindings are saved automatically when Learn completes. To keep your bindings across sessions, save them as a named profile — see [Save the current mapping as a named profile](save-the-current-mapping-as-a-named-profile.md).
- Check **Auto-connect on startup** (persisted as `MidiAutoConnect`) so the port reopens automatically next time. The selected port is persisted as `MidiPort`.
- The dialog geometry is automatically saved and restored across sessions.
- The dialog now uses the active theme for all visual elements. Text colors, backgrounds, and accents adjust automatically when you change the application theme.

## Troubleshooting

- **Learn does not complete after moving a control** — Verify the port status shows "Connected" in the MIDI Device section. If it shows "Disconnected", select the correct port in the **Port:** combo box and click **Connect**. Use the Activity indicator to confirm incoming MIDI messages are being received.
- **Parameter combo box is empty** — The selected Category may have no mapped parameters. Set **Category** to All and check whether the Parameter list populates.
- **Learn captures the wrong control** — Click **Cancel Learn**, wait until no controls on the hardware are being moved, then click **Learn** again and move only the intended control.
- **Import does not apply immediately** — After importing a profile file, click **Load** in the Profile section to apply the imported bindings.

## Related

- [Connect a MIDI controller](../../getting-started/setup/connect-a-midi-controller.md)
- [Auto-connect MIDI controller on startup](../../getting-started/setup/auto-connect-midi-controller-on-startup.md)
- [Invert a knob or treat it as an endless encoder](invert-a-knob-or-treat-it-as-an-endless-encoder.md)
- [Delete a binding](delete-a-binding.md)
- [Save the current mapping as a named profile](save-the-current-mapping-as-a-named-profile.md)
- [Load a previously saved MIDI profile](load-a-previously-saved-midi-profile.md)