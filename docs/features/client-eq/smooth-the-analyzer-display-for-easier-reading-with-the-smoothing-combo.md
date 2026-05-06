# Smooth the analyzer display for easier reading with the Smoothing combo

The Smoothing combo applies fractional-octave power-averaging to the live FFT analyzer trace in the Aetherial Parametric EQ editor. Use it to reduce trace jitter and make broad response trends easier to read while tuning. The setting affects display only — EQ math is unchanged.

## Before you start

- The floating editor must be open. Double-click the EQ stage in the CHAIN widget (TX or RX side) to open it. The editor is titled "Aetherial Parametric EQ — TX" or "Aetherial Parametric EQ — RX".
- The Smoothing combo is in the editor header strip. It is not available in the docked applet tile.

## Steps

1. Open the floating editor for either the TX or RX EQ stage by double-clicking the matching EQ stage in the CHAIN widget.
2. Locate the "Smoothing:" label in the editor header strip.
3. Click the combo box to the right of the "Smoothing:" label.
4. Select a smoothing level from the list:
   - `Off (1/96)` — effectively no smoothing (default)
   - `1/24` — light smoothing
   - `1/12` — moderate smoothing
   - `1/6` — heavier smoothing
   - `1/3` — most smoothed
5. The analyzer trace updates immediately.

## What each control does

| Control                             | Default                                                                                                                                                                                                                                                                                                                                                                         | Valid values                                                                                                                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Smoothing                           | `Off (1/96)`                                                                                                                                                                                                                                                                                                                                                                    | `Off (1/96)` / `1/24` / `1/12` / `1/6` / `1/3`                                                                                                                                                                       |
| Filter-type icon row                | A row of 8 custom-painted icons (one per band slot) at the top of the editor canvas area. Each icon draws the current filter shape (peak bell, shelf ramp, HP/LP slope) in its band's palette colour. Click an icon to cycle through the filter types for that band; clicking also selects the band, highlighting its handle on the canvas and its column in the parameter row. | Located in the floating editor only. Icons dim to 35 % opacity when the band is bypassed. Implemented by ClientEqIconRow.                                                                                            |
| Parameter text row                  | A row of 8 text columns (one per band slot) below the canvas showing each band's Freq, Gain, and Q values. Values update live during canvas drags. Clicking a column selects that band. Labels are bottom-aligned within each column and the row background is transparent so the band-plan strip above the row is not obscured.                                                 | Located in the floating editor only. Implemented by ClientEqParamRow.                                                                                                                                                |
| Filter cutoff guide lines (TX / RX) | Dashed yellow vertical lines overlaid on the canvas at the radio's current TX low/high filter cutoff (TX tile) or RX passband edges (RX tile). Hovering near a line changes the cursor to a horizontal-resize arrow. Dragging a line in the editor moves the radio's corresponding filter cutoff in real time.                                                                  | Dragging the TX cutoff guides emits cutoffsDragRequested(Tx, lo, hi), which MainWindow forwards to TransmitModel. Dragging the RX guides writes to the active SliceModel. Pass 0 for an edge to suppress that guide. |

**Smoothing** — Applies fractional-octave power-averaging to the analyzer trace. Lower fraction values produce a smoother trace: `1/3` is the most smoothed; `Off (1/96)` is effectively unsmoothed. The setting is shared between the TX and RX editors — changing it in one editor also affects the other. EQ math and the peak-hold trace are not affected.

## Tips

- The peak-hold trace tracks raw bins regardless of the smoothing setting. If you want to see both the smoothed trend and the raw peaks simultaneously, enable Peak Hold while smoothing is active.
- `1/6` or `1/3` smoothing is useful for comparing your EQ curve against the broad shape of the analyzer fill without fine bin-level noise obscuring the comparison.

## Troubleshooting

- **Smoothing combo is not visible** — The combo is only present in the floating editor, not in the docked "Aetherial TX EQ" or "Aetherial RX EQ" applet tile. Open the editor by double-clicking the EQ stage in the CHAIN widget.
- **Changing smoothing in the TX editor also changes the RX editor** — This is expected. `ClientEqSmoothingFraction` is a single global preference shared between both editors.
- **Parameter text row overlaps the band-plan strip** — This was a display defect in versions prior to v0.9.7 where the parameter row's dark background bled upward over the canvas's band-plan strip. If you see this, update to v0.9.7 or later.

## Related

- [Freeze the analyzer peak-hold trace to spot resonances while tuning](freeze-the-analyzer-peak-hold-trace-to-spot-resonances-while-tuning.md)
- [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md)
- [Inspect the TX EQ curve and live spectrum](inspect-the-tx-eq-curve-and-live-spectrum.md)
- [Inspect the RX EQ curve and live spectrum](inspect-the-rx-eq-curve-and-live-spectrum.md)