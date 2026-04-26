# Connect a MIDI controller

This page explains how to select and connect a MIDI controller in AetherSDR so that physical knobs, faders, and buttons on the device become available for parameter bindings.

## Before you start

- Your MIDI controller must be plugged in and recognised by the operating system before opening AetherSDR.
- AetherSDR must have been built with MIDI support (`Settings > MIDI Mapping...` must be present in the menu; if it is missing, your build does not include MIDI).

## Steps

1. Go to `Settings > MIDI Mapping...`. The **MIDI Controller Mapping** dialog opens.
2. In the **MIDI Device** section, open the **Port:** drop-down and select your controller from the list.
3. If your controller does not appear, click **Refresh**. AetherSDR rescans available MIDI ports and repopulates the **Port:** list.
4. Click **Connect**. AetherSDR opens the selected port. The port status area changes to **Connected:** followed by the device name, and the **Connect** button label changes to **Disconnect**.
5. Move a knob or press a button on the controller. The activity indicator next to the port status should show the most recent MIDI message received (for example, `Ch 1 CC #7 = 64`). This confirms the device is sending data.
6. To have AetherSDR reopen this port every time it starts, check **Auto-connect on startup**.
7. Click **Close** when done.

## What each control does

| Control | Kind | Behavior | Persisted setting |
|---|---|---|---|
| **Port:** | Drop-down | Selects the MIDI input device to use. | `MidiPort` |
| **Refresh** | Button | Rescans available MIDI ports and repopulates the **Port:** list. | — |
| **Connect** | Button | Opens the selected MIDI port. Label changes to **Disconnect** while the port is open; clicking again closes it. | — |
| **Auto-connect on startup** | Checkbox | When checked, AetherSDR reopens the last connected MIDI port on launch. | `MidiAutoConnect` |
| Port status | Indicator | Shows **Connected:** followed by the device name when the port is open, or **Disconnected** when closed. | — |
| Activity indicator | Indicator | Displays the most recent MIDI message received (channel, type, number, and value). | — |

## Tips

- If the port status shows **Connected** but the activity indicator never updates, check that your controller is set to transmit on a MIDI channel and that no other application has the port exclusively locked.
- The activity indicator updates in real time. Use it to verify the correct port is selected before creating bindings.

## Troubleshooting

- **`Settings > MIDI Mapping...` is not in the menu** — Your AetherSDR build was compiled without MIDI support. Obtain a build that includes the `HAVE_MIDI` feature.
- **Controller does not appear in the Port: list** — Click **Refresh**. If the device still does not appear, check that the operating system recognises it (verify in your system's MIDI or audio device settings) and that no other application holds an exclusive lock on the port.
- **Port status shows Connected but the activity indicator is blank** — The device is open but not sending data. Check the controller's power, USB or DIN connection, and that it is configured to output MIDI.

## Related

- [MIDI Controller Mapping overview](../../features/midi-mapping/overview.md)
- [Auto-connect MIDI controller on startup](auto-connect-midi-controller-on-startup.md)
- [Record a new binding with Learn mode](../../features/midi-mapping/record-a-new-binding-with-learn-mode.md)
- [Load a previously saved MIDI profile](../../features/midi-mapping/load-a-previously-saved-midi-profile.md)
