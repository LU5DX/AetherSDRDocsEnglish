# Set DeepFilterNet3 Attenuation Limit for Strong or Weak Signals

Adjust how aggressively DeepFilterNet3 (DFNR) suppresses noise. A lower limit preserves more signal character on already-strong signals; the full 100 dB is appropriate when maximum noise removal is needed.

## Before you start

- AetherDSP Settings can be opened without a radio connection.
- DFNR must be active on a receiver slice for changes to take audible effect.

## Steps

1. Click `Settings > AetherDSP Settings...`.
2. Click the **DFNR** tab.
3. Drag the **Attenuation Limit** slider to the desired value.

The new value takes effect immediately; no confirmation is required. The setting is persisted automatically as `DfnrAttenLimit`.

## What each control does

| Control | Default | Valid range | Setting key | Behavior |
|---|---|---|---|---|
| Attenuation Limit | 100 | 0–100 dB | `DfnrAttenLimit` | Sets the maximum noise attenuation applied by DeepFilterNet3. 0 dB is full passthrough; 100 dB is maximum suppression. |
| Post-Filter Beta | 0.00 | 0.00–0.30 | `DfnrPostFilterBeta` | Applies an additional post-filter on top of DFNR for extra suppression. |

## Tips

- Set **Attenuation Limit** to a lower value (for example, 20–40 dB) when the incoming signal is already strong and you want to avoid over-processing that can make speech sound unnatural.
- Set **Attenuation Limit** to a higher value (for example, 80–100 dB) when the noise floor is high and the signal is weak.
- Combine a moderate **Attenuation Limit** with a non-zero **Post-Filter Beta** if residual noise remains after raising the limit. See [Configure DFNR post-filter beta for extra suppression](configure-dfnr-post-filter-beta-for-extra-suppression.md).

## Related

- [Configure DFNR post-filter beta for extra suppression](configure-dfnr-post-filter-beta-for-extra-suppression.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
- [Adjust NR4 reduction amount in dB](adjust-nr4-reduction-amount-in-db.md)
