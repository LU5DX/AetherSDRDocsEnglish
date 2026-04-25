# Adjust TCI RX gain per channel

The TCI Server applet provides four independent RX gain sliders — one per channel — so you can control how loudly each receiver channel is presented to connected TCI clients such as Log4OM or SunSDR tools.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The TCI applet requires a radio connection.
- The TCI server must be visible in the applet panel. If it is not, click the **TCI** tray button on the right sidebar to show it.

## Steps

1. Click the **TCI** tray button on the right sidebar to open the TCI Server applet.
2. Locate the **RX1**, **RX2**, **RX3**, or **RX4** row for the channel you want to adjust.
3. Drag the meter/slider on that row left to decrease gain or right to increase gain. The new value is saved immediately.
4. Repeat for any other RX channels you want to adjust.

## What each control does

| Control | Description | Default | Valid range | Setting key |
|---|---|---|---|---|
| RX1 gain+meter | Combined level meter and gain slider for TCI RX channel 1. | 0.5 | 0.0–1.0 | `TciRxGain1` |
| RX2 gain+meter | Combined level meter and gain slider for TCI RX channel 2. | 0.5 | 0.0–1.0 | `TciRxGain2` |
| RX3 gain+meter | Combined level meter and gain slider for TCI RX channel 3. | 0.5 | 0.0–1.0 | `TciRxGain3` |
| RX4 gain+meter | Combined level meter and gain slider for TCI RX channel 4. | 0.5 | 0.0–1.0 | `TciRxGain4` |
| Slice assignment label | Indicator showing which slice drives this RX row (e.g. `Slice A`). Shows `—` when no slice is assigned. | `—` | `—` or `Slice <letter>` | — |

Each RX channel shares its slice assignment with the DAX channel mapping. The label next to each meter shows which slice is currently routed to that channel.

## Tips

- The meter portion of each slider reflects live signal level with fast attack and slow decay smoothing, so brief peaks are visible without the display flickering constantly.
- Each gain value is persisted as soon as you release the slider. Restarting AetherSDR restores the last saved value.
- If a channel shows `—` in the slice label, no slice is currently assigned to that DAX channel. Assign a slice to the corresponding DAX channel to route audio through it.

## Related

- [TCI Server overview](overview.md)
- [Adjust TCI TX gain](adjust-tci-tx-gain.md)
- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
