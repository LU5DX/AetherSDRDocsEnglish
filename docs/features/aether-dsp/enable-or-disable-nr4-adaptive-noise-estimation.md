# Enable or disable NR4 adaptive noise estimation

NR4's adaptive noise estimation continuously re-estimates the noise floor as band conditions change. Enabling it helps maintain accurate noise reduction on signals with varying or non-stationary noise; disabling it freezes the noise floor estimate, which can be useful on very stable, quiet bands.

## Before you start

- AetherDSP Settings does not require a radio connection. You can adjust NR4 settings at any time.
- NR4 must be active on your receive chain for these settings to have audible effect.

## Steps

1. Click `Settings > AetherDSP Settings...`.
2. Click the **NR4** tab.
3. Check or uncheck **Adaptive Noise Estimation**.
   - Checked (default): NR4 continuously re-estimates the noise floor.
   - Unchecked: the noise floor estimate is frozen at its last computed value.

The setting takes effect immediately and is persisted as `NR4AdaptiveNoise`.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| **Adaptive Noise Estimation** | Enabled | On / Off | `NR4AdaptiveNoise` | Enables continuous re-estimation of the noise floor. |
| **Noise Estimation Method** | SPP-MMSE | SPP-MMSE \| Brandt \| Martin | `NR4NoiseEstimationMethod` | Selects which algorithm performs the noise-floor estimation that adaptive mode continuously updates. |
| **Reduction (dB):** | 10.0 dB | 0.0–40.0 dB | `NR4ReductionAmount` | Maximum noise reduction applied by NR4. |
| **Smoothing (%):** | 0 | 0–100 | `NR4SmoothingFactor` | Time-domain smoothing of the NR4 noise estimate. |
| **Whitening (%):** | 0 | 0–100 | `NR4WhiteningFactor` | Flattens residual noise spectral shape. |
| **Masking Depth:** | 0.50 | 0.00–1.00 | `NR4MaskingDepth` | Controls spectral-masking depth. |
| **Suppression:** | 0.50 | 0.00–1.00 | `NR4SuppressionStrength` | Overall NR4 suppression strength. |
| **Reset Defaults** | — | — | — | Restores NR4 defaults: SPP-MMSE, adaptive on, 10 dB, 0, 0, 0.50, 0.50. |

## Tips

- Adaptive noise estimation works in combination with the selected **Noise Estimation Method**. If you change the method, the adaptive tracker resets to that algorithm's initial estimate.
- On stable, low-noise bands where signals are consistent, disabling adaptive estimation and relying on a frozen noise floor can reduce unnecessary gain fluctuation during pauses in speech.
- If the noise floor changes frequently (e.g. moving between bands or during solar activity), keep adaptive estimation enabled.

## Troubleshooting

- **Noise reduction seems to pump or breathe on speech pauses** — try increasing **Smoothing (%):** or disabling **Adaptive Noise Estimation** to stabilize the noise floor estimate.
- **Noise is not being suppressed after conditions change** — if adaptive estimation is disabled, the frozen noise floor estimate may no longer match the actual noise. Re-enable **Adaptive Noise Estimation** or click **Reset Defaults** to restore a known state.

## Related

- [Adjust NR4 reduction amount in dB](adjust-nr4-reduction-amount-in-db.md)
- [Tune NR4 masking depth and suppression strength](tune-nr4-masking-depth-and-suppression-strength.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
