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
6. Observe the peak-hold trace — an off-white line that tracks the highest level seen at each frequency bin and decays at approximately 10 dB/sec. The trace operates on raw bins so peak detection is sample-accurate; display smoothing is applied separately and does not affect the underlying peak values. To freeze the trace at its current maximum, open the floating editor and enable the Peak Hold button.
7. Observe the dashed yellow filter cutoff guide lines overlaid on the canvas. These mark the radio's current TX low and high filter cutoff frequencies. In the docked applet the lines are view-only; drag them in the floating editor to move the radio's passband in real time.
8. Observe the audio band-plan strip at the bottom of the canvas. This 14 px strip shows E-SSB / SSB / AM-FM modulation regions as a reference and is always visible.

## What each control does

| Control | Description | Editable in applet |
|---|---|---|
| Analyzer / curve area | ClientEqCurveWidget — minimum 110 px tall in the docked applet, locked to the path supplied at construction (Path::Tx or Path::Rx). Shows log-freq grid (20 Hz–20 kHz, ±18 dB), summed EQ response, live FFT filled-gradient analyzer (25 Hz refresh), and a peak-hold trace that decays ~10 dB/sec between updates. Dashed yellow vertical lines mark the radio's current TX low/high filter cutoffs (TX tile) or RX passband edges (RX tile). | View-only in the applet; editing happens in the frameless ClientEqEditor. The peak-hold trace can be frozen (stops decaying) via the Peak Hold button in the editor toolbar. The cutoff guide lines are draggable in the editor canvas to move the radio's passband in real time. |
| Summed EQ response | Shows the cumulative frequency response of all enabled TX bands. Appears flat when no bands are shaping the signal. Dims to grey when the EQ stage is bypassed. | No |
| Live analyzer overlay | Real-time FFT of audio on the TX path. Idle when no audio is present; running when audio flows. Refreshed at 25 Hz. | No |
| Peak-hold trace | Off-white line showing the per-bin maximum level observed since the last reset. Operates on raw bins so peak detection is sample-accurate. Decays approximately 10 dB/sec under normal operation. Display smoothing is applied to the peak trace separately via `ClientEqSmoothingFraction` and affects only the visual representation. Freezes at the highest observed level when Peak Hold is enabled in the floating editor. | No — use Peak Hold button in the floating editor |
| Peak Hold | Toggle button in the floating editor header strip. When checked (amber background), the peak-hold trace stops decaying and holds at each frequency's highest observed level. Toggle off to resume normal decay. | Floating editor only |
| Smoothing | Combo box in the floating editor header strip. Applies fractional-octave power-averaging to the analyzer trace for display — does not affect EQ math. Options: Off (1/96), 1/24, 1/12, 1/6, 1/3. Lower fraction = smoother (1/3 is most smoothed; 1/96 is effectively off). Smoothing runs after the peak-hold update each frame so both the live and peak-hold traces reflect current data before averaging is applied. Shared between TX and RX editors. Persisted as `ClientEqSmoothingFraction`. Tooltip: "Fractional-octave smoothing applied to the analyzer trace. Lower fraction = smoother (1/3 = most, 1/96 = off). Affects display only — EQ math is unchanged." | Floating editor only |
| Filter family | Combo box in the floating editor header strip. Selects the HP/LP cascade mathematics: Butterworth (maximally flat passband), Chebyshev (steeper rolloff with 1 dB passband ripple), Bessel (linear phase / gentler rolloff), or Elliptic (steepest transition with ripple in both bands). Default is Butterworth. Applies only to HP and LP filter types; peak and shelf bands use their own fixed 2nd-order topology regardless. Persisted as `ClientEqTxFilterFamily` / `ClientEqRxFilterFamily`. | Floating editor only |
| Reset | Push button in the floating editor header strip. Resets all bands to the default 10-band template, restores the default band count, and resets the filter family to Butterworth. Saves immediately. Tooltip: "Reset all bands to default values". | Floating editor only |
| Output Fader | Vertical combined fader + level meter on the right edge of the floating editor. Drag to set post-EQ master gain; scroll wheel adjusts in 0.5 dB steps; double-click resets to 0 dB. Range: -36 to +12 dB. The level bar behind the handle shows the smoothed post-EQ peak in real time with the same green-amber-red gradient as the Tube level meter. Persisted as `ClientEqTxMasterGain` / `ClientEqRxMasterGain`. | Floating editor only |
| Filter-type icon row | A row of 8 custom-painted icons (one per band slot) at the top of the editor canvas area. Each icon draws the current filter shape (peak bell, shelf ramp, HP/LP slope) in its band's palette colour. Click an icon to cycle through the filter types for that band; clicking also selects the band, highlighting its handle on the canvas and its column in the parameter row. Icons dim to 35 % opacity when the band is bypassed. | Floating editor only |
| Parameter text row | A row of 8 text columns (one per band slot) below the canvas showing each band's Freq, Gain, and Q values. Values update live during canvas drags. Clicking a column selects that band. | Floating editor only |
| Filter cutoff guide lines (TX / RX) | Dashed yellow vertical lines overlaid on the canvas at the radio's current TX low/high filter cutoff (TX tile) or RX passband edges (RX tile). Hovering near a line changes the cursor to a horizontal-resize arrow. Dragging a line in the editor moves the radio's corresponding filter cutoff in real time. The TX and RX applets receive cutoff updates independently: the TX applet ignores RX cutoff changes and the RX applet ignores TX cutoff changes. Pass 0 for an edge to suppress that guide. | View-only in the applet; draggable in the floating editor only |
| Audio band-plan strip | A 14 px strip permanently visible at the bottom of the EQ canvas. Shows E-SSB / SSB / AM-FM modulation regions as a frequency reference. Cursor interaction in this area is excluded from band-handle hit-testing. | No |

