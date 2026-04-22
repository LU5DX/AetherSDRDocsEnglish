# Enable the TCI server for Log4OM / SunSDR clients

Start the built-in TCI WebSocket server so third-party logging and SDR software such as Log4OM or SunSDR tools can read and control the radio over the TCI protocol.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The TCI applet requires an active radio connection.
- The TCI applet must be visible. If you do not see it in the applet panel, click the TCI tray button on the right sidebar to show it.

## Steps

1. Click the TCI tray button on the right sidebar to open the TCI Server applet.
2. Check the Port field. The default is `50001`. Change it now if that port is already in use on your system — see [Change the TCI port](change-the-tci-port.md).
3. Click Enable.
4. Confirm the server started: the status indicator next to Enable changes from `(stopped)` to `:<port> (0 clients)`.
5. In your third-party software (Log4OM, SunSDR tool, etc.), enter `localhost` and the port number shown in the status indicator. Once the client connects, the status updates to `:<port> (1 clients)` or higher.

## What each control does

| Control | What it does | Default | Range | Setting key |
|---|---|---|---|---|
| Port | Sets the TCP port the TCI WebSocket server listens on. Changing the value while Enable is active restarts the server automatically. Out-of-range values snap to `50001`. | `50001` | 1024–65535 | `TciPort` |
| Enable | Starts or stops the TCI server. | Off | — | — |
| Server status | Shows current server state and connected client count. Turns red and shows `(port in use)` if the bind fails. | `(stopped)` | `(stopped)`, `:<port> (N clients)`, `(port in use)` | — |
| RX1–RX4 gain+meter | Combined level meter and gain slider for each TCI RX channel. Drag to set gain. The slice letter assigned to each channel is shown to the left of the meter. | 0.5 | 0.0–1.0 | `TciRxGain1`, `TciRxGain2`, `TciRxGain3`, `TciRxGain4` |
| TX gain+meter | Combined level meter and gain slider for the TCI TX channel. The active TX slice letter is shown to the left of the meter. | 0.5 | 0.0–1.0 | `TciTxGain` |
| RX/TX slice-assignment labels | Indicators showing which slice drives each RX or TX row. Displays `—` when no slice is assigned to that channel. | `—` | `—` or `Slice <letter>` | — |

## Tips

- To have the TCI server start automatically every time AetherSDR launches, enable `Settings > Autostart TCI with AetherSDR`. See [Autostart TCI on launch](autostart-tci-on-launch.md).
- The RX channel assignments follow DAX channel mapping. If a channel shows `—`, assign a DAX channel to the corresponding slice in radio setup.

## Troubleshooting

- **Enable snaps back to off and status shows `(port in use)`** — Another application is already bound to that port. Change the Port value to a free port (1024–65535) and click Enable again.
- **Status stays `(stopped)` after clicking Enable** — Confirm the radio is connected. The TCI server requires an active radio connection to start.
- **Third-party software cannot connect** — Verify the port number in the client matches the Port field in AetherSDR. Check that your firewall permits connections on that port.

## Related

- [TCI Server overview](overview.md)
- [Change the TCI port](change-the-tci-port.md)
- [Autostart TCI on launch](autostart-tci-on-launch.md)
- [Adjust TCI RX gain per channel](adjust-tci-rx-gain-per-channel.md)
- [Adjust TCI TX gain](adjust-tci-tx-gain.md)
- [See how many TCI clients are connected](../../getting-started/setup/see-how-many-tci-clients-are-connected.md)
