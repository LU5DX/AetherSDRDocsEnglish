# Use XIT to offset the transmit frequency without changing RX

XIT (Transmit Incremental Tuning) shifts your transmit frequency by a fixed Hz offset while leaving the receive frequency unchanged. This is useful for working split-frequency DX stations or compensating for a transceiver whose TX frequency needs to be nudged without retuning the VFO.

## Before you start

- AetherSDR must be connected to the radio. The RX applet requires an active radio connection.
- Select the slice you want to work with using the slice tabs (A..H) in the RX applet.

## Steps

1. Open the RX Controls applet by clicking the **RX** tray button on the right sidebar, if it is not already visible.
2. Scroll to the XIT row near the bottom of the applet.
3. Click **XIT** to enable Transmit Incremental Tuning. The button lights up when active.
4. Adjust the XIT offset using the **<** and **>** buttons on either side of the **XIT offset** spinbox, or use the mouse wheel over the spinbox. Each step moves the TX frequency by 10 Hz.
5. To return the TX offset to zero without disabling XIT, click **XIT 0**.
6. To disable XIT entirely, click **XIT** again to toggle it off.

## What each control does

| Control | Default | Valid range / step | Behavior |
|---|---|---|---|
| **XIT** | Off | On / Off | Enables or disables Transmit Incremental Tuning. |
| **XIT offset** | +0 Hz | Steps of 10 Hz | Sets the TX frequency offset relative to the VFO. Adjust with **<** / **>** or mouse wheel. |
| **XIT 0** | — | — | Immediately zeros the XIT offset. |

## Tips

- XIT and RIT are independent. You can run both simultaneously: RIT shifts what you hear, XIT shifts what you transmit.
- Because each step is 10 Hz, hold down **<** or **>** or spin the mouse wheel continuously to reach larger offsets quickly.
- If you switch slices using the A..H tabs, XIT state is per-slice. Check that XIT is set correctly on each slice you use for transmitting.

## Troubleshooting

- **XIT button appears but offset has no effect on transmit** — Confirm that the slice you adjusted is the active TX slice. Click the **TX (badge)** button in the RX applet header to set this slice as the TX slice, then verify the XIT offset is non-zero.
- **XIT offset resets unexpectedly** — Check whether a logging application or CAT controller is resending frequency commands that overwrite the offset.

## Related

- [Use RIT to offset the receive frequency for a drifting station](use-rit-to-offset-the-receive-frequency-for-a-drifting-station.md)
- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)
