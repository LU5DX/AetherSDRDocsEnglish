# See which slice is currently using each DAX channel

The DAX Audio applet shows a per-channel indicator next to each DAX channel and the TX row, letting you confirm at a glance which slice is routed to which channel without opening any additional dialog.

## Before you start

- AetherSDR must be connected to the radio. The slice-assignment indicators are not populated when no radio is connected.
- The DAX applet must be visible. It is hidden by default.

## Steps

1. Click the `DAX` tray button on the right sidebar to open the DAX Audio applet.
2. Look at the label to the right of each channel name (`DAX 1:` through `DAX 4:` and `TX:`).
3. Read the indicator for each channel:
   - `—` means no slice is currently assigned to that channel.
   - `Slice A` through `Slice H` means that slice is routed to the channel.

No further action is required. The indicators update automatically whenever a slice's DAX channel assignment changes.

## What each control does

| Indicator | Location | Possible values | Persisted setting |
|---|---|---|---|
| Slice-assignment status | Next to `DAX 1:` – `DAX 4:` | `—` or `Slice A`–`Slice H` | none |
| TX assignment status | Next to `TX:` | `—` or `Slice A`–`Slice H` | none |

The RX indicators reflect which slice has been assigned to each DAX channel on the radio. The TX indicator reflects which slice currently holds TX privileges; that slice drives the DAX TX stream.

## Tips

- A channel showing `—` will carry no audio even if its gain slider is set above zero. If you expect audio on a channel but see `—`, assign the slice to that DAX channel from the slice controls.
- The TX indicator changes automatically when you move TX between slices. You do not need to reopen the applet.

## Related

- [DAX Audio overview](overview.md)
- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Identify which slice is the TX slice](identify-which-slice-is-the-tx-slice.md)
- [Set DAX RX gain per channel](set-dax-rx-gain-per-channel.md)
