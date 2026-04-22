# MIDI Controller Mapping overview

The MIDI Controller Mapping feature lets you bind physical controls on a MIDI controller — knobs, faders, buttons — to radio parameters in AetherSDR. Open the dialog once to set up your device and record bindings, then use named profiles to switch between controller layouts.

## Before you start

- Your MIDI controller must be connected to your computer and recognized by the operating system before AetherSDR can list it.
- MIDI support must be compiled into your build of AetherSDR (`HAVE_MIDI`). If `Settings > MIDI Mapping...` does not appear in the menu, your build does not include MIDI support.

## How it works

Open the dialog via `Settings > MIDI Mapping...`. The dialog is divided into two sections: **MIDI Device** and **Parameter Bindings**.

**MIDI Device** handles selecting and opening your controller's port. Select a port from the `Port:` combo box and click `Connect` to open it. The port status indicator below the combo box shows either `Connected: <port name>` or `Disconnected`. The activity indicator next to it displays the most recent MIDI message received (for example, `Ch 1 CC #7 = 64`), which is useful for verifying that AetherSDR is seeing your controller's output.

**Parameter Bindings** is where you create and manage the mapping between MIDI controls and radio parameters. Use the `Category` combo box to narrow the parameter list, then pick a specific parameter from the `Parameter` combo box. Click `Learn`, move the physical control on your MIDI controller, and AetherSDR records the binding automatically. All current bindings appear in the bindings table. Each row shows the Parameter, MIDI Source, Channel, and per-binding options. Use named profiles to save and restore complete sets of bindings.

## What each control does

### MIDI Device section

| Control | Kind | Behavior | Persisted setting |
|---|---|---|---|
| `Port:` | Combo box | Selects the MIDI input device to use. | `MidiPort` |
| `Refresh` | Button | Rescans available MIDI ports and repopulates `Port:`. | — |
| `Connect` | Button | Opens the selected MIDI port. Label changes to `Disconnect` when the port is open. | — |
| `Auto-connect on startup` | Checkbox | When checked, AetherSDR reopens the last-used MIDI port on launch. | `MidiAutoConnect` |
| Port status | Indicator | Shows `Connected: <port name>` or `Disconnected`. | — |
| Activity indicator | Indicator | Shows the most recent MIDI message received (channel, type, number, value). | — |

### Parameter Bindings section

| Control | Kind | Behavior | Persisted setting |
|---|---|---|---|
| `Category` | Combo box | Filters the `Parameter` list to a control category (All, RX, TX, Phone/CW, EQ, Global). | — |
| `Parameter` | Combo box | Chooses the target radio parameter for a new binding. | — |
| `Learn` | Button | Starts listening for the next MIDI message and binds it to the selected parameter. Label changes to `Cancel Learn` while listening. | — |
| Bindings table | List | Shows all existing bindings. Columns: Parameter, MIDI Source, Channel, Invert, Relative, and a delete button per row. | — |
| `Invert` | Checkbox (per row) | Reverses the control direction for that binding. | — |
| `Relative` | Checkbox (per row) | Treats the control as an endless encoder rather than an absolute value source. | — |
| `×` | Button (per row) | Removes that binding. | — |
| `Clear All` | Button | Removes every binding. | — |
| `Profile:` | Combo box | Selects or names a saved MIDI mapping profile. The field is editable. | — |
| `Save` | Button | Saves the current bindings under the name shown in `Profile:`. | — |
| `Load` | Button | Loads the bindings from the profile named in `Profile:`. | — |
| `Close` | Button | Closes the dialog. | — |

## Tips

- Use the activity indicator to confirm AetherSDR is receiving MIDI before attempting `Learn`. If the indicator does not update when you move a control, the port is not open or the wrong port is selected.
- `Relative` should be enabled for endless encoders (knobs with no hard stops). Leave it unchecked for standard potentiometers and faders.
- Profile names are entered directly in the `Profile:` combo box. Type a new name and click `Save` to create a profile; select an existing name and click `Load` to restore it.

## Related

- [Connect a MIDI controller](../../getting-started/setup/connect-a-midi-controller.md)
- [Auto-connect MIDI controller on startup](../../getting-started/setup/auto-connect-midi-controller-on-startup.md)
- [Record a new binding with Learn mode](record-a-new-binding-with-learn-mode.md)
- [Invert a knob or treat it as an endless encoder](invert-a-knob-or-treat-it-as-an-endless-encoder.md)
- [Delete a binding](delete-a-binding.md)
- [Save the current mapping as a named profile](save-the-current-mapping-as-a-named-profile.md)
- [Load a previously saved MIDI profile](load-a-previously-saved-midi-profile.md)
