# Autostart DAX on launch

Configure AetherSDR to start the DAX audio bridge automatically every time the application connects to the radio, so you do not have to click Enable manually each session.

## Before you start

- AetherSDR must be installed and able to reach your FLEX-8600 on the network.
- DAX is available on macOS and PipeWire-equipped Linux systems.

## Steps

1. Open the DAX Audio applet by clicking the **DAX** tray button on the right sidebar. If the applet panel is not visible, enable it with `View > Applet Panel`.
2. To enable autostart via the menu: click `Settings > Autostart DAX with AetherSDR`. A checkmark appears next to the item when autostart is active. AetherSDR saves this as `AutoStartDAX`.
3. Alternatively, enable DAX for the current session by clicking **Enable** in the DAX Audio applet. This also persists `AutoStartDAX` so DAX starts automatically on the next launch.
4. To disable autostart, click `Settings > Autostart DAX with AetherSDR` again to remove the checkmark, or click **Enable** in the applet to toggle it off.

## What each control does

| Control | Description | Default | Range | Setting key |
|---|---|---|---|---|
| **Enable** (toggle button) | Starts or stops the DAX audio bridge. Checking this also sets autostart. | Off | On / Off | `AutoStartDAX` |
| DAX 1 gain+meter | Combined level meter and gain slider for DAX RX channel 1. | 0.5 | 0.0–1.0 | `DaxRxGain1` |
| DAX 2 gain+meter | Combined level meter and gain slider for DAX RX channel 2. | 0.5 | 0.0–1.0 | `DaxRxGain2` |
| DAX 3 gain+meter | Combined level meter and gain slider for DAX RX channel 3. | 0.5 | 0.0–1.0 | `DaxRxGain3` |
| DAX 4 gain+meter | Combined level meter and gain slider for DAX RX channel 4. | 0.5 | 0.0–1.0 | `DaxRxGain4` |
| TX gain+meter | Combined level meter and gain slider for the DAX TX stream. | 0.5 | 0.0–1.0 | `DaxTxGain` |
| Slice-assignment status | Read-only indicator showing which slice is routed to each DAX channel. Displays `—` when unassigned, or `Slice A`–`Slice H` when assigned. | `—` | — | — |

## Tips

- The menu item and the **Enable** button write to the same `AutoStartDAX` setting. Either method persists the choice across restarts.
- Gain settings (`DaxRxGain1`–`DaxRxGain4`, `DaxTxGain`) are saved independently each time you drag a slider. They are restored at the next launch regardless of whether autostart is on.

## Troubleshooting

- **DAX does not start automatically despite the checkmark being set** — Confirm your system meets the platform requirement (macOS or PipeWire on Linux). On other configurations the option has no effect.
- **Enable button is unresponsive** — The DAX applet requires an active radio connection. Connect to the FLEX-8600 first via `Settings > Connect to Radio...`, then try again.

## Related

- [DAX Audio overview](overview.md)
- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Set DAX RX gain per channel](set-dax-rx-gain-per-channel.md)
- [Set DAX TX gain](set-dax-tx-gain.md)
- [See which slice is currently using each DAX channel](see-which-slice-is-currently-using-each-dax-channel.md)
