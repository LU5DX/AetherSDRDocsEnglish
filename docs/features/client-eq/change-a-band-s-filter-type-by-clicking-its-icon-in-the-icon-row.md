# Change a band's filter type by clicking its icon in the icon row

Each band in the Aetherial Parametric EQ has a filter type (peak bell, shelf, HP slope, LP slope) shown as a small icon above the EQ canvas. Clicking an icon cycles that band to the next filter type without opening any additional dialog.

## Before you start

- The floating editor must be open. The icon row is only available in the "Aetherial Parametric EQ — TX" or "Aetherial Parametric EQ — RX" frameless editor window, not in the docked applet tile.
- If the editor is not open, double-click the EQ stage in the CHAIN widget on the TX or RX side to open it. See [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md).

## Steps

1. Open the floating editor for the TX or RX side as needed.
2. Locate the filter-type icon row at the top of the editor canvas area. There is one icon per band slot (up to 8 icons), each drawn in that band's palette colour showing its current filter shape.
3. Click the icon for the band whose filter type you want to change. Clicking cycles that band to the next filter type and simultaneously selects the band — its handle on the canvas is highlighted and its column in the parameter text row at the bottom is highlighted.
4. Continue clicking the same icon to cycle through the remaining filter types until the desired type is shown.

## What each control does

| Control                             | Behavior                                                                                                                                                                                                                                                                                                       | Default                                                                                                                                                                                                                           |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter-type icon row                | A row of up to 8 icons at the top of the editor canvas. Each icon draws the current filter shape for its band in that band's palette colour. Click to cycle the filter type; clicking also selects the band. Icons dim to 35% opacity when the band is bypassed.                                               | —                                                                                                                                                                                                                                 |
| Parameter text row                  | A row of up to 8 text columns below the canvas showing each band's Freq, Gain, and Q values. Updates live during canvas drags. Clicking a column selects that band. Right-click a column to enter numeric values directly via a context menu; pressing Enter or clicking elsewhere commits the value, saves settings immediately, and redraws the canvas and icon row. In v0.9.7 the row background is transparent so it no longer bleeds a dark fill over the band-plan strip at the bottom of the canvas; labels remain bottom-aligned within each column. | —                                                                                                                                                                                                                                 |
| Smoothing                           | Applies fractional-octave power-averaging to the analyzer trace for display — does not affect EQ math. Lower fraction = smoother (1/3 is most smoothed; 1/96 is effectively off). Shared between TX and RX editors.                                                                                            | Tooltip: 'Fractional-octave smoothing applied to the analyzer trace. Lower fraction = smoother (1/3 = most, 1/96 = off). Affects display only — EQ math is unchanged.' Located in the editor header strip (floating editor only). |
| Filter cutoff guide lines (TX / RX) | Dashed yellow vertical lines overlaid on the canvas at the radio's current TX low/high filter cutoff (TX tile) or RX passband edges (RX tile). Hovering near a line changes the cursor to a horizontal-resize arrow. Dragging a line in the editor moves the radio's corresponding filter cutoff in real time. | Dragging the TX cutoff guides emits cutoffsDragRequested(Tx, lo, hi), which MainWindow forwards to TransmitModel. Dragging the RX guides writes to the active SliceModel. Pass 0 for an edge to suppress that guide.              |
| Output Fader                        | Vertical combined fader + level meter on the right edge of the floating editor. Drag to set post-EQ master gain; scroll wheel adjusts in 0.5 dB steps; double-click resets to 0 dB. Click the numeric value at the bottom to edit it inline — type a dB value and press Enter to commit (clamped to -36 to +12 dB). Press Escape to cancel editing and restore the previous value. The level bar behind the handle shows the smoothed post-EQ peak in real time with the same green-amber-red gradient as the Tube level meter. | Persisted separately per path: ClientEqTxMasterGain / ClientEqRxMasterGain. Tooltip: 'Output gain (dB). Drag to set, wheel for fine step, double-click to reset to 0 dB.' Gain range is linear 0.0 to ~4.0; the scale labels run from -40 to 0 dB. Located in the floating editor only — not in the docked applet tile. |

## Tips

- The hint text in the editor header strip reads "click icon to cycle type" — this is the only action the icon row supports; there is no right-click menu on individual icons.
- If an icon appears dimmed (35% opacity), that band is bypassed. Its filter type can still be cycled, but the band will have no effect on the EQ curve until it is re-enabled.
- The filter family selected in the Filter family combo (default: Butterworth) governs HP and LP cascade mathematics. Changing a band to an HP or LP type will use the currently selected family. Peak and shelf bands use their own fixed 2nd-order topology regardless of the Filter family setting.
- To edit a band's numeric values directly, right-click a column in the parameter text row and enter the desired Freq, Gain, or Q value. Press Enter to commit — the value is clamped to the valid range, settings are saved immediately, and the canvas and icon row update to reflect the change.

## Troubleshooting

- **The icon row is not visible** — The icon row is only present in the floating editor, not in the docked "Aetherial TX EQ" or "Aetherial RX EQ" applet tile. Open the floating editor by double-clicking the EQ stage in the CHAIN widget.
- **Clicking an icon has no effect on the EQ curve** — The band may be bypassed (icon is dimmed to 35% opacity). Re-enable the band to hear the filter type change reflected in the summed curve.
- **The parameter text row appears to overlap the band-plan strip** — This was a display issue in versions prior to v0.9.7 where the row's dark background bled upward over the band-plan strip at the bottom of the canvas. Update to v0.9.7 or later to resolve it.

## Related

- [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md)
- [Change the HP/LP filter family (Butterworth, Chebyshev, Bessel, Elliptic)](change-the-hp-lp-filter-family-butterworth-chebyshev-bessel-elliptic.md)
- [Read exact freq / gain / Q values in the parameter text row](read-exact-freq-gain-q-values-in-the-parameter-text-row.md)
- [Aetherial Parametric EQ (TX / RX) overview](overview.md)