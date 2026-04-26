# Set DAX RX gain per channel

Use the DAX Audio applet to adjust the receive gain for each of the four DAX channels. Gain changes take effect immediately and persist across sessions.

## Before you start

- Connect to a FLEX-8600 radio. The DAX applet requires an active radio connection.
- Enable DAX by clicking Enable in the DAX Audio applet. The gain sliders are present regardless, but audio will not flow until DAX is running.

## Steps

1. Click the DAX tray button on the right sidebar to open the DAX Audio applet.
2. Locate the row for the channel you want to adjust: **DAX 1**, **DAX 2**, **DAX 3**, or **DAX 4**.
3. Drag the combined meter/slider for that channel left or right to set the RX gain. Dragging left decreases gain; dragging right increases it.
4. Release to confirm. The value is saved automatically.

Repeat for any other channel you want to adjust.

## What each control does

| Control | Default | Valid range | Persisted setting |
|---|---|---|---|
| DAX 1 gain+meter | 0.5 | 0.0 – 1.0 | `DaxRxGain1` |
| DAX 2 gain+meter | 0.5 | 0.0 – 1.0 | `DaxRxGain2` |
| DAX 3 gain+meter | 0.5 | 0.0 – 1.0 | `DaxRxGain3` |
| DAX 4 gain+meter | 0.5 | 0.0 – 1.0 | `DaxRxGain4` |
| Slice-assignment status | — | — or Slice A–H | (none) |

Each meter/slider is a combined control: the background bar shows the smoothed RMS receive level (post-fader, so it reflects the effective output after your gain setting), and the draggable thumb sets the gain. Gain values are stored as two decimal places, for example `0.75`.

The slice-assignment indicator to the left of each meter shows which slice is currently routed to that DAX channel. It displays — when no slice is assigned.

## Tips

- The level meter uses post-fader ballistics, meaning the bar reflects the actual output level after your gain setting. If you drag the thumb to zero, the meter bar disappears even if audio is present.
- Gain values persist between sessions. You do not need to re-adjust them after restarting AetherSDR.

## Troubleshooting

- **Dragging the slider has no audible effect** — Confirm that Enable is active (button appears highlighted). If DAX is not running, gain is stored but no audio flows.
- **Meter bar is not moving** — Check that a slice is assigned to the channel. The slice-assignment indicator shows — if no slice is routed there. See [See which slice is currently using each DAX channel](see-which-slice-is-currently-using-each-dax-channel.md).

## Related

- [DAX Audio overview](overview.md)
- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Set DAX TX gain](set-dax-tx-gain.md)
- [See which slice is currently using each DAX channel](see-which-slice-is-currently-using-each-dax-channel.md)
- [Autostart DAX on launch](autostart-dax-on-launch.md)
