# Understanding Slices and VFOs

A slice is an independent receive (and optionally transmit) channel within a panadapter. Understanding how slices and VFOs relate is the foundation for using AetherSDR effectively — every tuning, mode, and filter operation acts on a specific slice.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The RX Controls applet must be visible. If it is not, click the RX tray button on the right sidebar.

## What a slice is

The FLEX-8600 can run up to eight simultaneous receive slices, labeled A through H. Each slice is an independent radio channel with its own:

- VFO frequency
- Mode (USB, LSB, CW, AM, SAM, FM, NFM, DFM, DIGU, DIGL, RTTY)
- Filter passband
- RX and TX antenna assignment
- AGC, AF gain, squelch, RIT, and XIT settings

Each slice occupies a segment of the spectrum covered by its panadapter. In the Panadapter, the Slice title indicator shows which slice is bound to that view — for example, "Slice A".

## What the VFO is

The VFO is the tuned frequency of a slice. In the RX Controls applet, the Frequency label displays the current VFO frequency with dotted grouping (for example, `14.225.000`). Clicking the Frequency label switches it to the Frequency edit field, where you can type a frequency in MHz and press Enter to retune.

There is one VFO per slice. Slices are independent: tuning Slice A does not affect Slice B.

## Slices and the RX Controls applet

The RX Controls applet is bound to one slice at a time. The Slice badge (A, B, C, D, E, F, G, H) in the applet header shows which slice the controls currently affect. When more than one slice is active, a row of Slice tabs (A..H) appears at the top of the applet. Click a tab to bind the applet to that slice.

All controls in the applet — mode, frequency, filter width, AGC, AF gain, squelch, RIT, XIT — operate on the slice currently shown in the Slice badge.

## The TX slice

Only one slice transmits at a time. The TX badge in the RX Controls applet marks which slice is the TX slice. Click TX on any slice to make it the transmitting slice.

## Tune-lock

To prevent accidental retuning of a slice, click the 🔓 button in the RX Controls applet. The icon changes to 🔒 and the slice ignores frequency changes until you unlock it.

## Slices and panadapters

Each panadapter displays the spectrum and waterfall for its associated slice. In a multi-slice layout, each panadapter has its own title bar showing "Slice A", "Slice B", and so on. Clicking the spectrum or waterfall of a panadapter activates that panadapter's slice.

## RIT and XIT

RIT (Receive Incremental Tuning) offsets the receive frequency of the active slice without changing the displayed VFO. XIT (Transmit Incremental Tuning) offsets the transmit frequency without changing the RX frequency. Both are independent per slice and adjustable in 10 Hz steps using the RIT offset and XIT offset spinboxes.

## Tips

- The Slice tabs row is hidden when only one slice is active, because there is nothing to switch between.
- Double-clicking the L / R pan slider resets it to 50 (centre).
- The STEP spinbox cycles through per-mode step sizes. For SSB the steps are 1, 10, 50, 100, 500, 1000, 2000, and 3000 Hz. For CW the steps are 1, 5, 10, 50, 100, 200, and 400 Hz. The default step is 100 Hz.

## Related

- [Switch between multiple slices using the A..H tab row](../../features/rx/switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [Tune the radio to a frequency (type MHz in the readout)](../../features/rx/tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Change mode (USB, LSB, CW, AM, FM, etc.)](../../features/rx/change-mode-usb-lsb-cw-am-fm-etc.md)
- [Lock the slice to prevent accidental retuning](../../features/rx/lock-the-slice-to-prevent-accidental-retuning.md)
- [Use RIT to offset the receive frequency for a drifting station](../../features/rx/use-rit-to-offset-the-receive-frequency-for-a-drifting-station.md)
- [Use XIT to offset the transmit frequency without changing RX](../../features/rx/use-xit-to-offset-the-transmit-frequency-without-changing-rx.md)
- [Click the spectrum to activate a panadapter (multi-slice mode)](../../features/panadapter/click-the-spectrum-to-activate-a-panadapter-multi-slice-mode.md)
- [Make your first QSO with AetherSDR](../tutorials/first-qso.md)
