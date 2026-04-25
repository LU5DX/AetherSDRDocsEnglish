# Enable the TCI server for Log4OM / SunSDR clients

The TCI server lets third-party logging and digital-mode software such as Log4OM, and SunSDR tools, connect to AetherSDR over a WebSocket-based TCI protocol. Enable the server here so those clients can read frequency, mode, and audio data from the radio.

## Before you start

- AetherSDR must be connected to the radio. The TCI applet requires an active radio connection.
- Confirm that no other application is already listening on port 50001 (or whichever port you intend to use).

## Steps

1. Click the **TCI** tray button on the right sidebar. The TCI Server applet panel appears.
2. Check the **Port** field. The default is `50001`. Change it if needed — valid range is 1024–65535. Values outside that range snap back to `50001`.
3. Click **Enable**. The button highlights green when the server is running.
4. Watch the server status indicator next to **Enable**. It changes from `(stopped)` to `:<port> (N clients)` once the server is up. When a client connects, the client count increments.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Port | `50001` | 1024–65535 | `TciPort` | Sets the WebSocket port. Changing the port while the server is running restarts the server on the new port. Out-of-range values snap to `50001`. |
| Enable | Off | On / Off | — | Starts or stops the TCI server. If the port is already in use, the toggle snaps back to off and the status shows `(port in use)` in red. |
| RX1–RX4 gain+meter | 0.5 | 0.0–1.0 | `TciRxGain1`–`TciRxGain4` | Combined meter and slider. Drag to set the TCI RX gain for each channel. The slice letter shown next to each row reflects the DAX channel assignment for that slice. |
| TX gain+meter | 0.5 | 0.0–1.0 | `TciTxGain` | Combined meter and slider. Drag to set the TCI TX gain. The slice letter shown reflects whichever slice is currently the TX slice. |
| RX/TX slice-assignment labels | — | `—` or `Slice <letter>` | — | Read-only indicators. Show which slice drives each RX or TX row based on DAX channel mapping. |

## Tips

- To start the TCI server automatically every time AetherSDR launches, enable `Settings > Autostart TCI with AetherSDR` instead of clicking **Enable** each session.
- If the status stays at `(stopped)` immediately after clicking **Enable**, the port is likely in use. Change the **Port** value and click **Enable** again.

## Troubleshooting

- **Status shows `(port in use)` in red after clicking Enable** — Another process is bound to that port. Enter a different port number in the **Port** field and click **Enable** again.
- **Client count stays at 0 after the server starts** — Confirm the client software is pointed at the correct host address and port. Check that a firewall is not blocking the port.
- **RX/TX slice labels show `—`** — No slice has a DAX channel assigned. Assign a DAX channel to the slice in the radio's slice settings. The label updates automatically once a channel is mapped.

## Related

- [TCI Server overview](overview.md)
- [Change the TCI port](change-the-tci-port.md)
- [Adjust TCI RX gain per channel](adjust-tci-rx-gain-per-channel.md)
- [Adjust TCI TX gain](adjust-tci-tx-gain.md)
- [Autostart TCI on launch](autostart-tci-on-launch.md)
- [See how many TCI clients are connected](../../getting-started/setup/see-how-many-tci-clients-are-connected.md)
