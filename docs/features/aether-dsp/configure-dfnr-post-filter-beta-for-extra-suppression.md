# Configure DFNR Post-Filter Beta for Extra Suppression

Use this page to adjust the DeepFilterNet3 post-filter beta value, which applies an additional suppression stage on top of the main DFNR noise reduction. Raising beta increases residual noise removal at the cost of some audio naturalness.

## Before you start

- Open AetherSDR and confirm DFNR is active on the receiver you want to adjust.
- Know that `DfnrPostFilterBeta` is independent of `DfnrAttenLimit`; both controls affect the DFNR output but operate at different stages.

## Steps

1. Click `Settings > AetherDSP Settings...` to open the AetherDSP Settings dialog.
2. Click the **DFNR** tab.
3. Drag the **Post-Filter Beta** slider to the desired value. The default is `0.00` (post-filter off); the maximum is `0.30`.
4. Release the slider. The setting is saved immediately to `DfnrPostFilterBeta`.

## What each control does

| Control | Default | Valid range | Setting key | Behavior |
|---|---|---|---|---|
| **Post-Filter Beta** | 0.00 | 0.00 – 0.30 | `DfnrPostFilterBeta` | Applies an additional post-filter for extra suppression after the main DeepFilterNet3 stage. Higher values increase suppression. 0.00 disables the post-filter entirely. |
| **Attenuation Limit** | 100 | 0 – 100 dB | `DfnrAttenLimit` | Sets the maximum noise attenuation applied by DeepFilterNet3 before the post-filter stage. 0 passes audio through unprocessed; 100 applies maximum attenuation. |

## Tips

- Start with small beta increments (0.05 steps) and listen for any loss of speech clarity before increasing further.
- If residual noise is still audible after raising **Post-Filter Beta** to 0.30, consider also increasing **Attenuation Limit** rather than pushing beta beyond its range.
- Setting **Post-Filter Beta** to `0.00` leaves DFNR output unchanged by the post-filter, which is appropriate when the main attenuation stage alone gives clean results.

## Troubleshooting

- **Speech sounds muffled or over-processed** — Reduce **Post-Filter Beta** toward `0.00`. High beta values suppress low-level speech components along with noise.
- **No audible change when moving the slider** — Confirm the DFNR engine is enabled on the active receiver. The post-filter has no effect if DFNR is not running.

## Related

- [Set DeepFilterNet3 attenuation limit for strong or weak signals](set-deepfilternet3-attenuation-limit-for-strong-or-weak-signals.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
- [AetherDSP Settings overview](overview.md)
