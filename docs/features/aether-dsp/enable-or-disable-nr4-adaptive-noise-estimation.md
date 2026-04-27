# Enable or disable NR4 adaptive noise estimation

This page explains how to toggle NR4's continuous noise-floor re-estimation. With adaptive noise estimation enabled, NR4 tracks changes in the noise environment in real time; disabling it locks the noise-floor estimate to a static snapshot, which can suit highly stable noise conditions.

## Before you start

- AetherSDR does not need to be connected to a radio to adjust DSP settings.
- NR4 must already be active on your receive slice for these changes to have an audible effect.

## Steps

1. Open `Settings > AetherDSP Settings...`.
2. Click the **NR4** tab.
3. Check or uncheck **Adaptive Noise Estimation** to enable or disable continuous noise-floor re-estimation.

The setting takes effect immediately and is saved automatically to `NR4AdaptiveNoise`.

## What each control does

| Control | Default | Valid values | Setting key |
|---|---|---|---|
| **Adaptive Noise Estimation** | Enabled (checked) | Checked / unchecked | `NR4AdaptiveNoise` |
| **Noise Estimation Method** | SPP-MMSE | SPP-MMSE \| Brandt \| Martin | `NR4NoiseEstimationMethod` |
| **Reduction (dB):** | 10.0 dB | 0.0–40.0 dB | `NR4ReductionAmount` |
| **Smoothing (%):** | 0 | 0–100 | `NR4SmoothingFactor` |
| **Whitening (%):** | 0 | 0–100 | `NR4WhiteningFactor` |
| **Masking Depth:** | 0.50 | 0.00–1.00 | `NR4MaskingDepth` |
| **Suppression:** | 0.50 | 0.00–1.00 | `NR4SuppressionStrength` |

## Tips

- If the noise floor on your band is stable and consistent, unchecking **Adaptive Noise Estimation** can prevent the estimator from following signal-level changes and misclassifying speech as noise.
- If the noise floor varies rapidly — such as during band openings or with impulse noise — leave **Adaptive Noise Estimation** checked so NR4 can track the changing conditions.
- The **Noise Estimation Method** selector (SPP-MMSE, Brandt, Martin) determines how NR4 builds its noise model regardless of whether adaptive mode is on or off. Changing the method can affect how well the static or adaptive estimate tracks your noise floor.
- Click **Reset Defaults** on the NR4 tab to return all NR4 controls to their factory values (adaptive on, SPP-MMSE, 10 dB, 0, 0, 0.50, 0.50).

## Related

- [Adjust NR4 reduction amount in dB](adjust-nr4-reduction-amount-in-db.md)
- [Tune NR4 masking depth and suppression strength](tune-nr4-masking-depth-and-suppression-strength.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
