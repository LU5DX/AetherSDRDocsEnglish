# Adjust TCI RX gain per channel

The TCI Server applet provides four independent RX gain sliders, one per channel. Adjusting these lets you balance the audio level that TCI clients receive from each slice without affecting the radio's own receive gain.

## Before you start

- The TCI applet must be visible. If it is not, click the **TCI** tray button on the right sidebar to show it.
- The TCI server must be running (the **Enable** button must be in its checked state). Gain changes take effect immediately, but a client must be connected to receive audio.
- The radio must be connected. The applet requires an active radio connection.

## Steps

1. Open the TCI applet by clicking the **TCI** tray button on the right sidebar if it is not already visible.
2. Locate the **RX1**, **RX2**, **RX3**, or **RX4** row for the channel you want to adjust. Each row shows the channel label, a slice-assignment indicator, and a combined meter/slider.
3. Drag the slider portion of the meter/slider left to decrease gain or right to increase gain. The value is saved immediately.
4. Repeat for any other RX channels that need adjustment.

## What each control does

| Control | Default | Valid range | Persisted setting |
|---|---|---|---|
| RX1 gain+meter | 0.5 | 0.0–1.0 | `TciRxGain1` |
| RX2 gain+meter | 0.5 | 0.0–1.0 | `TciRxGain2` |
| RX3 gain+meter | 0.5 | 0.0–1.0 | `TciRxGain3` |
| RX4 gain+meter | 0.5 | 0.0–1.0 | `TciRxGain4` |
| RX/TX slice-assignment labels | — | — or Slice \<letter\> | *(none)* |

The slice-assignment indicator next to each RX row shows which slice is driving that channel (for example, **Slice A**) based on the DAX channel mapping. It displays **—** when no slice is assigned to that channel.

The meter portion of each slider reflects the live RX audio level with exponential smoothing: the display attacks quickly and decays slowly, so brief peaks are visible without constant flicker.

## Tips

- All four gain values are persisted as soon as you release the slider. They are restored automatically the next time AetherSDR starts.
- If a channel's slice-assignment indicator shows **—**, no audio will reach that TCI RX channel regardless of the gain setting. Assign a DAX channel to the relevant slice first.
- Gain values are on a linear 0.0–1.0 scale, not in dB. A value of 0.5 (the default) is half of the maximum output level presented to TCI clients.

## Related

- [Adjust TCI TX gain](adjust-tci-tx-gain.md)
- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [TCI Server overview](overview.md)
