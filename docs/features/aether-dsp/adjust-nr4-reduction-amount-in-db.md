# Adjust NR4 Reduction Amount in dB

The `NR4ReductionAmount` setting controls how aggressively NR4 attenuates noise. Raising the value increases suppression; lowering it preserves more of the original signal character.

## Before you start

- AetherSDR must be running. A radio connection is not required to change this setting.
- NR4 must be active in your receive chain for changes to have an audible effect.

## Steps

1. Click `Settings > AetherDSP Settings...`.
2. Click the **NR4** tab.
3. Drag the **Reduction (dB):** slider to the desired value. The current value is shown to the right of the slider.
4. Close the dialog. The setting is saved automatically.

## What each control does

| Control | Default | Valid range | Persisted key |
|---|---|---|---|
| **Reduction (dB):** | 10.0 dB | 0.0–40.0 dB | `NR4ReductionAmount` |
| **Smoothing (%):** | 0 | 0–100 | `NR4SmoothingFactor` |
| **Whitening (%):** | 0 | 0–100 | `NR4WhiteningFactor` |
| **Masking Depth:** | 0.50 | 0.00–1.00 | `NR4MaskingDepth` |
| **Suppression:** | 0.50 | 0.00–1.00 | `NR4SuppressionStrength` |
| **Noise Estimation Method** | SPP-MMSE | SPP-MMSE / Brandt / Martin | `NR4NoiseEstimationMethod` |
| **Adaptive Noise Estimation** | Enabled | On / Off | `NR4AdaptiveNoise` |

**Reduction (dB):** sets the maximum noise attenuation NR4 will apply. At 0.0 dB, no attenuation occurs. At 40.0 dB, NR4 suppresses noise by up to 40 dB below the estimated noise floor.

## Tips

- Start at the default of 10.0 dB and increase in small steps while monitoring for speech artifacts.
- Very high values (above 30 dB) on signals with rapidly changing noise can produce musical noise or speech distortion. If this occurs, reduce **Reduction (dB):** or increase **Smoothing (%):** to stabilize the noise estimate.
- To return all NR4 parameters to their factory values in one step, click **Reset Defaults** at the bottom of the NR4 tab. This restores **Reduction (dB):** to 10.0 dB along with the other NR4 defaults.

## Related

- [Enable or disable NR4 adaptive noise estimation](enable-or-disable-nr4-adaptive-noise-estimation.md)
- [Tune NR4 masking depth and suppression strength](tune-nr4-masking-depth-and-suppression-strength.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
