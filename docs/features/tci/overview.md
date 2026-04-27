# TCI Server Overview

The TCI Server applet runs a WebSocket server that speaks the Expert Electronics TCI protocol, letting third-party logging, digital-mode, and SDR applications — such as Log4OM and SunSDR tools — read and control the radio over a local network connection. Open the applet to start the server, set the port, and adjust audio gain for each RX and TX channel.

## Before you start

- AetherSDR must be connected to the radio. The TCI applet requires an active radio connection.
- This feature is only present in builds compiled with WebSocket support (`HAVE_WEBSOCKETS`). If the TCI tray button is absent, your build does not include TCI.

## How it works

The TCI applet is hidden by default. Toggle it open with the **TCI** tray button on the right sidebar.

When you click **Enable**, AetherSDR binds a WebSocket server on the configured port (default `50001`). Any TCI-compatible client that connects to `ws://<your-host>:<port>` can then query and command the radio using the TCI protocol. The applet displays the current server state and connected client count in the status area next to the **Enable** button.

RX audio for channels 1–4 follows the same DAX channel assignments as the DAX applet. The slice letter shown beside each RX and TX row — for example, `Slice A` — reflects whichever slice is currently assigned to that DAX channel. If no slice is assigned, the indicator shows `—`.

Gain levels set in the applet apply to the TCI audio stream and are independent of the radio's RF gain controls.

## What each control does

| Control | What it does | Default | Valid range | Persisted key |
|---|---|---|---|---|
| RX1–RX4 gain+meter | Combined level meter and gain slider for each TCI RX channel. Drag to set the output gain for that channel's audio stream. | 0.5 | 0.0–1.0 | `TciRxGain1`, `TciRxGain2`, `TciRxGain3`, `TciRxGain4` |
| TX gain+meter | Combined level meter and gain slider for the TCI TX channel. Drag to set the TX audio gain. | 0.5 | 0.0–1.0 | `TciTxGain` |
| RX/TX slice-assignment labels | Read-only indicators showing which slice drives each row (`Slice A`, `Slice B`, etc., or `—` if unassigned). | `—` | `—` or `Slice <letter>` | — |
| Port | WebSocket port the server listens on. Changing the value while the server is running restarts it on the new port. Values outside the valid range snap back to `50001`. | `50001` | 1024–65535 | `TciPort` |
| Enable | Starts or stops the TCI server. If the port is already in use, the button snaps back to off and the status shows `(port in use)` in red. | Off | — | — |
| Server status | Displays `(stopped)`, `:<port> (<N> clients)`, or `(port in use)`. Turns red on a bind failure. | `(stopped)` | — | — |

## Tips

- To start the TCI server automatically every time AetherSDR launches, enable `Settings > Autostart TCI with AetherSDR`. This sets the `AutoStartTCI` preference.
- The client count shown in the server status updates live as clients connect and disconnect. See [See how many TCI clients are connected](../../getting-started/setup/see-how-many-tci-clients-are-connected.md) for details.

## Troubleshooting

- **Status shows `(port in use)` and Enable snaps off** — Another process is already bound to that port. Change the port in the Port field to a free port in the range 1024–65535 and click Enable again. See [Change the TCI port](change-the-tci-port.md).
- **TCI tray button is missing** — This build of AetherSDR was compiled without WebSocket support. TCI is unavailable.
- **Slice labels show `—` for all channels** — No slices have a DAX channel assigned. Assign a DAX channel to a slice through the radio setup to populate the RX and TX labels.

## Related

- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Change the TCI port](change-the-tci-port.md)
- [Adjust TCI RX gain per channel](adjust-tci-rx-gain-per-channel.md)
- [Adjust TCI TX gain](adjust-tci-tx-gain.md)
- [Autostart TCI on launch](autostart-tci-on-launch.md)
- [See how many TCI clients are connected](../../getting-started/setup/see-how-many-tci-clients-are-connected.md)
