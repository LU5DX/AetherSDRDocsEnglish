# Adjust NR4 Reduction Amount in dB

The `NR4ReductionAmount` setting controls how many decibels of noise suppression NR4 (libspecbleach) applies. Raising it removes more noise; lowering it preserves more of the original signal character.

## Before you start

- AetherSDR must be running. A radio connection is not required to change this setting.
- Decide roughly how much suppression you need. The default of 10.0 dB suits most SSB conditions.

## Steps

1. Open `Settings > AetherDSP Settings...`.
2. Click the **NR4** tab.
3. Locate the **Reduction (dB):** slider.
4. Drag the slider left to decrease suppression or right to increase it. The current value is displayed to the right of the slider.
5. Close the dialog. The value is saved automatically.

## What each control does

| Control | Default | Valid range | Persisted key |
|---|---|---|---|
| **Reduction (dB):** | 10.0 dB | 0.0–40.0 dB | `NR4ReductionAmount` |

**Reduction (dB):** sets the maximum noise reduction NR4 will apply in decibels. At 0.0 dB, NR4 applies no attenuation. At 40.0 dB, it applies the maximum available suppression.

## Tips

- Start near the default of 10.0 dB and increase in small steps while monitoring audio quality. High values (above 25–30 dB) can introduce processing artifacts on weaker signals.
- **Smoothing (%):** (`NR4SmoothingFactor`) and **Suppression:** (`NR4SuppressionStrength`) interact with the reduction amount. If raising `NR4ReductionAmount` causes musical noise, try increasing smoothing first.
- If the noise floor varies rapidly, enable **Adaptive Noise Estimation** (`NR4AdaptiveNoise`) so NR4 re-estimates the floor continuously rather than relying on a static measurement.

## Troubleshooting

- **Slider has no audible effect** — confirm that NR4 is the active noise-reduction engine for your slice. Enabling NR2 or another engine simultaneously may mask NR4's contribution.
- **Speech sounds hollow or distorted at high reduction values** — lower **Reduction (dB):** and check that **Adaptive Noise Estimation** is enabled so the noise floor estimate stays accurate.

## Related

- [Enable or disable NR4 adaptive noise estimation](enable-or-disable-nr4-adaptive-noise-estimation.md)
- [Tune NR4 masking depth and suppression strength](tune-nr4-masking-depth-and-suppression-strength.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
