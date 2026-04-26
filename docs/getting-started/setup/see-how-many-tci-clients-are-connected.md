# See how many TCI clients are connected

The TCI Server applet shows a live client count in its status indicator. Use this to confirm that third-party software such as Log4OM or SunSDR tools has successfully connected.

## Before you start

- The TCI server must be running. The Enable button must be in its checked (green) state.
- The TCI applet must be visible. If it is not, click the **TCI** tray button on the right sidebar to show it.

## Steps

1. Click the **TCI** tray button on the right sidebar to open the TCI Server applet.
2. Read the status indicator next to the Port field at the bottom of the applet. When the server is running, it displays in the form `:<port> (N clients)` — for example, `:50001 (2 clients)`. The count updates automatically whenever a client connects or disconnects.

## What each control does

| Control | Description | Default | Range | Setting key |
|---|---|---|---|---|
| Port | TCP port the TCI WebSocket server listens on. Out-of-range values snap to 50001. | `50001` | 1024–65535 | `TciPort` |
| Enable | Starts or stops the TCI server. When checked, the button turns green. If the port is already in use, the toggle snaps back to off and the status shows `(port in use)` in red. | Off | — | — |
| Server status | Read-only indicator showing server state and connected client count. Shows `(stopped)`, `:<port> (N clients)`, or `(port in use)`. Text turns blue when one or more clients are connected. | `(stopped)` | — | — |
| RX1–RX4 gain+meter | Combined meter and slider setting the TCI RX gain for each channel. | 0.5 | 0.0–1.0 | `TciRxGain1`–`TciRxGain4` |
| TX gain+meter | Combined meter and slider setting the TCI TX gain. | 0.5 | 0.0–1.0 | `TciTxGain` |
| RX/TX slice-assignment labels | Read-only. Shows which slice drives each RX or TX row (for example, `Slice A`), or `—` if unassigned. | `—` | — | — |

## Troubleshooting

- **Status shows `(stopped)` instead of a client count** — Enable has not been toggled on, or the server stopped after a failed bind. Click Enable to start the server. If the status immediately changes to `(port in use)`, another application is occupying the configured port. Change the value in the Port field to a free port in the range 1024–65535 and click Enable again.
- **Status shows `:<port> (0 clients)` but your software should be connected** — Confirm the external application is connecting to the same port shown in the status indicator. Check that no firewall is blocking the port.

## Related

- [Enable the TCI server for Log4OM / SunSDR clients](../../features/tci/enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Change the TCI port](../../features/tci/change-the-tci-port.md)
- [Autostart TCI on launch](../../features/tci/autostart-tci-on-launch.md)
- [TCI Server overview](../../features/tci/overview.md)
