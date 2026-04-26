# TCI Server overview

The TCI Server applet runs a WebSocket server that speaks the Expert Electronics TCI protocol, letting third-party software — such as Log4OM, SunSDR tools, and other TCI-aware applications — read and control the radio. Open this applet to start the server, set its port, and adjust audio gain for each RX and TX channel.

## Before you start

- AetherSDR must be connected to the radio. The TCI applet requires an active radio connection.
- The TCI Server feature is only present in builds that include WebSocket support. If the TCI tray button is absent, your build does not include it.

## How it works

The TCI Server applet is hidden by default. Click the **TCI** tray button on the right sidebar to show it.

When you click **Enable**, AetherSDR binds a WebSocket server to the configured port (default `50001`). Any TCI-compatible client on the network can then connect to that port. The server status indicator shows the current state: `(stopped)` when the server is off, `:<port> (<N> clients)` when running, or `(port in use)` in red if the bind failed.

Each of the four RX channels maps to a DAX channel assignment. The slice-assignment indicator next to each row shows which slice is feeding that channel (for example, `Slice A`), or `—` if no slice is assigned. The TX row works the same way, showing the active TX slice.

Audio levels for all channels are displayed live on the combined meter/slider controls. Dragging the slider portion sets the gain for that channel, which is stored immediately.

Autostart is configured separately via `Settings > Autostart TCI with AetherSDR`. When enabled, AetherSDR starts the TCI server each time it launches without requiring you to click **Enable** manually.

## What each control does

| Control | Description | Default | Range | Setting key |
|---|---|---|---|---|
| RX1–RX4 gain+meter | Sets TCI RX audio gain for each channel. The meter shows live signal level; drag to adjust gain. | 0.5 | 0.0–1.0 | `TciRxGain1`, `TciRxGain2`, `TciRxGain3`, `TciRxGain4` |
| TX gain+meter | Sets TCI TX audio gain. The meter shows live TX level; drag to adjust gain. | 0.5 | 0.0–1.0 | `TciTxGain` |
| Port | The WebSocket port the server binds to. Changing the value while the server is running restarts it automatically. Values outside 1024–65535 snap to `50001`. | `50001` | 1024–65535 | `TciPort` |
| Enable | Starts or stops the TCI server. If the bind fails, the toggle snaps back to off and the status shows `(port in use)` in red. | Off | On / Off | — |
| RX/TX slice-assignment labels | Read-only indicators showing which slice drives each RX or TX row. Displays `Slice <letter>` or `—`. | `—` | — | — |
| Server status | Shows `(stopped)`, `:<port> (<N> clients)`, or `(port in use)`. Turns red on bind failure. | `(stopped)` | — | — |

## Tips

- If you want the server to start every time AetherSDR launches, use `Settings > Autostart TCI with AetherSDR` instead of clicking **Enable** each session. See [Autostart TCI on launch](autostart-tci-on-launch.md).
- RX channel gain and slice assignment follow the DAX channel mapping. If a channel shows `—`, assign a DAX channel to the corresponding slice first.

## Troubleshooting

- **Status shows `(port in use)` and Enable snaps back to off** — Another application is already bound to that port. Change the port in the Port field to an unused value between 1024 and 65535 and click **Enable** again. See [Change the TCI port](change-the-tci-port.md).
- **TCI tray button is not visible** — This build of AetherSDR was compiled without WebSocket support. The TCI Server feature is not available.

## Related

- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Change the TCI port](change-the-tci-port.md)
- [Adjust TCI RX gain per channel](adjust-tci-rx-gain-per-channel.md)
- [Adjust TCI TX gain](adjust-tci-tx-gain.md)
- [Autostart TCI on launch](autostart-tci-on-launch.md)
- [See how many TCI clients are connected](../../getting-started/setup/see-how-many-tci-clients-are-connected.md)
