# Enable the TCI server for Log4OM / SunSDR clients

AetherSDR includes a built-in TCI WebSocket server that lets third-party software — such as Log4OM and SunSDR tools — read and control the radio over the TCI protocol. This page walks through opening the TCI applet and starting the server.

## Before you start

- AetherSDR must be connected to the radio. The TCI applet requires an active radio connection.
- The applet panel must be visible. If it is not, click `View > Applet Panel` to show it.

## Steps

1. Click the **TCI** tray button on the right sidebar. The TCI Server applet appears in the applet panel.
2. Check the **Port** field. The default is `50001`. Change it if another application is already using that port (valid range: 1024–65535; out-of-range values snap back to `50001`).
3. Click **Enable**. The button highlights green when the server is running.
4. Confirm the server status indicator next to **Enable** changes from `(stopped)` to `:<port> (0 clients)`. When a client connects, the count increments — for example, `50001 (1 client)`.

## What each control does

| Control | Description | Default | Range | Setting key |
|---|---|---|---|---|
| **Port** | TCP port the TCI WebSocket server listens on. Changing the value while the server is running restarts it automatically. | `50001` | 1024–65535 | `TciPort` |
| **Enable** | Starts or stops the TCI server. | Off | — | — |
| **RX1–RX4** gain+meter | Combined meter and slider. Drag to set the TCI RX gain for each channel. | 0.5 | 0.0–1.0 | `TciRxGain1`, `TciRxGain2`, `TciRxGain3`, `TciRxGain4` |
| **TX** gain+meter | Combined meter and slider. Drag to set the TCI TX gain. | 0.5 | 0.0–1.0 | `TciTxGain` |
| RX/TX slice-assignment labels | Read-only indicators showing which slice drives each RX or TX row (for example, `Slice A`). Shows `—` when no slice is assigned. | `—` | — | — |
| Server status | Shows the current server state and connected client count. Turns red and displays `(port in use)` on bind failure. | `(stopped)` | — | — |

## Tips

- To have the TCI server start automatically every time AetherSDR launches, enable `Settings > Autostart TCI with AetherSDR` instead of clicking **Enable** each session.
- The slice-assignment labels next to each RX row follow the same DAX channel mapping. If a row shows `—`, assign a DAX channel to the corresponding slice.

## Troubleshooting

- **Enable button snaps back off and status shows `(port in use)`** — Another application is already bound to the configured port. Enter a different value in **Port** and click **Enable** again.
- **TCI applet does not appear in the applet panel** — Your build of AetherSDR may not include WebSocket support. The TCI applet is present only in builds compiled with WebSocket support enabled.

## Related

- [TCI Server overview](overview.md)
- [Change the TCI port](change-the-tci-port.md)
- [Autostart TCI on launch](autostart-tci-on-launch.md)
- [Adjust TCI RX gain per channel](adjust-tci-rx-gain-per-channel.md)
- [Adjust TCI TX gain](adjust-tci-tx-gain.md)
- [See how many TCI clients are connected](../../getting-started/setup/see-how-many-tci-clients-are-connected.md)
