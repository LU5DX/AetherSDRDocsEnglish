# Configure DFNR post-filter beta for extra suppression

The DFNR post-filter beta applies an additional suppression stage after DeepFilterNet3's main noise reduction. Use it when the primary attenuation leaves residual noise you want to push down further.

## Before you start

- Open AetherSDR.
- DFNR (DeepFilterNet3) must be enabled on your slice receiver. The AetherDSP Settings dialog does not require a radio connection, but DFNR processing must be active for changes to have an audible effect.

## Steps

1. Click `Settings > AetherDSP Settings...`.
2. Click the **DFNR** tab.
3. Drag the **Post-Filter Beta** slider to the right to increase post-filter suppression. The default is `0.00`; the valid range is `0.00` to `0.30`.
4. Close the dialog. The value is saved automatically to `DfnrPostFilterBeta`.

## What each control does

| Control | Default | Valid range | Setting key | Behavior |
|---|---|---|---|---|
| **Attenuation Limit** | `100` | `0`–`100` dB | `DfnrAttenLimit` | Sets the maximum noise attenuation applied by DeepFilterNet3. `0` passes audio through without attenuation; `100` allows maximum attenuation. |
| **Post-Filter Beta** | `0.00` | `0.00`–`0.30` | `DfnrPostFilterBeta` | Applies an additional post-filter stage on top of the main DeepFilterNet3 output for extra noise suppression. |

## Tips

- Start with **Post-Filter Beta** at `0.00` and raise it in small increments. Because the post-filter acts after the main model, high values can affect speech naturalness even when the primary reduction sounds clean.
- If you only need moderate suppression, adjust **Attenuation Limit** first before increasing **Post-Filter Beta**. See [Set DeepFilterNet3 attenuation limit for strong or weak signals](set-deepfilternet3-attenuation-limit-for-strong-or-weak-signals.md).

## Troubleshooting

- **Post-Filter Beta change has no audible effect** — DFNR processing may not be active on the current slice. Confirm DFNR is enabled before adjusting this control.
- **Speech sounds over-processed or muffled** — Reduce **Post-Filter Beta** toward `0.00`. The post-filter adds suppression beyond the neural model's own output, so small values are usually sufficient.

## Related

- [Set DeepFilterNet3 attenuation limit for strong or weak signals](set-deepfilternet3-attenuation-limit-for-strong-or-weak-signals.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
- [AetherDSP Settings overview](overview.md)
