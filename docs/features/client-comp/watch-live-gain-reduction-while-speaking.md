# Watch live gain reduction while speaking

The Compressor applet shows a real-time gain-reduction meter and a live transfer-curve indicator while you transmit. Use these to confirm the compressor is working and to judge how hard it is squeezing your voice peaks.

## Before you start

- The Compressor stage must be enabled (bypass off). If the COMPRESSOR tile is hidden, enable the stage via the CHAIN widget or double-click the Comp stage in the CHAIN widget to open the floating editor and turn it on there.
- The COMPRESSOR sub-container must be visible inside the PooDoo Audio (TXDSP) parent container.
- A microphone must be routed through the TX audio path so there is a live input signal to compress.

## Steps

1. Locate the COMPRESSOR sub-container in the PooDoo Audio (TXDSP) parent container in the applet panel.
2. Key the radio and speak into the microphone at your normal voice level.
3. Watch the **Gain-reduction bar** — the horizontal amber strip at the top of the knob row. When the compressor is acting on your voice, the bar fills from the right. A wider fill means more reduction.
4. Note the tick mark one-third of the way from the right edge. That tick marks −6 dB of gain reduction, a typical working amount for voice.
5. Watch the **Transfer curve** display above the bar. The small ball moves along the static input/output curve to show your current envelope level. When you speak louder, the ball moves up and to the right; when the ball travels past the knee, the curve flattens and the gain-reduction bar grows.
6. If the bar is consistently empty, your input level is below the threshold. Raise your microphone gain or lower the **Thresh** knob (default −18.0 dB) until the bar shows activity on voice peaks.
7. If the bar is pegged at the right edge, the compressor is applying more than 20 dB of reduction. Raise **Thresh** or lower **Ratio** (default 3.0:1) to reduce the amount of compression.

## What each control does

| Control | What it shows or does | Default | Range | Setting key |
|---|---|---|---|---|
| Transfer curve | Static input/output curve with a live ball at the current envelope level. View-only in the applet. | — | — | — |
| Gain-reduction bar | Horizontal amber strip. Fills from the right to show current gain reduction. Empty = no reduction. Tick at −6 dB marks a typical working level. Maximum scale is 20 dB. | — | 0–20 dB | — |
| Thresh | Level above which compression starts. | −18.0 dB | −60.0 to 0.0 dB | `ClientCompTxThresholdDb` |
| Ratio | How hard peaks are held once threshold is crossed. | 3.0:1 | 1.0 to 20.0 | `ClientCompTxRatio` |
| Attack | How quickly the compressor clamps down after threshold is crossed. | 20.0 ms | 0.1 to 300.0 ms | `ClientCompTxAttackMs` |
| Release | How quickly gain returns after input drops back below threshold. | 200 ms | 5 to 2000 ms | `ClientCompTxReleaseMs` |
| Makeup | Gain added back after compression. | +0.0 dB | −12.0 to +24.0 dB | `ClientCompTxMakeupDb` |

## Tips

- The gain-reduction bar refreshes at approximately 30 Hz with smoothed ballistics, so brief transients may not show their full peak; use the ball on the transfer curve as a secondary check on envelope movement.
- A consistent reduction of 3–6 dB (bar roughly reaching or just touching the tick) is a reasonable starting point for voice compression without over-processing.
- Knee and limiter ceiling controls (`ClientCompTxKneeDb`, `ClientCompTxLimEnabled`, `ClientCompTxLimCeilingDb`) are not available in the applet. Open the full editor to adjust them.

## Troubleshooting

- **Gain-reduction bar stays empty while transmitting** — The input level is not reaching the threshold. Lower the **Thresh** knob or increase microphone gain until the bar begins to move on voice peaks.
- **Gain-reduction bar is always full (pegged at maximum)** — Threshold is set too low or ratio too high for your microphone level. Raise **Thresh** toward 0 dB or reduce **Ratio** toward 1.0:1.
- **COMPRESSOR tile is not visible** — The Compressor stage is bypassed or disabled. Enable it from the CHAIN widget. See [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md).

## Related

- [Adjust compressor threshold](adjust-compressor-threshold.md)
- [Set compression ratio for voice](set-compression-ratio-for-voice.md)
- [Tune attack / release for a natural-sounding squeeze](tune-attack-release-for-a-natural-sounding-squeeze.md)
- [Apply make-up gain after compression](apply-make-up-gain-after-compression.md)
- [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md)
- [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md)
