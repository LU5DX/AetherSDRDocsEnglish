The diff shows only internal implementation details of the SWR sweep overlay — the rendering functions, positioning logic, and drawing code. The user-facing behavior, API, and documentation for the SWR sweep overlay is already fully and accurately described in the current documentation (which already references v0.9.4 and documents `setSwrSweepPoints()`, `clearSwrSweepPoints()`, `SwrSweepPoint`, all parameters, and all three overlay states). The catalog entry shows `VfoPos` struct with no controls. No user-visible documentation change is warranted.

# Understanding Slices and VFOs

In AetherSDR, a slice is an independent receiver within a panadapter. Each slice has its own VFO frequency, mode, filter, and audio settings. The FLEX-8600 supports up to eight simultaneous slices (labeled A through H), letting you monitor multiple frequencies at once within the same or different panadapters.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. Slices only exist when a radio connection is active.
- The RX Controls applet must be visible. If it is not, click the **RX** tray button on the right sidebar.

## How slices work

Each slice is a fully independent receive channel. It has:

- A **VFO frequency** — the center tuning frequency for that slice, shown in the **Frequency label** in the RX Controls applet.
- A **mode** — USB, LSB, CW, AM, SAM, FM, NFM, DFM, DIGU, DIGL, or RTTY — set with the **Mode combo**.
- A **filter passband** — adjustable via filter width presets or by dragging the **Filter passband widget**.
- Its own **AF gain**, **AGC**, **squelch**, **RIT**, and **XIT** settings.
- Assigned RX and TX antennas.

A slice is always bound to a panadapter. The panadapter shows the FFT spectrum for the slice's band segment, and the slice's VFO marker appears as a line on that spectrum.

## Slices and the panadapter

The panadapter's **Spectrum / waterfall** display shows the slice's current VFO position. Clicking or dragging on the spectrum tunes the active slice. The panadapter title bar shows which slice is bound to it (for example, **Slice A**).

In multi-slice mode, each panadapter can contain one or more slice markers. Clicking the spectrum of a different panadapter activates that panadapter and its associated slice.

## Switching between slices

The RX Controls applet shows a row of tabs labeled **A** through **H** (up to the radio's maximum slice count). Click a tab to bind the RX Controls applet to that slice. The **Slice badge** indicator in the applet updates to show the active slice letter, colored by slice identity.

The tab row is hidden when only one slice is in use.

## The TX slice

Only one slice transmits at a time. The currently transmitting slice is the TX slice. To make a slice the TX slice, click its **TX (badge)** button in the RX Controls applet. This routes transmit through that slice's frequency, mode, and TX antenna.

## RIT and XIT

RIT (Receive Incremental Tuning) offsets the receive frequency without moving the VFO. Enable it with the **RIT** button; adjust with the **RIT offset** spinbox (10 Hz steps); reset with **RIT 0**.

XIT (Transmit Incremental Tuning) offsets the transmit frequency without changing the receive frequency. Enable it with the **XIT** button; adjust with the **XIT offset** spinbox (10 Hz steps); reset with **XIT 0**.

Both are independent per slice.

## Locking a slice

To prevent accidental retuning, click the 🔓 button in the RX Controls applet. The icon changes to 🔒 and the slice ignores frequency changes until unlocked.

## SWR sweep overlay

V0.9.4 adds a SWR sweep overlay that draws SWR versus frequency data directly on the panadapter spectrum. When a sweep is active, each data point maps its frequency (in MHz) to a horizontal position on the spectrum and plots the corresponding SWR value as a line overlay. The overlay is drawn on both the GPU-accelerated and software-rendered painting paths.

The overlay has three states:

| State | Description |
|-------|-------------|
| No data | Overlay is not drawn. Call `clearSwrSweepPoints()` to return to this state. |
| Sweep in progress | Overlay is drawn and a cursor marks the current sweep frequency. Set `running = true` and supply `currentFreqMhz` when calling `setSwrSweepPoints()`. |
| Sweep complete | Overlay is drawn without a cursor marker. Set `running = false` when calling `setSwrSweepPoints()`. |

An optional source label (for example, the name of the antenna tuner or analyser providing the data) can be passed via the `sourceLabel` parameter and is displayed on the overlay.

To update the overlay, call `setSwrSweepPoints()` with a vector of `SwrSweepPoint` values. Each point carries:

- `freqMhz` — frequency of the measurement, in MHz (default `0.0`).
- `swr` — SWR value at that frequency (default `1.0`).

Points with non-finite `freqMhz` or `swr` values are silently skipped. Points whose mapped x-coordinate falls outside the visible spectrum area are not drawn.

To remove the overlay, call `clearSwrSweepPoints()`.

## Tips

- The **Frequency label** displays the VFO frequency with dotted grouping (for example, `14.225.000`). Click it to enter edit mode and type a frequency in MHz, then press Enter to tune and re-center the panadapter.
- The **STEP** spinbox controls how far the VFO moves per scroll-wheel click or per press of the **<** / **>** buttons. Step sizes are per-mode — for example, SSB steps are 1, 10, 50, 100, 500, 1000, 2000, or 3000 Hz; CW steps are 1, 5, 10, 50, 100, 200, or 400 Hz.
- The default step size is 100 Hz (index 2 in the per-mode list).
- Pressing Escape in the frequency edit field cancels the entry, restores the previous frequency, and dismisses the editor.

## Related

- [RX Controls overview](../../features/rx/overview.md)
- [Switch between multiple slices using the A..H tab row](../../features/rx/switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [Tune the radio to a frequency (type MHz in the readout)](../../features/rx/tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Lock the slice to prevent accidental retuning](../../features/rx/lock-the-slice-to-prevent-accidental-retuning.md)
- [Use RIT to offset the receive frequency for a drifting station](../../features/rx/use-rit-to-offset-the-receive-frequency-for-a-drifting-station.md)
- [Use XIT to offset the transmit frequency without changing RX](../../features/rx/use-xit-to-offset-the-transmit-frequency-without-changing-rx.md)
- [Click the spectrum to activate a panadapter (multi-slice mode)](../../features/panadapter/click-the-spectrum-to-activate-a-panadapter-multi-slice-mode.md)
- [Panadapter overview](../../features/panadapter/overview.md)
- [Make your first QSO with AetherSDR](../tutorials/first-qso.md)
<!-- docmesh:llm version=v0.9.4 date=2026-05-01 -->