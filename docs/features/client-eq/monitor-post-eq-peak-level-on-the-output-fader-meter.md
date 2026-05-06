# Monitor post-EQ peak level on the Output Fader meter

The Output Fader in the floating EQ editor displays a live post-EQ peak level meter behind its handle, letting you see how much headroom remains after your EQ curve and master gain setting are applied.

## Before you start

- The floating EQ editor must be open for the path you want to monitor (TX or RX). The Output Fader is not present in the docked applet tile.
- The EQ stage should be enabled. If the stage is bypassed, the meter still reflects the signal passing through, but the EQ curve has no effect.

## Steps

1. Open the floating editor for the path you want to monitor. Double-click the matching EQ stage in the CHAIN widget — either the TX or RX side — to open the editor titled "Aetherial Parametric EQ — TX" or "Aetherial Parametric EQ — RX".
2. Locate the Output Fader on the right edge of the floating editor. It is a vertical combined fader and level meter.
3. Observe the level bar behind the fader handle. The bar displays the smoothed post-EQ peak level in real time using a green-amber-red gradient, the same as the Tube level meter.
4. Transmit or receive audio as normal. The level bar updates continuously, reflecting the signal level after all EQ bands and the master gain offset have been applied.

## What each control does

| Control                             | Default                                                                                                                                                                                                                                                                                                                                                                         | Valid range                                                                                                                                                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Output Fader (TX)                   | 0 dB                                                                                                                                                                                                                                                                                                                                                                            | −36.0 to +12.0 dB                                                                                                                                                                                                                 |
| Output Fader (RX)                   | 0 dB                                                                                                                                                                                                                                                                                                                                                                            | −36.0 to +12.0 dB                                                                                                                                                                                                                 |
| Smoothing                           | Applies fractional-octave power-averaging to the analyzer trace for display — does not affect EQ math. Lower fraction = smoother (1/3 is most smoothed; 1/96 is effectively off). Shared between TX and RX editors.                                                                                                                                                             | Tooltip: 'Fractional-octave smoothing applied to the analyzer trace. Lower fraction = smoother (1/3 = most, 1/96 = off). Affects display only — EQ math is unchanged.' Located in the editor header strip (floating editor only). |
| Filter-type icon row                | A row of 8 custom-painted icons (one per band slot) at the top of the editor canvas area. Each icon draws the current filter shape (peak bell, shelf ramp, HP/LP slope) in its band's palette colour. Click an icon to cycle through the filter types for that band; clicking also selects the band, highlighting its handle on the canvas and its column in the parameter row. | Located in the floating editor only. Icons dim to 35 % opacity when the band is bypassed. Implemented by ClientEqIconRow.                                                                                                         |
| Parameter text row                  | A row of 8 text columns (one per band slot) below the canvas showing each band's Freq, Gain, and Q values. Values update live during canvas drags. Clicking a column selects that band. In v0.9.7 each column has a transparent background so it no longer bleeds a dark fill over the canvas's band-plan strip above; labels are bottom-aligned within the column.             | Located in the floating editor only. Implemented by ClientEqParamRow.                                                                                                                                                             |
| Filter cutoff guide lines (TX / RX) | Dashed yellow vertical lines overlaid on the canvas at the radio's current TX low/high filter cutoff (TX tile) or RX passband edges (RX tile). Hovering near a line changes the cursor to a horizontal-resize arrow. Dragging a line in the editor moves the radio's corresponding filter cutoff in real time.                                                                  | Dragging the TX cutoff guides emits cutoffsDragRequested(Tx, lo, hi), which MainWindow forwards to TransmitModel. Dragging the RX guides writes to the active SliceModel. Pass 0 for an edge to suppress that guide.              |

The level meter behind the fader handle is an indicator only. It shows the smoothed post-EQ peak for the path bound to this editor instance. It does not have a separate control or persisted key.

## Tips

- If the meter is consistently hitting amber or red, drag the Output Fader handle down to reduce post-EQ gain, or reduce individual band gains to bring levels down before the master stage.
- Scroll the mouse wheel over the Output Fader for fine 0.5 dB adjustments while watching the meter.
- Double-click the Output Fader to reset it to 0 dB without disturbing your band settings.

## Related

- [Adjust post-EQ output gain with the Output Fader](adjust-post-eq-output-gain-with-the-output-fader.md)
- [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md)
- [Freeze the analyzer peak-hold trace to spot resonances while tuning](freeze-the-analyzer-peak-hold-trace-to-spot-resonances-while-tuning.md)
- [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md)