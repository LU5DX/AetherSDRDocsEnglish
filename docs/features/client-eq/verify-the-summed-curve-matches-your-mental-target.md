# Verify the summed curve matches your mental target

After adjusting bands in the parametric EQ editor, use the applet tiles to confirm that the summed EQ response curve reflects the overall shape you intended, with the live analyzer overlay showing how real audio aligns with it.

## Before you start

- The EQ stage you want to check must be enabled. If the "Aetherial TX EQ" or "Aetherial RX EQ" tile is hidden, enable the matching EQ stage via the CHAIN widget first.
- Bands must already be configured. If you have not yet added or tuned bands, see [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md).

## Steps

1. Locate the "Aetherial TX EQ" or "Aetherial RX EQ" sub-container in the Aetherial Audio (TXDSP) parent container in the applet panel.
2. Look at the curve area — the 110 px tall display showing a grid, the summed EQ response, the live FFT analyzer overlay, and the peak-hold trace.
3. Trace the summed EQ response curve across the frequency axis. It reflects the cumulative response of all enabled bands for that path.
4. Compare the curve shape to your intended target. Peaks, shelves, and high-pass or low-pass roll-offs appear as deviations from a flat line.
5. Watch the live analyzer overlay while audio passes through. The overlay shows the real-time FFT of audio on that path, letting you confirm that the shaped response is affecting the spectrum as expected.
6. Observe the peak-hold trace (off-white line) to identify frequency bins that have reached high levels recently. The trace decays at approximately 10 dB/sec between updates, so transient resonances remain visible for a short time after they occur.
7. If the curve does not match your target, double-click the EQ stage in the CHAIN widget to reopen the frameless editor ("Aetherial Parametric EQ — TX" or "— RX") and adjust bands there.

## What each control does

| Control | Description | Notes |
|---|---|---|
| Analyzer / curve area | Displays the grid, summed EQ response, live FFT analyzer overlay, and peak-hold trace for the tile's locked path (TX or RX). | View-only in the applet tile. Editing requires the floating editor. |
| Summed EQ response | The cumulative frequency response of all enabled bands on this path. Appears flat when no bands alter the response; shaped when one or more bands are active. Dims to grey when the EQ stage is bypassed. | Persisted via `ClientEqTxBands` (TX) or `ClientEqRxBands` (RX). |
| Live analyzer overlay | Real-time FFT of audio passing through this path. Shows idle when no audio is present, running when audio is active. Filled with a cyan gradient from 0 dB at the top fading to transparent at the bottom. | Provides visual confirmation that the curve is affecting real signal. |
| Peak-hold trace | Off-white line drawn on top of the live analyzer. Each frequency bin holds the highest level observed, then decays at approximately 10 dB/sec. Stops decaying when **Peak Hold** is checked in the floating editor. | Helps identify resonances and harsh peaks while tuning. Visible in both the applet tile and the floating editor. |
| Peak Hold | Toggle button in the floating editor header strip. When checked (amber background), the peak-hold trace stops decaying — every frequency bin's highest observed level is held until the button is toggled off. | Located in the floating editor only, not in the docked applet tile. Toggle off to resume normal decay. |
| Filter family | Combo box in the floating editor header strip. Selects the mathematics used for HP and LP cascade filters. Options: Butterworth (maximally flat passband), Chebyshev (steeper rolloff with 1 dB passband ripple), Bessel (linear phase / gentler rolloff), Elliptic (steepest transition with ripple in both bands). Default: Butterworth. | Applies only to HP and LP filter types. Peak and shelf bands use their own fixed 2nd-order topology regardless. Persisted separately per path: `ClientEqTxFilterFamily` / `ClientEqRxFilterFamily`. |
| Reset | Push button in the floating editor header strip. Resets all bands to the default 10-band template, restores the default band count, and resets the filter family to Butterworth. Saves immediately. | Tooltip: "Reset all bands to default values". Located in the floating editor only. |
| Output Fader | Vertical combined fader + level meter on the right edge of the floating editor. Drag to set post-EQ master gain; scroll wheel adjusts in 0.5 dB steps; double-click resets to 0 dB. The level bar behind the handle shows the smoothed post-EQ peak in real time with the same green-amber-red gradient as the Tube level meter. | Persisted separately per path: `ClientEqTxMasterGain` / `ClientEqRxMasterGain`. Tooltip: "Output gain (dB). Drag to set, wheel for fine step, double-click to reset to 0 dB." Gain range is linear 0.0 to ~4.0; the scale labels run from -40 to 0 dB. Located in the floating editor only — not in the docked applet tile. |

## Tips

- The applet tile is view-only. No editing happens here. All band changes must be made in the frameless editor opened from the CHAIN widget.
- There is one tile per side. "Aetherial TX EQ" is locked to the TX path; "Aetherial RX EQ" is locked to the RX path. They do not share a selector.
- Use **Peak Hold** in the floating editor to freeze the peak-hold trace while you tune a band. This makes it easier to see whether a resonance has been reduced without the trace decaying away between adjustments. Toggle **Peak Hold** off when you are done to resume normal decay.
- If the curve appears flat but you expect shaping, check whether the EQ stage is bypassed. A bypassed stage does not apply its bands to the audio path even though the curve display may still render the shape. See [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md).
- Use **Reset** in the floating editor to return the EQ to a known starting point. All bands, band count, and the filter family are restored to their defaults and saved immediately.

## Troubleshooting

- **The applet tile is not visible** — The EQ stage is not enabled. Enable it via the CHAIN widget or the floating editor. The tile remains hidden until the matching stage is active.
- **The summed curve is flat despite configured bands** — All bands may have 0 dB gain, or the EQ stage may be bypassed. Open the frameless editor to inspect individual band settings, or check the bypass state in the CHAIN widget.
- **The live analyzer overlay is idle** — No audio is passing through that path. For RX, ensure the radio is receiving and audio routing is active. For TX, ensure a signal is being processed through the TX DSP chain.
- **The peak-hold trace is not moving** — Check whether **Peak Hold** is checked in the floating editor. If it is checked (amber background), the trace is frozen intentionally. Toggle it off to resume decay.

## Related

- [Aetherial Parametric EQ (TX / RX) overview](overview.md)
- [Inspect the TX EQ curve and live spectrum](inspect-the-tx-eq-curve-and-live-spectrum.md)
- [Inspect the RX EQ curve and live spectrum](inspect-the-rx-eq-curve-and-live-spectrum.md)
- [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md)
- [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md)