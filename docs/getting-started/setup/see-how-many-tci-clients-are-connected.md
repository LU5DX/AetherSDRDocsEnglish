# See how many TCI clients are connected

The TCI Server applet shows a live client count in its status indicator. Use this to confirm that Log4OM, SunSDR tools, or any other TCI client has successfully connected.

## Before you start

- AetherSDR must be connected to a radio. The TCI applet requires an active radio connection.
- The TCI server must be running (Enable toggled on). If it is stopped, the status shows `(stopped)` and no client count is available.

## Steps

1. Click the **TCI** tray button on the right sidebar to open the TCI Server applet.
2. Read the status indicator next to the Port field.

When the server is running and at least one client is connected, the status reads:

```
:<port> (N clients)
```

For example, with two clients connected on the default port:

```
:50001 (2 clients)
```

When the server is running but no clients are connected, the status reads the port and `(0 clients)`. When the server is stopped, the status reads `(stopped)`.

## What each control does

| Control | Description | Default | Valid range | Setting key |
|---|---|---|---|---|
| Port | Port the TCI WebSocket server listens on. Out-of-range values snap to `50001`. | `50001` | 1024–65535 | `TciPort` |
| Enable | Starts or stops the TCI server. | Off | On / Off | — |
| Server status | Displays `(stopped)`, `:<port> (N clients)`, or `(port in use)`. Turns red on bind failure. | `(stopped)` | — | — |
| RX1–RX4 gain+meter | Gain slider and level meter for each TCI RX channel. | 0.5 | 0.0–1.0 | `TciRxGain1`–`TciRxGain4` |
| TX gain+meter | Gain slider and level meter for the TCI TX channel. | 0.5 | 0.0–1.0 | `TciTxGain` |

## Tips

- The client count updates automatically whenever a client connects or disconnects — no need to refresh.
- When one client is connected the status reads `(1 client)` (singular); two or more reads `(N clients)` (plural).
- The status text turns blue when one or more clients are connected, making it easy to spot at a glance.

## Troubleshooting

- **Status shows `(port in use)`** — Another process is already bound to the configured port. Change the value in the Port field to an unused port in the range 1024–65535 and press Enter. The server restarts automatically if Enable is on.
- **Status stays `(stopped)` after clicking Enable** — The bind failed and Enable snapped back to off. Check the Port value and confirm no other application is using that port.
- **Client count stays at 0** — Confirm the third-party application is configured to connect to the correct host and port. The port in use is shown in the status indicator.

## Related

- [Enable the TCI server for Log4OM / SunSDR clients](../../features/tci/enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Change the TCI port](../../features/tci/change-the-tci-port.md)
- [Autostart TCI on launch](../../features/tci/autostart-tci-on-launch.md)
- [TCI Server overview](../../features/tci/overview.md)
