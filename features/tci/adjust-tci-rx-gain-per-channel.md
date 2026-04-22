# Adjust TCI RX gain per channel

The TCI Server applet provides four independent RX gain sliders — one per channel — that scale the audio level sent to connected TCI clients. Adjust these when a client receives audio that is too loud or too quiet relative to your operating setup.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The TCI applet requires a radio connection.
- The TCI server must be enabled. If it is not, the gain values are still saved but no audio is being sent to clients. See [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md).

## Steps

1. Click the **TCI** tray button on the right sidebar to open the TCI Server applet.
2. Locate the **RX1**, **RX2**, **RX3**, or **RX4** row for the channel you want to adjust. The slice currently assigned to each channel is shown in the indicator next to the row label (for example, `Slice A`); rows with no slice assigned show `—`.
3. Drag the meter/slider for that row left to reduce gain or right to increase gain. The value is saved immediately.
4. Repeat for any other channels that need adjustment.

## What each control does

| Label | Kind | Default | Valid range | Persisted setting |
|---|---|---|---|---|
| RX1 gain+meter | Meter/slider | 0.5 | 0.0–1.0 | `TciRxGain1` |
| RX2 gain+meter | Meter/slider | 0.5 | 0.0–1.0 | `TciRxGain2` |
| RX3 gain+meter | Meter/slider | 0.5 | 0.0–1.0 | `TciRxGain3` |
| RX4 gain+meter | Meter/slider | 0.5 | 0.0–1.0 | `TciRxGain4` |

Each slider also acts as a live meter, displaying the smoothed RX audio level for the channel.

## Tips

- The meter display uses fast attack and slow decay smoothing, so peaks are visible briefly even during gaps in audio.
- Gain values are persisted as soon as you release the slider. They are restored automatically the next time AetherSDR starts.
- RX channel assignments follow DAX channel mapping. If a channel shows `—`, no slice is currently assigned to that DAX channel; assign a DAX channel to a slice to drive that TCI RX row.

## Troubleshooting

- **All RX meters are dark and no audio reaches the client** — The TCI server may not be running. Check that the server status shows `:<port> (N clients)` and not `(stopped)`. Click **Enable** to start the server if needed.
- **Gain changes have no effect on the client** — Confirm the client is connected to the correct port (`TciPort`, default `50001`). The server status shows the active port and client count.

## Related

- [Adjust TCI TX gain](adjust-tci-tx-gain.md)
- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Change the TCI port](change-the-tci-port.md)
- [Autostart TCI on launch](autostart-tci-on-launch.md)
