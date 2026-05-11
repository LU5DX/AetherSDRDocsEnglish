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

## AF gain and pan

Adjust the **AF gain** slider (0–100) to set the slice audio output volume. Use the **L / R pan** slider (0–100) to position the slice audio in the stereo field: 0 is full left, 50 is centre, 100 is full right. Double-click the pan slider to reset to centre.

## Squelch

Enable the squelch by clicking the **SQL** button, then adjust the **Squelch level** slider (0–100) to set the threshold. The squelch only takes effect when SQL is toggled on.

## AGC

Select the AGC mode from the **AGC mode** combo box: Off, Slow, Med, or Fast. The **AGC threshold** slider adjusts the AGC threshold level. When AGC mode is Off, the slider sets the off-level instead. The mode combo is hidden in FM family modes (FM, NFM, DFM).

## FM repeater duplex

When operating in FM, NFM, or DFM mode, the FM duplex controls appear:

- **Tone mode (FM)** — Select "CTCSS TX" to enable CTCSS tone transmission.
- **CTCSS tone value** — Select the CTCSS tone frequency from 41 standard EIA/TIA-603 tones (67.0 Hz to 254.1 Hz). Only enabled when Tone mode is set to CTCSS TX.
- **Offset (FM)** — Set the repeater offset frequency (0.0–100.0 MHz in 0.1 MHz steps).
- **− (offset down)** — Click to set TX frequency below RX.
- **Simplex** — Click to set TX frequency equal to RX (default).
- **+ (offset up)** — Click to set TX frequency above RX.
- **REV** — Click to invert the TX offset sign for a reversed repeater pair.

## Filter width presets

Click a **Filter width presets** button to apply a preset filter width. Right-click a preset button to save the current filter width as a preset. Presets are per-mode and hidden for FM/NFM/DFM modes.

The **Filter width label** indicator displays the current filter bandwidth (e.g., "2.7K", "3.3K", "500", "6.0K"). The filter width readout is shared with the VFO panel for consistent display.

Use the **Filter passband widget** to drag the low and high edges and adjust the filter passband manually.

## Step filter width

Use the **Widen** and **Narrow** commands to step through the per-mode filter preset list. Each press moves to the next wider or narrower preset in the list. The command walks the per-mode preset list so it always produces mode-correct passband edges.

## Mute

Click the 🔊 / 🔇 button to mute or unmute the slice audio output.

## QSK indicator

The **QSK** indicator lights amber when CW break-in (QSK) is active. This is read-only and controlled via the CW applet Breakin button.

## SWR sweep overlay

V0.9.4 adds a SWR sweep overlay that draws SWR versus frequency data directly on the panadapter spectrum. When a sweep is active, each data point maps its frequency (in MHz) to a horizontal position on the spectrum and plots the corresponding SWR value as a line overlay. The overlay is drawn on both the GPU-accelerated and software-rendered painting paths.

The overlay has three states:

| State             | Description                                                                                                                                           | Notes |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| No data           | Overlay is not drawn. Call `clearSwrSweepPoints()` to return to this state.                                                                           |       |
| Sweep in progress | Overlay is drawn and a cursor marks the current sweep frequency. Set `running = true` and supply `currentFreqMhz` when calling `setSwrSweepPoints()`. |       |
| Sweep complete    | Overlay is drawn without a cursor marker. Set `running = false` when calling `setSwrSweepPoints()`.                                                   |       |

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
- The **AF gain** and **L / R pan** sliders have a default value of 70 and 50 (centre) respectively.
- The **Squelch level** default is 20.
- The **AGC threshold** default is 65.

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
<!-- docmesh:llm version=v0.9.8 date=2026-06-01 -->