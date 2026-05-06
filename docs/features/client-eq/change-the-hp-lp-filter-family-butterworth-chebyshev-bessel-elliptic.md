# Change the HP/LP filter family (Butterworth, Chebyshev, Bessel, Elliptic)

The **Filter family** selector controls the mathematics used for HP and LP filter bands in the client EQ. Changing it lets you trade off rolloff steepness, passband flatness, and phase linearity to suit your audio goals.

## Before you start

- The EQ stage for the path you want to change (TX or RX) must be enabled. See [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md).
- The floating editor must be open. The **Filter family** selector is only available in the frameless editor, not the docked applet tile. See [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md).
- At least one band must be set to an HP or LP filter type. The setting has no audible effect if only peak and shelf bands are present.

## Steps

1. Open the floating editor for the path you want to change — double-click the EQ stage in the CHAIN widget on the TX or RX side. The window title will read "Aetherial Parametric EQ — TX" or "Aetherial Parametric EQ — RX".
2. Locate the **Filter family** combo box in the editor header strip, to the right of the **Peak Hold** button.
3. Click the combo box and select one of the four options: **Butterworth**, **Chebyshev**, **Bessel**, or **Elliptic**.
4. The EQ curve on the canvas updates immediately. If HP or LP bands are present, their slopes will redraw to reflect the new family.

The selection is saved automatically. It is stored separately for each path: `ClientEqTxFilterFamily` for the TX editor and `ClientEqRxFilterFamily` for the RX editor.

## What each control does

| Control                             | Default                                                                                                                                                                                                                                                                                                                                                                         | Valid values                                                                                                                                                                                                                      |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Filter family** (TX editor)       | Butterworth                                                                                                                                                                                                                                                                                                                                                                     | Butterworth, Chebyshev, Bessel, Elliptic                                                                                                                                                                                          |
| **Filter family** (RX editor)       | Butterworth                                                                                                                                                                                                                                                                                                                                                                     | Butterworth, Chebyshev, Bessel, Elliptic                                                                                                                                                                                          |
| Smoothing                           | Applies fractional-octave power-averaging to the analyzer trace for display — does not affect EQ math. Lower fraction = smoother (1/3 is most smoothed; 1/96 is effectively off). Shared between TX and RX editors.                                                                                                                                                             | Tooltip: 'Fractional-octave smoothing applied to the analyzer trace. Lower fraction = smoother (1/3 = most, 1/96 = off). Affects display only — EQ math is unchanged.' Located in the editor header strip (floating editor only). |
| Filter-type icon row                | A row of 8 custom-painted icons (one per band slot) at the top of the editor canvas area. Each icon draws the current filter shape (peak bell, shelf ramp, HP/LP slope) in its band's palette colour. Click an icon to cycle through the filter types for that band; clicking also selects the band, highlighting its handle on the canvas and its column in the parameter row. | Located in the floating editor only. Icons dim to 35 % opacity when the band is bypassed. Implemented by ClientEqIconRow.                                                                                                         |
| Parameter text row                  | A row of 8 text columns (one per band slot) below the canvas showing each band's Freq, Gain, and Q values. Values update live during canvas drags. Clicking a column selects that band. Labels are bottom-aligned within each column and the row background is transparent so it does not bleed over the band-plan strip above.                                                  | Located in the floating editor only. Implemented by ClientEqParamRow.                                                                                                                                                             |
| Filter cutoff guide lines (TX / RX) | Dashed yellow vertical lines overlaid on the canvas at the radio's current TX low/high filter cutoff (TX tile) or RX passband edges (RX tile). Hovering near a line changes the cursor to a horizontal-resize arrow. Dragging a line in the editor moves the radio's corresponding filter cutoff in real time.                                                                  | Dragging the TX cutoff guides emits cutoffsDragRequested(Tx, lo, hi), which MainWindow forwards to TransmitModel. Dragging the RX guides writes to the active SliceModel. Pass 0 for an edge to suppress that guide.              |

**Butterworth** — maximally flat passband; no ripple in the passband or stopband. The default choice for general use.

**Chebyshev** — steeper transition band than Butterworth, with 1 dB of ripple in the passband.

**Bessel** — linear phase response and the gentlest rolloff of the four families. Preserves transient shape.

**Elliptic** — steepest transition of all four options, with ripple in both the passband and the stopband.

These options apply only to HP and LP band types. Peak and shelf bands use their own fixed second-order topology regardless of this setting.

## Tips

- If you have no HP or LP bands in the current EQ, switching the filter family changes nothing audible. Add an HP or LP band first via the filter-type icon row.
- The filter family is set independently for TX and RX. Changing it in the TX editor does not affect the RX editor, and vice versa.
- Clicking **Reset** in the editor header strip resets the filter family back to **Butterworth** along with all band parameters.

## Troubleshooting

- **The Filter family combo is not visible** — The combo is only present in the floating editor, not the docked applet tile. Double-click the EQ stage in the CHAIN widget to open the editor.
- **Changing the family has no effect on the curve** — No HP or LP bands are active. The setting only affects HP and LP cascade math. Check each band's type using the filter-type icon row.
- **The parameter text row appears to overlap the band-plan strip** — This was a display issue in versions before v0.9.7 where the row's dark background bled upward over the canvas. Update to v0.9.7 or later; the row is now transparent and its labels are bottom-aligned within each column.

## Related

- [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md)
- [Change a band's filter type by clicking its icon in the icon row](change-a-band-s-filter-type-by-clicking-its-icon-in-the-icon-row.md)
- [Reset all EQ bands to the default 10-band template](reset-all-eq-bands-to-the-default-10-band-template.md)
- [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md)
- [Aetherial Parametric EQ (TX / RX) overview](overview.md)