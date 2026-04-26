# Use RIT to offset the receive frequency for a drifting station

RIT (Receive Incremental Tuning) shifts only the receive frequency while leaving your transmit frequency unchanged. Use it when a station you are working drifts slightly off your dial frequency and you want to follow them without moving your VFO.

## Before you start

- AetherSDR must be connected to the radio. RIT is a per-slice control and requires an active slice.
- Open the RX Controls applet. If it is not visible, click the **RX** tray button on the right sidebar.

## Steps

1. In the RX Controls applet, click **RIT** to enable Receive Incremental Tuning. The button latches on.
2. Use the **<** and **>** buttons flanking the **RIT offset** spinbox, or scroll the mouse wheel over the spinbox, to shift the receive frequency. Each step moves 10 Hz.
3. Continue adjusting until the drifting station is centred in the passband.
4. To return to zero offset, click **RIT 0**.
5. To disable RIT entirely, click **RIT** again to unlatch it.

## What each control does

| Control | Behavior | Default |
|---|---|---|
| **RIT** | Toggle button. Enables or disables Receive Incremental Tuning for the active slice. | Off |
| **RIT offset** | Spinbox showing the current RIT offset in Hz. Adjust with **<** / **>** or the mouse wheel. | +0 Hz |
| **RIT 0** | Push button. Immediately zeroes the RIT offset without disabling RIT. | — |

## Tips

- RIT offset steps are fixed at 10 Hz per click or wheel detent. For larger corrections, click or scroll repeatedly.
- Clicking **RIT 0** zeroes the offset but leaves RIT enabled, so you can re-apply an offset without toggling the feature off and back on.
- If you need to offset the transmit frequency instead of the receive frequency, use **XIT** — its controls work the same way. See [Use XIT to offset the transmit frequency without changing RX](use-xit-to-offset-the-transmit-frequency-without-changing-rx.md).

## Troubleshooting

- **RIT button does not respond** — The slice may be locked. Check whether the lock icon (🔒) is shown in the applet header. If it is, click it to unlock the slice. See [Lock the slice to prevent accidental retuning](lock-the-slice-to-prevent-accidental-retuning.md).
- **Receive frequency does not shift when RIT is on** — Confirm the correct slice tab (A–H) is selected in the applet. RIT applies only to the slice the applet is currently bound to.

## Related

- [Use XIT to offset the transmit frequency without changing RX](use-xit-to-offset-the-transmit-frequency-without-changing-rx.md)
- [Lock the slice to prevent accidental retuning](lock-the-slice-to-prevent-accidental-retuning.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
