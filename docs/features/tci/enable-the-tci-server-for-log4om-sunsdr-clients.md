# Enable the TCI server for Log4OM / SunSDR clients

The TCI applet runs a WebSocket server that exposes radio control and audio to third-party software such as Log4OM and SunSDR tools. Enable it to let those clients connect to AetherSDR over the TCI protocol.

## Before you start

- AetherSDR must be connected to the radio. The TCI server requires an active radio connection.
- Decide which port the server will listen on. The default is `50001`. If another application already occupies that port, choose a different one in the range 1024–65535.

## Steps

1. Click the **TCI** tray button on the right sidebar. The TCI Server applet panel opens.
2. Confirm the **Port** field shows the port you want. The default is `50001`. To change it, click the field, type a new value (1024–65535), and press Enter. Values outside that range snap back to `50001`.
3. Click **Enable**. The button turns green when the server is running.
4. Check the status indicator to the left of **Enable**. It shows `:<port> (0 clients)` when the server is up and waiting, and updates the client count as software connects.

## What each control does

| Control | Default | Range / States | Persisted key |
|---|---|---|---|
| **Port** text field | `50001` | 1024–65535; invalid values snap to `50001` | `TciPort` |
| **Enable** toggle | Off | Off / On (green) | — |
| **RX1**–**RX4** gain meter/slider | `0.5` | 0.0–1.0 | `TciRxGain1`–`TciRxGain4` |
| **TX** gain meter/slider | `0.5` | 0.0–1.0 | `TciTxGain` |
| RX/TX slice-assignment labels | `—` | `—` or `Slice <letter>` | — |
| Server status indicator | `(stopped)` | `(stopped)`, `:<port> (N clients)`, `(port in use)` | — |

The RX1–RX4 rows show which slice drives each TCI channel. The label reads `Slice A`, `Slice B`, and so on, based on the DAX channel assignment of each slice. The TX row shows the currently active TX slice.

## Tips

- To start the TCI server automatically every time AetherSDR launches, go to `Settings > Autostart TCI with AetherSDR` and enable that item. See [Autostart TCI on launch](autostart-tci-on-launch.md).
- The client count in the status indicator updates in real time as software connects or disconnects.

## Troubleshooting

- **Enable snaps back to off and status shows `(port in use)`** — Another application is already bound to that port. Enter a different port number in the **Port** field and click **Enable** again.
- **Status stays `(stopped)` after clicking Enable** — Verify that AetherSDR is connected to the radio. The TCI server requires an active radio connection.

## Related

- [TCI Server overview](overview.md)
- [Change the TCI port](change-the-tci-port.md)
- [Adjust TCI RX gain per channel](adjust-tci-rx-gain-per-channel.md)
- [Adjust TCI TX gain](adjust-tci-tx-gain.md)
- [Autostart TCI on launch](autostart-tci-on-launch.md)
- [See how many TCI clients are connected](../../getting-started/setup/see-how-many-tci-clients-are-connected.md)
