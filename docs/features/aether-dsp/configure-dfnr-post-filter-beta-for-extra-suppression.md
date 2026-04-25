# Configure DFNR Post-Filter Beta for Extra Suppression

Use this page to adjust the DeepFilterNet3 post-filter beta, which applies an additional suppression stage on top of the main attenuation. Raise this value when residual noise remains audible after setting the attenuation limit.

## Before you start

- AetherDSP Settings can be opened without an active radio connection.
- DFNR (DeepFilterNet3) must already be selected as your active noise reduction engine. If you are unsure which engine to use, see [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md).

## Steps

1. Click `Settings > AetherDSP Settings...` to open the AetherDSP Settings dialog.
2. Click the **DFNR** tab.
3. Adjust the **Post-Filter Beta** slider to the desired value (default: `0.00`, range: `0.00`–`0.30`).
4. Close the dialog. The value is saved immediately when the slider moves.

## What each control does

| Control | Default | Valid range | Setting key | Behavior |
|---|---|---|---|---|
| **Attenuation Limit** | `100` | `0`–`100` dB | `DfnrAttenLimit` | Sets the maximum noise attenuation applied by DeepFilterNet3. `0` is passthrough; `100` is maximum. |
| **Post-Filter Beta** | `0.00` | `0.00`–`0.30` | `DfnrPostFilterBeta` | Applies an additional post-filter for extra suppression on top of the attenuation limit. |

## Tips

- Start with **Post-Filter Beta** at `0.00` and increase in small increments. Higher values provide more suppression but may affect speech naturalness.
- If the noise floor is acceptable but occasional bursts break through, try a moderate **Post-Filter Beta** value such as `0.05`–`0.10` before raising **Attenuation Limit** further.
- **Attenuation Limit** at `0` bypasses DFNR attenuation entirely, making **Post-Filter Beta** the only active stage.

## Troubleshooting

- **Post-Filter Beta has no audible effect** — Confirm that DFNR is the active noise reduction engine in your receiver chain. If **Attenuation Limit** is set to `0`, DFNR attenuation is bypassed; raise **Attenuation Limit** first so DFNR is processing audio.
- **Speech sounds distorted after raising Post-Filter Beta** — Reduce **Post-Filter Beta** toward `0.00`. Values above `0.15` can introduce audible artifacts on weak or low-SNR signals.

## Related

- [Set DeepFilterNet3 attenuation limit for strong or weak signals](set-deepfilternet3-attenuation-limit-for-strong-or-weak-signals.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
- [AetherDSP Settings overview](overview.md)
