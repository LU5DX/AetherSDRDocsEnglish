# Understanding Slices and VFOs

A slice is an independent receive (and optionally transmit) channel running inside a single panadapter on the FLEX-8600. Understanding how slices map to VFOs helps you navigate AetherSDR's controls and work multiple signals simultaneously.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. Slice controls are not available offline.
- Familiarize yourself with the Applet Panel on the right sidebar. The RX Controls applet (toggle with the RX tray button) is where per-slice settings live.

## How slices and VFOs work

The FLEX-8600 supports up to eight simultaneous slices, labeled A through H. Each slice is an independent receiver with its own:

- **VFO frequency** — shown in the Frequency label in the RX Controls applet, formatted as dotted MHz groups (for example, `14.225.000`).
- **Mode** — USB, LSB, CW, AM, FM, and others selectable from the Mode combo.
- **Filter passband** — a lo/hi pair you can set with filter width presets or by dragging the Filter passband widget edges.
- **Antenna assignment** — separate RX and TX antenna selectors.
- **Audio controls** — AF gain, L/R pan, squelch, AGC, RIT, and XIT, all independent per slice.

One slice at a time is the **TX slice** — the one that transmits when you key up. The TX badge in the RX Controls applet identifies and sets the TX slice.

Slices appear as overlaid markers on the panadapter spectrum/waterfall. Each slice is color-coded; the Slice badge (A, B, C …) in the RX Controls applet uses the same color as the corresponding marker on the panadapter.

## Switching between slices

The RX Controls applet shows a row of **Slice tabs (A..H)** at the top when more than one slice exists. Click a tab to bind the applet to that slice. All controls below the tab row — frequency, mode, filter, AGC, RIT/XIT, and so on — then apply to the selected slice.

The row is hidden when only one slice is active.

## The TX slice

Only one slice transmits at a time. Click the **TX (badge)** button in the RX Controls applet for the slice you want to transmit on. The TX badge lights to indicate that slice is active for transmit. Changing the TX slice does not affect any slice's receive frequency or settings.

## Frequency and the VFO readout

The **Frequency label** displays the slice's current VFO frequency. Click it to enter edit mode; type an MHz value and press Enter to tune and re-center the panadapter on that frequency. The field accepts values from 0.001 to 54.000 MHz (up to 450.000 MHz when the slice is on a transverter antenna).

The **STEP** spinbox controls how much the frequency moves per scroll-wheel tick or per click of the `<` / `>` arrows. The default step is 100 Hz. Available steps depend on the active mode — for example, SSB offers 1, 10, 50, 100, 500, 1000, 2000, and 3000 Hz steps.

## RIT and XIT

Two incremental offsets let you shift receive or transmit independently without touching the main VFO:

- **RIT** (Receive Incremental Tuning) — shifts only the receive frequency. Enable it with the RIT toggle button; adjust with the RIT offset spinbox in 10 Hz steps; zero it with RIT 0.
- **XIT** (Transmit Incremental Tuning) — shifts only the transmit frequency. Enable it with the XIT toggle button; adjust with the XIT offset spinbox in 10 Hz steps; zero it with XIT 0.

Both default to +0 Hz.

## Locking a slice

The 🔓 / 🔒 toggle button locks the slice against frequency changes. When locked (🔒), the slice ignores tuning input — useful when you want to monitor a fixed frequency while working another slice. Click again to unlock (🔓).

## Panadapter relationship

Each panadapter displays the spectrum around one or more slices. The **Slice title** indicator at the top of each panadapter panel shows which slice it is bound to (for example, `Slice A`). In multi-slice mode you can click the spectrum/waterfall area to activate a different panadapter. The **Pan Follows VFO** option (`View > Pan Follows VFO`, on by default) keeps the active slice's VFO marker visible as you tune.

## Related

- [Switch between multiple slices using the A..H tab row](../../features/rx/switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [Tune the radio to a frequency (type MHz in the readout)](../../features/rx/tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Change mode (USB, LSB, CW, AM, FM, etc.)](../../features/rx/change-mode-usb-lsb-cw-am-fm-etc.md)
- [Lock the slice to prevent accidental retuning](../../features/rx/lock-the-slice-to-prevent-accidental-retuning.md)
- [Use RIT to offset the receive frequency for a drifting station](../../features/rx/use-rit-to-offset-the-receive-frequency-for-a-drifting-station.md)
- [Use XIT to offset the transmit frequency without changing RX](../../features/rx/use-xit-to-offset-the-transmit-frequency-without-changing-rx.md)
- [Click the spectrum to activate a panadapter (multi-slice mode)](../../features/panadapter/click-the-spectrum-to-activate-a-panadapter-multi-slice-mode.md)
- [RX Controls overview](../../features/rx/overview.md)
- [Panadapter overview](../../features/panadapter/overview.md)
- [Make your first QSO with AetherSDR](../tutorials/first-qso.md)
