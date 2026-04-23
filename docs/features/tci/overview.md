# TCI Server overview

The TCI Server applet runs a WebSocket server inside AetherSDR that speaks the Expert Electronics TCI protocol. Third-party logging, digital-mode, and SDR applications — such as Log4OM and SunSDR tools — can connect to this server to read and control the radio without any additional bridge software.

## Before you start

- AetherSDR must be connected to the radio. The TCI applet requires an active radio connection.
- The TCI applet is hidden by default. Click the TCI tray button on the right sidebar to show it.

## How it works

When you click Enable, AetherSDR binds a WebSocket server to the configured port (default `50001`). Any TCI-compatible client on the same network can then connect to `<host>:<port>`. The server handles up to four simultaneous RX audio streams, one TX audio stream, and bidirectional frequency and mode control.

Each RX channel maps to a DAX channel assignment. The slice-assignment indicators next to each RX and TX row show which slice currently drives that channel — for example, `Slice A`. If no slice is assigned, the indicator shows `—`.

The server status indicator updates in real time as clients connect and disconnect. When the server is running, it shows `:<port> (N clients)`. When stopped, it shows `(stopped)`. If the port is already in use when you click Enable, the status shows `(port in use)` in red and Enable snaps back off.

You can configure the server to start automatically every time AetherSDR launches via `Settings > Autostart TCI with AetherSDR`.

## What each control does

| Control | Description | Default | Valid range | Setting key |
|---|---|---|---|---|
| RX1–RX4 gain+meter | Combined level meter and gain slider for each TCI RX channel. Drag to set gain. | 0.5 | 0.0–1.0 | `TciRxGain1`, `TciRxGain2`, `TciRxGain3`, `TciRxGain4` |
| TX gain+meter | Combined level meter and gain slider for the TCI TX channel. Drag to set gain. | 0.5 | 0.0–1.0 | `TciTxGain` |
| Port | WebSocket port the server listens on. Changing this while the server is running restarts the server immediately. Values outside 1024–65535 snap to `50001`. | `50001` | 1024–65535 | `TciPort` |
| Enable | Starts or stops the TCI server. If the port cannot be bound, the button snaps back to off. | Off | On / Off | — |
| RX/TX slice-assignment labels | Read-only indicators showing which slice is assigned to each RX or TX row. Displays `Slice <letter>` or `—`. | `—` | `—` or `Slice <letter>` | — |
| Server status | Shows current server state and connected client count. Turns red on bind failure. | `(stopped)` | `(stopped)`, `:<port> (N clients)`, `(port in use)` | — |

## Related

- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Change the TCI port](change-the-tci-port.md)
- [Adjust TCI RX gain per channel](adjust-tci-rx-gain-per-channel.md)
- [Adjust TCI TX gain](adjust-tci-tx-gain.md)
- [Autostart TCI on launch](autostart-tci-on-launch.md)
- [See how many TCI clients are connected](../../getting-started/setup/see-how-many-tci-clients-are-connected.md)
