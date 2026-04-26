# Autostart DAX on launch

Configure AetherSDR to start the DAX audio bridge automatically every time the application launches, so you do not have to manually enable DAX after each restart.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio before DAX streams become active, even if autostart is enabled.
- DAX autostart is available on macOS and PipeWire-enabled Linux systems.

## Steps

1. Open the DAX Audio applet by clicking the **DAX** tray button on the right sidebar. If the applet panel is not visible, enable it with `View > Applet Panel`.
2. To enable autostart via the menu, click `Settings > Autostart DAX with AetherSDR`. A checkmark appears next to the item when autostart is on. This persists the `AutoStartDAX` setting.
3. Alternatively, click **Enable** inside the DAX Audio applet. Clicking **Enable** both starts the DAX bridge immediately and saves `AutoStartDAX` so the bridge starts automatically on the next launch.
4. Verify the setting took effect by restarting AetherSDR and confirming that **Enable** appears active (highlighted green) when the DAX Audio applet opens.

## What each control does

| Control | Description | Default | Range | Setting key |
|---|---|---|---|---|
| **Enable** | Master toggle for the DAX audio bridge. Starts or stops all DAX RX and TX streams. State is persisted and restored on launch. | Off | On / Off | `AutoStartDAX` |
| DAX 1 gain+meter | Combined level meter and gain slider for DAX RX channel 1. Drag to adjust gain. | 0.5 | 0.0–1.0 | `DaxRxGain1` |
| DAX 2 gain+meter | Combined level meter and gain slider for DAX RX channel 2. | 0.5 | 0.0–1.0 | `DaxRxGain2` |
| DAX 3 gain+meter | Combined level meter and gain slider for DAX RX channel 3. | 0.5 | 0.0–1.0 | `DaxRxGain3` |
| DAX 4 gain+meter | Combined level meter and gain slider for DAX RX channel 4. | 0.5 | 0.0–1.0 | `DaxRxGain4` |
| TX gain+meter | Combined level meter and gain slider for the DAX TX stream. | 0.5 | 0.0–1.0 | `DaxTxGain` |

## Tips

- The menu item `Settings > Autostart DAX with AetherSDR` and the **Enable** button inside the applet write to the same `AutoStartDAX` setting. Either method produces the same result.
- Gain values for all channels (`DaxRxGain1` through `DaxRxGain4` and `DaxTxGain`) are saved independently each time you drag a slider, and are restored at launch regardless of whether autostart is on.

## Troubleshooting

- **Enable appears active after launch but no audio passes** — DAX streams require an active radio connection. Confirm AetherSDR is connected to the FLEX-8600 before expecting audio. The slice-assignment indicator next to each channel will show `—` if no slice is routed to that channel.
- **`Settings > Autostart DAX with AetherSDR` is missing** — This menu item is only present on supported platforms (macOS and PipeWire-enabled Linux). On unsupported systems, use the **Enable** button in the applet each session.

## Related

- [DAX Audio overview](overview.md)
- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Set DAX RX gain per channel](set-dax-rx-gain-per-channel.md)
- [Set DAX TX gain](set-dax-tx-gain.md)
- [See which slice is currently using each DAX channel](see-which-slice-is-currently-using-each-dax-channel.md)
