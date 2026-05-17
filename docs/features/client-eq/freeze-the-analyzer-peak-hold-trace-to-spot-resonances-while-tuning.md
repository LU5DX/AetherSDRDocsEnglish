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

| Control                             | Location                                                                                                                                                                                                                                                                                                                                                                        | Default                                                                                                                                                                                                                           |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Peak Hold`                         | Editor header strip                                                                                                                                                                                                                                                                                                                                                             | Unchecked                                                                                                                                                                                                                         |
| `Smoothing`                         | Editor header strip                                                                                                                                                                                                                                                                                                                                                             | `Off (1/96)`                                                                                                                                                                                                                      |
| Smoothing                           | Applies fractional-octave power-averaging to the analyzer trace for display — does not affect EQ math. Lower fraction = smoother (1/3 is most smoothed; 1/96 is effectively off). Shared between TX and RX editors.                                                                                                                                                             | Tooltip: 'Fractional-octave smoothing applied to the analyzer trace. Lower fraction = smoother (1/3 = most, 1/96 = off). Affects display only — EQ math is unchanged.' Located in the editor header strip (floating editor only). |
| Filter-type icon row                | A row of 8 custom-painted icons (one per band slot) at the top of the editor canvas area. Each icon draws the current filter shape (peak bell, shelf ramp, HP/LP slope) in its band's palette colour. Click an icon to cycle through the filter types for that band; clicking also selects the band, highlighting its handle on the canvas and its column in the parameter row. | Located in the floating editor only. Icons dim to 35 % opacity when the band is bypassed. Implemented by ClientEqIconRow.                                                                                                         |
| Parameter text row                  | A row of 8 text columns (one per band slot) below the canvas showing each band's Freq, Gain, and Q values. Values update live during canvas drags. Clicking a column selects that band. Right-click a column to open a context menu for entering exact numeric values for Freq, Gain, and Q.                                                                                     | Located in the floating editor only. Implemented by ClientEqParamRow.                                                                                                                                                             |
| Filter cutoff guide lines (TX / RX) | Dashed yellow vertical lines overlaid on the canvas at the radio's current TX low/high filter cutoff (TX tile) or RX passband edges (RX tile). Hovering near a line changes the cursor to a horizontal-resize arrow. Dragging a line in the editor moves the radio's corresponding filter cutoff in real time.                                                                  | Dragging the TX cutoff guides emits cutoffsDragRequested(Tx, lo, hi), which MainWindow forwards to TransmitModel. Dragging the RX guides writes to the active SliceModel. Pass 0 for an edge to suppress that guide.              |
| Output Fader                        | Vertical combined fader + level meter on the right edge of the floating editor. Drag to set post-EQ master gain; scroll wheel adjusts in 0.5 dB steps; double-click resets to 0 dB. The level bar behind the handle shows the smoothed post-EQ peak in real time with the same green-amber-red gradient as the Tube level meter. Click the value text at the bottom to type a precise dB value directly. | 0 dB (linear 1.0), range -36.0 to +12.0 dB. Persisted separately per path: `ClientEqTxMasterGain` / `ClientEqRxMasterGain`.                                                                                                      |

## Tips

- The peak-hold trace tracks raw frequency bins even when display smoothing (`Smoothing` combo) is set to a coarse value such as `1/3`. If a resonance appears in the frozen trace but looks rounded at a coarse smoothing setting, switch `Smoothing` to `Off (1/96)` to see the full bin-level detail.
- To clear the accumulated peak data without toggling `Peak Hold` off and on, uncheck then immediately recheck the button after a moment of silence or reduced signal.
- The dashed yellow filter cutoff guide lines remain draggable while `Peak Hold` is active. This lets you align the radio passband edges directly to features visible on the frozen trace.
- To type an exact Output Fader value, click the numeric display at the bottom of the fader, type a dB value, and press Enter. Press Escape to cancel editing and restore the previous display. The value is clamped to the -36 to +12 dB range.

## Troubleshooting

- **`Peak Hold` button is not visible** — The button is in the floating editor only, not in the docked `Aetherial TX EQ` or `Aetherial RX EQ` applet tile. Open the floating editor by double-clicking the EQ stage in the CHAIN widget.
- **Trace decays immediately after clicking `Peak Hold`** — Confirm the button shows an amber background, which indicates it is checked. A single click that registers as a double-click may toggle the button back off. Click once firmly and verify the amber state.

## Related

- [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md)
- [Smooth the analyzer display for easier reading with the Smoothing combo](smooth-the-analyzer-display-for-easier-reading-with-the-smoothing-combo.md)
- [Drag the TX or RX filter cutoff guide line to move the radio passband](drag-the-tx-or-rx-filter-cutoff-guide-line-to-move-the-radio-passband.md)
- [Inspect the TX EQ curve and live spectrum](inspect-the-tx-eq-curve-and-live-spectrum.md)
- [Inspect the RX EQ curve and live spectrum](inspect-the-rx-eq-curve-and-live-spectrum.md)