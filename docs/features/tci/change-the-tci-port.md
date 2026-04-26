# Change the TCI port

Change the port the TCI WebSocket server listens on so it does not conflict with other software on your system.

## Before you start

- The radio must be connected. The TCI applet is unavailable without a radio connection.
- Open the TCI applet by clicking the TCI tray button on the right sidebar if it is not already visible.

## Steps

1. In the TCI applet, locate the Port field next to the "Port:" label at the bottom of the applet.
2. Click the Port field and type the new port number. Valid range: 1024–65535. Default: `50001`. Values outside this range snap back to `50001`.
3. Press Enter or Tab to commit the change. AetherSDR saves the value to `TciPort` immediately.
4. If the server is already running (Enable is checked), AetherSDR stops and restarts the server on the new port automatically. No manual restart is needed.
5. Confirm the new port is active by checking the status indicator next to the Port field. It shows `:<port> (N clients)` when the server is running successfully.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Port | `50001` | 1024–65535 | `TciPort` | Sets the TCP port the TCI WebSocket server binds to. Out-of-range values snap to `50001`. If the server is running when the value is committed, the server restarts on the new port. |
| Enable | Off | On / Off | — | Starts or stops the TCI server. If the port is already in use, the toggle snaps back to off and the status shows `(port in use)` in red. |

## Troubleshooting

- **Status shows `(port in use)` and Enable snaps off** — Another process is already bound to the port you entered. Choose a different port number, press Enter to commit it, then click Enable again.
- **Port field reverts to `50001`** — The value you entered was outside the 1024–65535 range. Enter a value within that range.

## Related

- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Autostart TCI on launch](autostart-tci-on-launch.md)
- [TCI Server overview](overview.md)