Editing bands requires the floating editor. See [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md).

## Tips

- The applet is view-only. All band editing — adding, removing, and tuning — happens in the floating "Aetherial Parametric EQ — TX" editor, opened by double-clicking the TX EQ stage in the CHAIN widget.
- Use the peak-hold trace in the docked applet to spot resonances and harsh peaks while adjusting other controls. Open the floating editor and click Peak Hold to freeze the trace at its current maximum before making a tuning pass.
- Because smoothing runs after each peak-hold update, enabling Smoothing in the floating editor does not cause the peak trace to lag behind the live analyzer — both are smoothed from the same current frame.
- The dashed yellow filter cutoff guide lines in the applet update automatically whenever the radio's TX or RX filter settings change. To adjust the passband, drag the guide lines in the floating editor rather than navigating to the radio's filter controls separately.
- To float, pop out, or hide the "Aetherial TX EQ" sub-container, right-click its titlebar.

## Troubleshooting

- **The "Aetherial TX EQ" sub-container is not visible** — The applet is hidden until the TX EQ stage is enabled. Enable it from the CHAIN widget or from the floating editor. See [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md).
- **The live analyzer overlay appears idle** — No audio is passing through the TX path. Transmit audio must be present for the FFT overlay to run.
- **The peak-hold trace is not moving** — Peak Hold is enabled in the floating editor. Click Peak Hold again to resume normal decay.
- **The filter cutoff guide lines are not visible** — The radio has reported a cutoff value of 0 for that edge, which suppresses the corresponding guide line. Check the radio's TX or RX filter settings.

## Related

- [Aetherial Parametric EQ (TX / RX) overview](overview.md)
- [Inspect the RX EQ curve and live spectrum](inspect-the-rx-eq-curve-and-live-spectrum.md)
- [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md)
- [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md)
- [Verify the summed curve matches your mental target](verify-the-summed-curve-matches-your-mental-target.md)