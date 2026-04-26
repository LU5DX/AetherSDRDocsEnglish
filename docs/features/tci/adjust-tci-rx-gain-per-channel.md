# Adjust TCI RX gain per channel

The TCI Server applet provides four independent RX gain sliders — one per channel — so you can control the audio level that TCI clients receive from each active slice.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The TCI applet requires an active radio connection.
- The TCI server must be running (Enable toggled on). See [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md).
- Each RX channel you want to adjust must have a slice assigned to it. Unassigned channels show `—` in the slice indicator.

## Steps

1. Click the TCI tray button on the right sidebar to open the TCI Server applet.
2. Locate the **RX1**, **RX2**, **RX3**, or **RX4** row for the channel you want to adjust. The label to the right of the channel name shows which slice is assigned (for example, `Slice A`), or `—` if no slice is assigned.
3. Drag the meter/slider on that row left to reduce gain or right to increase gain. The valid range is 0.0 to 1.0. The default is 0.5.
4. Release the drag. The new value is saved immediately to the corresponding setting (`TciRxGain1`, `TciRxGain2`, `TciRxGain3`, or `TciRxGain4`).

## What each control does

| Control | Default | Valid range | Persisted setting |
|---|---|---|---|
| RX1 gain meter/slider | 0.5 | 0.0 – 1.0 | `TciRxGain1` |
| RX2 gain meter/slider | 0.5 | 0.0 – 1.0 | `TciRxGain2` |
| RX3 gain meter/slider | 0.5 | 0.0 – 1.0 | `TciRxGain3` |
| RX4 gain meter/slider | 0.5 | 0.0 – 1.0 | `TciRxGain4` |
| Slice indicator | `—` | `—` or `Slice <letter>` | — |

The meter portion of each RX row displays a live signal level using exponential smoothing — fast attack, slow decay — so brief peaks are visible without the reading being erratic.

The slice indicator for each RX channel follows the DAX channel assignment. If you reassign a slice to a different DAX channel, the RX indicator updates automatically.

## Tips

- Channels with no slice assigned (`—`) carry no audio. Adjusting the gain on an unassigned channel has no audible effect until a slice is assigned to that DAX channel.
- Gain values are stored as two decimal places (for example, `0.75`). They persist across restarts; you do not need to re-enter them each session.

## Related

- [Adjust TCI TX gain](adjust-tci-tx-gain.md)
- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [TCI Server overview](overview.md)
