# MIDI Controller Mapping

Use this page to map buttons, knobs, and other controls on your MIDI controller to radio functions on your FLEX-8600.

## Before you start

- Your MIDI controller is connected to the computer and recognized by the operating system.
- AetherSDR was built with MIDI support (`HAVE_MIDI`).
- The MIDI Mapping dialog is not already in Learn mode from a previous session.

## Configure a MIDI controller

1. Open `Settings > MIDI Mapping...`.
2. In the **Port:** combo box, select your MIDI controller from the list. If it does not appear, click **Refresh**.
3. Click **Connect**. The status indicator changes to `Opened`.
4. (Optional) Check **Auto-connect on startup** to reopen the same port next time AetherSDR launches.

> The dialog remembers its size and position between sessions.

## Create a binding with Learn mode

1. In the **Category** combo box, select a category to narrow the parameter list.
2. In the **Parameter** combo box, select the target parameter.
3. Click **Learn**. The button label changes to `Cancel Learn`.
4. Move the control (button, knob, or fader) on your MIDI controller that you want to bind. AetherSDR detects the MIDI message and completes the binding automatically.
5. Confirm the new row appears in the **Bindings table**, showing the parameter name, MIDI source, and channel.
6. Repeat for each additional binding.

## Create or edit a binding manually

If you prefer not to use Learn mode, or you need to correct an existing binding:

1. Click **Manual…** to type a binding's channel (1–16), message type (Note, Control Change, Program Change, Pitch Bend), and message number.
   - The same editor is available per row: click the **✎ (edit binding)** button in the row you want to fix.
2. Change the values and confirm to apply the binding.

## Edit, invert, or make a binding relative

- **Invert** — Check this box to reverse the control direction for that row.
- **Relative** — Check this box to treat the control as an endless encoder.
- **✎ (edit binding)** — Opens the same manual editor described above, pre-filled with the row's current values, so you can correct channel, message type, or number.
- **× (delete row)** — Removes that binding.
- **Clear All** — Removes every binding.

## Manage profiles

1. To save the current bindings as a profile, click **Save** and give it a name.
2. To apply a previously saved profile, choose it in the **Profile:** combo box and click **Load**.
3. To bring in bindings from a file:
   - Click **Import...** and select an AetherSDR profile XML or a SmartSDR `.map` file.
   - AetherSDR reports how many bindings were imported. Click **Load** to apply them.
4. To write the current bindings to a file, click **Export...** and choose a location. The export is saved as an AetherSDR profile XML file.
   - AetherSDR remembers the last directory used for Import/Export and reopens it next time.

## Control reference

| Control                    | Kind      | Behavior                                                                                    |
|----------------------------|-----------|---------------------------------------------------------------------------------------------|
| Port:                      | Combo box | Selects the MIDI input device                                                               |
| Refresh                    | Button    | Rescans available MIDI ports                                                                |
| Connect                    | Button    | Opens or closes the selected MIDI port                                                      |
| Port status                | Indicator | Shows whether the MIDI port is currently open (`Opened` or `Closed`)                        |
| Activity indicator         | Indicator | Shows the most recent MIDI message received                                                 |
| Auto-connect on startup    | Checkbox  | Reopens the MIDI port on launch                                                             |
| Category                   | Combo box | Filters the parameter list by control category                                              |
| Parameter                  | Combo box | Chooses the target parameter for a new binding                                              |
| Learn                      | Button    | Starts listening for the next MIDI message and binds it to the selected parameter           |
| Manual…                    | Button    | Opens a dialog to type a binding's channel, message type and number instead of using Learn  |
| Bindings table             | List      | Shows existing bindings; columns: Parameter, MIDI Source, Channel, Invert, Relative, edit, delete |
| ✎ (edit binding)           | Button    | Opens the manual editor for that row                                                        |
| Invert                     | Checkbox  | Reverses the control direction for the row                                                  |
| Relative                   | Checkbox  | Treats the control as an endless encoder                                                    |
| × (delete row)             | Button    | Removes that binding                                                                        |
| Clear All                  | Button    | Removes every binding                                                                       |
| Profile:                   | Combo box | Picks a saved MIDI mapping profile                                                          |
| Save                       | Button    | Saves current bindings as a profile                                                         |
| Load                       | Button    | Loads the selected profile                                                                  |
| Import...                  | Button    | Imports a profile file into the store — AetherSDR profile XML or a SmartSDR `.map` file     |
| Export...                  | Button    | Exports the current bindings as an AetherSDR profile XML file                               |
| Close                      | Button    | Closes the dialog                                                                           |

## Bind a MIDI button to CW keying

These steps map a physical button on your MIDI controller to the straight key, left paddle, or right paddle CW inputs.

1. In the **Category** combo box, select `Phone/CW`.
2. In the **Parameter** combo box, select one of the following:
   - `Trigger straight key` — sends a straight key press
   - `Trigger CW Left Paddle` — sends a left paddle (dit) event
   - `Trigger CW Right Paddle` — sends a right paddle (dah) event
3. Click **Learn**, then press and hold the physical button on your MIDI controller.
4. Confirm the new row appears in the **Bindings table**.

These three CW actions are momentary (gate) type: the key is held for as long as the MIDI note or button remains active, then released. Use a pad or button that sends both Note On and Note Off messages for correct keying behavior.

If you previously saved a mapping that used the legacy IDs `cw.key`, `cw.dit`, or `cw.dah`, AetherSDR migrates those automatically to the current IDs (`cwkey`, `cwdit`, `cwdah`) on load. No manual action is needed.

## Troubleshooting

- **Learn completes but the key does not fire when pressed** — Check that the port status shows `Opened`. Verify the MIDI controller is sending Note On/Off messages, visible in the Activity indicator.
- **The binding disappears after restarting AetherSDR** — Bindings are saved automatically when Learn completes. If the file was not written, check that AetherSDR has write permission to its settings directory.
- **The `Phone/CW` category is missing from the Parameter list** — Confirm your build of AetherSDR is v0.9.7 or later. The three CW gate actions were added in that release.

## Related

- [Record a new binding with Learn mode](record-a-new-binding-with-learn-mode.md)
- [Connect a MIDI controller](../../getting-started/setup/connect-a-midi-controller.md)
- [Auto-connect MIDI controller on startup](../../getting-started/setup/auto-connect-midi-controller-on-startup.md)
- [Delete a binding](delete-a-binding.md)
- [Save the current mapping as a named profile](save-the-current-mapping-as-a-named-profile.md)