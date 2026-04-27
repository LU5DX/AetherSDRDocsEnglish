# Inspect the TX EQ curve and live spectrum

The "Aetherial TX EQ" applet shows the summed EQ response curve and a live FFT analyzer overlay for the TX audio path. Use this view to monitor how your transmit signal is being shaped without opening the full editor.

## Before you start

- The "Aetherial TX EQ" sub-container is hidden until the TX EQ stage is enabled. Enable it via the CHAIN widget or the floating editor ("Aetherial Parametric EQ — TX") before expecting the applet to appear.
- The applet lives inside the Aetherial Audio (TXDSP) parent container in the applet panel. If the applet panel is not visible, check `View > Applet Panel`.

## Steps

1. Locate the Aetherial Audio (TXDSP) parent container in the applet panel.
2. Find the "Aetherial TX EQ" sub-container inside it.
3. Look at the analyzer / curve area — the 110 px tall display showing the grid, summed EQ response, and live FFT analyzer overlay for the TX path.
4. Observe the summed EQ response line, which reflects the cumulative frequency response of all enabled TX bands.
5. Observe the live analyzer overlay, which shows real-time FFT of audio passing through the TX path. The overlay is idle when no audio is present and running when audio flows through the TX path.

## What each control does

| Control | Description | Editable in applet |
|---|---|---|
| Analyzer / curve area | Displays the grid, summed EQ response curve, and live FFT analyzer overlay for the TX path. | No — view only |
| Summed EQ response | Shows the cumulative frequency response of all enabled TX bands. Appears flat when no bands are shaping the signal. | No |
| Live analyzer overlay | Real-time FFT of audio on the TX path. Idle when no audio is present; running when audio flows. | No |

Editing bands requires the floating editor. See [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md).

## Tips

- The applet is view-only. All band editing — adding, removing, and tuning — happens in the floating "Aetherial Parametric EQ — TX" editor, opened by double-clicking the TX EQ stage in the CHAIN widget.
- To float, pop out, or hide the "Aetherial TX EQ" sub-container, right-click its titlebar.

## Troubleshooting

- **The "Aetherial TX EQ" sub-container is not visible** — The applet is hidden until the TX EQ stage is enabled. Enable it from the CHAIN widget or from the floating editor. See [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md).
- **The live analyzer overlay appears idle** — No audio is passing through the TX path. Transmit audio must be present for the FFT overlay to run.

## Related

- [Aetherial Parametric EQ (TX / RX) overview](overview.md)
- [Inspect the RX EQ curve and live spectrum](inspect-the-rx-eq-curve-and-live-spectrum.md)
- [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md)
- [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md)
- [Verify the summed curve matches your mental target](verify-the-summed-curve-matches-your-mental-target.md)
