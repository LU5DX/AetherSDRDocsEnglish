# TCI Server Overview

The TCI Server applet runs a WebSocket server that speaks the Expert TCI protocol, letting third-party software such as Log4OM and SunSDR tools read and control the radio. Use this page to understand what each control does; follow the linked task pages to perform specific operations.

## Before you start

- AetherSDR must be connected to the radio. The TCI applet requires an active radio connection.
- The TCI applet is hidden by default. Click the TCI tray button on the right sidebar to show it.

## How it works

AetherSDR's TCI Server listens on a configurable TCP port for WebSocket connections from TCI-compatible clients. When enabled, it exposes up to four RX channels and one TX channel, each mapped to a radio slice via the DAX channel assignments. Clients connect, receive radio state, and can issue control commands over the TCI protocol.

Each RX channel (RX1–RX4) carries audio from the slice assigned to the matching DAX channel. The TX channel carries audio from whichever slice is currently the TX slice. The slice-assignment indicators in the applet update automatically as slices are added or reassigned.

The server status indicator shows the current state at a glance. When the server is stopped it reads `(stopped)`. When running it reads `:<port> (N clients)` — for example `:50001 (2 clients)`. If the port cannot be bound, the status turns red and reads `(port in use)`.

Enabling autostart via `Settings > Autostart TCI with AetherSDR` causes the server to start automatically each time AetherSDR launches, using the saved `TciPort` value.

## What each control does

| Control | Description | Default | Valid range | Setting key |
|---|---|---|---|---|
| RX1–RX4 gain+meter | Combined meter and slider. The meter reflects incoming RX audio level. Drag to set the TCI RX gain for that channel. | 0.5 | 0.0–1.0 | `TciRxGain1`, `TciRxGain2`, `TciRxGain3`, `TciRxGain4` |
| TX gain+meter | Combined meter and slider. The meter reflects outgoing TX audio level. Drag to set the TCI TX gain. | 0.5 | 0.0–1.0 | `TciTxGain` |
| RX/TX slice-assignment labels | Read-only indicators showing which slice drives each channel. Displays `—` when no slice is assigned, or `Slice <letter>` when a slice is mapped. | `—` | `—` or `Slice <letter>` | — |
| Port | Sets the TCP port the server listens on. If the server is running when you change this value, it restarts automatically on the new port. Out-of-range values snap to `50001`. | `50001` | 1024–65535 | `TciPort` |
| Enable | Starts or stops the TCI server. If the port cannot be bound, the button snaps back to off and the status shows `(port in use)`. | Off | — | — |
| Server status | Read-only indicator showing `(stopped)`, `:<port> (N clients)`, or `(port in use)`. Turns red on a bind failure. | `(stopped)` | — | — |

## Troubleshooting

- **Status shows `(port in use)` and Enable snaps off** — Another application is already bound to that port. Change the port in the Port field to a different value in the range 1024–65535 and click Enable again.
- **Slice-assignment labels show `—` for all channels** — No slice has been assigned to a DAX channel. Assign DAX channels to your slices; the TCI RX assignments follow the same mapping.

## Related

- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Change the TCI port](change-the-tci-port.md)
- [Adjust TCI RX gain per channel](adjust-tci-rx-gain-per-channel.md)
- [Adjust TCI TX gain](adjust-tci-tx-gain.md)
- [Autostart TCI on launch](autostart-tci-on-launch.md)
- [See how many TCI clients are connected](../../getting-started/setup/see-how-many-tci-clients-are-connected.md)
