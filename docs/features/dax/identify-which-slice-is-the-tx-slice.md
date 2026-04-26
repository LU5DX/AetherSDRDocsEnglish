# Identify which slice is the TX slice

The DAX Audio applet shows a live TX assignment indicator so you can see at a glance which slice currently holds transmit privileges. This is useful when running multiple slices or digital mode software where you need to confirm the correct slice is driving the DAX TX stream.

## Before you start

- AetherSDR must be connected to the radio. The TX assignment indicator requires an active radio connection.
- The DAX applet must be visible. If it is not, click the DAX tray button on the right sidebar to open it.

## Steps

1. Click the DAX tray button on the right sidebar to open the DAX Audio applet.
2. Look at the TX row at the bottom of the applet. The label immediately to the right of "TX:" shows the current TX slice.
3. Read the TX assignment indicator. It displays either `—` (no TX slice assigned) or `Slice A` through `Slice H` (the letter of the slice currently holding TX privileges).

## What each control does

| Control | Description | States |
|---|---|---|
| TX assignment indicator | Shows which slice currently has TX privileges and drives the DAX TX stream. Updates automatically when TX is transferred between slices. No persisted setting. | `—` or `Slice A`–`Slice H` |

## Tips

- The TX indicator updates in real time. If you transfer TX to a different slice (for example, by clicking a slice's TX button on the panadapter), the indicator changes immediately without any action in the DAX applet.
- The RX channel rows above the TX row each have their own slice assignment indicator showing `—` or `Slice A`–`Slice H`. Those show which slice is routed to each DAX RX channel, which is separate from TX assignment. See [See which slice is currently using each DAX channel](see-which-slice-is-currently-using-each-dax-channel.md).

## Related

- [See which slice is currently using each DAX channel](see-which-slice-is-currently-using-each-dax-channel.md)
- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [DAX Audio overview](overview.md)
