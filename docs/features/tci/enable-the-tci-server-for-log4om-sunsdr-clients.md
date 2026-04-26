# Enable the TCI server for Log4OM / SunSDR clients

The TCI Server applet runs a WebSocket server that lets third-party software — such as Log4OM and SunSDR tools — read and control the radio over the Expert TCI protocol. This page explains how to start the server for the first time.

## Before you start

- AetherSDR must be connected to the radio. The TCI applet requires an active radio connection.
- The applet panel must be visible. If it is not, click `View > Applet Panel` to show it.

## Steps

1. Click the **TCI** tray button on the right sidebar to open the TCI Server applet.
2. Confirm the **Port** field shows the port your client expects. The default is `50001`. Valid values are 1024–65535; values outside that range snap back to `50001`.
3. Click **Enable**.
4. Check the server status indicator next to the **Enable** button. When the server starts successfully it reads `:<port> (0 clients)`. When a client connects, the count increments.

## What each control does

| Control | Description | Default | Range | Setting key |
|---|---|---|---|---|
| **Port** | TCP port the TCI WebSocket server listens on. Changing the port while the server is running restarts it automatically. | `50001` | 1024–65535 | `TciPort` |
| **Enable** | Starts or stops the TCI server. | Off | On / Off | — |
| **RX1–RX4 gain+meter** | Combined level meter and gain slider for each TCI receive channel. Drag to set the output gain for that channel. | 0.5 | 0.0–1.0 | `TciRxGain1`, `TciRxGain2`, `TciRxGain3`, `TciRxGain4` |
| **TX gain+meter** | Combined level meter and gain slider for the TCI transmit channel. | 0.5 | 0.0–1.0 | `TciTxGain` |
| RX/TX slice-assignment labels | Read-only indicators showing which slice drives each RX or TX row (for example, `Slice A`). Shows `—` when no slice is assigned. | `—` | `—` or `Slice <letter>` | — |
| Server status | Shows `(stopped)`, `:<port> (N clients)`, or `(port in use)`. Turns red on bind failure. | `(stopped)` | — | — |

## Tips

- The RX1–RX4 channels share the same DAX channel assignments. The slice letter shown next to each row reflects the slice currently mapped to that DAX channel.
- To have the server start automatically every time AetherSDR launches, use `Settings > Autostart TCI with AetherSDR` instead of clicking **Enable** each session.

## Troubleshooting

- **Status shows `(port in use)` and Enable snaps back off** — Another application is already bound to that port. Enter a different port number in the **Port** field, then click **Enable** again.

## Related

- [TCI Server overview](overview.md)
- [Change the TCI port](change-the-tci-port.md)
- [Autostart TCI on launch](autostart-tci-on-launch.md)
- [Adjust TCI RX gain per channel](adjust-tci-rx-gain-per-channel.md)
- [Adjust TCI TX gain](adjust-tci-tx-gain.md)
- [See how many TCI clients are connected](../../getting-started/setup/see-how-many-tci-clients-are-connected.md)
