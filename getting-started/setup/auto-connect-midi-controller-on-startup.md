# Auto-connect MIDI controller on startup

Configure AetherSDR to reopen your MIDI controller automatically each time the application launches, so you do not have to connect it manually after every restart.

## Before you start

- A MIDI controller must already be connected to your computer and visible as a MIDI input device.
- You must have connected to the device at least once using the Port: selector and Connect button so that AetherSDR has a device name to remember. See [Connect a MIDI controller](connect-a-midi-controller.md).

## Steps

1. Open `Settings > MIDI Mapping...`.
2. In the **Port:** combo box, select your MIDI controller from the list. If it does not appear, click Refresh.
3. Click Connect. The port status changes to show the connected device name.
4. Check **Auto-connect on startup**.

AetherSDR immediately saves both `MidiPort` and `MidiAutoConnect` to persistent settings. On the next launch, the port will be opened automatically without further action.

## What each control does

| Control | Kind | Behavior | Setting key |
|---|---|---|---|
| Port: | Combo box | Selects the MIDI input device to open. | `MidiPort` |
| Refresh | Button | Rescans available MIDI ports and repopulates Port:. | — |
| Connect | Button | Opens or closes the selected MIDI port. Label toggles to Disconnect when the port is open. | — |
| Auto-connect on startup | Checkbox | When checked, AetherSDR reopens the saved MIDI port on every launch. | `MidiAutoConnect` |

## Tips

- If you rename or replug the controller and the port name changes, uncheck **Auto-connect on startup**, reselect the correct port from Port:, click Connect, then re-check **Auto-connect on startup** to update the saved device name.
- The activity indicator next to the port status updates with each incoming MIDI message, which is a quick way to confirm the port opened successfully at startup.

## Troubleshooting

- **Port does not appear in Port: after launch** — The controller was not plugged in before AetherSDR started. Click Refresh to rescan, select the port, click Connect, and re-save the preference by checking **Auto-connect on startup** again.
- **Auto-connect on startup is checked but the controller is not connected after launch** — The device name saved in `MidiPort` no longer matches any available port, likely because the controller was renamed by the OS or connected to a different USB port. Select the correct port from Port:, click Connect, and re-check **Auto-connect on startup**.

## Related

- [Connect a MIDI controller](connect-a-midi-controller.md)
- [MIDI Controller Mapping overview](../../features/midi-mapping/overview.md)
- [Record a new binding with Learn mode](../../features/midi-mapping/record-a-new-binding-with-learn-mode.md)
- [Save the current mapping as a named profile](../../features/midi-mapping/save-the-current-mapping-as-a-named-profile.md)
- [Load a previously saved MIDI profile](../../features/midi-mapping/load-a-previously-saved-midi-profile.md)
