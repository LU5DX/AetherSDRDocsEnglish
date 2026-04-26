# Use XIT to offset the transmit frequency without changing RX

XIT (Transmit Incremental Tuning) shifts the transmit frequency by a fixed amount while leaving the receive frequency unchanged. This is useful when you need to transmit slightly off your receive VFO — for example, to work a split pile-up or compensate for a transceiver offset at the other station.

## Before you start

- AetherSDR must be connected to the radio. The RX Controls applet requires an active radio connection.
- The RX applet must be visible. If it is not, click the RX tray button on the right sidebar to show it.
- Select the correct slice using the slice tabs (A..H) if you have more than one slice active.

## Steps

1. Open the RX applet by clicking the RX tray button on the right sidebar if it is not already visible.
2. Scroll down to the XIT row near the bottom of the applet.
3. Click XIT to enable Transmit Incremental Tuning. The button highlights when active.
4. Adjust the XIT offset using the XIT offset spinbox:
   - Click `<` to decrease the offset in 10 Hz steps.
   - Click `>` to increase the offset in 10 Hz steps.
   - Scroll the mouse wheel over the spinbox to change the offset in 10 Hz steps.
5. To return the TX frequency to the RX frequency, click XIT 0. This zeroes the offset without turning XIT off.
6. To disable XIT entirely, click XIT again to toggle it off.

## What each control does

| Control | Default | Valid range / step | Behavior |
|---|---|---|---|
| XIT | Off (unchecked) | On / Off | Toggles Transmit Incremental Tuning on or off. |
| XIT offset | +0 Hz | Step: 10 Hz | Sets the TX frequency offset relative to the RX VFO. Adjust with `<` / `>` or the mouse wheel. |
| XIT 0 | — | — | Immediately zeroes the XIT offset. Does not turn XIT off. |

## Tips

- RIT and XIT are independent. You can run both simultaneously: RIT shifts what you hear, XIT shifts where you transmit.
- The XIT offset spinbox responds to the mouse wheel when the cursor is positioned over it, which is convenient when operating without moving focus away from the panadapter.
- If the slice is tune-locked (🔒), frequency-related controls are suppressed. Unlock the slice first if XIT controls do not respond.

## Troubleshooting

- **XIT offset spinbox has no effect** — Confirm XIT is enabled (button should be highlighted). If the slice is locked, click the 🔓 / 🔒 toggle to unlock it first.
- **TX frequency does not shift as expected** — Verify this slice is the active TX slice. Check that the TX (badge) button is active for this slice; only the TX slice uses the XIT offset on transmit.

## Related

- [Use RIT to offset the receive frequency for a drifting station](use-rit-to-offset-the-receive-frequency-for-a-drifting-station.md)
- [RX Controls overview](overview.md)
- [Lock the slice to prevent accidental retuning](lock-the-slice-to-prevent-accidental-retuning.md)
- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
