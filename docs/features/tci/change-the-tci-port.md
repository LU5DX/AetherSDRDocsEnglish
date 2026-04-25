# Change the TCI port

Change the port that the TCI WebSocket server listens on. Do this when the default port conflicts with another application or when your logging or digital-mode software requires a specific port.

## Before you start

- AetherSDR must be connected to your FLEX-8600 radio. The TCI applet is not available without a radio connection.
- Open the TCI applet by clicking the TCI tray button on the right sidebar if it is not already visible.

## Steps

1. In the TCI applet, locate the Port field next to the "Port:" label.
2. Click the Port field and type the new port number. Valid values are 1024–65535. The default is `50001`. Values outside this range snap back to `50001`.
3. Press Enter or Tab to confirm the change. The setting is saved immediately to `TciPort`.
4. If the server is currently enabled, it restarts automatically on the new port. The status indicator updates to show the new port number and connected client count.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Port | `50001` | 1024–65535 | `TciPort` | Sets the WebSocket port. If the server is running when you change the value, the server restarts on the new port. Out-of-range values snap to `50001`. |
| Enable | Off | On / Off | — | Starts or stops the TCI server. If the port is already in use, the toggle snaps back to off and the status shows `(port in use)`. |

## Tips

- If you change the port while the server is stopped, the new value is saved and used the next time you click Enable.
- Tell your TCI client software (Log4OM, SunSDR tools, etc.) the new port number before restarting the server, or clients will fail to connect.

## Troubleshooting

- **Status shows `(port in use)` and Enable snaps off** — Another application is already bound to that port. Choose a different port number and click Enable again.
- **Clients cannot connect after a port change** — The client software still has the old port configured. Update the port in the client and reconnect.

## Related

- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Autostart TCI on launch](autostart-tci-on-launch.md)
- [TCI Server overview](overview.md)
