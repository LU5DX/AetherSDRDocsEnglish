# Identify which slice is the TX slice

The DAX Applet shows a live TX assignment indicator that tells you which slice currently holds TX privileges. Use this when you need to confirm the transmit slice before operating digital modes or checking DAX TX audio routing.

## Before you start

- AetherSDR must be connected to the radio. The TX assignment indicator requires an active radio connection.
- The DAX Applet must be visible. It is hidden by default.

## Steps

1. Click the **DAX** tray button on the right sidebar to open the DAX Applet.
2. Look at the **TX:** row at the bottom of the applet.
3. Read the status indicator to the right of the **TX:** label. It shows either `—` (no TX slice assigned) or `Slice A` through `Slice H` (the slice currently holding TX privileges).

## What each control does

| Control | Description | Default | Valid states | Setting key |
|---|---|---|---|---|
| TX assignment indicator | Shows which slice currently has TX privileges. Updates automatically when TX is moved between slices. | `—` | `—` or `Slice A`–`Slice H` | none |

## Tips

- The TX indicator updates in real time. If you transfer TX to another slice on the radio, the indicator changes immediately without any manual refresh.
- The RX rows above the TX row show per-channel DAX assignments (`DAX 1:` through `DAX 4:`). These indicate which slice is routed to each DAX RX channel and are separate from the TX assignment.

## Related

- [See which slice is currently using each DAX channel](see-which-slice-is-currently-using-each-dax-channel.md)
- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [DAX Audio overview](overview.md)
