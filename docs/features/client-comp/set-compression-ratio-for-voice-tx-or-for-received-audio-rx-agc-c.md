# Set Compression Ratio for Voice (TX) or Received Audio (RX AGC-C)

The Ratio knob controls how hard the compressor clamps peaks once the signal crosses the threshold. A higher ratio gives a more aggressive squeeze on loud voice peaks (TX side) or loud received audio (RX AGC-C side).

## Before you start

- The compressor stage must be enabled (bypass off) on the side you want to adjust. The applet tile stays hidden until the stage is active. See [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md).
- Open the Aetherial Audio (TXDSP) parent container and expand the relevant sub-container: "Aetherial Compressor" for TX, or "Aetherial AGC-C" for RX.

## Steps

1. Locate the five-knob row at the bottom of the applet tile. The knobs are labeled Thresh, Ratio, Attack, Release, and Makeup, left to right.
2. Turn the **Ratio** knob to set the compression ratio.
   - For TX voice compression, this knob persists to `ClientCompTxRatio`.
   - For RX AGC-C, this knob persists to `ClientCompRxRatio`.
3. Read the current value from the label beneath the knob. It is formatted as `X.XX:1` (for example, `3.00:1`).
4. Watch the gain-reduction bar and the envelope ball on the transfer curve while you speak (TX) or while audio plays (RX) to confirm the ratio is producing the intended amount of gain reduction.

## What each control does

| Control | Default | Valid range | Persisted setting (TX / RX) |
|---|---|---|---|
| Ratio | 3.0 | 1.0 to 20.0 | `ClientCompTxRatio` / `ClientCompRxRatio` |
| Thresh | -18.0 dB | -60.0 to 0.0 dB | `ClientCompTxThresholdDb` / `ClientCompRxThresholdDb` |
| Attack | 20.0 ms | 0.1 to 300.0 ms | `ClientCompTxAttackMs` / `ClientCompRxAttackMs` |
| Release | 200 ms | 5 to 2000 ms | `ClientCompTxReleaseMs` / `ClientCompRxReleaseMs` |
| Makeup | 0.0 dB | -12.0 to 24.0 dB | `ClientCompTxMakeupDb` / `ClientCompRxMakeupDb` |

The Ratio knob uses a logarithmic mapping (`1 × 20^n`) so that low ratios (gentle compression, 1.0–4.0:1) occupy most of the knob travel and high ratios (hard limiting, up to 20.0:1) are compressed into the upper end.

## Tips

- A ratio between 2.0:1 and 4.0:1 is typical for voice TX compression. Values above 10.0:1 approach limiting behavior.
- The gain-reduction bar shows up to 20 dB of reduction. A tick mark at -6 dB indicates a typical working amount of gain reduction. If the bar rarely reaches that tick, the threshold may be set too high for the current ratio to have much effect.
- Raising the ratio while reducing Makeup keeps the average output level steady while tightening the dynamic range.
- To access the Knee and limiter ceiling controls, which further shape how the ratio is applied, open the full editor by double-clicking the COMP stage in the CHAIN widget.

## Troubleshooting

- **Ratio knob has no audible effect** — The stage may still be in bypass. Confirm the compressor is enabled on the correct side (TX or RX) via the CHAIN widget. The applet tile is hidden while the stage is bypassed.
- **Gain-reduction bar is pinned at maximum** — The threshold is likely too low relative to the incoming signal level. Lower the ratio or raise the Thresh knob until the bar shows moderate, intermittent reduction.

## Related

- [Adjust compressor threshold (TX or RX side)](adjust-compressor-threshold-tx-or-rx-side.md)
- [Tune attack / release for a natural-sounding squeeze](tune-attack-release-for-a-natural-sounding-squeeze.md)
- [Apply make-up gain after compression](apply-make-up-gain-after-compression.md)
- [Watch live gain reduction while speaking or listening](watch-live-gain-reduction-while-speaking-or-listening.md)
- [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md)
- [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md)
