# Change the TCI port

Change the port the TCI WebSocket server listens on. Do this when port 50001 conflicts with another application or when your logging or digital-mode software expects a different port.

## Before you start

- AetherSDR must be connected to the radio. The TCI applet requires an active radio connection.
- Have the TCI applet open. If it is not visible, click the **TCI** tray button on the right sidebar.

## Steps

1. In the TCI applet, locate the **Port** field at the bottom of the panel.
2. Click the **Port** field and type the new port number. Valid values are 1024–65535. The default is `50001`.
3. Press **Enter** or click away from the field to confirm. Values outside 1024–65535 snap back to `50001`.
4. If the server is already running (Enable is active), AetherSDR stops and restarts the server on the new port automatically. No manual toggle is needed.
5. The server status indicator updates to show the new port in the format `:<port> (N clients)`.

The new port is saved to `TciPort` and persists across restarts.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| **Port** | `50001` | 1024–65535 | `TciPort` | Sets the port the TCI WebSocket server binds to. Changing the value while the server is running restarts the server on the new port. Out-of-range values snap to `50001`. |
| **Enable** | Off | On / Off | — | Starts or stops the TCI server. If the port is already in use, the toggle snaps back to off and the status shows `(port in use)`. |

## Troubleshooting

- **Status shows `(port in use)` and Enable snaps off** — Another application is already bound to that port. Enter a different port number in the **Port** field and click Enable again.
- **Port field reverts to `50001` after editing** — The value you entered was outside the 1024–65535 range. Enter a value within that range.

## Related

- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Autostart TCI on launch](autostart-tci-on-launch.md)
- [TCI Server overview](overview.md)
