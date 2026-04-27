# Change the TCI port

The TCI server listens on a configurable port. Change the port when the default conflicts with another application or when your logging or digital-mode software requires a specific port number.

## Before you start

- AetherSDR must be connected to the radio. The TCI applet requires an active radio connection.
- Open the TCI applet by clicking the **TCI** tray button on the right sidebar if it is not already visible.

## Steps

1. In the TCI applet, locate the **Port** field next to the "Port:" label at the bottom of the applet.
2. Click the **Port** field and type the new port number. Valid values are 1024–65535. The default is `50001`. Values outside this range snap back to `50001`.
3. Press **Enter** or move focus away from the field to confirm. The value is saved to `TciPort`.
4. If the server is currently running (Enable is checked), AetherSDR stops the server and restarts it on the new port automatically. No additional action is required.
5. If the server is not running, click **Enable** to start it on the new port.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| **Port** field | `50001` | 1024–65535 | `TciPort` | Sets the WebSocket port. Out-of-range values snap to `50001`. If the server is enabled, changing the port restarts the server immediately. |
| **Enable** | Off | On / Off | — | Starts or stops the TCI server. If the port is already in use, the toggle snaps back to off and the status shows `(port in use)`. |
| Server status indicator | `(stopped)` | `(stopped)`, `:<port> (N clients)`, `(port in use)` | — | Shows current server state. Turns red on bind failure. |

## Tips

- If you change the port while the server is enabled, the restart is immediate. Connected clients will be disconnected and must reconnect to the new port.
- If the status shows `(port in use)` after clicking **Enable**, choose a different port number and try again.

## Troubleshooting

- **Status shows `(port in use)` after enabling** — Another application is already bound to that port. Enter a different port number in the **Port** field and click **Enable** again.
- **Port field reverts to `50001`** — The value entered was outside the 1024–65535 range. Enter a value within the valid range.

## Related

- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Autostart TCI on launch](autostart-tci-on-launch.md)
- [TCI Server overview](overview.md)
