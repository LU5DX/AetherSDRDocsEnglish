# Reset NR2 or NR4 parameters to defaults

Use this page to restore all NR2 or NR4 controls to their factory defaults with a single click, undoing any experimental tuning.

## Before you start

- Open `Settings > AetherDSP Settings...` to reach the AetherDSP Settings dialog.
- Identify which engine you want to reset: NR2 or NR4.

## Steps

### Reset NR2 to defaults

1. Click `Settings > AetherDSP Settings...`.
2. Click the **NR2** tab.
3. Click **Reset Defaults**.

All NR2 controls return to their default values immediately.

### Reset NR4 to defaults

1. Click `Settings > AetherDSP Settings...`.
2. Click the **NR4** tab.
3. Click **Reset Defaults**.

All NR4 controls return to their default values immediately.

## What each control does

### NR2 defaults restored by Reset Defaults

| Control | Default | Valid Range | Setting key |
|---|---|---|---|
| Gain Method | Gamma | Linear \| Log \| Gamma \| Trained | `NR2GainMethod` |
| NPE Method | OSMS | OSMS \| MMSE \| NSTAT | `NR2NpeMethod` |
| AE Filter (artifact elimination) | Enabled | — | `NR2AeFilter` |
| Reduction Depth: | 1.50 | 0.50–2.00 | `NR2GainMax` |
| Smoothing: | 0.85 | 0.50–0.98 | `NR2GainSmooth` |
| Voice Threshold: | 0.20 | 0.05–0.50 | `NR2Qspp` |

### NR4 defaults restored by Reset Defaults

| Control | Default | Valid Range | Setting key |
|---|---|---|---|
| Noise Estimation Method | SPP-MMSE | SPP-MMSE \| Brandt \| Martin | `NR4NoiseEstimationMethod` |
| Adaptive Noise Estimation | Enabled | — | `NR4AdaptiveNoise` |
| Reduction (dB): | 10.0 | 0.0–40.0 dB | `NR4ReductionAmount` |
| Smoothing (%): | 0 | 0–100 | `NR4SmoothingFactor` |
| Whitening (%): | 0 | 0–100 | `NR4WhiteningFactor` |
| Masking Depth: | 0.50 | 0.00–1.00 | `NR4MaskingDepth` |
| Suppression: | 0.50 | 0.00–1.00 | `NR4SuppressionStrength` |

## Tips

- **Reset Defaults** applies changes immediately. There is no confirmation prompt, but you can re-tune individual controls afterwards without reopening the dialog.
- Each tab has its own **Reset Defaults** button. Clicking it on the NR2 tab does not affect NR4 settings, and vice versa.
- All values are persisted as soon as a control changes, including when reset. Closing the dialog without further changes leaves the defaults saved.

## Related

- [AetherDSP Settings overview](overview.md)
- [Tune NR2 reduction depth and voice threshold](tune-nr2-reduction-depth-and-voice-threshold.md)
- [Switch NR2 gain method between Linear, Log, Gamma and Trained](switch-nr2-gain-method-between-linear-log-gamma-and-trained.md)
- [Change NR2 noise power estimator (OSMS/MMSE/NSTAT)](change-nr2-noise-power-estimator-osms-mmse-nstat.md)
- [Adjust NR4 reduction amount in dB](adjust-nr4-reduction-amount-in-db.md)
- [Enable or disable NR4 adaptive noise estimation](enable-or-disable-nr4-adaptive-noise-estimation.md)
- [Tune NR4 masking depth and suppression strength](tune-nr4-masking-depth-and-suppression-strength.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
