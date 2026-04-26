# Inspect the RX EQ curve and live spectrum

The "Aetherial RX EQ" applet shows the summed frequency response of your RX equalizer bands alongside a real-time FFT analyzer overlay. Use it to verify that your RX EQ is shaping audio the way you intend without opening the full editor.

## Before you start

- The "Aetherial RX EQ" sub-container is hidden until the RX EQ stage is enabled. Enable it via the CHAIN widget or the floating editor first.
- The applet lives inside the Aetherial Audio (TXDSP) parent container in the applet panel. Make sure the applet panel is visible (`View > Applet Panel`).

## Steps

1. Locate the "Aetherial Audio (TXDSP)" parent container in the applet panel.
2. Expand it to find the "Aetherial RX EQ" sub-container.
3. Look at the analyzer / curve area — the 110 px tall display inside the tile. It shows two overlaid elements:
   - **Summed EQ response** — the cumulative frequency response of all enabled RX bands.
   - **Live analyzer overlay** — a real-time FFT of audio passing through the RX path.
4. Audio must be passing through the RX path for the live analyzer overlay to show activity. Receive a signal or play audio through the chain to see the FFT animate.

## What each control does

| Control | Behavior | Setting key |
|---|---|---|
| Analyzer / curve area | View-only display showing the summed EQ response curve and live FFT analyzer overlay for the RX path. Editing is not available here. | — |
| Summed EQ response | Displays the cumulative frequency response of all enabled bands. Appears flat when no bands are active or all are set to 0 dB. | `ClientEqRxBands` |
| Live analyzer overlay | Real-time FFT of audio passing through the RX path. Idle when no audio is present; animates when audio flows. | `ClientEqRxEnabled` |

## Tips

- The analyzer / curve area is view-only in the applet. To add, remove, or tune bands, open the frameless editor by double-clicking the RX EQ stage in the CHAIN widget.
- Right-click the "Aetherial RX EQ" sub-container titlebar to float, pop-out, or hide it if you want to position it independently.
- The live analyzer overlay runs only while audio is flowing through the RX path. If the overlay appears idle, confirm you are receiving audio and that `ClientEqRxEnabled` is active.

## Troubleshooting

- **"Aetherial RX EQ" sub-container is not visible** — The applet is hidden until the RX EQ stage is enabled. Enable it from the CHAIN widget or the floating editor. See [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md).
- **Live analyzer overlay shows no activity** — No audio is passing through the RX path. Tune to a signal or otherwise route audio through the RX chain.
- **Summed EQ response appears flat** — No bands are configured, all bands are bypassed, or all bands are set to 0 dB gain. Open the editor to inspect band settings. See [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md).

## Related

- [Aetherial Parametric EQ (TX / RX) overview](overview.md)
- [Inspect the TX EQ curve and live spectrum](inspect-the-tx-eq-curve-and-live-spectrum.md)
- [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md)
- [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md)
- [Verify the summed curve matches your mental target](verify-the-summed-curve-matches-your-mental-target.md)
