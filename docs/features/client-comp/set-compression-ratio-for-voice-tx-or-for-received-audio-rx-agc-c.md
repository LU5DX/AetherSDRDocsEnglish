# Set Compression Ratio for Voice (TX) or Received Audio (RX AGC-C)

The Ratio knob controls how hard the compressor clamps peaks once the signal crosses the threshold. A higher ratio gives a more aggressive squeeze on loud voice peaks (TX side) or loud received audio (RX AGC-C side).

## Before you start

- The compressor stage must be enabled (bypass off) on the side you want to adjust. When the stage is bypassed, the entire applet tile dims to approximately 55% opacity to indicate it is inactive. See [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md).
- Open the Aetherial Audio (TXDSP) parent container and expand the relevant sub-container: "Aetherial Compressor" for TX, or "Aetherial AGC-C" for RX.

## Steps

1. Locate the five-knob row at the bottom of the applet tile. The knobs are labeled Thresh, Ratio, Attack, Release, and Makeup, left to right.
2. Turn the **Ratio** knob to set the compression ratio.
   - For TX voice compression, this knob persists to `ClientCompTxRatio`.
   - For RX AGC-C, this knob persists to `ClientCompRxRatio`.
3. Read the current value from the label beneath the knob. It is formatted as `X.XX:1` (for example, `3.00:1`).
4. Optionally click the value label beneath a knob to enter a precise numeric value. The label turns into an editable text field with a dark background and cyan border. Type a value and press Enter, or click elsewhere, to commit the new value. Press Escape to cancel editing and restore the previous value. This inline editor is available on all five knobs (Thresh, Ratio, Attack, Release, Makeup).
5. Watch the gain-reduction bar and the envelope ball on the transfer curve while you speak (TX) or while audio plays (RX) to confirm the ratio is producing the intended amount of gain reduction.

## What each control does

| Control | Default        | Valid range      |
|---------|----------------|------------------|
| Ratio   | 3.0            | 1.0 to 20.0      |
| Thresh  | -18.0 dB       | -60.0 to 0.0 dB  |
| Attack  | 20.0 ms        | 0.1 to 300.0 ms  |
| Release | 200 ms         | 5 to 2000 ms     |
| Makeup  | 0.0 dB         | -12.0 to 24.0 dB |
| Drive   | 0.0 dB         | 0.0 to 18.0 dB   |
| Phase   | 0 stages (off) | 0 to 6 stages    |

The Ratio knob uses a logarithmic mapping (`1 × 20^n`) so that low ratios (gentle compression, 1.0–4.0:1) occupy most of the knob travel and high ratios (hard limiting, up to 20.0:1) are compressed into the upper end.

The Drive knob provides pre-comp gain boost with linked auto-makeup. It pushes more signal across the threshold so the compressor engages harder, and simultaneously adds equal gain at the output so average RMS lifts alongside peaks rather than dropping. Pair with Phase to keep peaks clean. Drive is displayed in the floating StripCompPanel only (right column). The label shows as '+X.X dB'. Auto-makeup matches the broadcast-Optimod model — Drive pushes more material into the curve AND adds equal gain back, so the user's fixed Makeup stays a clean post-everything trim knob.

The Phase knob controls the number of cascaded all-pass sections (0 = off, 1–6 stages). Each stage adds 12 dB/oct of phase rotation at staggered frequencies (300/700/1500/2500 Hz, plus optional 1000/2000 Hz). The phase rotator symmetrizes asymmetric voice peaks before compression to reduce peak-to-average-power-ratio (PAPR). Phase is displayed in the floating StripCompPanel only (right column). The label shows 'Off' when 0, 'N stg' when active. The tooltip explains: 'Pre-comp phase rotator (#2887). All-pass cascade that symmetrizes asymmetric voice peaks before compression. 0 = off, 4 = broadcast default.' The default centres (300/700/1500/2500 Hz with optional 1000/2000 Hz) cover the speech formant range without bunching.

## Transfer curve display

The compact-mode ClientCompCurveWidget draws the static input/output transfer curve with a live "ball" showing the current envelope level. Axis labels are rendered using cached QStaticText objects that rebuild automatically when the applet switches between compact and expanded views. In the applet, the curve is view-only; to edit Knee and limiter ceiling parameters, open the floating ClientCompEditor by double-clicking the COMP stage in the CHAIN widget.

The transfer curve widget uses color tokens from the active theme via `ThemeManager::color()`:
- Background: `color.background.0`
- Grid lines: `color.background.1`
- Axis labels: `color.text.label`
- Unity diagonal: `color.background.1`
- Compressor curve: `color.accent.dim`
- Envelope ball glow: `color.accent.warning`
- Envelope ball core: `color.text.primary`

## Gain-reduction meter

The horizontal amber strip fills from right to left, showing up to 20 dB of gain reduction. A tick mark at -6 dB indicates a typical working amount of reduction. The meter refreshes at approximately 30 Hz using MeterSmoother ballistics applied to the `ClientComp::gainReductionDb()` value. The gain-reduction bar repaints only when the smoothed value changes or when the animation timer is active, conserving CPU cycles during quiet periods.

## Tips

- A ratio between 2.0:1 and 4.0:1 is typical for voice TX compression. Values above 10.0:1 approach limiting behavior.
- The gain-reduction bar shows up to 20 dB of reduction. A tick mark at -6 dB indicates a typical working amount of gain reduction. If the bar rarely reaches that tick, the threshold may be set too high for the current ratio to have much effect.
- Raising the ratio while reducing Makeup keeps the average output level steady while tightening the dynamic range.
- To access the Knee and limiter ceiling controls, which further shape how the ratio is applied, open the full editor by double-clicking the COMP stage in the CHAIN widget.
- Clicking a knob's value label opens an inline editor for precise numeric entry. This works on all five knobs and supports locale-aware decimal separators (for example, "12,5" in comma-decimal locales). The editor also accepts values with trailing units or symbols (for example, "12.5 ms" or "−6 dB").
- For TX operation, pair Drive with the Phase Rotator (in the floating StripCompPanel) to increase average power while keeping peaks clean through PAPR reduction.

## Troubleshooting

- **Ratio knob has no audible effect** — The stage may still be in bypass. Confirm the compressor is enabled on the correct side (TX or RX) via the CHAIN widget. When the stage is bypassed, the applet tile dims to approximately 55% opacity; restore full opacity by enabling the stage.
- **Gain-reduction bar is pinned at maximum** — The threshold is likely too low relative to the incoming signal level. Lower the ratio or raise the Thresh knob until the bar shows moderate, intermittent reduction.
- **Inline editor does not accept the entered value** — Ensure the value is within the valid range for that knob (see the table above). The editor clamps out-of-range values to the nearest valid limit when you press Enter or click elsewhere.

## Related

- [Adjust compressor threshold (TX or RX side)](adjust-compressor-threshold-tx-or-rx-side.md)
- [Tune attack / release for a natural-sounding squeeze](tune-attack-release-for-a-natural-sounding-squeeze.md)
- [Apply make-up gain after compression](apply-make-up-gain-after-compression.md)
- [Watch live gain reduction while speaking or listening](watch-live-gain-reduction-while-speaking-or-listening.md)
- [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md)
- [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md)
- [Set pre-comp Drive and Phase Rotator for PAPR reduction](set-pre-comp-drive-and-phase-rotator-for-papr-reduction.md)