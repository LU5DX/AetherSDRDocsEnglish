# Read exact freq / gain / Q values in the parameter text row

The parameter text row shows the precise frequency, gain, and Q value for every EQ band in a single glance. Use it to confirm exact settings after dragging bands on the canvas, or to identify which band is selected before making adjustments.

## Before you start

- The parameter text row is only visible in the floating ClientEqEditor window, not in the docked applet tile. Open the editor first.
- At least one EQ band must exist. The row shows one column per band slot, up to eight bands.

## Steps

1. Open the floating editor for the side you want to inspect. Double-click the EQ stage in the CHAIN widget on either the TX or RX side. The editor window is titled "Aetherial Parametric EQ — TX" or "Aetherial Parametric EQ — RX".
2. Locate the parameter text row at the bottom of the editor canvas area. It displays one column per band, each showing that band's Freq, Gain, and Q values.
3. Read the values directly. The row updates live as you drag band handles on the canvas — no extra action is needed.
4. To read values for a specific band, click its column in the parameter text row. This selects that band, highlighting its handle on the canvas and its icon in the filter-type icon row above.

## What each control does

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| Parameter text row | Displays Freq, Gain, and Q for each of the eight band slots. Updates live during canvas drags. Clicking a column selects that band. | — | — |
| Filter-type icon row | Row of icons above the canvas, one per band slot. Clicking an icon selects that band and cycles its filter type. Selected band is highlighted in both the icon row and the parameter text row. | — | — |

## Tips

- Dragging a band handle on the canvas updates the parameter text row in real time, so you can watch the numeric values change while tuning by ear.
- Clicking a column in the parameter text row is equivalent to clicking the matching icon in the filter-type icon row — both select the same band.
- Bands that are bypassed show dimmed icons (35% opacity) in the icon row above; their values still appear in the parameter text row.

## Related

- [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md)
- [Change a band's filter type by clicking its icon in the icon row](change-a-band-s-filter-type-by-clicking-its-icon-in-the-icon-row.md)
- [Verify the summed curve matches your mental target](verify-the-summed-curve-matches-your-mental-target.md)
