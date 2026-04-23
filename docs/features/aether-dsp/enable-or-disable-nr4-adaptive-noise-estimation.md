# Enable or disable NR4 adaptive noise estimation

NR4's adaptive noise estimation continuously re-estimates the noise floor as band conditions change. Disabling it locks the estimate at its last computed value, which can help on very stable noise environments but will cause under- or over-suppression when noise changes.

## Before you start

- AetherSDR must be running. A radio connection is not required to adjust DSP settings.
- NR4 must be the active noise-reduction engine in your receive chain. If you are using NR2, MNR, or DFNR, this setting has no effect.

## Steps

1. Click `Settings > AetherDSP Settings...`.
2. Click the **NR4** tab.
3. Check or uncheck **Adaptive Noise Estimation**.
   - Checked (default): NR4 continuously re-estimates the noise floor.
   - Unchecked: NR4 holds the noise estimate fixed.

The change takes effect immediately and is persisted automatically.

## What each control does

| Control | Kind | Default | Valid range | Setting key |
|---|---|---|---|---|
| **Adaptive Noise Estimation** | Checkbox | Checked | On / Off | `NR4AdaptiveNoise` |
| **Noise Estimation Method** | Radio buttons | SPP-MMSE | SPP-MMSE \| Brandt \| Martin | `NR4NoiseEstimationMethod` |
| **Reduction (dB):** | Slider | 10.0 | 0.0–40.0 dB | `NR4ReductionAmount` |
| **Smoothing (%):** | Slider | 0 | 0–100 | `NR4SmoothingFactor` |
| **Whitening (%):** | Slider | 0 | 0–100 | `NR4WhiteningFactor` |
| **Masking Depth:** | Slider | 0.50 | 0.00–1.00 | `NR4MaskingDepth` |
| **Suppression:** | Slider | 0.50 | 0.00–1.00 | `NR4SuppressionStrength` |
| **Reset Defaults** | Button | — | — | — |

## Tips

- If the noise floor on the band is stable (for example, a quiet local noise environment late at night), disabling **Adaptive Noise Estimation** can prevent the estimator from drifting toward signal peaks and inadvertently suppressing weak stations.
- If you disable adaptive estimation and then notice the noise reduction is no longer tracking correctly after a band condition change, re-enable it and allow a few seconds for the estimator to converge before adjusting other sliders.
- The **Noise Estimation Method** selection determines which algorithm feeds the adaptive estimator. SPP-MMSE is the default and suits most conditions; switch to Brandt or Martin if you are working with rapidly changing or slowly varying noise floors respectively.
- Click **Reset Defaults** to restore `NR4AdaptiveNoise` to checked along with all other NR4 parameters.

## Troubleshooting

- **Noise suppression stops tracking after a QSB fade** — Adaptive noise estimation is likely disabled. Open `Settings > AetherDSP Settings...`, select the **NR4** tab, and check **Adaptive Noise Estimation**.
- **NR4 is suppressing signal peaks along with noise** — The estimator may be adapting too aggressively. Disable **Adaptive Noise Estimation** temporarily, or reduce **Reduction (dB):** and **Suppression:** to lower values.

## Related

- [Adjust NR4 reduction amount in dB](adjust-nr4-reduction-amount-in-db.md)
- [Tune NR4 masking depth and suppression strength](tune-nr4-masking-depth-and-suppression-strength.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
