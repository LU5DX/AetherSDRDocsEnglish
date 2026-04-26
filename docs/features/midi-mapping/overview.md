# MIDI Controller Mapping Overview

The MIDI Controller Mapping feature lets you bind physical knobs, faders, and buttons on a MIDI controller to radio parameters in AetherSDR. Once bindings are saved, you can recall them as named profiles and optionally reconnect the controller automatically on each launch.

## Before you start

- Your MIDI controller must be connected to the computer before opening the dialog.
- MIDI support must be present in your AetherSDR build. If `Settings > MIDI Mapping...` does not appear in the menu, your build was compiled without MIDI support.

## How it works

Open the dialog at `Settings > MIDI Mapping...`. The dialog is divided into two sections: **MIDI Device** and **Parameter Bindings**.

**MIDI Device** handles port selection and connection. Select your controller from the Port: combo box, click Refresh if it does not appear, then click Connect to open the port. The port status indicator shows "Connected" (green) or "Disconnected" (grey). The activity indicator displays the most recent MIDI message received — for example, `Ch 1 CC #7 = 64` — which is useful for confirming your controller is sending data.

**Parameter Bindings** is where you create and manage the mappings between MIDI messages and radio controls. Use the Category and Parameter combo boxes to locate the target parameter, then click Learn and move a knob or fader on your controller. AetherSDR records the incoming MIDI message and adds a row to the bindings table. Each row in the table can be adjusted individually with Invert and Relative checkboxes, or removed with the × (delete row) button. Click Clear All to remove every binding at once.

Bindings can be saved to and loaded from named profiles using the Profile:, Save, and Load controls at the bottom of the dialog.

Bindings and the last-used port are persisted automatically. The `MidiPort` setting stores the selected port name and `MidiAutoConnect` stores whether the port should be reopened on launch.

## What each control does

| Control | Kind | Behavior | Persisted setting |
|---|---|---|---|
| Port: | Combo box | Selects the MIDI input device. | `MidiPort` |
| Refresh | Button | Rescans available MIDI ports. | — |
| Connect | Button | Opens the selected MIDI port. When a port is open the label changes to Disconnect. | — |
| Port status | Indicator | Shows whether the MIDI port is currently open. States: Opened, Closed. | — |
| Activity indicator | Indicator | Shows the most recent MIDI message received. | — |
| Auto-connect on startup | Checkbox | Reopens the saved MIDI port automatically when AetherSDR launches. | `MidiAutoConnect` |
| Category | Combo box | Filters the Parameter combo box to a control category (All, RX, TX, Phone/CW, EQ, Global). | — |
| Parameter | Combo box | Selects the target radio parameter for a new binding. | — |
| Learn | Button | Starts listening for the next incoming MIDI message and binds it to the selected parameter. Click again (labelled Cancel Learn) to abort. | — |
| Bindings table | List | Shows all existing bindings. Columns: Parameter, MIDI Source, Channel, Invert, Relative, and a delete button. | — |
| Invert | Checkbox (per row) | Reverses the control direction for that binding. | — |
| Relative | Checkbox (per row) | Treats the control as an endless encoder rather than an absolute value. | — |
| × (delete row) | Button (per row) | Removes that binding. | — |
| Clear All | Button | Removes every binding. | — |
| Profile: | Combo box | Selects or names a saved MIDI mapping profile. The field is editable. | — |
| Save | Button | Saves the current bindings under the name entered in Profile:. | — |
| Load | Button | Loads bindings from the profile selected in Profile:. | — |
| Close | Button | Closes the dialog. | — |

## Tips

- Move a control on your MIDI hardware while the activity indicator is visible to confirm AetherSDR is receiving messages before attempting to add a binding.
- If you use multiple controllers or different physical setups, save a separate profile for each with a distinct name in Profile: so you can switch quickly with Load.

## Related

- [Connect a MIDI controller](../../getting-started/setup/connect-a-midi-controller.md)
- [Auto-connect MIDI controller on startup](../../getting-started/setup/auto-connect-midi-controller-on-startup.md)
- [Record a new binding with Learn mode](record-a-new-binding-with-learn-mode.md)
- [Invert a knob or treat it as an endless encoder](invert-a-knob-or-treat-it-as-an-endless-encoder.md)
- [Delete a binding](delete-a-binding.md)
- [Save the current mapping as a named profile](save-the-current-mapping-as-a-named-profile.md)
- [Load a previously saved MIDI profile](load-a-previously-saved-midi-profile.md)
