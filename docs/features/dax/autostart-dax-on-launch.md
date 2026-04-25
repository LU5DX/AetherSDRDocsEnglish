# Autostart DAX on launch

Configure AetherSDR to start the DAX audio bridge automatically each time the application launches, so DAX channels are ready without manual enabling.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The DAX applet requires an active radio connection.
- The DAX feature is available on macOS and PipeWire-based Linux systems.

## Steps

1. To set DAX to start automatically on every launch, go to `Settings > Autostart DAX with AetherSDR` and click the menu item to check it. This persists the `AutoStartDAX` setting to `True`.
2. To enable DAX immediately in the current session without restarting, open the DAX applet: click the **DAX** tray button on the right sidebar.
3. In the DAX applet, click **Enable** to start the audio bridge now. The button lights green when active.

To turn off autostart, go to `Settings > Autostart DAX with AetherSDR` again to uncheck it.

## What each control does

| Control | Description | Default | Range | Setting key |
|---|---|---|---|---|
| `Settings > Autostart DAX with AetherSDR` | Checkable menu item. When checked, DAX starts automatically on launch. | Off | On / Off | `AutoStartDAX` |
| **Enable** (in DAX applet) | Master toggle for the DAX audio bridge. Also reads and writes `AutoStartDAX`. | Off | On / Off | `AutoStartDAX` |
| DAX 1 gain+meter | Combined meter and gain slider for DAX RX channel 1. | 0.5 | 0.0–1.0 | `DaxRxGain1` |
| DAX 2 gain+meter | Combined meter and gain slider for DAX RX channel 2. | 0.5 | 0.0–1.0 | `DaxRxGain2` |
| DAX 3 gain+meter | Combined meter and gain slider for DAX RX channel 3. | 0.5 | 0.0–1.0 | `DaxRxGain3` |
| DAX 4 gain+meter | Combined meter and gain slider for DAX RX channel 4. | 0.5 | 0.0–1.0 | `DaxRxGain4` |
| TX gain+meter | Combined meter and gain slider for the DAX TX stream. | 0.5 | 0.0–1.0 | `DaxTxGain` |

## Tips

- The **Enable** button in the DAX applet and `Settings > Autostart DAX with AetherSDR` both write the same `AutoStartDAX` setting. Clicking **Enable** in the applet is equivalent to checking the menu item for future launches.
- Gain values for all channels are persisted immediately on change. If you adjust gains in one session, they are restored in the next.

## Troubleshooting

- **DAX applet is not visible** — The applet is hidden by default. Click the **DAX** tray button on the right sidebar to show it.
- **`Settings > Autostart DAX with AetherSDR` is not present in the menu** — This item only appears on supported platforms (macOS and PipeWire-based Linux). It is not available on all configurations.
- **DAX starts but no audio passes through** — Verify that a slice is assigned to a DAX channel. Each channel's status indicator shows `—` when no slice is routed to it, or `Slice A`–`Slice H` when one is assigned. See [See which slice is currently using each DAX channel](see-which-slice-is-currently-using-each-dax-channel.md).

## Related

- [DAX Audio overview](overview.md)
- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Set DAX RX gain per channel](set-dax-rx-gain-per-channel.md)
- [Set DAX TX gain](set-dax-tx-gain.md)
- [See which slice is currently using each DAX channel](see-which-slice-is-currently-using-each-dax-channel.md)
