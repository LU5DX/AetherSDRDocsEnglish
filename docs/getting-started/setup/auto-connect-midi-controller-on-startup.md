# Auto-connect MIDI controller on startup

When AetherSDR launches, it can automatically reopen the last-used MIDI port so your controller is ready without manual intervention each session.

## Before you start

- AetherSDR must have been built with MIDI support (`Settings > MIDI Mapping...` must appear in the Settings menu).
- Your MIDI controller must be physically connected and recognized by the operating system.
- You must have connected to the port at least once manually so that AetherSDR has a device to reopen. See [Connect a MIDI controller](connect-a-midi-controller.md).

## Steps

1. Go to `Settings > MIDI Mapping...`.
2. In the **Port:** combo box, select your MIDI controller.
3. Click **Connect**. The port status changes to show the connected device name.
4. Check **Auto-connect on startup**.

AetherSDR saves both `MidiPort` and `MidiAutoConnect` immediately. On the next launch, the port reopens automatically without any further action.

## What each control does

| Control | Kind | Behavior | Persisted setting |
|---|---|---|---|
| **Port:** | Combo box | Selects the MIDI input device to use | `MidiPort` |
| **Refresh** | Button | Rescans available MIDI ports | — |
| **Connect** | Button | Opens or closes the selected MIDI port | — |
| **Auto-connect on startup** | Checkbox | Reopens the saved MIDI port each time AetherSDR launches | `MidiAutoConnect` |

## Tips

- If you unplug and replug the controller, click **Refresh** to repopulate the **Port:** list before clicking **Connect**.
- The port status and activity indicator update in real time. Confirm the activity indicator shows incoming messages before closing the dialog.

## Troubleshooting

- **Port list is empty after plugging in the controller** — Click **Refresh** to rescan. If the port still does not appear, verify the operating system recognizes the device.
- **Auto-connect does not work on the next launch** — Confirm you clicked **Connect** and saw a connected status before checking **Auto-connect on startup**. The setting saves the most recently opened port name; if the device name changed (for example, on a different USB port on some systems), select the correct port manually, connect again, and re-check **Auto-connect on startup**.

## Related

- [Connect a MIDI controller](connect-a-midi-controller.md)
- [MIDI Controller Mapping overview](../../features/midi-mapping/overview.md)
- [Record a new binding with Learn mode](../../features/midi-mapping/record-a-new-binding-with-learn-mode.md)
- [Save the current mapping as a named profile](../../features/midi-mapping/save-the-current-mapping-as-a-named-profile.md)
