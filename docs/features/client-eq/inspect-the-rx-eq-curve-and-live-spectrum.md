# Inspect the RX EQ curve and live spectrum

The "Aetherial RX EQ" applet gives you a compact, always-visible view of the RX equalizer's summed frequency response and a live FFT analyzer overlay of audio passing through the RX path. Use this to monitor the effect of your RX EQ settings at a glance without opening the full editor.

## Before you start

- The "Aetherial RX EQ" sub-container is hidden until the RX EQ stage is enabled. Enable it via the CHAIN widget or the floating editor before expecting the applet to appear.
- The applet lives inside the "Aetherial Audio (TXDSP)" parent container in the applet panel. Make sure the applet panel is visible (`View > Applet Panel`).

## Steps

1. In the applet panel, locate the "Aetherial Audio (TXDSP)" parent container.
2. Expand it and find the "Aetherial RX EQ" sub-container.
3. Look at the analyzer / curve area — the 110 px tall display showing the frequency grid.
4. The summed EQ response curve shows the cumulative frequency response of all enabled RX bands. A flat line means no net shaping; a shaped line reflects the active band settings stored in `ClientEqRxBands`.
5. The live analyzer overlay running across the same area shows the real-time FFT of audio passing through the RX path. When audio is present, the overlay is active; when no audio passes through, the overlay is idle.
6. To inspect in more detail or edit bands, double-click the RX EQ stage in the CHAIN widget to open the floating "Aetherial Parametric EQ — RX" editor.

## What each control does

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| Analyzer / curve area | Displays the summed EQ response curve and live FFT analyzer overlay for the RX path. View-only in this applet. | — | — |
| Summed EQ response | Shows the cumulative frequency response of all enabled RX bands. | flat | `ClientEqRxBands` |
| Live analyzer overlay | Real-time FFT of audio passing through the RX path. | idle | — |
| RX EQ enabled state | Whether the RX EQ stage is active. Controlled from the CHAIN widget or the floating editor, not from within this applet. | — | `ClientEqRxEnabled` |

## Tips

- The analyzer / curve area is view-only in the applet. To add, remove, or tune bands, open the floating editor by double-clicking the RX EQ stage in the CHAIN widget.
- If you want to float, pop out, or hide the "Aetherial RX EQ" sub-container, right-click its titlebar for those options.

## Troubleshooting

- **The "Aetherial RX EQ" sub-container is not visible** — The applet is hidden until the RX EQ stage is enabled. Enable the stage from the CHAIN widget or the floating editor. Check that `ClientEqRxEnabled` is set.
- **The live analyzer overlay appears idle even during reception** — Audio must be passing through the RX path for the FFT to run. Confirm the radio is connected and audio routing is active.

## Related

- [Aetherial Parametric EQ (TX / RX) overview](overview.md)
- [Inspect the TX EQ curve and live spectrum](inspect-the-tx-eq-curve-and-live-spectrum.md)
- [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md)
- [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md)
