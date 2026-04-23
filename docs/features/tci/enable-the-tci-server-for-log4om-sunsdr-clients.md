# Enable the TCI server for Log4OM / SunSDR clients

The TCI Server applet runs a WebSocket server that lets third-party software such as Log4OM and SunSDR tools read and control the radio over the TCI protocol. Use this page to open the applet and start the server.

## Before you start

- AetherSDR must be connected to the radio. The TCI applet requires an active radio connection.
- The Applet Panel must be visible. If it is hidden, go to `View > Applet Panel` to show it.

## Steps

1. Click the **TCI** tray button on the right sidebar. The TCI Server applet appears in the Applet Panel.
2. Check the **Port** field. The default is `50001`. Change it if another application already uses that port (valid range: 1024–65535; out-of-range values reset to `50001`).
3. Click **Enable**. The button highlights and the server status changes from `(stopped)` to `:<port> (0 clients)`.
4. Point your TCI client (Log4OM, SunSDR tool, etc.) at the AetherSDR host address and the port shown in the status area.

When a client connects, the status updates to `:<port> (1 client)` or shows the client count.

## What each control does

| Control | What it does | Default | Range | Setting key |
|---|---|---|---|---|
| **Port** | Sets the TCP port the TCI WebSocket server listens on. Changing the port while the server is running restarts it automatically. | `50001` | 1024–65535 | `TciPort` |
| **Enable** | Starts or stops the TCI server. | Off | — | — |
| **RX1–RX4** gain+meter | Combined meter and slider. Drag to set the TCI RX gain for that channel. The label beside each row shows which slice is assigned (e.g. `Slice A`), or `—` if unassigned. | 0.5 | 0.0–1.0 | `TciRxGain1` – `TciRxGain4` |
| **TX** gain+meter | Combined meter and slider. Drag to set the TCI TX gain. The label shows the current TX slice or `—`. | 0.5 | 0.0–1.0 | `TciTxGain` |
| Server status | Read-only indicator showing server state and connected client count. Turns red and shows `(port in use)` on a bind failure. | `(stopped)` | — | — |

## Tips

- To start the TCI server automatically every time AetherSDR launches, enable `Settings > Autostart TCI with AetherSDR`.
- The RX slice assignments shown next to each RX row follow the DAX channel mapping. Assign a DAX channel to a slice to populate those labels.

## Troubleshooting

- **Enable snaps back off and status shows `(port in use)`** — Another application is already bound to that port. Enter a different port number in the **Port** field and click **Enable** again.
- **Status stays `(stopped)` after clicking Enable** — Confirm the radio is connected. The TCI applet requires an active radio connection and will not start without one.
- **TCI applet or TCI tray button is not visible** — Your build may not include WebSocket support. The TCI feature requires a WebSocket-enabled build of AetherSDR.

## Related

- [TCI Server overview](overview.md)
- [Change the TCI port](change-the-tci-port.md)
- [Adjust TCI RX gain per channel](adjust-tci-rx-gain-per-channel.md)
- [Adjust TCI TX gain](adjust-tci-tx-gain.md)
- [Autostart TCI on launch](autostart-tci-on-launch.md)
- [See how many TCI clients are connected](../../getting-started/setup/see-how-many-tci-clients-are-connected.md)
