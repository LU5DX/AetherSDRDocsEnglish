# Understanding Slices and VFOs

A slice is an independent receive (and optionally transmit) channel within a single panadapter. Each slice has its own VFO frequency, mode, filter, and audio path. Understanding how slices map to VFOs helps you manage multiple simultaneous signals on the FLEX-8600.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The RX Controls applet must be visible. Toggle it with the RX tray button on the right sidebar.

## How slices work

The FLEX-8600 supports up to eight simultaneous slices, labelled A through H. Each slice is an independent receiver with its own:

- **VFO frequency** — shown in the Frequency label in the RX Controls applet.
- **Mode** — set with the Mode combo (USB, LSB, CW, AM, SAM, FM, NFM, DFM, DIGU, DIGL, RTTY).
- **Filter passband** — shown in the filter width indicator (for example, `2.7K`) and adjustable via the Filter passband widget or Filter width presets.
- **Audio path** — independent AF gain, L/R pan, and squelch controls.
- **AGC** — separate AGC mode and AGC threshold per slice.

Slices within a panadapter share the same FFT span, so all visible slices tune across the same portion of spectrum. You can see all active slice markers simultaneously on the Spectrum / waterfall display.

## The TX slice

Only one slice transmits at a time. That slice is the TX slice. The TX (badge) button in the RX Controls applet designates the current slice as the TX slice. The Frequency label for the TX slice determines what frequency you transmit on.

## Selecting and switching slices

The RX Controls applet shows a row of slice tabs labelled A through H (the row is hidden when only one slice is active). Click a tab to bind the applet to that slice. The Slice badge updates to reflect the letter of the currently bound slice.

In the panadapter, each slice appears as a separate marker on the Spectrum / waterfall. Clicking the spectrum activates the panadapter; in multi-slice mode, clicking near a slice marker tunes or selects that slice.

## RIT and XIT

RIT (Receive Incremental Tuning) shifts the receive frequency without moving the VFO. Enable it with the RIT toggle button and adjust the offset using the RIT offset spinbox (10 Hz steps). Click RIT 0 to zero the offset.

XIT (Transmit Incremental Tuning) shifts the transmit frequency without changing the receive frequency. Enable it with the XIT toggle button and adjust with the XIT offset spinbox (10 Hz steps). Click XIT 0 to zero the offset.

Both RIT and XIT default to `+0 Hz`.

## Locking a slice

The 🔓 / 🔒 toggle in the RX Controls applet locks the slice frequency. A locked slice ignores frequency changes from clicking the panadapter or external CAT commands. The icon switches between open and closed padlock to indicate the current state.

## Tips

- The Frequency label displays the VFO frequency with dotted grouping. Click it to enter edit mode and type a frequency in MHz, then press Enter to tune and re-center the panadapter. Press Escape to cancel and restore the previous frequency.
- If you have RIT active and the station sounds on-frequency but shows as off-center, zero the RIT with RIT 0 and retune.
- Double-clicking the L / R pan slider resets it to center (50).

## Related

- [Switch between multiple slices using the A..H tab row](../../features/rx/switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [Tune the radio to a frequency (type MHz in the readout)](../../features/rx/tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Change mode (USB, LSB, CW, AM, FM, etc.)](../../features/rx/change-mode-usb-lsb-cw-am-fm-etc.md)
- [Lock the slice to prevent accidental retuning](../../features/rx/lock-the-slice-to-prevent-accidental-retuning.md)
- [Use RIT to offset the receive frequency for a drifting station](../../features/rx/use-rit-to-offset-the-receive-frequency-for-a-drifting-station.md)
- [Use XIT to offset the transmit frequency without changing RX](../../features/rx/use-xit-to-offset-the-transmit-frequency-without-changing-rx.md)
- [Click the spectrum to activate a panadapter (multi-slice mode)](../../features/panadapter/click-the-spectrum-to-activate-a-panadapter-multi-slice-mode.md)
- [RX Controls overview](../../features/rx/overview.md)
