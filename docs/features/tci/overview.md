# TCI Server overview

The TCI Server applet runs a WebSocket server that speaks the Expert TCI protocol, letting third-party applications such as Log4OM and SunSDR tools read and control the radio. Use this page to understand what the applet provides; follow the linked pages for specific tasks.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The TCI applet requires an active radio connection.
- The TCI applet is only available in builds that include WebSocket support (`HAVE_WEBSOCKETS`). If the TCI tray button is absent, your build does not include this feature.

## How it works

The TCI Server applet listens on a configurable TCP port and accepts WebSocket connections from TCI-compatible clients. When a client connects, it can read receiver audio, control the radio's slices, and send and receive audio on the TX channel.

RX channels 1–4 map to the same DAX channel assignments used by the DAX audio bridge — the slice letter shown next to each RX row reflects whichever slice has that DAX channel assigned. The TX row shows the currently active TX slice. Gain sliders for each channel let you scale the audio level independently before it reaches the connected client.

The server status indicator in the applet shows the current state:

| Status text | Meaning |
|---|---|
| `(stopped)` | Server is not running. |
| `:<port> (N clients)` | Server is running on the given port with N connected clients. |
| `(port in use)` | Bind failed; another process holds the port. |

The status turns red on a bind failure. When the port is already in use, Enable snaps back to off automatically.

## What each control does

| Control | Description | Default | Valid range | Setting key |
|---|---|---|---|---|
| RX1–RX4 gain+meter | Combined meter and slider. Drag to set the TCI RX gain for each channel. The meter reflects live receive level with exponential smoothing. | 0.5 | 0.0–1.0 | `TciRxGain1`, `TciRxGain2`, `TciRxGain3`, `TciRxGain4` |
| TX gain+meter | Combined meter and slider. Drag to set the TCI TX gain. The meter reflects live transmit level. | 0.5 | 0.0–1.0 | `TciTxGain` |
| RX/TX slice-assignment labels | Indicators next to each row showing which slice drives that channel (e.g. `Slice A`). Shows `—` when no slice is assigned. | `—` | `—` or `Slice <letter>` | — |
| Port | TCP port the server binds to. Changing this field while the server is running restarts it on the new port. Out-of-range values snap to `50001`. | `50001` | 1024–65535 | `TciPort` |
| Enable | Toggle button. Starts the server when checked; stops it when unchecked. Snaps back to off if the port bind fails. | Off | — | — |
| Server status | Read-only label showing server state and connected client count. Turns red on bind failure. | `(stopped)` | — | — |

## Tips

- To open the TCI applet, click the TCI tray button on the right sidebar. The applet is hidden by default.
- To start the TCI server automatically every time AetherSDR launches, enable `Settings > Autostart TCI with AetherSDR`. This is independent of the Enable toggle in the applet.
- The slice-assignment labels follow DAX channel mapping. If a slice is not assigned a DAX channel, its row shows `—`.

## Related

- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Change the TCI port](change-the-tci-port.md)
- [Adjust TCI RX gain per channel](adjust-tci-rx-gain-per-channel.md)
- [Adjust TCI TX gain](adjust-tci-tx-gain.md)
- [Autostart TCI on launch](autostart-tci-on-launch.md)
- [See how many TCI clients are connected](../../getting-started/setup/see-how-many-tci-clients-are-connected.md)
