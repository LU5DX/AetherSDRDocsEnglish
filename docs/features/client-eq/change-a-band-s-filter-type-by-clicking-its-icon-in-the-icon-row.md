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

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| Filter-type icon row | A row of up to 8 icons at the top of the editor canvas. Each icon draws the current filter shape for its band in that band's palette colour. Click to cycle the filter type; clicking also selects the band. Icons dim to 35% opacity when the band is bypassed. | — | — |
| Parameter text row | A row of up to 8 text columns below the canvas showing each band's Freq, Gain, and Q values. Updates live during canvas drags. Clicking a column selects that band. | — | — |

## Tips

- The hint text in the editor header strip reads "click icon to cycle type" — this is the only action the icon row supports; there is no right-click menu on individual icons.
- If an icon appears dimmed (35% opacity), that band is bypassed. Its filter type can still be cycled, but the band will have no effect on the EQ curve until it is re-enabled.
- The filter family selected in the Filter family combo (default: Butterworth) governs HP and LP cascade mathematics. Changing a band to an HP or LP type will use the currently selected family. Peak and shelf bands use their own fixed 2nd-order topology regardless of the Filter family setting.

## Troubleshooting

- **The icon row is not visible** — The icon row is only present in the floating editor, not in the docked "Aetherial TX EQ" or "Aetherial RX EQ" applet tile. Open the floating editor by double-clicking the EQ stage in the CHAIN widget.
- **Clicking an icon has no effect on the EQ curve** — The band may be bypassed (icon is dimmed to 35% opacity). Re-enable the band to hear the filter type change reflected in the summed curve.

## Related

- [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md)
- [Change the HP/LP filter family (Butterworth, Chebyshev, Bessel, Elliptic)](change-the-hp-lp-filter-family-butterworth-chebyshev-bessel-elliptic.md)
- [Read exact freq / gain / Q values in the parameter text row](read-exact-freq-gain-q-values-in-the-parameter-text-row.md)
- [Aetherial Parametric EQ (TX / RX) overview](overview.md)
