# Set DAX RX gain per channel

Use the DAX Audio applet to adjust the receive gain for each of the four DAX channels independently. Each channel's gain is saved and restored between sessions.

## Before you start

- AetherSDR must be connected to the radio. DAX controls are unavailable without an active radio connection.
- The DAX audio bridge must be running. Click Enable in the DAX Audio applet to start it if you have not already done so.

## Steps

1. Click the DAX tray button on the right sidebar to open the DAX Audio applet. If the applet panel is not visible, enable it first with `View > Applet Panel`.
2. Locate the row for the channel you want to adjust: **DAX 1**, **DAX 2**, **DAX 3**, or **DAX 4**.
3. Drag the combined meter/slider for that channel left to reduce gain or right to increase gain. The gain range is 0.0 to 1.0; the default is 0.5.
4. Release the drag. The new value is saved immediately to the corresponding setting key (`DaxRxGain1`, `DaxRxGain2`, `DaxRxGain3`, or `DaxRxGain4`) and takes effect at once.

Repeat for any other channel you want to adjust.

## What each control does

| Control | Default | Valid range | Setting key | Behavior |
|---|---|---|---|---|
| DAX 1 gain+meter | 0.5 | 0.0–1.0 | `DaxRxGain1` | Sets RX gain for DAX channel 1. The meter bar shows the post-fader output level. |
| DAX 2 gain+meter | 0.5 | 0.0–1.0 | `DaxRxGain2` | Sets RX gain for DAX channel 2. |
| DAX 3 gain+meter | 0.5 | 0.0–1.0 | `DaxRxGain3` | Sets RX gain for DAX channel 3. |
| DAX 4 gain+meter | 0.5 | 0.0–1.0 | `DaxRxGain4` | Sets RX gain for DAX channel 4. |
| Slice-assignment status | — | — or Slice A–H | — (not persisted) | Shows which slice is routed to each DAX channel. Read-only. |
| Enable | off | on/off | `AutoStartDAX` | Master switch for the DAX audio bridge. All gain sliders are inactive when this is off. |

## Tips

- The meter background shows the smoothed RMS level multiplied by the current gain, so the bar reflects actual output level. Moving the slider gives immediate visual feedback even before audio arrives.
- Gain values are stored as two decimal places (for example, `0.50`). They are restored from disk when AetherSDR next launches, so you do not need to re-set them after restarting.
- The status indicator next to each channel label shows which slice is assigned to that DAX channel. If the indicator shows —, no slice is currently routed there. See [See which slice is currently using each DAX channel](see-which-slice-is-currently-using-each-dax-channel.md).

## Troubleshooting

- **Dragging the slider has no effect on the audio level** — Check that Enable is active (lit green). The gain change is applied by the DAX bridge; if the bridge is not running, the setting is saved but not applied to the audio stream.
- **The meter bar shows no activity** — The status indicator next to the channel may show —, meaning no slice is assigned to that DAX channel. Assign a slice to the channel in your radio's slice settings.

## Related

- [DAX Audio overview](overview.md)
- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Set DAX TX gain](set-dax-tx-gain.md)
- [See which slice is currently using each DAX channel](see-which-slice-is-currently-using-each-dax-channel.md)
- [Autostart DAX on launch](autostart-dax-on-launch.md)
