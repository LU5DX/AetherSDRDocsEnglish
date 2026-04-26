# Inspect the TX EQ curve and live spectrum

The "Aetherial TX EQ" tile in the applet panel shows the summed EQ response curve and a live FFT analyzer overlay for the TX audio path. Use this view to monitor your transmit equalization at a glance without opening the full editor.

## Before you start

- The "Aetherial TX EQ" sub-container is hidden until the TX EQ stage is enabled. Enable it via the CHAIN widget or the floating editor ("Aetherial Parametric EQ — TX") first.
- The "Aetherial TX EQ" tile lives inside the Aetherial Audio (TXDSP) parent container in the applet panel. Confirm that container is visible before proceeding.

## Steps

1. Locate the **Aetherial Audio (TXDSP)** parent container in the applet panel.
2. Expand it to reveal the **Aetherial TX EQ** sub-container.
3. Look at the analyzer / curve area — the 110 px tall display showing the frequency grid, summed EQ response, and live FFT overlay for the TX path.
4. Transmit audio (or key the radio) to drive the live analyzer overlay from idle to running.
5. Observe the summed EQ response curve, which reflects the cumulative frequency response of all enabled TX bands (`ClientEqTxBands`).

## What each control does

| Control | Behavior | Setting key |
|---|---|---|
| Analyzer / curve area | Displays the frequency grid, summed EQ response curve, and a real-time FFT analyzer overlay locked to the TX audio path. View-only in this tile. | — |
| Summed EQ response | Shows the combined frequency response of all enabled TX bands. Appears flat when no bands are active or all are bypassed. | `ClientEqTxBands` |
| Live analyzer overlay | Real-time FFT of audio passing through the TX path. Runs while audio is present; idle when no audio is flowing. | — |

The TX EQ enabled state is persisted in `ClientEqTxEnabled`.

## Tips

- The tile is view-only. To add, remove, or tune bands, double-click the TX EQ stage in the CHAIN widget to open the floating editor titled "Aetherial Parametric EQ — TX".
- Right-click the "Aetherial TX EQ" sub-container titlebar to float, pop-out, or hide the tile independently of the rest of the applet panel.
- If the curve area appears blank or the tile is not visible, the TX EQ stage may still be disabled. Check `ClientEqTxEnabled` by enabling the stage from the CHAIN widget.

## Troubleshooting

- **"Aetherial TX EQ" sub-container is not visible** — The tile is hidden until the TX EQ stage is enabled. Enable the stage via the CHAIN widget or the floating editor, then the sub-container will appear inside Aetherial Audio (TXDSP).
- **Live analyzer overlay stays idle during transmit** — Confirm audio is actually reaching the TX DSP path. If no audio engine is connected to the applet, the FFT has no samples to display.

## Related

- [Aetherial Parametric EQ (TX / RX) overview](overview.md)
- [Inspect the RX EQ curve and live spectrum](inspect-the-rx-eq-curve-and-live-spectrum.md)
- [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md)
- [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md)
- [Verify the summed curve matches your mental target](verify-the-summed-curve-matches-your-mental-target.md)
