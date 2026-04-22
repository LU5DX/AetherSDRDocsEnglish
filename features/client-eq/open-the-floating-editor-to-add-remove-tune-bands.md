# Open the floating editor to add / remove / tune bands

The ClientEqEditor floating window is where you add, remove, and tune individual EQ bands for the RX and TX paths. The compact applet view is read-only; all band editing happens in this separate window.

## Before you start

- The CEQ sub-container must be visible inside the PooDoo Audio (TXDSP) parent container. If it is hidden, enable the EQ stage via the CHAIN widget first.
- Locate the CHAIN widget for the audio path you want to edit (RX or TX).

## Steps

1. In the CHAIN widget, double-click the EQ stage to open the ClientEqEditor floating window.

That is the only supported way to open the editor. The applet itself does not contain an edit button; bypass and editor-open are both handled from the CHAIN widget.

## What each control does

| Control | Kind | Default | Persisted setting |
|---|---|---|---|
| RX | Tab | Checked | — |
| TX | Tab | Unchecked | — |
| Analyzer / curve area | Indicator (view-only) | — | — |
| RX EQ enabled state | — | — | `ClientEqRxEnabled` |
| TX EQ enabled state | — | — | `ClientEqTxEnabled` |
| RX band configuration | — | — | `ClientEqRxBands` |
| TX band configuration | — | — | `ClientEqTxBands` |

The analyzer / curve area is 110 px tall and shows the summed EQ response for the selected path overlaid with a live FFT analyzer. It is view-only; use the floating editor for all band changes.

## Tips

- The CEQ applet starts hidden and only becomes visible after the EQ stage is enabled via the CHAIN widget or the floating editor.
- The RX tab is selected by default. If you intend to edit the TX path, click TX in the applet before opening the editor so the curve area reflects the correct path.
- Right-click the CEQ sub-container titlebar for options to float, pop out, or hide the applet panel.

## Troubleshooting

- **Double-clicking the EQ stage in the CHAIN widget does nothing** — The CEQ sub-container may be hidden. Verify the EQ stage is enabled in the CHAIN widget; the applet must be active before the editor can open.
- **The CEQ applet is not visible** — It is hidden until the EQ stage is toggled on. Enable the stage from the CHAIN widget to make the CEQ sub-container appear.

## Related

- [Parametric EQ (Client) overview](overview.md)
- [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md)
- [Switch between viewing RX and TX EQ](switch-between-viewing-rx-and-tx-eq.md)
- [See the live spectrum of the selected path](see-the-live-spectrum-of-the-selected-path.md)
- [Verify the summed curve matches your mental target](verify-the-summed-curve-matches-your-mental-target.md)
