# Open the Frameless Editor to Add / Remove / Tune Bands on Either Side

The frameless editor is where you add, remove, and adjust individual EQ bands for the TX or RX path. The applet tiles show the resulting curve read-only; all editing happens in this floating window.

## Before you start

- The Aetherial Audio (TXDSP) parent container must be visible in the applet panel.
- The EQ stage for the side you want to edit (TX or RX) must be enabled. If it is not yet enabled, see [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md).

## Steps

1. Locate the CHAIN widget inside the Aetherial Audio (TXDSP) container.
2. Double-click the EQ stage on the side you want to edit — the TX stage to open "Aetherial Parametric EQ — TX", or the RX stage to open "Aetherial Parametric EQ — RX".
3. The frameless editor opens at its default size (900 × 520 px). The title bar shows which path is active.
4. To **add a band**, click an empty slot in the icon row along the top of the canvas area.
5. To **remove a band**, select it in the icon row or by clicking its handle on the canvas, then use the remove control in that row.
6. To **tune a band**:
   - Drag a peak or shelf node on the canvas horizontally to adjust frequency, vertically to adjust gain.
   - Hold Shift and drag to adjust Q.
   - Drag an HP or LP node horizontally to adjust frequency; drag vertically to adjust Q.
   - Click a band icon to cycle its filter type.
7. To change the filter family used for HP/LP cascade math, select an option from the dropdown in the top-right strip of the editor: **Butterworth**, **Chebyshev**, **Bessel**, or **Elliptic**.
8. To switch to the other path without closing the editor, double-click the opposite EQ stage in the CHAIN widget. The editor title and content update to reflect the new path.
9. Close the editor by clicking the close button in the editor's title bar. Band settings are saved automatically to `ClientEqTxBands` or `ClientEqRxBands`.

## What each control does

| Control | Description | Notes |
|---|---|---|
| Canvas | Interactive frequency-response display. Drag band nodes to tune. | Editing target; the applet tile is view-only. |
| Icon row | One icon per band. Click to select or cycle filter type. | Rebuilds when bands are added or removed. |
| Parameter row | Numeric readout and entry for the selected band's frequency, gain, and Q. | Updates live during canvas drags. |
| Filter family dropdown | Sets HP/LP cascade math for the active path. Options: **Butterworth**, **Chebyshev**, **Bessel**, **Elliptic**. Default: Butterworth. | Applies only to HP and LP band types; peaks and shelves use fixed second-order topology. |
| Output fader | Vertical slider and meter on the right edge. Sets master output gain for the active path. | Adjusts `setMasterGain` for the bound EQ; value saved on change. |
| Title bar | Displays "Aetherial Parametric EQ — TX" or "— RX". Drag to move the window. | One shared editor instance; title flips when the path changes. |

## Tips

- The editor reuses a single window instance for both paths. The title bar label is the reliable indicator of which side you are currently editing.
- The live FFT analyzer inside the editor runs at 25 Hz while the editor is open and stops automatically when you close it.
- Interaction hints printed at the top of the editor ("Drag peak/shelf = freq + gain · drag HP/LP = freq + Q · Shift + drag for Q · click icon to cycle type") summarize the canvas gestures.

## Troubleshooting

- **The EQ stage double-click does nothing** — The EQ stage may be bypassed or the Aetherial Audio container may not be fully loaded. Verify the stage is enabled via the CHAIN widget, then try again.
- **Band changes are not audible** — Check that `ClientEqRxEnabled` or `ClientEqTxEnabled` is on for the relevant path. A bypassed stage passes audio unmodified regardless of band settings.

## Related

- [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md)
- [Inspect the TX EQ curve and live spectrum](inspect-the-tx-eq-curve-and-live-spectrum.md)
- [Inspect the RX EQ curve and live spectrum](inspect-the-rx-eq-curve-and-live-spectrum.md)
- [Verify the summed curve matches your mental target](verify-the-summed-curve-matches-your-mental-target.md)
