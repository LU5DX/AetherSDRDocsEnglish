# Set DeepFilterNet3 Attenuation Limit for Strong or Weak Signals

The `DfnrAttenLimit` setting controls how aggressively DeepFilterNet3 suppresses noise. Lowering it preserves more of the original signal on strong stations; raising it maximizes noise removal on weak ones.

## Before you start

- AetherSDR must be running. A radio connection is not required to change this setting.
- DeepFilterNet3 (DFNR) must be active as your selected noise-reduction engine for this setting to have an audible effect.

## Steps

1. Click `Settings > AetherDSP Settings...`.
2. Click the **DFNR** tab.
3. Drag the **Attenuation Limit** slider to the desired value (0–100 dB).
4. Close the dialog. The value is saved immediately.

## What each control does

| Control | Default | Valid range | Setting key | Behavior |
|---|---|---|---|---|
| **Attenuation Limit** | 100 | 0–100 dB | `DfnrAttenLimit` | Sets the maximum noise attenuation applied by DeepFilterNet3. 0 = passthrough (no attenuation); 100 = maximum attenuation. |
| **Post-Filter Beta** | 0.00 | 0.00–0.30 | `DfnrPostFilterBeta` | Applies an additional post-filter on top of DeepFilterNet3 for extra suppression. |

## Tips

- For strong signals where over-processing is noticeable, set **Attenuation Limit** to a lower value (for example, 40–60 dB) to reduce artifacts while still removing background noise.
- For weak or buried signals, leave **Attenuation Limit** at 100 to allow maximum suppression.
- **Attenuation Limit** at 0 passes audio through DeepFilterNet3 unchanged, which is useful for A/B comparisons.

## Related

- [Configure DFNR post-filter beta for extra suppression](configure-dfnr-post-filter-beta-for-extra-suppression.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
- [AetherDSP Settings overview](overview.md)
