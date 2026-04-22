# Set DAX RX gain per channel

Adjust the receive audio level for each of the four DAX channels (DAX 1–4) so that digital mode software or other audio consumers receive audio at the right level.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The DAX applet must be open. If it is not visible, click the DAX tray button on the right sidebar to show it.
- DAX must be enabled. If the Enable button is not lit, click Enable to start the DAX audio bridge.

## Steps

1. Click the DAX tray button on the right sidebar to open the DAX Audio applet.
2. Locate the row for the channel you want to adjust: DAX 1, DAX 2, DAX 3, or DAX 4.
3. Drag the meter/slider on that row left or right to decrease or increase the RX gain.
4. Release the mouse button. The new gain is saved immediately.

Repeat for any other channels that need adjustment.

## What each control does

| Control | Default | Valid range | Persisted setting |
|---|---|---|---|
| DAX 1 gain+meter | 0.5 | 0.0–1.0 | `DaxRxGain1` |
| DAX 2 gain+meter | 0.5 | 0.0–1.0 | `DaxRxGain2` |
| DAX 3 gain+meter | 0.5 | 0.0–1.0 | `DaxRxGain3` |
| DAX 4 gain+meter | 0.5 | 0.0–1.0 | `DaxRxGain4` |
| Slice-assignment status | — | — or Slice A–H | _(not persisted)_ |

Each meter/slider is a combined control. The background bar shows the smoothed RMS audio level post-fader; the draggable thumb sets the gain. Moving the thumb immediately updates the displayed level. Gain values are stored as two decimal places (for example, `0.50`).

The slice-assignment indicator to the left of each meter shows which slice is currently routed to that channel (for example, Slice A). A dash (—) means no slice is assigned.

## Tips

- Gain is applied post-fader: the meter bar reflects the actual output level after your gain adjustment, not the raw input level. Use this to confirm that the signal reaching your digital mode software is neither clipped nor too low.
- Gain settings persist across restarts. You do not need to re-adjust them each session.
- If a channel shows — in the slice-assignment indicator, no audio will pass through regardless of the gain setting. Assign a slice to that DAX channel first.

## Troubleshooting

- **Dragging the slider has no effect** — Verify that Enable is active (lit green). Gain changes are accepted at any time, but no audio flows unless the DAX bridge is running.
- **Meter bar shows no movement after adjusting gain** — Check that a slice is assigned to the channel (the indicator should show Slice A–H, not —). If the indicator shows —, assign a slice to the DAX channel from the radio's slice controls.
- **Gain resets to 0.5 after restart** — This can happen if AetherSDR cannot write its settings file. Check file-system permissions for the AetherSDR settings directory.

## Related

- [DAX Audio overview](overview.md)
- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Set DAX TX gain](set-dax-tx-gain.md)
- [See which slice is currently using each DAX channel](see-which-slice-is-currently-using-each-dax-channel.md)
- [Autostart DAX on launch](autostart-dax-on-launch.md)
