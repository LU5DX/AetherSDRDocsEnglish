# Tune NR4 masking depth and suppression strength

Use this page to adjust NR4's spectral-masking depth and overall suppression strength, controlling how aggressively the NR4 engine attenuates noise relative to speech-like content.

## Before you start

- Open AetherSDR.
- NR4 must be selected as your active noise-reduction engine. See [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md) if you are unsure.

## Steps

1. Click `Settings > AetherDSP Settings...`.
2. Click the **NR4** tab.
3. Adjust **Masking Depth:** to set how deeply spectral masking is applied. Lower values apply less masking; higher values apply more.
4. Adjust **Suppression:** to set the overall NR4 suppression strength. Lower values are gentler; higher values are more aggressive.
5. Close the dialog. Changes take effect immediately.

## What each control does

| Control | Default | Valid range | Setting key |
|---|---|---|---|
| **Masking Depth:** | 0.50 | 0.00–1.00 | `NR4MaskingDepth` |
| **Suppression:** | 0.50 | 0.00–1.00 | `NR4SuppressionStrength` |

**Masking Depth:** controls the depth of spectral masking applied by the NR4 engine. At 0.00 masking is not applied; at 1.00 masking is applied at full depth.

**Suppression:** sets the overall suppression strength of the NR4 engine. At 0.00 suppression is minimal; at 1.00 it is at maximum.

## Tips

- Start with both sliders at their defaults (0.50) and make small incremental adjustments. Increasing **Suppression:** too far can cause audible artifacts on weak signals.
- If residual noise remains after raising **Suppression:**, also raise **Masking Depth:** gradually. The two controls interact: masking depth shapes which spectral bins are targeted, while suppression determines how much gain reduction is applied to them.
- Use **Reset Defaults** to return both sliders — along with all other NR4 parameters — to their factory values (SPP-MMSE, adaptive on, 10.0 dB, Smoothing 0, Whitening 0, Masking Depth 0.50, Suppression 0.50).

## Troubleshooting

- **Speech sounds muffled after increasing Suppression:** — The suppression level is too high. Reduce **Suppression:** and, if needed, also reduce **Masking Depth:** to restore speech clarity.
- **Noise floor is still audible at maximum Suppression:** — Check that **Reduction (dB):** is set high enough and that **Adaptive Noise Estimation** is enabled. See [Adjust NR4 reduction amount in dB](adjust-nr4-reduction-amount-in-db.md) and [Enable or disable NR4 adaptive noise estimation](enable-or-disable-nr4-adaptive-noise-estimation.md).

## Related

- [Adjust NR4 reduction amount in dB](adjust-nr4-reduction-amount-in-db.md)
- [Enable or disable NR4 adaptive noise estimation](enable-or-disable-nr4-adaptive-noise-estimation.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
