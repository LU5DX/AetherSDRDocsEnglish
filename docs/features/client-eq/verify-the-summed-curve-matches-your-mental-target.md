# Verify the summed curve matches your mental target

Use the curve area in the "Aetherial TX EQ" or "Aetherial RX EQ" applet tile to confirm that the combined response of all your enabled bands matches the shape you intended before transmitting or listening.

## Before you start

- The matching EQ stage must be enabled. If the applet tile is hidden, enable the EQ stage via the CHAIN widget or open the floating editor first.
- At least one band should be configured so the curve shows a non-flat response. A flat line means either no bands are active or all bands are bypassed.

## Steps

1. Locate the "Aetherial TX EQ" or "Aetherial RX EQ" sub-container inside the Aetherial Audio (TXDSP) parent container in the applet panel.
2. Look at the curve area — the 110 px display that fills the tile. The white (or highlighted) line drawn across the frequency grid is the summed EQ response: the cumulative effect of every enabled band for that path.
3. Compare the shape of the summed response against your target:
   - A boost at a particular frequency appears as an upward peak.
   - A cut appears as a downward dip.
   - High-pass and low-pass filtering appears as a rolloff at the edges.
4. If the live FFT analyzer overlay is running, a second trace shows the real-time spectrum of audio passing through that path. Use it to cross-check that the curve is affecting the audio where you expect.
5. If the shape does not match your target, double-click the EQ stage in the CHAIN widget for the same path (TX or RX) to open the floating editor titled "Aetherial Parametric EQ — TX" or "Aetherial Parametric EQ — RX", then adjust your bands there. The curve in the applet tile updates as you make changes.

## What each control does

| Control | Kind | Behavior | Setting key |
|---|---|---|---|
| Analyzer / curve area | Indicator (view-only) | Displays the summed EQ response for this tile's path (TX or RX) and a live FFT analyzer overlay of audio passing through that path. Not editable from the applet; editing requires the floating editor. | — |
| Summed EQ response | Indicator state | Shows the cumulative frequency response of all enabled bands. Displays as flat when no bands are active or shaping is zero; displays as shaped when one or more bands alter the response. | `ClientEqTxBands` (TX) / `ClientEqRxBands` (RX) |
| Live analyzer overlay | Indicator state | Real-time FFT of audio passing through this path. Runs while the applet is visible; idle when no audio is flowing. | — |

## Tips

- The applet tile is view-only. You cannot drag bands or change parameters from it. All editing happens in the floating editor.
- Both the TX and RX tiles are independent. Checking one does not tell you anything about the other path.
- If the curve looks correct in the applet but the audio does not sound right, confirm the EQ stage is not in bypass. A bypassed stage passes audio unchanged regardless of what the curve shows.

## Troubleshooting

- **The curve area is flat even though bands are configured** — The EQ stage may be disabled or bypassed. Check the CHAIN widget and confirm `ClientEqTxEnabled` or `ClientEqRxEnabled` is active for the relevant path.
- **The applet tile is not visible** — The EQ stage has not been enabled yet. Enable it via the CHAIN widget or open the floating editor, which also makes the tile appear.
- **The live analyzer overlay is not moving** — No audio is passing through that path, or the EQ stage is disabled. Transmit audio (TX path) or receive a signal (RX path) and confirm the stage is enabled.

## Related

- [Aetherial Parametric EQ (TX / RX) overview](overview.md)
- [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md)
- [Inspect the TX EQ curve and live spectrum](inspect-the-tx-eq-curve-and-live-spectrum.md)
- [Inspect the RX EQ curve and live spectrum](inspect-the-rx-eq-curve-and-live-spectrum.md)
- [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md)
