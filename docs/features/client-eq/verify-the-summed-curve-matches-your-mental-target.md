# Verify the summed curve matches your mental target

The analyzer / curve area in the ClientEq applet shows the cumulative frequency response of all enabled bands for a path alongside a live FFT of audio passing through it. Use this view to confirm that what you have built in the editor produces the shape you intended.

## Before you start

- The EQ stage must be enabled. The applet is hidden until the EQ stage is enabled via the CHAIN widget or the floating editor.
- At least one band must be configured for the relevant path. The curve area displays "(no bands — add one in the editor)" when no bands exist.
- Open the floating editor first if you still need to add or tune bands. See [Open the floating editor to add / remove / tune bands](open-the-floating-editor-to-add-remove-tune-bands.md).

## Steps

1. Locate the CEQ sub-container inside the PooDoo Audio (TXDSP) parent container in the applet panel.
2. Look at the analyzer / curve area. The summed EQ response curve is drawn over the live FFT analyzer overlay.
3. Check that the curve rises and falls at the frequencies you expect. The vertical extent is ±18 dB. Gridlines appear at ±6 dB and ±12 dB; the 0 dB reference line is drawn slightly brighter. Frequency gridlines are labeled along the bottom at 20, 50, 100, 200, 500, 1k, 2k, 5k, 10k, and 20k Hz.
4. If you are checking the RX path, confirm the RX instance is bound. If you are checking the TX path, confirm the TX instance is bound. Each CEQ tile is bound to a single path at construction — RX tiles show only the RX response, TX tiles show only the TX response. See [Switch between viewing RX and TX EQ](switch-between-viewing-rx-and-tx-eq.md) if you need to view the other path.
5. Compare the summed curve shape against your target. If the shape is wrong, return to the floating editor to adjust band parameters.
6. While audio is passing through the path, observe the live analyzer overlay (the cyan-gradient filled region). Confirm the post-EQ spectrum matches the summed curve's shaping.

## What each control does

| Control | Kind | Behavior | Default | Setting key |
|---|---|---|---|---|
| Analyzer / curve area | Indicator | Displays the grid, summed EQ response for the bound path, and a live FFT analyzer overlay. View-only; 110 px tall. | — | — |
| Summed EQ response | Indicator state | Cumulative frequency response of all enabled bands. Shows "flat" when no bands contribute boost or cut; "shaped" when bands are active. | flat | `ClientEqRxBands` / `ClientEqTxBands` |
| Live analyzer overlay | Indicator state | Real-time FFT of audio passing through the bound path. "idle" when no audio is present; "running" when audio flows. | idle | — |

## Tips

- If the curve area shows "(no EQ connected)" the applet has not been linked to an audio engine. Ensure the radio is connected and the EQ stage has been enabled.
- The summed curve is drawn using an analog-prototype reference across the full 20 Hz–20 kHz canvas, so it represents the ideal response the digital filters approximate. Small deviations between the curve and measured audio are normal near Nyquist.
- The live FFT reflects audio post-EQ. If the FFT shape does not follow the summed curve, check that the EQ stage is not bypassed in the chain. See [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md).

## Troubleshooting

- **Curve area shows "(no bands — add one in the editor)"** — No bands have been added for the bound path. Open the floating editor and add at least one band.
- **Curve area shows "(no EQ connected)"** — The applet is not linked to the audio engine. Verify the radio is connected and the EQ stage is enabled via the CHAIN widget.
- **Live analyzer overlay is absent or empty** — No audio is passing through the path, or the FFT has not received data yet. Transmit or receive a signal and the overlay will populate.
- **Summed curve appears flat despite bands being configured** — The EQ stage may be bypassed. Check the CHAIN widget and confirm `ClientEqRxEnabled` or `ClientEqTxEnabled` is active for the relevant path.

## Related

- [Open the floating editor to add / remove / tune bands](open-the-floating-editor-to-add-remove-tune-bands.md)
- [See the live spectrum of the selected path](see-the-live-spectrum-of-the-selected-path.md)
- [Switch between viewing RX and TX EQ](switch-between-viewing-rx-and-tx-eq.md)
- [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md)
