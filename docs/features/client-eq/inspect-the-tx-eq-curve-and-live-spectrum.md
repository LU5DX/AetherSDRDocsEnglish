# Inspect the TX EQ curve and live spectrum

The "Aetherial TX EQ" applet shows the summed EQ response curve, a live FFT analyzer overlay, and a peak-hold trace for the TX audio path. Use this view to monitor how your transmit signal is being shaped without opening the full editor.

## Before you start

- The "Aetherial TX EQ" sub-container is hidden until the TX EQ stage is enabled. Enable it via the CHAIN widget or the floating editor ("Aetherial Parametric EQ — TX") before expecting the applet to appear.
- The applet lives inside the Aetherial Audio (TXDSP) parent container in the applet panel. If the applet panel is not visible, check `View > Applet Panel`.

## Steps

1. Locate the Aetherial Audio (TXDSP) parent container in the applet panel.
2. Find the "Aetherial TX EQ" sub-container inside it.
3. Look at the analyzer / curve area — the display showing the grid, summed EQ response, live FFT analyzer overlay, and peak-hold trace for the TX path.
4. Observe the summed EQ response line, which reflects the cumulative frequency response of all enabled TX bands.
5. Observe the live analyzer overlay, which shows real-time FFT of audio passing through the TX path. The overlay is idle when no audio is present and running when audio flows through the TX path.
6. Observe the peak-hold trace — an off-white line that tracks the highest level seen at each frequency bin and decays at approximately 10 dB/sec. To freeze the trace at its current maximum, open the floating editor and enable the Peak Hold button.

## What each control does

| Control | Description | Editable in applet |
|---|---|---|
| Analyzer / curve area | Displays the grid, summed EQ response curve, live FFT analyzer overlay, and peak-hold trace for the TX path. | No — view only |
| Summed EQ response | Shows the cumulative frequency response of all enabled TX bands. Appears flat when no bands are shaping the signal. Dims to grey when the EQ stage is bypassed. | No |
| Live analyzer overlay | Real-time FFT of audio on the TX path. Idle when no audio is present; running when audio flows. | No |
| Peak-hold trace | Off-white line showing the per-bin maximum level observed since the last reset. Decays approximately 10 dB/sec under normal operation. Freezes at the highest observed level when Peak Hold is enabled in the floating editor. | No — use Peak Hold button in the floating editor |
| Peak Hold | Toggle button in the floating editor header strip. When checked (amber background), the peak-hold trace stops decaying and holds at each frequency's highest observed level. Toggle off to resume normal decay. | Floating editor only |
| Filter family | Combo box in the floating editor header strip. Selects the HP/LP cascade mathematics: Butterworth (maximally flat passband), Chebyshev (steeper rolloff with 1 dB passband ripple), Bessel (linear phase / gentler rolloff), or Elliptic (steepest transition with ripple in both bands). Default is Butterworth. Applies only to HP and LP filter types; peak and shelf bands use their own fixed 2nd-order topology regardless. Persisted as `ClientEqTxFilterFamily` / `ClientEqRxFilterFamily`. | Floating editor only |
| Reset | Push button in the floating editor header strip. Resets all bands to the default 10-band template, restores the default band count, and resets the filter family to Butterworth. Saves immediately. Tooltip: "Reset all bands to default values". | Floating editor only |
| Output Fader | Vertical combined fader + level meter on the right edge of the floating editor. Drag to set post-EQ master gain; scroll wheel adjusts in 0.5 dB steps; double-click resets to 0 dB. Range: -36 to +12 dB. The level bar behind the handle shows the smoothed post-EQ peak in real time with the same green-amber-red gradient as the Tube level meter. Persisted as `ClientEqTxMasterGain` / `ClientEqRxMasterGain`. | Floating editor only |

Editing bands requires the floating editor. See [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md).

## Tips

- The applet is view-only. All band editing — adding, removing, and tuning — happens in the floating "Aetherial Parametric EQ — TX" editor, opened by double-clicking the TX EQ stage in the CHAIN widget.
- Use the peak-hold trace in the docked applet to spot resonances and harsh peaks while adjusting other controls. Open the floating editor and click Peak Hold to freeze the trace at its current maximum before making a tuning pass.
- To float, pop out, or hide the "Aetherial TX EQ" sub-container, right-click its titlebar.

## Troubleshooting

- **The "Aetherial TX EQ" sub-container is not visible** — The applet is hidden until the TX EQ stage is enabled. Enable it from the CHAIN widget or from the floating editor. See [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md).
- **The live analyzer overlay appears idle** — No audio is passing through the TX path. Transmit audio must be present for the FFT overlay to run.
- **The peak-hold trace is not moving** — Peak Hold is enabled in the floating editor. Click Peak Hold again to resume normal decay.

## Related

- [Aetherial Parametric EQ (TX / RX) overview](overview.md)
- [Inspect the RX EQ curve and live spectrum](inspect-the-rx-eq-curve-and-live-spectrum.md)
- [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md)
- [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md)
- [Verify the summed curve matches your mental target](verify-the-summed-curve-matches-your-mental-target.md)