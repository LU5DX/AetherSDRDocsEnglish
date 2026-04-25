# See how many TCI clients are connected

The TCI Server applet shows a live client count in its status indicator. Use this to confirm that logging or digital-mode software has successfully connected to AetherSDR's TCI server.

## Before you start

- The TCI server must be running. Click Enable in the TCI applet if it is not already active. See [Enable the TCI server for Log4OM / SunSDR clients](../../features/tci/enable-the-tci-server-for-log4om-sunsdr-clients.md).
- AetherSDR must be connected to the radio. The TCI applet requires an active radio connection.

## Steps

1. Click the **TCI** tray button on the right sidebar to open the TCI Server applet.
2. Read the server status indicator in the bottom row of the applet, to the right of the **Port** field.

The status indicator shows one of the following:

| Text | Meaning |
|------|---------|
| `(stopped)` | The TCI server is not running. |
| `:<port> (N clients)` | The server is running on the given port with N connected clients. |
| `(port in use)` | The server failed to bind — another process is using the port. |

When at least one client is connected, the status text turns blue. When the server is running but no clients are connected, the text is grey.

## Tips

- The client count updates automatically whenever a client connects or disconnects — there is no need to refresh manually.
- If you expect a client to appear but the count stays at 0, confirm that the client is pointed at the correct port. The current port is shown in the **Port** field directly to the left of the status indicator. The default port is `50001`.

## Troubleshooting

- **Status shows `(port in use)` and Enable snaps off** — another application is already listening on the configured port. Change the port to a different value in the range 1024–65535. Values outside this range revert to `50001`. See [Change the TCI port](../../features/tci/change-the-tci-port.md).
- **Status shows `:<port> (0 clients)` but external software is running** — verify the external software is configured to connect to the same port shown in the **Port** field and to the correct host address.

## Related

- [Enable the TCI server for Log4OM / SunSDR clients](../../features/tci/enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Change the TCI port](../../features/tci/change-the-tci-port.md)
- [Autostart TCI on launch](../../features/tci/autostart-tci-on-launch.md)
- [TCI Server overview](../../features/tci/overview.md)
