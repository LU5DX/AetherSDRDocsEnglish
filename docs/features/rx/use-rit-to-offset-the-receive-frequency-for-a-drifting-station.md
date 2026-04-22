# Use RIT to offset the receive frequency for a drifting station

RIT (Receive Incremental Tuning) shifts only the receive frequency without moving your transmit frequency or VFO readout. Use it when a station you are working drifts slightly off your dial frequency and you want to follow them without retuning.

## Before you start

- AetherSDR must be connected to the radio. RIT controls are inactive without a radio connection.
- The RX Controls applet must be visible. If it is not, click the RX tray button on the right sidebar to show it.
- Select the slice you want to adjust using the slice tabs (A..H) at the top of the applet.

## Steps

1. In the RX Controls applet, scroll down to the RIT row.
2. Click RIT to enable Receive Incremental Tuning. The button activates.
3. Use the `<` and `>` buttons flanking the RIT offset spinbox, or roll the mouse wheel over it, to shift the receive frequency. Each step moves the offset by 10 Hz.
4. Read the current offset in the RIT offset spinbox. The default is `+0 Hz`.
5. To return to zero offset without disabling RIT, click RIT 0.
6. To turn RIT off entirely, click RIT again so the button is no longer active.

## What each control does

| Control | Kind | Default | Valid range / step | Behavior |
|---|---|---|---|---|
| RIT | Toggle button | Off | On / Off | Enables or disables Receive Incremental Tuning for the active slice. |
| RIT offset | Spinbox | +0 Hz | Step: 10 Hz | Sets the receive frequency offset. Adjust with `<` / `>` or the mouse wheel. |
| RIT 0 | Push button | — | — | Instantly zeroes the RIT offset without turning RIT off. |

## Tips

- RIT affects only the receive side. Your transmit frequency remains on the VFO frequency shown in the Frequency label.
- If you also need to offset the transmit frequency, use XIT independently. The two offsets are separate.
- To reset the offset and disable RIT in one action, click RIT 0 and then click RIT.

## Related

- [Use XIT to offset the transmit frequency without changing RX](use-xit-to-offset-the-transmit-frequency-without-changing-rx.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [RX Controls overview](overview.md)
