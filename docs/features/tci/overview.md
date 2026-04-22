# TCI Server overview

The TCI Server applet runs a WebSocket server that speaks the Expert Electronics TCI protocol, letting third-party software — such as Log4OM, SunSDR tools, and other TCI-aware logging or digital-mode applications — read and control the radio without a direct SmartSDR connection. Open this applet to start the server, set the port, and adjust per-channel audio gain levels.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The TCI applet is not available without an active radio connection.
- The TCI Server feature requires a build of AetherSDR that includes WebSocket support (`HAVE_WEBSOCKETS`). If the TCI tray button is absent, your build does not include this feature.

## How it works

The TCI applet is hidden by default. Toggle it open with the **TCI** tray button on the right sidebar. Once open, click **Enable** to bind the server to the configured port. Connected clients are counted and displayed in the server status indicator.

RX audio for each TCI channel follows the same DAX channel assignments already configured on your slices. The slice driving each channel is shown in the RX/TX slice-assignment labels next to each meter. When no slice is assigned to a channel, the label shows —.

The TX channel carries audio from whichever slice is currently the transmit slice.

## What each control does

| Control | What it does | Default | Range | Setting key |
|---|---|---|---|---|
| RX1–RX4 gain+meter | Sets the TCI RX audio gain for channels 1–4. Drag to adjust; the meter shows live signal level. | 0.5 | 0.0–1.0 | `TciRxGain1`, `TciRxGain2`, `TciRxGain3`, `TciRxGain4` |
| TX gain+meter | Sets the TCI TX audio gain. Drag to adjust; the meter shows live signal level. | 0.5 | 0.0–1.0 | `TciTxGain` |
| Port | The TCP port the TCI WebSocket server listens on. Changing the port restarts the server if it is already running. Values outside 1024–65535 snap back to 50001. | 50001 | 1024–65535 | `TciPort` |
| Enable | Starts or stops the TCI server. If the port cannot be bound, the button snaps back to off and the status indicator shows `(port in use)` in red. | Off | — | — |
| RX/TX slice-assignment labels | Read-only indicators showing which slice drives each RX or TX row. Displays `Slice <letter>` when a slice is assigned, or — when none is. | — | — or Slice A–H | — |
| Server status | Shows the current server state: `(stopped)`, `:<port> (<N> clients)`, or `(port in use)`. Turns red on bind failure. | (stopped) | — | — |

## Tips

- To start the TCI server automatically every time AetherSDR launches, use `Settings > Autostart TCI with AetherSDR`.
- If the status shows `(port in use)`, another application is already bound to that port. Change the port number and click **Enable** again.
- The RX level meters use exponential smoothing: level rises quickly on a signal and decays slowly, so brief peaks remain visible.

## Troubleshooting

- **Enable snaps back to off immediately** — The server could not bind to the specified port. Check that no other application is using that port, then enter a different value in Port and click **Enable**.
- **Slice-assignment labels show — for all channels** — No slices have DAX channels assigned. Configure DAX channel assignments on your slices; TCI RX channels follow the same mapping.
- **TCI tray button is not visible** — Your AetherSDR build does not include WebSocket support. The TCI Server feature is unavailable in this build.

## Related

- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Change the TCI port](change-the-tci-port.md)
- [Adjust TCI RX gain per channel](adjust-tci-rx-gain-per-channel.md)
- [Adjust TCI TX gain](adjust-tci-tx-gain.md)
- [Autostart TCI on launch](autostart-tci-on-launch.md)
- [See how many TCI clients are connected](../../getting-started/setup/see-how-many-tci-clients-are-connected.md)
