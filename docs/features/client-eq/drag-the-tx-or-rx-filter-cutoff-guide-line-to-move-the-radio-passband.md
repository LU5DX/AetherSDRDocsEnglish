# Drag the TX or RX filter cutoff guide line to move the radio passband

The EQ editor canvas shows dashed yellow vertical lines at the radio's current TX or RX filter cutoff edges. Dragging these lines moves the radio's passband in real time, letting you match your EQ shaping to the actual filter boundaries without leaving the EQ editor.

## Before you start

- AetherSDR must be connected to the radio.
- The floating editor for the relevant side (TX or RX) must be open. The guide lines are draggable only in the frameless editor canvas, not in the docked applet tile.
- To open the floating editor, double-click the EQ stage in the CHAIN widget on the TX or RX side. See [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md).

## Steps

1. Open the floating editor for the side you want to adjust: double-click the EQ stage in the CHAIN widget. The editor title bar reads "Aetherial Parametric EQ — TX" or "Aetherial Parametric EQ — RX".
2. Locate the dashed yellow vertical lines on the canvas. There are two: one at the low cutoff edge and one at the high cutoff edge of the radio's current passband.
3. Move the pointer toward one of the dashed yellow lines. When the pointer is close enough to the line, the cursor changes to a horizontal-resize arrow.
4. Click and drag the line left or right. The radio's corresponding filter cutoff updates in real time as you drag.
5. Release to set the new cutoff position.
6. Repeat for the other guide line if you want to adjust the opposite passband edge.

## What each control does

| Control                             | Behavior                                                                                                                                                                                                                                                                                                                                                                        | Notes                                                                                                                                                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter cutoff guide lines (TX)      | Dashed yellow vertical lines on the TX editor canvas marking the radio's current TX low and high filter cutoffs. Drag in the editor to move the radio's TX passband in real time.                                                                                                                                                                                               | Cursor changes to a horizontal-resize arrow when hovering near a line.                                                                                                                                                            |
| Filter cutoff guide lines (RX)      | Dashed yellow vertical lines on the RX editor canvas marking the active slice's RX passband edges (in the audio-frequency domain). Drag in the editor to move the radio's RX passband in real time.                                                                                                                                                                             | Cursor changes to a horizontal-resize arrow when hovering near a line.                                                                                                                                                            |
| Smoothing                           | Applies fractional-octave power-averaging to the analyzer trace for display — does not affect EQ math. Lower fraction = smoother (1/3 is most smoothed; 1/96 is effectively off). Shared between TX and RX editors.                                                                                                                                                             | Tooltip: 'Fractional-octave smoothing applied to the analyzer trace. Lower fraction = smoother (1/3 = most, 1/96 = off). Affects display only — EQ math is unchanged.' Located in the editor header strip (floating editor only). |
| Filter-type icon row                | A row of 8 custom-painted icons (one per band slot) at the top of the editor canvas area. Each icon draws the current filter shape (peak bell, shelf ramp, HP/LP slope) in its band's palette colour. Click an icon to cycle through the filter types for that band; clicking also selects the band, highlighting its handle on the canvas and its column in the parameter row. | Located in the floating editor only. Icons dim to 35 % opacity when the band is bypassed. Implemented by ClientEqIconRow.                                                                                                         |
| Parameter text row                  | A row of 8 text columns (one per band slot) below the canvas showing each band's Freq, Gain, and Q values. Values update live during canvas drags. Clicking a column selects that band. In v0.9.7 the row background is transparent so it no longer obscures the audio band-plan strip directly above it; labels are bottom-aligned within each column.                          | Located in the floating editor only. Implemented by ClientEqParamRow.                                                                                                                                                             |
| Filter cutoff guide lines (TX / RX) | Dashed yellow vertical lines overlaid on the canvas at the radio's current TX low/high filter cutoff (TX tile) or RX passband edges (RX tile). Hovering near a line changes the cursor to a horizontal-resize arrow. Dragging a line in the editor moves the radio's corresponding filter cutoff in real time.                                                                  | Dragging the TX cutoff guides emits cutoffsDragRequested(Tx, lo, hi), which MainWindow forwards to TransmitModel. Dragging the RX guides writes to the active SliceModel. Pass 0 for an edge to suppress that guide.              |

## Tips

- The guide lines are visible in both the docked applet tile and the floating editor, but dragging is only active in the floating editor canvas.
- A guide line is absent when the corresponding cutoff value is 0 or not set by the radio.
- Watch the parameter text row at the bottom of the editor while dragging to confirm the resulting passband edges.

## Troubleshooting

- **Cursor does not change to a horizontal-resize arrow near the line** — You are hovering over the docked applet tile, not the floating editor canvas. Open the floating editor by double-clicking the EQ stage in the CHAIN widget, then try again.
- **No dashed yellow lines are visible on the canvas** — The radio has not reported filter cutoff values, or both cutoff values are 0. Verify the radio is connected and a slice is active.

## Related

- [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md)
- [Inspect the TX EQ curve and live spectrum](inspect-the-tx-eq-curve-and-live-spectrum.md)
- [Inspect the RX EQ curve and live spectrum](inspect-the-rx-eq-curve-and-live-spectrum.md)
- [Read exact freq / gain / Q values in the parameter text row](read-exact-freq-gain-q-values-in-the-parameter-text-row.md)