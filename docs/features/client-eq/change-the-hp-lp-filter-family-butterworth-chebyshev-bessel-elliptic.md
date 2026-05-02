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

| Control | Default | Valid values | Setting key |
|---|---|---|---|
| **Filter family** (TX editor) | Butterworth | Butterworth, Chebyshev, Bessel, Elliptic | `ClientEqTxFilterFamily` |
| **Filter family** (RX editor) | Butterworth | Butterworth, Chebyshev, Bessel, Elliptic | `ClientEqRxFilterFamily` |

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

## Related

- [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md)
- [Change a band's filter type by clicking its icon in the icon row](change-a-band-s-filter-type-by-clicking-its-icon-in-the-icon-row.md)
- [Reset all EQ bands to the default 10-band template](reset-all-eq-bands-to-the-default-10-band-template.md)
- [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md)
- [Aetherial Parametric EQ (TX / RX) overview](overview.md)
