# Use XIT to offset the transmit frequency without changing RX

XIT (Transmit Incremental Tuning) shifts your transmit frequency by a fixed offset while leaving the receive frequency unchanged. This is useful when working split, answering a DX station on a slightly different frequency, or compensating for a transceiver on the other end that is slightly off.

## Before you start

- AetherSDR must be connected to the radio. XIT controls are unavailable without an active radio connection.
- Open the RX Controls applet by clicking the RX tray button on the right sidebar if it is not already visible.
- Select the slice you want to work on using the slice tabs (A..H) at the top of the applet.

## Steps

1. In the RX Controls applet, locate the XIT row near the bottom of the applet, below the RIT row.
2. Click XIT to enable transmit incremental tuning. The button lights up when active.
3. Adjust the XIT offset using the XIT offset spinbox:
   - Click `<` to decrease the offset in 10 Hz steps.
   - Click `>` to increase the offset in 10 Hz steps.
   - Scroll the mouse wheel over the spinbox to change the offset in 10 Hz steps.
4. Transmit. Your TX frequency will be shifted by the displayed XIT offset; the RX frequency and the panadapter VFO position remain unchanged.
5. To remove the offset without disabling XIT, click XIT 0. The offset resets to +0 Hz.
6. To disable XIT entirely, click XIT again so the button is no longer active.

## What each control does

| Control | What it does | Default | Step |
|---|---|---|---|
| XIT | Toggles transmit incremental tuning on or off. | Off | — |
| XIT offset | Sets the TX frequency offset in Hz. Adjusted with `<` / `>` or the mouse wheel. | +0 Hz | 10 Hz |
| XIT 0 | Resets the XIT offset to +0 Hz without turning XIT off. | — | — |

## Tips

- XIT and RIT are independent. You can run both at the same time to offset TX and RX separately on the same slice.
- The XIT offset adjusts in 10 Hz steps. For a large offset, hold the `>` or `<` button or spin the mouse wheel quickly.
- To zero the offset and disable XIT in one sequence, click XIT 0 then click XIT.

## Related

- [Use RIT to offset the receive frequency for a drifting station](use-rit-to-offset-the-receive-frequency-for-a-drifting-station.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
