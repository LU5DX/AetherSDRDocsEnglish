# See which slice is currently using each DAX channel

The DAX Audio applet shows a slice-assignment indicator next to each DAX channel so you can confirm at a glance which slice is routed where, without opening any menus or dialogs.

## Before you start

- AetherSDR must be connected to the radio. The slice-assignment indicators reflect live radio state and show `—` when no radio is connected.
- The DAX applet must be visible. It is hidden by default.

## Steps

1. Click the **DAX** tray button on the right sidebar to open the DAX Audio applet.
2. Look at the status indicator to the right of each channel label (**DAX 1:**, **DAX 2:**, **DAX 3:**, **DAX 4:**).
3. Read the indicator value:
   - `Slice A` through `Slice H` — that slice is currently routed to this DAX channel.
   - `—` — no slice is assigned to this channel.
4. To check which slice is currently driving the DAX TX stream, read the status indicator to the right of the **TX:** label.

## What each control does

| Label | Kind | Possible values | Meaning |
|---|---|---|---|
| Slice-assignment indicator (DAX 1–4) | Indicator | `—` or `Slice A`–`Slice H` | The slice currently routed to that RX channel. Updates automatically when slice DAX assignments change. No persisted setting. |
| TX assignment indicator | Indicator | `—` or `Slice A`–`Slice H` | The slice currently holding TX privileges. Updates automatically when the TX slice changes. No persisted setting. |

## Tips

- The indicators update in real time. If you reassign a slice to a different DAX channel on the radio, the label changes immediately without any manual refresh.
- A channel showing `—` carries no audio. If you expect audio on a channel and see `—`, assign a DAX channel to the relevant slice from the radio or from the slice controls in AetherSDR.

## Related

- [DAX Audio overview](overview.md)
- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Identify which slice is the TX slice](identify-which-slice-is-the-tx-slice.md)
- [Set DAX RX gain per channel](set-dax-rx-gain-per-channel.md)
