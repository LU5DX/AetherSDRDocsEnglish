# Adjust TCI RX gain per channel

The TCI Server applet provides four independent RX gain sliders, one per channel. Adjusting these lets you match the audio level that TCI clients (such as Log4OM or SunSDR tools) receive from each active slice.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The TCI applet must be visible. If it is not, click the TCI tray button on the right sidebar to show it.
- The TCI server should be running (Enable toggled on) so you can see live metering while you adjust.

## Steps

1. Click the TCI tray button on the right sidebar to open the TCI Server applet.
2. Locate the RX1, RX2, RX3, or RX4 row for the channel you want to adjust. The slice label to the right of the channel name (for example, `Slice A`) shows which slice is driving that channel. A `—` means no slice is assigned.
3. Drag the combined meter/slider for that row left to decrease gain or right to increase gain. The valid range is 0.0 to 1.0; the default is 0.5.
4. Repeat for any other RX channels you want to adjust.

The new value is saved immediately. It persists across restarts as `TciRxGain1`, `TciRxGain2`, `TciRxGain3`, or `TciRxGain4` depending on the channel.

## What each control does

| Control | Default | Valid range | Persisted key |
|---|---|---|---|
| RX1 gain+meter | 0.5 | 0.0 – 1.0 | `TciRxGain1` |
| RX2 gain+meter | 0.5 | 0.0 – 1.0 | `TciRxGain2` |
| RX3 gain+meter | 0.5 | 0.0 – 1.0 | `TciRxGain3` |
| RX4 gain+meter | 0.5 | 0.0 – 1.0 | `TciRxGain4` |
| Slice assignment label | — | — or `Slice <letter>` | (none) |

The meter portion of each slider reflects live RX signal level using exponential smoothing: fast attack, slow decay. This lets you judge a suitable gain setting while audio is flowing.

## Tips

- If a channel shows `—` in the slice label, no slice is assigned to that DAX channel. Gain changes are saved but will have no audible effect until a slice is mapped to that channel.
- All four gain values are independent. Setting RX1 does not affect RX2–RX4.

## Troubleshooting

- **Meter shows no movement** — The TCI server may not be running. Check that Enable is toggled on and the server status does not read `(stopped)` or `(port in use)`. See [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md).
- **Slice label shows `—` for all channels** — No slice has a DAX channel assignment. Assign a DAX channel to each slice via the radio's slice settings, then return here to set gain.

## Related

- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Adjust TCI TX gain](adjust-tci-tx-gain.md)
- [TCI Server overview](overview.md)
- [Change the TCI port](change-the-tci-port.md)
