# MIDI Controller Mapping

The MIDI Controller Mapping dialog lets you configure a MIDI controller for use with AetherSDR. You can select a device, record bindings using Learn mode or add them manually, tune per-binding behavior, and save, load, import, or export mapping profiles.

## Open the dialog

1. Go to `Settings > MIDI Mapping...`.

The dialog opens, showing the current MIDI port status and any existing bindings.

## Select a MIDI device

1. From the `Port:` combo box, select the MIDI input device you want to use.
2. Click `Refresh` to rescan available MIDI ports if your device is not listed.
3. Click `Connect` to open the selected port. The button text changes to "Disconnect" when the port is open.
4. (Optional) Check `Auto-connect on startup` to automatically reopen this port the next time you launch AetherSDR.

The port status indicator shows "Connected: [device name]" with a green label when the port is open, and "Disconnected" with a gray label when it is closed.

## Record a new binding with Learn mode

1. From the `Category` combo box, select the control category for the parameter you want to map.
2. From the `Parameter` combo box, select the target parameter for the new binding.
3. Click `Learn`. The button highlights to indicate it is listening.
4. Move or press the control on your MIDI device that you want to map.

The binding appears in the bindings table with the parameter name, MIDI source, and channel.

### Note on momentary (Gate) actions

In v0.9.7, three new momentary (Gate) actions were added in the Phone/CW category:

- `Trigger straight key` (id: `cwkey`)
- `Trigger CW Left Paddle` (id: `cwdit`)
- `Trigger CW Right Paddle` (id: `cwdah`)

Legacy dotted IDs (`cw.key`, `cw.dit`, `cw.dah`) are automatically migrated on read.

## Add a binding manually

Instead of using Learn mode, you can type a binding's MIDI details directly.

1. Select the `Category` and `Parameter` as described above.
2. Click `Manual…`. A dialog opens where you can enter the binding's channel, message type, and number.
3. Enter the required values and confirm.

The binding appears in the table. You can also reopen this editor for an existing binding by clicking the `✎` button in its row.

## Tune per-binding behavior

Each binding row in the bindings table has two optional controls:

- **Invert**: Check this checkbox to reverse the control direction for that row. For example, if turning a knob clockwise normally increases a value, checking Invert makes it decrease the value instead.
- **Relative**: Check this checkbox to treat the control as an endless encoder. Use this for rotary encoders that do not have physical stops and send relative position changes.

## Edit an existing binding

1. In the bindings table, locate the row for the binding you want to correct.
2. Click `✎` in that row.
3. Adjust the channel, message type, or number in the manual editor that opens.
4. Confirm your changes.

## Delete a binding

### Delete a single binding

1. In the bindings table, locate the row for the binding you want to remove.
2. Click `×` in the rightmost column of that row.

The row is removed immediately. The change is saved automatically.

### Delete all bindings at once

1. Click `Clear All`.

Every row in the bindings table is removed. The change is saved automatically.

## Save the current mapping as a named profile

1. In the `Profile:` combo box, type a name for your profile.
2. Click `Save`.

The profile is saved and appears in the profile list for future use.

## Load a previously saved MIDI profile

1. From the `Profile:` combo box, select the profile you want to load.
2. Click `Load`.

The bindings from the selected profile replace the current bindings in the table.

## Import a profile from a file

1. Click `Import...`.
2. Choose a profile file. You can import an AetherSDR profile XML file or a SmartSDR `.map` file.

AetherSDR reports how many bindings were imported. Click `Load` to apply the imported bindings.

## Export the current bindings to a file

1. Click `Export...`.
2. Choose a location and file name for the exported profile.

The current bindings are written as an AetherSDR profile XML file. The directory you choose is remembered for the next import or export.

## Activity monitoring

The activity indicator shows the most recent MIDI message received, displayed in a monospace font. Use this to verify that your MIDI controller is sending messages and that the port is working correctly.

## What each control does

| Control                | Description                                     | Notes |
|------------------------|-------------------------------------------------|-------|
| `Port:`                | Selects MIDI input device.                      |       |
| `Refresh`              | Rescans available MIDI ports.                   |       |
| `Connect`              | Opens/closes the selected MIDI port.            |       |
| `Auto-connect on startup` | Reopens MIDI port on launch.                 |       |
| `Category`             | Filters parameter combo to a control category.  |       |
| `Parameter`            | Chooses the target parameter for a new binding. |       |
| `Learn`                | Starts listening for the next MIDI message.     |       |
| `Manual…`              | Opens a dialog to type a binding's channel, message type and number. | New in v26.8.4. |
| Bindings table         | Shows existing bindings with per-row controls.  | Columns: Parameter, MIDI Source, Channel, Invert, Relative, (edit), (delete). |
| `✎` (edit binding)     | Opens the manual editor to correct this binding's channel, type and number. | New in v26.8.4. |
| `Invert` (per row)     | Reverses the control direction for the row.     |       |
| `Relative` (per row)   | Treats the control as an endless encoder.       |       |
| `×` (delete row)       | Removes that binding.                           |       |
| `Clear All`            | Removes every binding.                          |       |
| `Profile:`             | Picks a saved MIDI mapping profile.             |       |
| `Save`                 | Saves current bindings as a profile.            |       |
| `Load`                 | Loads the selected profile.                     |       |
| `Import...`            | Imports a profile file (AetherSDR XML or SmartSDR `.map`). | New in v26.8.4. |
| `Export...`            | Exports current bindings as an AetherSDR profile XML file. | New in v26.8.4. |
| `Close`                | Closes the dialog.                              |       |

## Tips

- If you delete a binding by mistake, you can restore it by loading a previously saved profile.
- Before using `Clear All`, consider saving your current bindings as a profile first.
- Use `Import...` to bring in bindings from SmartSDR if you are migrating from that software.
- The activity indicator is helpful for diagnosing connection issues—if you move a control and see no activity, check that the correct port is selected and connected.

## Related

- [Record a new binding with Learn mode](#record-a-new-binding-with-learn-mode)
- [Add a binding manually](#add-a-binding-manually)
- [Delete a binding](#delete-a-binding)
- [Save the current mapping as a named profile](#save-the-current-mapping-as-a-named-profile)
- [Load a previously saved MIDI profile](#load-a-previously-saved-midi-profile)