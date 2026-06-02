# Read exact freq / gain / Q values in the parameter text row

The parameter text row shows the precise frequency, gain, and Q value for every EQ band in a single glance. Use it to confirm exact settings after dragging bands on the canvas, or to identify which band is selected before making adjustments.

## Before you start

- The parameter text row is only visible in the floating ClientEqEditor window, not in the docked applet tile. Open the editor first.
- At least one EQ band must exist. The row shows one column per band slot, up to eight bands.

## Steps

1. Open the floating editor for the side you want to inspect. Double-click the EQ stage in the CHAIN widget on either the TX or RX side. The editor window is titled "Aetherial Parametric EQ — TX" or "Aetherial Parametric EQ — RX".
2. Locate the parameter text row at the bottom of the editor canvas area. It displays one column per band, each showing that band's Freq, Gain, and Q values. The row has a transparent background so it does not obscure the audio band-plan strip immediately above it on the canvas.
3. Read the values directly. The row updates live as you drag band handles on the canvas — no extra action is needed.
4. To read values for a specific band, click its column in the parameter text row. This selects that band, highlighting its handle on the canvas and its icon in the filter-type icon row above.

## Edit band parameters numerically

You can type exact frequency, gain, or Q values for any band directly into the parameter text row. This is useful for precise settings that are difficult to achieve by dragging.

1. Right-click a column in the parameter text row to open the numeric entry menu.
2. Choose the parameter you want to edit: Freq, Gain, or Q.
3. Type the new value and press Enter. The change is committed immediately, the EQ settings are saved, and the canvas curve redraws to reflect the new value.

## What each control does

| Control                             | Behavior                                                                                                                                                                                                                                                                                                       | Default                                                                                                                                                                                                                           |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameter text row                  | Displays Freq, Gain, and Q for each of the eight band slots. Updates live during canvas drags. Clicking a column selects that band. Right-click a column to edit any parameter numerically via a context menu. Each column has a transparent background so the band-plan strip at the bottom of the canvas remains visible above the row.                                                 | —                                                                                                                                                                                                                                 |
| Filter-type icon row                | Row of icons above the canvas, one per band slot. Clicking an icon selects that band and cycles its filter type. Selected band is highlighted in both the icon row and the parameter text row.                                                                                                                 | —                                                                                                                                                                                                                                 |
| Smoothing                           | Applies fractional-octave power-averaging to the analyzer trace for display — does not affect EQ math. Lower fraction = smoother (1/3 is most smoothed; 1/96 is effectively off). Shared between TX and RX editors.                                                                                            | Tooltip: 'Fractional-octave smoothing applied to the analyzer trace. Lower fraction = smoother (1/3 = most, 1/96 = off). Affects display only — EQ math is unchanged.' Located in the editor header strip (floating editor only). |
| Peak Hold                             | When checked, the per-bin peak-hold trace in the analyzer stops decaying — every frequency's highest observed level is held until the button is toggled off. | Amber background when checked. Located in the editor header strip (floating editor only, not the docked applet tile). |
| Filter family                         | Selects the HP/LP cascade mathematics. Butterworth = maximally flat passband; Chebyshev = steeper rolloff with 1 dB passband ripple; Bessel = linear phase / gentler rolloff; Elliptic = steepest transition with ripple in both bands. | Butterworth. Applies only to HP and LP filter types; peak and shelf bands use their own fixed 2nd-order topology regardless. Persisted separately per path: `ClientEqTxFilterFamily` / `ClientEqRxFilterFamily`. Located in the editor header strip. |
| Reset                                 | Resets all bands to the default 10-band template, restores the default band count, and resets the filter family to Butterworth. Saves immediately. | Tooltip: 'Reset all bands to default values'. Located in the editor header strip (floating editor only). |
| Output Fader                          | Vertical combined fader + level meter on the right edge of the floating editor. Drag to set post-EQ master gain; scroll wheel adjusts in 0.5 dB steps; double-click resets to 0 dB. Click the value display to edit the gain numerically — type a dB value and press Enter or click away to commit. The level bar behind the handle shows the smoothed post-EQ peak in real time with the same green-amber-red gradient as the Tube level meter. | 0 dB (linear 1.0). Range -36.0 to +12.0 dB. Tooltip: 'Output gain (dB). Drag to set, wheel for fine step, double-click to reset to 0 dB. Click value to type exact dB.' Persisted separately per path: `ClientEqTxMasterGain` / `ClientEqRxMasterGain`. Located in the floating editor only — not in the docked applet tile. |
| Filter cutoff guide lines (TX / RX) | Dashed yellow vertical lines overlaid on the canvas at the radio's current TX low/high filter cutoff (TX tile) or RX passband edges (RX tile). Hovering near a line changes the cursor to a horizontal-resize arrow. Dragging a line in the editor moves the radio's corresponding filter cutoff in real time. | Dragging the TX cutoff guides emits cutoffsDragRequested(Tx, lo, hi), which MainWindow forwards to TransmitModel. Dragging the RX guides writes to the active SliceModel. Pass 0 for an edge to suppress that guide.              |
| Reference curve overlay               | Displays a semi-transparent amber target curve on the EQ canvas based on a classic microphone or speech response. Select from Off, AT&T 1959, Heil DX, Astatic D-104, Shure 444, or Heil HC-5. The curve is drawn after the analyzer but before the EQ band curves so your adjustments sit on top of the target. | Off. Persisted separately per path: `ClientEqTxReferenceCurve` / `ClientEqRxReferenceCurve`. Located in the editor header strip (floating editor only). |

## Tips

- Dragging a band handle on the canvas updates the parameter text row in real time, so you can watch the numeric values change while tuning by ear.
- Clicking a column in the parameter text row is equivalent to clicking the matching icon in the filter-type icon row — both select the same band.
- Bands that are bypassed show dimmed icons (35% opacity) in the icon row above; their values still appear in the parameter text row.
- The parameter text row and its individual band columns use a transparent background. If the row appeared to cover or darken the band-plan strip at the bottom of the canvas in an earlier version, this is corrected in v0.9.7.
- Right-click a column to enter exact numeric values instead of dragging — useful for precise filter settings.
- The Output Fader value display is now an inline text field. Click the displayed dB value to edit it directly. Press Enter or click away to commit the value. Press Escape to cancel editing and restore the previous value.
- The reference curve overlay provides a visual target to shape your parametric EQ toward. Select a preset from the Reference curve combo box in the editor header strip. The curve appears as a semi-transparent amber line. Use it as a guide when adjusting band parameters — the summed EQ response will show how closely you match the target.

## Related

- [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md)
- [Change a band's filter type by clicking its icon in the icon row](change-a-band-s-filter-type-by-clicking-its-icon-in-the-icon-row.md)
- [Verify the summed curve matches your mental target](verify-the-summed-curve-matches-your-mental-target.md)