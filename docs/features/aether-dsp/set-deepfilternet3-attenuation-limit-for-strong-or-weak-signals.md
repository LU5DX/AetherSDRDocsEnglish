# Set DeepFilterNet3 Attenuation Limit for Strong or Weak Signals

The `DfnrAttenLimit` setting controls how aggressively DeepFilterNet3 suppresses noise. Lowering it preserves more of the original signal on strong, clean signals; raising it maximizes suppression on signals buried in noise.

## Before you start

- AetherSDR must be running. No radio connection is required to adjust this setting.
- DeepFilterNet3 (DFNR) must be active in your receive chain for this setting to have any audible effect.

## Steps

1. Click `Settings > AetherDSP Settings...` to open the AetherDSP Settings dialog.
2. Click the `DFNR` tab.
3. Drag the `Attenuation Limit` slider to the desired value.

## What each control does

| Control | Default | Valid Range | Persisted Key | Behavior |
|---|---|---|---|---|
| `Attenuation Limit` | 100 | 0–100 dB | `DfnrAttenLimit` | Sets the maximum noise attenuation DeepFilterNet3 may apply. 0 passes the signal through unprocessed; 100 allows full attenuation. |
| `Post-Filter Beta` | 0.00 | 0.00–0.30 | `DfnrPostFilterBeta` | Applies an additional post-filter on top of the attenuation limit for extra suppression. |

## Tips

- For strong signals with a clean noise floor, lower `Attenuation Limit` (for example, 20–40) to reduce processing artifacts and preserve audio naturalness.
- For weak signals in heavy noise, set `Attenuation Limit` to 100 to allow DeepFilterNet3 to apply its full suppression capability.
- If residual noise remains after reaching 100, combine with a non-zero `Post-Filter Beta` value. See [Configure DFNR post-filter beta for extra suppression](configure-dfnr-post-filter-beta-for-extra-suppression.md).

## Troubleshooting

- **Changing the slider has no audible effect** — DFNR may not be the active noise reduction engine on your receive slice. Confirm that DeepFilterNet3 is enabled in your receive chain.
- **Audio sounds over-processed or distorted at high values** — Reduce `Attenuation Limit`. Values above 60–70 may introduce artifacts on some signal types.

## Related

- [Configure DFNR post-filter beta for extra suppression](configure-dfnr-post-filter-beta-for-extra-suppression.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
- [AetherDSP Settings overview](overview.md)
