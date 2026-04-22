# See how many TCI clients are connected

The TCI Server applet shows a live client count in its status indicator. Use this page to open the applet and read that count.

## Before you start

- AetherSDR must be connected to the radio. The TCI applet requires an active radio connection.
- The TCI server must be enabled. If it is not running, the status shows `(stopped)` and no client count is available.

## Steps

1. Click the **TCI** tray button on the right sidebar to open the TCI Server applet.
2. Look at the status indicator in the bottom row of the applet, to the right of the **Port** field.
3. Read the client count. When the server is running, the status reads `:<port> (N clients)` — for example, `:50001 (2 clients)`. When no clients are connected it reads `:50001 (0 clients)`. When the server is stopped it reads `(stopped)`.

## What each control does

| Control | Description | Default | Range / States | Setting key |
|---|---|---|---|---|
| **Port** | The port the TCI WebSocket server listens on. Changing it restarts the server if enabled. Out-of-range values snap to `50001`. | `50001` | 1024–65535 | `TciPort` |
| **Enable** | Starts or stops the TCI server. If the port is already in use, the toggle snaps back to off and the status shows `(port in use)`. | Off | On / Off | — |
| Server status indicator | Shows current server state and connected client count. Turns blue when one or more clients are connected; turns red on bind failure. | `(stopped)` | `(stopped)`, `:<port> (N clients)`, `(port in use)` | — |
| **RX1–RX4** gain+meter | Combined meter and slider setting the TCI RX gain for each channel. | 0.5 | 0.0–1.0 | `TciRxGain1`–`TciRxGain4` |
| **TX** gain+meter | Combined meter and slider setting the TCI TX gain. | 0.5 | 0.0–1.0 | `TciTxGain` |
| RX/TX slice-assignment labels | Indicate which slice drives each RX or TX row. Show `—` when no slice is assigned or `Slice <letter>` when one is. | `—` | `—` or `Slice <letter>` | — |

## Tips

- The client count updates live. You do not need to reopen the applet; the status indicator refreshes each time a client connects or disconnects.
- If the status shows `(port in use)`, another application is already bound to that port. Change the value in the **Port** field to a different number in the range 1024–65535 and press Enter.

## Troubleshooting

- **Status shows `(stopped)` even though Enable appears active** — The bind failed silently. Close and reopen the applet. Click **Enable** again. If the status immediately shows `(port in use)`, choose a different port.
- **Client count stays at 0** — Confirm the third-party application is configured to connect to the same port shown in the **Port** field, and that no firewall is blocking that port.

## Related

- [Enable the TCI server for Log4OM / SunSDR clients](../../features/tci/enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Change the TCI port](../../features/tci/change-the-tci-port.md)
- [Autostart TCI on launch](../../features/tci/autostart-tci-on-launch.md)
- [TCI Server overview](../../features/tci/overview.md)
