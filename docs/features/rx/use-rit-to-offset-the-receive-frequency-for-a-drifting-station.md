# Use RIT to offset the receive frequency for a drifting station

RIT (Receive Incremental Tuning) shifts only the receive frequency by a small offset, leaving the transmit frequency and the VFO dial unchanged. Use it when a station you are working has drifted slightly off your dial frequency.

## Before you start

- AetherSDR must be connected to the radio. RX Controls are unavailable without a radio connection.
- Open the RX Controls applet. If it is not visible, click the RX tray button on the right sidebar.
- Select the slice you want to adjust using the slice tabs (A..H) if more than one slice is active.

## Steps

1. In the RX Controls applet, click RIT to enable Receive Incremental Tuning. The button latches on.
2. Use the `<` and `>` arrows beside the RIT offset spinbox, or scroll the mousewheel over it, to adjust the offset. Each step moves the receive frequency by 10 Hz.
3. Continue adjusting until the drifting station is centred in the passband.
4. To return the receive frequency to zero offset, click RIT 0.
5. To turn RIT off entirely, click RIT again to deactivate it.

## What each control does

| Control | What it does | Default | Range/Step |
|---|---|---|---|
| RIT | Toggles Receive Incremental Tuning on/off. | Off | — |
| RIT offset | Sets the RIT offset in Hz. Adjust with `<` / `>` or mousewheel. | +0 Hz | Steps of 10 Hz |
| RIT 0 | Zeroes the RIT offset immediately without turning RIT off. | — | — |

## Tips

- RIT affects only the receive frequency. Your transmit frequency remains on the VFO dial, so your transmitted signal stays on the frequency the other station expects.
- Clicking RIT 0 clears the offset but leaves RIT enabled, so you can re-apply an offset without toggling the feature back on.
- The RIT offset spinbox has no documented hard limit in the catalog; use the smallest offset that brings the station into the passband rather than retuning the VFO.

## Troubleshooting

- **RIT has no audible effect** — Confirm that RIT is showing as active (button latched). If the slice is tune-locked (🔒 padlock shown), the lock may prevent frequency changes; click the padlock to unlock the slice first.
- **Offset jumps back to +0 Hz** — Clicking RIT 0 is a one-shot action that always resets to zero. If you want to hold an offset, do not click RIT 0.

## Related

- [Use XIT to offset the transmit frequency without changing RX](use-xit-to-offset-the-transmit-frequency-without-changing-rx.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Lock the slice to prevent accidental retuning](lock-the-slice-to-prevent-accidental-retuning.md)
- [RX Controls overview](overview.md)
