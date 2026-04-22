# See which slice is currently using each DAX channel

The DAX Audio applet shows a per-channel status indicator next to each DAX channel row. Use it to confirm which slice is currently routed to DAX 1–4 and which slice holds TX privileges, without opening any additional dialogs.

## Before you start

- AetherSDR must be connected to the radio. The indicators update from live radio state and show `—` when no connection is present.
- The DAX applet must be visible. It is hidden by default.

## Steps

1. Click the **DAX** tray button on the right sidebar to open the DAX Audio applet.
2. Read the status indicator to the right of each channel label:
   - **DAX 1:** through **DAX 4:** — each shows either `—` (no slice assigned) or `Slice A` through `Slice H` (the slice currently routed to that channel).
   - **TX:** — shows `—` or the letter of the slice currently holding TX privileges.

No further action is required. The indicators update automatically whenever slice DAX assignments or the TX slice changes.

## What each control does

| Indicator | Location | Possible values | Meaning |
|---|---|---|---|
| Slice-assignment status (DAX 1) | Right of "DAX 1:" label | `—`, `Slice A`–`Slice H` | The slice routed to DAX channel 1, if any. |
| Slice-assignment status (DAX 2) | Right of "DAX 2:" label | `—`, `Slice A`–`Slice H` | The slice routed to DAX channel 2, if any. |
| Slice-assignment status (DAX 3) | Right of "DAX 3:" label | `—`, `Slice A`–`Slice H` | The slice routed to DAX channel 3, if any. |
| Slice-assignment status (DAX 4) | Right of "DAX 4:" label | `—`, `Slice A`–`Slice H` | The slice routed to DAX channel 4, if any. |
| TX assignment status | Right of "TX:" label | `—`, `Slice A`–`Slice H` | The slice currently holding TX privileges (drives the DAX TX stream). |

None of these indicators have a persisted setting key. They are read-only and reflect live radio state.

## Tips

- If all indicators show `—` and the radio is connected, no slices have a DAX channel assigned. Assign a DAX channel to a slice from the slice controls in the main window.
- The TX indicator and the RX channel indicators update independently. A slice can appear in both if it is the TX slice and also has a DAX RX channel assigned.

## Related

- [DAX Audio overview](overview.md)
- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Identify which slice is the TX slice](identify-which-slice-is-the-tx-slice.md)
- [Set DAX RX gain per channel](set-dax-rx-gain-per-channel.md)
