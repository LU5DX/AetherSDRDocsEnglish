# Connect a MIDI controller

Use this page to select your MIDI input device, open the port, and confirm AetherSDR is receiving messages from your controller.

## Before you start

- Your MIDI controller must be connected to the computer and recognized by the OS before opening AetherSDR.
- MIDI support must be compiled in (`HAVE_MIDI`). If `Settings > MIDI Mapping...` does not appear in the menu, your build does not include MIDI.

## Steps

1. Go to `Settings > MIDI Mapping...`. The MIDI Controller Mapping dialog opens.
2. In the Port: combo box, select your MIDI controller from the list of available devices. If the list is empty or your device is missing, click Refresh to rescan.
3. Click Connect. The port status label changes to **Connected:** followed by the device name. If the connection fails, the label remains **Disconnected**.
4. Move a knob, fader, or button on your controller. The activity indicator displays the most recent message received, for example `Ch 1 CC #7 = 64`. This confirms AetherSDR is receiving MIDI data.
5. If you want AetherSDR to open this device automatically on every launch, check Auto-connect on startup. This persists as `MidiAutoConnect`.
6. Click Close.

## What each control does

| Control | Kind | Behavior | Setting key |
|---|---|---|---|
| Port: | Combo box | Selects the MIDI input device. | `MidiPort` |
| Refresh | Button | Rescans available MIDI ports. | — |
| Connect | Button | Opens or closes the selected MIDI port. Label toggles to **Disconnect** when the port is open. | — |
| Auto-connect on startup | Checkbox | Reopens the saved MIDI port each time AetherSDR launches. | `MidiAutoConnect` |
| Port status | Indicator | Shows **Connected:** with the device name, or **Disconnected**. | — |
| Activity indicator | Indicator | Shows the most recent MIDI message received (channel, type, number, value). | — |

## Troubleshooting

- **Port: list is empty** — Your OS has not enumerated the device yet. Unplug and replug the controller, then click Refresh.
- **Connect fails and status stays Disconnected** — Another application may have exclusive access to the MIDI port. Close any DAW, virtual MIDI router, or other SDR application that might hold the port open, then click Connect again.
- **Activity indicator shows no messages after connecting** — Verify the controller is sending on the channel and message type you expect. Try moving a different control. If nothing appears, the port may have opened but the device is not transmitting.

## Related

- [MIDI Controller Mapping overview](../../features/midi-mapping/overview.md)
- [Record a new binding with Learn mode](../../features/midi-mapping/record-a-new-binding-with-learn-mode.md)
- [Auto-connect MIDI controller on startup](auto-connect-midi-controller-on-startup.md)
- [Load a previously saved MIDI profile](../../features/midi-mapping/load-a-previously-saved-midi-profile.md)
- [Save the current mapping as a named profile](../../features/midi-mapping/save-the-current-mapping-as-a-named-profile.md)
