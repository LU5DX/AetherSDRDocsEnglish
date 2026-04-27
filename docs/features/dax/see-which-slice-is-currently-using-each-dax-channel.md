# See which slice is currently using each DAX channel

The DAX Audio applet shows a slice-assignment indicator next to each DAX channel so you can confirm at a glance which slice is routed where without leaving the main window.

## Before you start

- AetherSDR must be connected to the radio. The slice-assignment indicators require a live radio connection.
- At least one slice must have a DAX channel assigned. If no slices are assigned, all indicators show `—`.

## Steps

1. Click the **DAX** tray button on the right sidebar to open the DAX Audio applet.
2. Look at the status label to the right of each channel label (**DAX 1:**, **DAX 2:**, **DAX 3:**, **DAX 4:**).
3. Read the indicator for each channel. It shows either `—` (no slice assigned) or `Slice A` through `Slice H` (the letter of the slice currently routed to that channel).
4. To see which slice is driving the DAX TX stream, read the status label on the **TX:** row. It follows the same format: `—` or `Slice A` through `Slice H`.

## What each control does

| Indicator | Location | Possible values | Persisted setting |
|---|---|---|---|
| Slice-assignment status (per channel) | Right of **DAX 1:** – **DAX 4:** labels | `—` or `Slice A`–`Slice H` | None |
| TX assignment status | Right of **TX:** label | `—` or `Slice A`–`Slice H` | None |

These indicators are read-only. They update automatically when a slice's DAX channel assignment changes. Slice-to-channel assignment is configured on the slice itself, not in this applet.

## Tips

- The indicators update in real time. If you change a slice's DAX channel assignment on the radio or in another part of the UI, the applet reflects the change immediately without requiring a manual refresh.
- A channel showing `—` means no slice is currently assigned to it; audio will not flow on that channel.

## Related

- [DAX Audio overview](overview.md)
- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Identify which slice is the TX slice](identify-which-slice-is-the-tx-slice.md)
- [Set DAX RX gain per channel](set-dax-rx-gain-per-channel.md)
