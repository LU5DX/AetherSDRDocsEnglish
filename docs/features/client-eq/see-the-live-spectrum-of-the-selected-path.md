# See the live spectrum of the selected path

The analyzer overlay in the ClientEqApplet shows a real-time FFT of the audio passing through the currently bound path (RX or TX), drawn on top of the summed EQ response curve. Use this to confirm what the audio actually looks like after equalization, without opening the floating editor.

## Before you start

- The ClientEqApplet (labeled "CEQ") must be visible. It is hidden until the EQ stage is enabled via the CHAIN widget or the floating editor. See [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md) if the applet is not shown.
- Audio must be flowing through the selected path for the analyzer overlay to display anything other than an idle state.

## Steps

1. Locate the "CEQ" sub-container inside the PooDoo Audio (TXDSP) parent container in the applet panel.
2. The analyzer / curve area updates automatically — no action is needed to start it. The live FFT overlay appears as a filled cyan gradient over the grid whenever audio is present on the bound path.
3. To view the spectrum for the other path, switch the bound path by selecting the appropriate chain tile. Each CEQ applet instance is fixed to either RX or TX at construction; there is no RX / TX selector inside the applet itself. See [Switch between viewing RX and TX EQ](switch-between-viewing-rx-and-tx-eq.md).

## What each control does

| Control | Kind | Default | Behavior |
|---|---|---|---|
| Analyzer / curve area | Indicator (view-only) | — | Displays a live FFT analyzer overlay (cyan filled gradient, 20 Hz–20 kHz, −70 dB to 0 dB scale) and the summed EQ response for the bound path. Editing is done in the floating ClientEqEditor, not here. |
| Summed EQ response | Indicator | Flat (no bands) | Shows the cumulative frequency response of all enabled bands. Displays "(no bands — add one in the editor)" when no bands exist, or "(no EQ connected)" if the applet has no EQ bound. |
| Live analyzer overlay | Indicator | Idle | Real-time FFT of audio passing through the bound path, drawn beneath the EQ curve. Active only when audio is flowing. |

Persisted settings that affect what is displayed: `ClientEqRxEnabled`, `ClientEqTxEnabled`, `ClientEqRxBands`, `ClientEqTxBands`.

## Tips

- The frequency grid runs from 20 Hz to 20 kHz on a logarithmic scale. dB gridlines appear at ±6 dB and ±12 dB, with a brighter 0 dB reference line at center.
- The analyzer overlay is drawn beneath the EQ curve and per-band indicators, so the summed response remains readable even when signal is present.
- The FFT covers only up to the Nyquist frequency of the audio path; no content is drawn above that point, so a gap at the high end of the display is normal.
- The applet is 110 px tall and view-only. To add, remove, or tune bands, double-click the EQ stage in the CHAIN widget to open the floating editor.

## Troubleshooting

- **Analyzer overlay is not visible** — Confirm audio is actively flowing through the bound path. If the path is idle (no receive audio or no active transmission), the FFT has no signal to display and the overlay will not appear.
- **Display shows "(no EQ connected)"** — The applet has not been bound to an audio engine instance. Ensure the EQ stage is enabled via the CHAIN widget so the applet is initialized correctly.
- **Display shows "(no bands — add one in the editor)"** — No EQ bands have been configured for this path. Open the floating editor to add at least one band. See [Open the floating editor to add / remove / tune bands](open-the-floating-editor-to-add-remove-tune-bands.md).
- **CEQ sub-container is not visible** — The applet hides itself until the EQ stage is enabled. See [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md).

## Related

- [Switch between viewing RX and TX EQ](switch-between-viewing-rx-and-tx-eq.md)
- [Verify the summed curve matches your mental target](verify-the-summed-curve-matches-your-mental-target.md)
- [Open the floating editor to add / remove / tune bands](open-the-floating-editor-to-add-remove-tune-bands.md)
- [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md)
