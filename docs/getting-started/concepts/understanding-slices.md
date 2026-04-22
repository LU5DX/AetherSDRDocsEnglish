# Understanding Slices and VFOs

A slice is an independent receive (and optionally transmit) channel within a single panadapter. Understanding how slices and VFOs relate to each other helps you use AetherSDR's multi-channel capability without confusion.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. Slice controls are unavailable without a radio connection.
- The RX Controls applet must be visible. If it is not, click the RX tray button on the right sidebar to show it.

## What a slice is

The FLEX-8600 can run up to eight simultaneous receive channels inside one or more panadapters. Each channel is called a **slice** and is identified by a letter: A through H. Every slice has its own:

- VFO frequency (shown in the **Frequency label** in the RX Controls applet)
- Receive mode (USB, LSB, CW, AM, SAM, FM, NFM, DFM, DIGU, DIGL, RTTY)
- Filter passband
- AGC, AF gain, squelch, RIT, and XIT settings
- RX and TX antenna assignment

The slice letter appears in the **Slice badge** indicator at the top of the RX Controls applet, colored to match that slice's identity.

## What a VFO is

In AetherSDR, the VFO is the frequency assigned to a slice. There is no separate "VFO A / VFO B" concept distinct from slices. Each slice carries its own VFO. Slice A's frequency is VFO A; Slice B's frequency is VFO B, and so on.

The current VFO frequency is displayed in the **Frequency label** (format: `0.000.000`). Click the label to enter edit mode, type a frequency in MHz, and press Enter to tune that slice's VFO to the new frequency.

## How slices relate to panadapters

Each panadapter displays a segment of spectrum. Slices appear as markers within that panadapter's frequency range. The **Slice title** indicator at the top of each panadapter (for example, `Slice A`) shows which slice is bound to that view.

In single-slice mode only one slice is active and its panadapter fills the main window. In multi-slice mode, additional slices can share the same panadapter or occupy separate ones. The ⬈ (pop-out), □ (maximize), and × (close) buttons in each panadapter title bar are available only in multi-pan layouts.

## Switching between slices

The **Slice tabs (A..H)** row at the top of the RX Controls applet shows one tab per active slice. Click a tab to bind the RX Controls applet to that slice. The tab row is hidden when the radio is running only one slice.

Only one slice at a time is the TX slice. Click the **TX (badge)** button in the RX Controls applet for a given slice to make that slice the transmit channel.

## Locking a slice VFO

To prevent a slice from being retuned accidentally, click the 🔓 button in the RX Controls applet. The icon changes to 🔒 and the slice ignores frequency changes until you click it again to unlock.

## Tips

- RIT offsets the receive frequency of the active slice without moving its VFO. XIT offsets the transmit frequency without changing receive. Both adjustments are per-slice and are independent across slices.
- The **L / R pan** slider (default 50, center) lets you place each slice's audio in a different position in the stereo field when monitoring multiple slices simultaneously. Double-click the slider to reset it to center.
- Slice step size is per-mode. For example, SSB steps are 1, 10, 50, 100, 500, 1000, 2000, and 3000 Hz; CW steps are 1, 5, 10, 50, 100, 200, and 400 Hz. Cycle through them with the **STEP** `<` and `>` buttons or the mouse wheel.

## Related

- [Switch between multiple slices using the A..H tab row](../../features/rx/switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [Tune the radio to a frequency (type MHz in the readout)](../../features/rx/tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Lock the slice to prevent accidental retuning](../../features/rx/lock-the-slice-to-prevent-accidental-retuning.md)
- [Use RIT to offset the receive frequency for a drifting station](../../features/rx/use-rit-to-offset-the-receive-frequency-for-a-drifting-station.md)
- [Use XIT to offset the transmit frequency without changing RX](../../features/rx/use-xit-to-offset-the-transmit-frequency-without-changing-rx.md)
- [Panadapter overview](../../features/panadapter/overview.md)
- [RX Controls overview](../../features/rx/overview.md)
- [Click the spectrum to activate a panadapter (multi-slice mode)](../../features/panadapter/click-the-spectrum-to-activate-a-panadapter-multi-slice-mode.md)
