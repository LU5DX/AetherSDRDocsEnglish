# Freeze the analyzer peak-hold trace to spot resonances while tuning

The peak-hold trace marks the highest energy level observed at each frequency since the last reset. Freezing it stops the normal ~10 dB/sec decay so the trace stays stationary while you adjust EQ bands or passband edges — making it easier to identify resonances and harsh peaks.

## Before you start

- Open the floating editor for the TX or RX EQ side. The `Peak Hold` button is in the editor header strip only — it is not available on the docked applet tile. See [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md).
- Ensure audio is passing through the EQ path so the live FFT analyzer is active and the peak-hold trace is accumulating data.

## Steps

1. Open the floating editor for the side you want to inspect (TX or RX) by double-clicking the EQ stage in the CHAIN widget.
2. Let audio run for a few seconds so the peak-hold trace builds up across the frequency range.
3. Click `Peak Hold` in the editor header strip. The button turns amber to confirm it is checked.
4. Adjust your EQ bands, filter cutoffs, or other settings while reading the frozen trace. The trace remains stationary regardless of current signal level.
5. Click `Peak Hold` again to uncheck it. The trace resumes normal decay (~10 dB/sec).

## What each control does

| Control | Location | Default | Behavior | Persisted key |
|---|---|---|---|---|
| `Peak Hold` | Editor header strip | Unchecked | When checked, freezes the per-bin peak-hold trace at the highest level observed at each frequency. No decay occurs until toggled off. Amber background when checked. | — (not persisted) |
| `Smoothing` | Editor header strip | `Off (1/96)` | Fractional-octave power-averaging applied to the analyzer display only. Options: `Off (1/96)`, `1/24`, `1/12`, `1/6`, `1/3`. Lower fraction = smoother. Does not affect the peak-hold trace bins or EQ math. | `ClientEqSmoothingFraction` |

## Tips

- The peak-hold trace tracks raw frequency bins even when display smoothing (`Smoothing` combo) is set to a coarse value such as `1/3`. If a resonance appears in the frozen trace but looks rounded at a coarse smoothing setting, switch `Smoothing` to `Off (1/96)` to see the full bin-level detail.
- To clear the accumulated peak data without toggling `Peak Hold` off and on, uncheck then immediately recheck the button after a moment of silence or reduced signal.
- The dashed yellow filter cutoff guide lines remain draggable while `Peak Hold` is active. This lets you align the radio passband edges directly to features visible on the frozen trace.

## Troubleshooting

- **`Peak Hold` button is not visible** — The button is in the floating editor only, not in the docked `Aetherial TX EQ` or `Aetherial RX EQ` applet tile. Open the floating editor by double-clicking the EQ stage in the CHAIN widget.
- **Trace decays immediately after clicking `Peak Hold`** — Confirm the button shows an amber background, which indicates it is checked. A single click that registers as a double-click may toggle the button back off. Click once firmly and verify the amber state.

## Related

- [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md)
- [Smooth the analyzer display for easier reading with the Smoothing combo](smooth-the-analyzer-display-for-easier-reading-with-the-smoothing-combo.md)
- [Drag the TX or RX filter cutoff guide line to move the radio passband](drag-the-tx-or-rx-filter-cutoff-guide-line-to-move-the-radio-passband.md)
- [Inspect the TX EQ curve and live spectrum](inspect-the-tx-eq-curve-and-live-spectrum.md)
- [Inspect the RX EQ curve and live spectrum](inspect-the-rx-eq-curve-and-live-spectrum.md)
