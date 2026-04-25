# Enable or disable NR4 adaptive noise estimation

NR4's adaptive noise estimation continuously re-measures the noise floor as conditions change on the band. Enabling it lets the engine track drifting interference; disabling it locks the noise floor estimate in place, which can help on very stable, consistent noise backgrounds.

## Before you start

- AetherSDR must be running. A radio connection is not required to change this setting.
- Open the AetherDSP Settings dialog via `Settings > AetherDSP Settings...`.

## Steps

1. Go to `Settings > AetherDSP Settings...`.
2. Click the **NR4** tab.
3. Check or uncheck **Adaptive Noise Estimation**.
   - Checked (default): NR4 continuously re-estimates the noise floor.
   - Unchecked: the noise floor estimate is frozen at the value captured when NR4 was last started.

The setting is saved immediately. No confirmation or restart is needed.

## What each control does

| Control | Default | Valid range | Setting key |
|---|---|---|---|
| **Noise Estimation Method** (radio buttons: SPP-MMSE, Brandt, Martin) | SPP-MMSE | SPP-MMSE \| Brandt \| Martin | `NR4NoiseEstimationMethod` |
| **Adaptive Noise Estimation** (checkbox) | Enabled | On / Off | `NR4AdaptiveNoise` |
| **Reduction (dB):** | 10.0 dB | 0.0–40.0 dB | `NR4ReductionAmount` |
| **Smoothing (%):** | 0 | 0–100 | `NR4SmoothingFactor` |
| **Whitening (%):** | 0 | 0–100 | `NR4WhiteningFactor` |
| **Masking Depth:** | 0.50 | 0.00–1.00 | `NR4MaskingDepth` |
| **Suppression:** | 0.50 | 0.00–1.00 | `NR4SuppressionStrength` |
| **Reset Defaults** (button) | — | — | — |

## Tips

- If the noise character on your frequency changes rapidly (pulse noise, QRM bursts), keep **Adaptive Noise Estimation** enabled so the estimator can follow the changing floor.
- If you notice the noise estimator pulling down signals during a long transmission from a weak station, try disabling **Adaptive Noise Estimation** to prevent the engine from treating the incoming signal as part of the noise floor.
- Clicking **Reset Defaults** on the NR4 tab restores all NR4 parameters to their defaults, including re-enabling **Adaptive Noise Estimation**.

## Troubleshooting

- **Desired signals are being suppressed along with noise** — the adaptive estimator may be classifying a weak or steady signal as noise. Uncheck **Adaptive Noise Estimation** to freeze the noise floor estimate.
- **Noise suppression stops tracking after a while** — verify that **Adaptive Noise Estimation** is checked. If the noise character has changed significantly since AetherSDR started, the frozen estimate may no longer match the current floor.

## Related

- [Adjust NR4 reduction amount in dB](adjust-nr4-reduction-amount-in-db.md)
- [Tune NR4 masking depth and suppression strength](tune-nr4-masking-depth-and-suppression-strength.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
