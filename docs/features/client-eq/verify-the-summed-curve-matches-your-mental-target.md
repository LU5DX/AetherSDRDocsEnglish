# Verify the summed curve matches your mental target

After adjusting bands in the parametric EQ editor, use the applet tiles to confirm that the summed EQ response curve reflects the overall shape you intended, with the live analyzer overlay showing how real audio aligns with it.

## Before you start

- The EQ stage you want to check must be enabled. If the "Aetherial TX EQ" or "Aetherial RX EQ" tile is hidden, enable the matching EQ stage via the CHAIN widget first.
- Bands must already be configured. If you have not yet added or tuned bands, see [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md).

## Steps

1. Locate the "Aetherial TX EQ" or "Aetherial RX EQ" sub-container in the Aetherial Audio (TXDSP) parent container in the applet panel.
2. Look at the curve area — the 110 px tall display showing a grid, the summed EQ response, and the live FFT analyzer overlay.
3. Trace the summed EQ response curve across the frequency axis. It reflects the cumulative response of all enabled bands for that path.
4. Compare the curve shape to your intended target. Peaks, shelves, and high-pass or low-pass roll-offs appear as deviations from a flat line.
5. Watch the live analyzer overlay while audio passes through. The overlay shows the real-time FFT of audio on that path, letting you confirm that the shaped response is affecting the spectrum as expected.
6. If the curve does not match your target, double-click the EQ stage in the CHAIN widget to reopen the frameless editor ("Aetherial Parametric EQ — TX" or "— RX") and adjust bands there.

## What each control does

| Control | Description | Notes |
|---|---|---|
| Analyzer / curve area | Displays the grid, summed EQ response, and live FFT analyzer overlay for the tile's locked path (TX or RX). | View-only in the applet tile. Editing requires the floating editor. |
| Summed EQ response | The cumulative frequency response of all enabled bands on this path. Appears flat when no bands alter the response; shaped when one or more bands are active. | Persisted via `ClientEqTxBands` (TX) or `ClientEqRxBands` (RX). |
| Live analyzer overlay | Real-time FFT of audio passing through this path. Shows idle when no audio is present, running when audio is active. | Provides visual confirmation that the curve is affecting real signal. |

## Tips

- The applet tile is view-only. No editing happens here. All band changes must be made in the frameless editor opened from the CHAIN widget.
- There is one tile per side. "Aetherial TX EQ" is locked to the TX path; "Aetherial RX EQ" is locked to the RX path. They do not share a selector.
- If the curve appears flat but you expect shaping, check whether the EQ stage is bypassed. A bypassed stage does not apply its bands to the audio path even though the curve display may still render the shape. See [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md).

## Troubleshooting

- **The applet tile is not visible** — The EQ stage is not enabled. Enable it via the CHAIN widget or the floating editor. The tile remains hidden until the matching stage is active.
- **The summed curve is flat despite configured bands** — All bands may have 0 dB gain, or the EQ stage may be bypassed. Open the frameless editor to inspect individual band settings, or check the bypass state in the CHAIN widget.
- **The live analyzer overlay is idle** — No audio is passing through that path. For RX, ensure the radio is receiving and audio routing is active. For TX, ensure a signal is being processed through the TX DSP chain.

## Related

- [Aetherial Parametric EQ (TX / RX) overview](overview.md)
- [Inspect the TX EQ curve and live spectrum](inspect-the-tx-eq-curve-and-live-spectrum.md)
- [Inspect the RX EQ curve and live spectrum](inspect-the-rx-eq-curve-and-live-spectrum.md)
- [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md)
- [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md)
