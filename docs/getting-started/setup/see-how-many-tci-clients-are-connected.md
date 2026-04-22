# See how many TCI clients are connected

The TCI Server applet displays a live client count in its status indicator. Use this to confirm that external software (Log4OM, SunSDR tools, etc.) has successfully connected to AetherSDR's TCI server.

## Before you start

- The TCI server must be running. The status indicator reads `(stopped)` if it is not. Click Enable in the TCI applet to start it, or see [Enable the TCI server for Log4OM / SunSDR clients](../../features/tci/enable-the-tci-server-for-log4om-sunsdr-clients.md).
- AetherSDR must be connected to a radio. The TCI applet requires an active radio connection.

## Steps

1. Click the **TCI** tray button on the right sidebar to open the TCI Server applet.
2. Look at the status indicator to the left of the Enable button.

The indicator shows the current state in one of three forms:

| Status text | Meaning |
|---|---|
| `(stopped)` | Server is not running. |
| `:<port> (N clients)` | Server is running on the given port; N is the number of connected clients. |
| `(port in use)` | Server failed to bind; the port is occupied by another process. |

When one or more clients are connected, the status text turns blue. When the server is running but no clients are connected, the text is grey. The count updates automatically each time a client connects or disconnects.

## Tips

- The client count reflects WebSocket connections currently open to the TCI server. If a client disconnects ungracefully, the count drops as soon as AetherSDR detects the closed connection.
- The port shown in the status indicator matches the value in the Port field (default `50001`, stored as `TciPort`). If you changed the port, confirm the external client is targeting the same value.

## Troubleshooting

- **Status stays `(stopped)` even after clicking Enable** — The port may already be in use by another application. The status indicator will display `(port in use)` in red. Change the Port value to a free port in the range 1024–65535 and click Enable again. Out-of-range values snap back to `50001`.
- **Client count stays at 0** — Verify the external application is configured to connect to the correct host address and port. Check that no firewall is blocking the TCI port.

## Related

- [Enable the TCI server for Log4OM / SunSDR clients](../../features/tci/enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Change the TCI port](../../features/tci/change-the-tci-port.md)
- [Autostart TCI on launch](../../features/tci/autostart-tci-on-launch.md)
- [TCI Server overview](../../features/tci/overview.md)
