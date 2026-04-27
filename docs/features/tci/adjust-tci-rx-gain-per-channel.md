# Adjust TCI RX gain per channel

The TCI Server applet provides a gain slider for each of its four RX channels. Adjusting these lets you match the audio level that TCI clients (such as Log4OM or SunSDR tools) receive from each slice.

## Before you start

- The radio must be connected. The TCI applet requires an active radio connection.
- The TCI Server applet must be visible. If the applet panel is not showing, click the **TCI** tray button on the right sidebar to reveal it.

## Steps

1. Click the **TCI** tray button on the right sidebar to open the TCI Server applet.
2. Locate the **RX1**, **RX2**, **RX3**, or **RX4** row for the channel you want to adjust. The slice assignment label next to the channel name (for example, `Slice A`) shows which slice is driving that channel. A `—` means no slice is currently assigned.
3. Drag the meter/slider for that row left or right to set the gain. The value is saved immediately.
4. Repeat for any other RX channels you want to adjust.

## What each control does

| Control | Default | Valid range | Persisted setting |
|---|---|---|---|
| RX1 gain meter/slider | 0.5 | 0.0 – 1.0 | `TciRxGain1` |
| RX2 gain meter/slider | 0.5 | 0.0 – 1.0 | `TciRxGain2` |
| RX3 gain meter/slider | 0.5 | 0.0 – 1.0 | `TciRxGain3` |
| RX4 gain meter/slider | 0.5 | 0.0 – 1.0 | `TciRxGain4` |
| Slice assignment label | — | — or `Slice <letter>` | *(not persisted)* |

Each meter/slider also displays a live RX level using exponential smoothing — fast attack, slow decay — so the bar reflects signal activity on that channel while the drag position sets the gain.

## Tips

- The slice assignment labels (for example, `Slice A`) follow the DAX channel mapping. If a slice's DAX channel assignment changes, the label updates automatically.
- Gain values are persisted as two-decimal floats (for example, `0.75`). They are restored the next time AetherSDR starts.

## Troubleshooting

- **A channel shows `—` and passes no audio to the TCI client** — No slice is assigned to that DAX channel. Assign a slice to the corresponding DAX channel in your radio setup so TCI RX audio is routed to that channel.

## Related

- [TCI Server overview](overview.md)
- [Adjust TCI TX gain](adjust-tci-tx-gain.md)
- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
