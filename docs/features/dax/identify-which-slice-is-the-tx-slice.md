# Identify which slice is the TX slice

The DAX Audio applet shows a TX assignment indicator that tells you at a glance which slice currently holds TX privileges. Use this when you need to confirm that the correct slice is driving the DAX TX stream before transmitting from digital mode software.

## Before you start

- AetherSDR must be connected to the radio. The TX indicator is only populated when a radio connection is active.
- The DAX Audio applet must be visible. If it is not, click the DAX tray button on the right sidebar to open it.

## Steps

1. Click the DAX tray button on the right sidebar to open the DAX Audio applet.
2. Look at the row labeled **TX:** near the bottom of the applet.
3. Read the indicator to the right of the **TX:** label. It shows either `—` (no TX slice assigned) or `Slice A` through `Slice H` (the slice currently holding TX privileges).

## What each control does

| Control | Description | Default | Notes |
|---|---|---|---|
| TX assignment indicator | Shows which slice currently has TX privileges. Updates automatically when TX changes between slices. | `—` | Display only; not configurable here. |
| TX gain+meter | Combined level meter and gain slider for the DAX TX stream. Drag to adjust. | 0.5 (range 0.0–1.0) | Persisted as `DaxTxGain`. |

## Tips

- The TX indicator updates automatically whenever TX moves to a different slice — you do not need to refresh or re-open the applet.
- If the indicator shows `—` and you expect a slice to be transmitting, verify that the radio has an active slice with TX enabled.
- The RX rows above the TX row each have their own slice assignment indicator showing `Slice A`–`Slice H` or `—`. Compare these with the TX row to understand the full routing picture.

## Troubleshooting

- **TX indicator shows `—` even though a slice is active** — The radio connection may not be fully established, or no slice currently holds TX privileges. Check the connection status and ensure at least one slice is configured for TX on the radio.

## Related

- [See which slice is currently using each DAX channel](see-which-slice-is-currently-using-each-dax-channel.md)
- [Set DAX TX gain](set-dax-tx-gain.md)
- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [DAX Audio overview](overview.md)
