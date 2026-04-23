# Change the TCI port

The TCI server listens on a configurable TCP port. Change the port if the default conflicts with another application or if your logging or digital-mode software requires a specific port number.

## Before you start

- AetherSDR must be connected to the radio. The TCI applet requires an active radio connection.
- Open the TCI applet by clicking the **TCI** tray button on the right sidebar if it is not already visible.

## Steps

1. Locate the **Port** field at the bottom of the TCI applet, to the right of the "Port:" label.
2. Click the **Port** field and type the new port number. Valid values are 1024–65535. The default is `50001`.
3. Press **Enter** or click away from the field to confirm. If you enter a value outside 1024–65535, the field resets to `50001` and saves that value.
4. If the server is already running (Enable is checked), it restarts automatically on the new port. No additional action is required.

The new port is saved to `TciPort` and persists across sessions.

## What each control does

| Control | Default | Valid range | Persisted setting |
|---|---|---|---|
| **Port** field | `50001` | 1024–65535 | `TciPort` |
| **Enable** toggle | Off | On / Off | — |
| Server status indicator | `(stopped)` | `(stopped)`, `:<port> (N clients)`, `(port in use)` | — |

## Tips

- The server status indicator updates immediately after a port change. If the status shows `(port in use)` and **Enable** snaps back to unchecked, another process is already bound to that port. Choose a different port number.
- If you have `Settings > Autostart TCI with AetherSDR` enabled, the saved `TciPort` value is used at the next launch with no further action needed.

## Troubleshooting

- **Status shows `(port in use)` and Enable turns off** — The port is already bound by another application. Enter a different port number, then click **Enable** again.
- **Port field resets to 50001** — The value you entered was outside the 1024–65535 range. Enter a value within that range.

## Related

- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Autostart TCI on launch](autostart-tci-on-launch.md)
- [TCI Server overview](overview.md)
