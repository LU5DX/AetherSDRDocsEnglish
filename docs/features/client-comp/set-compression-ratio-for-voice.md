# Set compression ratio for voice

The Ratio knob controls how hard the compressor clamps signal peaks once they cross the threshold. A higher ratio produces a more aggressive, broadcast-style squeeze; a lower ratio gives a gentler, more transparent result.

## Before you start

- The Compressor stage must be enabled (bypass off). If the COMPRESSOR sub-container is hidden, enable the stage via the CHAIN widget first. See [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md).
- The COMPRESSOR sub-container must be visible inside the PooDoo Audio (TXDSP) parent container in the applet panel.

## Steps

1. Locate the COMPRESSOR sub-container in the applet panel.
2. Find the **Ratio** knob in the five-knob row at the bottom of the applet.
3. Turn the **Ratio** knob clockwise to increase the ratio or counter-clockwise to decrease it. The label below the knob updates in real time and displays the current value as `X.XX:1`.
4. Watch the gain-reduction bar above the knob row while speaking into the microphone. An amber fill moving toward the -6 dB tick indicates the compressor is actively working at the ratio you have set.
5. Adjust **Thresh** and **Makeup** as needed to compensate for level changes caused by the new ratio.

## What each control does

| Control | Default | Valid range | Persisted key |
|---|---|---|---|
| Ratio | 3.0 | 1.0 to 20.0 | `ClientCompTxRatio` |
| Thresh | -18.0 dB | -60.0 to 0.0 dB | `ClientCompTxThresholdDb` |
| Attack | 20.0 ms | 0.1 to 300.0 ms | `ClientCompTxAttackMs` |
| Release | 200 ms | 5 to 2000 ms | `ClientCompTxReleaseMs` |
| Makeup | 0.0 dB | -12.0 to 24.0 dB | `ClientCompTxMakeupDb` |

The **Ratio** knob uses a logarithmic scale. Small movements near the low end of the range produce fine control around typical voice ratios (2:1 to 4:1). Large movements near the top approach limiting behavior (20:1).

The gain-reduction bar maxes at 20 dB of reduction. A tick mark at -6 dB indicates a typical working amount of gain reduction for voice.

Knee and limiter settings (`ClientCompTxKneeDb`, `ClientCompTxLimEnabled`, `ClientCompTxLimCeilingDb`) are not available in the applet. See [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md).

## Tips

- For voice on SSB, ratios between 2:1 and 4:1 are a common starting point. The default of 3.0:1 suits most microphone and voice combinations.
- If the gain-reduction bar is pinned hard to the right during normal speech, the ratio may be too high or the threshold too low. Lower the ratio or raise the threshold, then re-check with **Makeup**.
- The transfer curve in the applet shows the static input/output relationship. The envelope ball moves along the curve in real time as you speak, giving you a visual reference for where your voice sits relative to the threshold and ratio you have set.

## Related

- [Adjust compressor threshold](adjust-compressor-threshold.md)
- [Apply make-up gain after compression](apply-make-up-gain-after-compression.md)
- [Tune attack / release for a natural-sounding squeeze](tune-attack-release-for-a-natural-sounding-squeeze.md)
- [Watch live gain reduction while speaking](watch-live-gain-reduction-while-speaking.md)
- [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md)
- [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md)
