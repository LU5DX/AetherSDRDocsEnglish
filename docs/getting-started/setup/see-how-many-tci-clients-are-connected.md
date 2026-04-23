# See how many TCI clients are connected

The TCI Server applet shows a live client count in its status indicator whenever the server is running. Use this to confirm that external software such as Log4OM or SunSDR tools has successfully connected.

## Before you start

- AetherSDR must be connected to a radio. The TCI applet requires an active radio connection.
- The TCI server must be enabled. If it is not, the status indicator shows `(stopped)` and no client count is available.

## Steps

1. Click the **TCI** tray button on the right sidebar to open the TCI Server applet.
2. Read the status indicator to the left of the **Enable** button.

When the server is running, the indicator shows `:<port> (N clients)` — for example, `:50001 (2 clients)`. The count updates automatically each time a client connects or disconnects. When no clients are connected the count reads `0 clients`.

## What each control does

| Control | Description | Default | Valid range | Setting key |
|---|---|---|---|---|
| Port | TCP port the TCI WebSocket server listens on. Changing it while the server is running restarts the server. Out-of-range values snap to `50001`. | `50001` | 1024–65535 | `TciPort` |
| Enable | Starts or stops the TCI server. If the port cannot be bound, the button snaps back to off and the status shows `(port in use)`. | Off | — | — |
| Server status | Displays `(stopped)`, `:<port> (N clients)`, or `(port in use)`. Turns red on a bind failure. Turns blue when one or more clients are connected. | `(stopped)` | — | — |
| RX1–RX4 gain+meter | Combined meter and slider setting the TCI RX gain for each channel. | 0.5 | 0.0–1.0 | `TciRxGain1`, `TciRxGain2`, `TciRxGain3`, `TciRxGain4` |
| TX gain+meter | Combined meter and slider setting the TCI TX gain. | 0.5 | 0.0–1.0 | `TciTxGain` |
| RX/TX slice-assignment labels | Show which slice drives each RX or TX row. Displays `—` when no slice is assigned. | `—` | `—` or `Slice <letter>` | — |

## Troubleshooting

- **Status shows `(stopped)` even though Enable appears active** — The port bind failed silently. Click **Enable** to toggle it off, verify the port is not in use by another application, then click **Enable** again.
- **Status shows `(port in use)`** — Another process is already listening on the configured port. Enter a different port number in the **Port** field and click **Enable**.
- **Client count stays at 0 after connecting external software** — Confirm the external software is pointed at the same port shown in the **Port** field and that no firewall is blocking the connection.

## Related

- [TCI Server overview](../../features/tci/overview.md)
- [Enable the TCI server for Log4OM / SunSDR clients](../../features/tci/enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Change the TCI port](../../features/tci/change-the-tci-port.md)
- [Autostart TCI on launch](../../features/tci/autostart-tci-on-launch.md)
