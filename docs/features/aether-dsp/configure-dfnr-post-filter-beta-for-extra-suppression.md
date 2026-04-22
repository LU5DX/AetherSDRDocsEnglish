# Configure DFNR Post-Filter Beta for Extra Suppression

The Post-Filter Beta control adds a second stage of suppression after DeepFilterNet3's main noise reduction. Use it when residual noise remains after setting the attenuation limit.

## Before you start

- Open AetherSDR.
- DFNR (DeepFilterNet3) must be active on your receiver. Post-Filter Beta has no effect unless DFNR is running.

## Steps

1. Click `Settings > AetherDSP Settings...`.
2. Click the **DFNR** tab.
3. Adjust the **Post-Filter Beta** slider to the desired value.

## What each control does

| Control | Default | Valid range | Setting key | Behavior |
|---|---|---|---|---|
| Attenuation Limit | 100 | 0–100 dB | `DfnrAttenLimit` | Sets the maximum noise attenuation applied by DeepFilterNet3. 0 = passthrough; 100 = maximum. |
| Post-Filter Beta | 0.00 | 0.00–0.30 | `DfnrPostFilterBeta` | Applies an additional post-filter stage for extra suppression beyond the main attenuation limit. |

## Tips

- Start with **Post-Filter Beta** at 0.00 and increase in small steps. Higher values suppress more residual noise but can affect speech fidelity.
- If the signal sounds over-processed at a given **Post-Filter Beta**, reduce **Attenuation Limit** first, then re-raise **Post-Filter Beta** to taste.
- A **Post-Filter Beta** of 0.00 disables the post-filter entirely, leaving only the main DeepFilterNet3 stage active.

## Related

- [Set DeepFilterNet3 attenuation limit for strong or weak signals](set-deepfilternet3-attenuation-limit-for-strong-or-weak-signals.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
- [AetherDSP Settings overview](overview.md)
