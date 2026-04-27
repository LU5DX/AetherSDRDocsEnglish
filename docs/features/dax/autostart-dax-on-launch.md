# Autostart DAX on Launch

Enable the `AutoStartDAX` setting so that the DAX audio bridge starts automatically every time AetherSDR opens, without requiring a manual click of Enable each session.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The DAX applet requires an active radio connection.
- The DAX applet must be visible. If it is not, click the **DAX** tray button on the right sidebar to show it.

## Steps

1. Open the DAX applet by clicking the **DAX** tray button on the right sidebar if it is not already visible.
2. Click **Settings > Autostart DAX with AetherSDR** to place a check mark next to the item. This persists `AutoStartDAX` as `True`.
3. Confirm the **Enable** button in the DAX applet is checked (lit green). If it is not, click **Enable** to start the bridge for the current session.

On the next launch, AetherSDR will read `AutoStartDAX` and activate the bridge automatically, reflecting the checked state on the **Enable** button.

To turn autostart off, click **Settings > Autostart DAX with AetherSDR** again to remove the check mark.

## What each control does

| Control | What it does | Default | Range | Setting key |
|---|---|---|---|---|
| **Enable** (in the DAX applet) | Master toggle. Starts or stops the DAX audio bridge for the current session and persists the state. | Off | On / Off | `AutoStartDAX` |
| **Settings > Autostart DAX with AetherSDR** | Checkable menu item. When checked, AetherSDR starts the DAX bridge on every launch. | Off (unchecked) | Checked / Unchecked | `AutoStartDAX` |
| DAX 1 gain+meter | Combined level meter and gain slider for DAX RX channel 1. Drag to adjust. | 0.5 | 0.0 – 1.0 | `DaxRxGain1` |
| DAX 2 gain+meter | Combined level meter and gain slider for DAX RX channel 2. Drag to adjust. | 0.5 | 0.0 – 1.0 | `DaxRxGain2` |
| DAX 3 gain+meter | Combined level meter and gain slider for DAX RX channel 3. Drag to adjust. | 0.5 | 0.0 – 1.0 | `DaxRxGain3` |
| DAX 4 gain+meter | Combined level meter and gain slider for DAX RX channel 4. Drag to adjust. | 0.5 | 0.0 – 1.0 | `DaxRxGain4` |
| TX gain+meter | Combined level meter and gain slider for the DAX TX stream. Drag to adjust. | 0.5 | 0.0 – 1.0 | `DaxTxGain` |

## Tips

- The **Enable** button and **Settings > Autostart DAX with AetherSDR** both write the same `AutoStartDAX` key. Clicking either one updates the shared setting.
- Gain values for all four RX channels and the TX channel are saved independently. Adjusting them before enabling autostart means they will be restored at the same levels on the next launch.

## Troubleshooting

- **The DAX applet is not visible** — Click the **DAX** tray button on the right sidebar to show it.
- **Enable is checked but the bridge does not start on the next launch** — Verify that **Settings > Autostart DAX with AetherSDR** has a check mark. Clicking **Enable** in the applet alone sets the bridge state for the current session and persists `AutoStartDAX`, but confirming the menu item is checked ensures the autostart path runs at launch.
- **The Enable button is unchecked after launch despite autostart being on** — This can occur if AetherSDR launches before a radio connection is established. The DAX applet requires a connected radio. Connect to the radio and click **Enable** manually, or allow AetherSDR to connect before checking the bridge state.

## Related

- [DAX Audio overview](overview.md)
- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Set DAX RX gain per channel](set-dax-rx-gain-per-channel.md)
- [Set DAX TX gain](set-dax-tx-gain.md)
- [See which slice is currently using each DAX channel](see-which-slice-is-currently-using-each-dax-channel.md)
