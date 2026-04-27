# Configure DFNR post-filter beta for extra suppression

The DFNR tab in AetherDSP Settings lets you apply an additional post-filter on top of DeepFilterNet3's main noise reduction. Raising the Post-Filter Beta value increases suppression beyond what the attenuation limit alone provides, at the cost of some speech fidelity.

## Before you start

- AetherDSP Settings can be opened without a radio connection, but the effect is only audible during live reception.
- Verify that DeepFilterNet3 is already active in your slice receiver before adjusting these parameters. See [Set DeepFilterNet3 attenuation limit for strong or weak signals](set-deepfilternet3-attenuation-limit-for-strong-or-weak-signals.md) for how to enable it and set the attenuation limit.

## Steps

1. Open `Settings > AetherDSP Settings...`.
2. Click the **DFNR** tab.
3. Locate the **Post-Filter Beta** slider.
4. Drag the slider right to increase post-filter suppression. The valid range is 0.00–0.30; the default is 0.00 (post-filter inactive).
5. Release the slider. The value is saved immediately to `DfnrPostFilterBeta`.
6. Monitor audio quality. If speech becomes hollow or distorted, reduce the value toward 0.00.

## What each control does

| Control | Default | Valid range | Setting key | Behavior |
|---|---|---|---|---|
| **Attenuation Limit** | 100 | 0–100 dB | `DfnrAttenLimit` | Sets maximum noise attenuation applied by DeepFilterNet3. 0 = passthrough; 100 = maximum. |
| **Post-Filter Beta** | 0.00 | 0.00–0.30 | `DfnrPostFilterBeta` | Applies an additional post-filter on top of DeepFilterNet3 for extra suppression. Higher values suppress more residual noise. |

## Tips

- Start with **Post-Filter Beta** at or below 0.10. Audible artefacts tend to appear before 0.30 is reached, especially on SSB voice signals.
- If you need stronger overall attenuation without touching the post-filter, increase **Attenuation Limit** first, then add **Post-Filter Beta** only for residual noise that remains.
- A value of 0.00 disables the post-filter entirely, leaving DeepFilterNet3's output unchanged.

## Troubleshooting

- **Speech sounds hollow or phasey** — **Post-Filter Beta** is set too high. Reduce it toward 0.00 in small increments until naturalness returns.
- **No audible change when moving the slider** — DeepFilterNet3 may not be active on the current slice. Confirm the DFNR engine is selected and that **Attenuation Limit** is above 0.

## Related

- [Set DeepFilterNet3 attenuation limit for strong or weak signals](set-deepfilternet3-attenuation-limit-for-strong-or-weak-signals.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
- [Tune NR2 reduction depth and voice threshold](tune-nr2-reduction-depth-and-voice-threshold.md)
