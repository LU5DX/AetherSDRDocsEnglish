# MIDI Controller Mapping Overview

The MIDI Controller Mapping feature lets you bind physical knobs, faders, and buttons on a MIDI controller to radio parameters in AetherSDR. Once bindings are saved, you can recall them as named profiles and optionally reconnect the controller automatically on each launch.

## Before you start

- Your MIDI controller must be connected to the computer before opening the dialog.
- MIDI support must be present in your AetherSDR build. If `Settings > MIDI Mapping...` does not appear in the menu, your build was compiled without MIDI support.

## How it works

Open the dialog at `Settings > MIDI Mapping...`. The dialog is divided into two sections: **MIDI Device** and **Parameter Bindings**.

**MIDI Device** handles port selection and connection. Select your controller from the Port: combo box, click Refresh if it does not appear, then click Connect to open the port. The port status indicator shows "Connected" (green) or "Disconnected" (grey). The activity indicator displays the most recent MIDI message received — for example, `Ch 1 CC #7 = 64` — which is useful for confirming your controller is sending data.

**Parameter Bindings** is where you create and manage the mappings between MIDI messages and radio controls. Use the Category and Parameter combo boxes to locate the target parameter, then click Learn and move a knob or fader on your controller. AetherSDR records the incoming MIDI message and adds a row to the bindings table. Each row in the table can be adjusted individually with Invert and Relative checkboxes, edited with the ✎ (edit) button, or removed with the × (delete row) button. Click Clear All to remove every binding at once.

As an alternative to Learn mode, you can click Manual… to type a binding's channel, message type, and number directly instead of moving a hardware control. The same manual editor is also available per row via the ✎ (edit) button.

Bindings can be saved to, loaded from, imported into, and exported from named profiles using the Profile:, Save, Load, Import..., and Export... controls at the bottom of the dialog.

Bindings and the last-used port are persisted automatically. The `MidiPort` setting stores the selected port name and `MidiAutoConnect` stores whether the port should be reopened on launch. The dialog remembers its size and position between sessions.

## What each control does

| Control | Kind | Behavior | Persisted setting |
|---|---|---|---|
| Port: | Combo box | Selects the MIDI input device. | `MidiPort` |
| Refresh | Button | Rescans available MIDI ports. | — |
| Connect | Button | Opens the selected MIDI port. When a port is open the label changes to Disconnect. | — |
| Port status | Indicator | Shows whether the MIDI port is currently open. States: Opened, Closed. | — |
| Activity indicator | Indicator | Shows the most recent MIDI message received. | — |
| Auto-connect on startup | Checkbox | Reopens the saved MIDI port automatically when AetherSDR launches. | `MidiAutoConnect` |
| Category | Combo box | Filters the Parameter combo box to a control category. Categories include: All, RX, TX, Phone/CW, EQ, Global, Mode, Band, Filter, Slice, Display, Frequency. | — |
| Parameter | Combo box | Selects the target radio parameter for a new binding. In v0.9.7, three new momentary (Gate) actions were added in the Phone/CW category: "Trigger straight key" (id: `cwkey`), "Trigger CW Left Paddle" (id: `cwdit`), "Trigger CW Right Paddle" (id: `cwdah`). Legacy dotted IDs (`cw.key`, `cw.dit`, `cw.dah`) are auto-migrated on read. | — |
| Learn | Button | Starts listening for the next incoming MIDI message and binds it to the selected parameter. Click again (labelled Cancel Learn) to abort. | — |
| Manual… | Button | Opens a dialog to type a binding's channel, message type and number instead of using Learn mode. New in v26.8.4. Opens the same manual editor used by the per-row edit button. | — |
| Bindings table | List | Shows all existing bindings. Columns: Parameter, MIDI Source, Channel, Invert, Relative, edit (✎) and delete (×) buttons. | — |
| ✎ (edit binding) | Button (per row) | Opens the manual editor to correct this binding's channel, message type and number. New in v26.8.4. | — |
| Invert | Checkbox (per row) | Reverses the control direction for that binding. | — |
| Relative | Checkbox (per row) | Treats the control as an endless encoder rather than an absolute value. | — |
| × (delete row) | Button (per row) | Removes that binding. | — |
| Clear All | Button | Removes every binding. | — |
| Profile: | Combo box | Selects or names a saved MIDI mapping profile. The field is editable. | — |
| Save | Button | Saves the current bindings under the name entered in Profile:. | — |
| Load | Button | Loads bindings from the profile selected in Profile:. | — |
| Import... | Button | Imports a profile file into the store — an AetherSDR profile XML or a SmartSDR ".map" file. New in v26.8.4. Reports how many bindings were imported and lets you Load to apply. | — |
| Export... | Button | Exports the current bindings as an AetherSDR profile XML file. New in v26.8.4. The last-used directory is remembered. | `MidiImportExportPath` |
| Close | Button | Closes the dialog. | — |

## Tips

- Move a control on your MIDI hardware while the activity indicator is visible to confirm AetherSDR is receiving messages before attempting to add a binding.
- If you use multiple controllers or different physical setups, save a separate profile for each with a distinct name in Profile: so you can switch quickly with Load.
- Use the expanded Category options (Mode, Band, Filter, Slice, Display, Frequency) to quickly narrow down parameters for specific functions.
- The dialog now adapts to the current theme. Port status and activity labels, as well as the bindings table, use theme colors instead of hardcoded values.
- When adding a binding, Learn mode is the fastest way to capture the exact message your hardware sends. Use Manual… or the per-row ✎ button only when you need to specify a message that is difficult to generate with hardware, or to correct an existing binding.

## Related

- [Connect a MIDI controller](../../getting-started/setup/connect-a-midi-controller.md)
- [Auto-connect MIDI controller on startup](../../getting-started/setup/auto-connect-midi-controller-on-startup.md)
- [Record a new binding with Learn mode](record-a-new-binding-with-learn-mode.md)
- Enter a binding manually
- Edit an existing binding
- [Invert a knob or treat it as an endless encoder](invert-a-knob-or-treat-it-as-an-endless-encoder.md)
- [Delete a binding](delete-a-binding.md)
- [Save the current mapping as a named profile](save-the-current-mapping-as-a-named-profile.md)
- [Load a previously saved MIDI profile](load-a-previously-saved-midi-profile.md)
- Import a MIDI mapping from a file
- Export the current mapping to a file