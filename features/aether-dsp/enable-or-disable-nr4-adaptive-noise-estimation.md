# Enable or disable NR4 adaptive noise estimation

NR4's adaptive noise estimation continuously re-estimates the noise floor as band conditions change. Disabling it locks the noise floor to a fixed estimate, which can help on very steady noise but may degrade suppression when conditions shift.

## Before you start

- AetherSDR must be running. A radio connection is not required to change this setting.
- Open the NR4 tab in AetherDSP Settings. If you are not already there, follow the steps below.

## Steps

1. Click `Settings > AetherDSP Settings...`.
2. Click the **NR4** tab.
3. Check or uncheck **Adaptive Noise Estimation** to enable or disable it.

The setting takes effect immediately and is saved automatically to `NR4AdaptiveNoise`.

## What each control does

| Control | Kind | Default | Valid range | Setting key |
|---|---|---|---|---|
| **Adaptive Noise Estimation** | Checkbox | Enabled (True) | On / Off | `NR4AdaptiveNoise` |
| **Noise Estimation Method** | Radio button | SPP-MMSE | SPP-MMSE \| Brandt \| Martin | `NR4NoiseEstimationMethod` |
| **Reduction (dB):** | Slider | 10.0 | 0.0–40.0 dB | `NR4ReductionAmount` |
| **Smoothing (%):** | Slider | 0 | 0–100 | `NR4SmoothingFactor` |
| **Whitening (%):** | Slider | 0 | 0–100 | `NR4WhiteningFactor` |
| **Masking Depth:** | Slider | 0.50 | 0.00–1.00 | `NR4MaskingDepth` |
| **Suppression:** | Slider | 0.50 | 0.00–1.00 | `NR4SuppressionStrength` |
| **Reset Defaults** | Button | — | — | — |

**Adaptive Noise Estimation** controls whether NR4 continuously updates its noise floor model. When enabled, NR4 tracks noise that changes over time. When disabled, the noise floor is fixed at the estimate captured when NR4 was last initialized.

**Noise Estimation Method** selects the algorithm used to estimate the noise floor. SPP-MMSE balances noise estimation with speech preservation; Brandt uses recursive smoothing across critical frequency bands and suits non-stationary noise; Martin uses running spectral minima and suits slowly varying noise floors.

## Tips

- If the noise floor on your band is stable and you are hearing suppression artifacts that follow the signal, try disabling **Adaptive Noise Estimation** and selecting the Martin method, which is designed for slowly varying noise floors.
- After disabling adaptive estimation, increase **Smoothing (%):** to stabilize the fixed noise floor estimate against short-term fluctuations.
- Click **Reset Defaults** to return all NR4 controls to their factory values (SPP-MMSE, adaptive on, 10 dB, Smoothing 0, Whitening 0, Masking Depth 0.50, Suppression 0.50).

## Related

- [Adjust NR4 reduction amount in dB](adjust-nr4-reduction-amount-in-db.md)
- [Tune NR4 masking depth and suppression strength](tune-nr4-masking-depth-and-suppression-strength.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
