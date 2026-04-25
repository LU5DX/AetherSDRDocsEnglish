# Reset NR2 or NR4 parameters to defaults

Use this page to restore all NR2 or NR4 noise-reduction parameters to their factory defaults in a single click. This is useful after experimenting with settings and wanting a clean starting point.

## Before you start

- Open AetherSDR. No radio connection is required.

## Steps

### Reset NR2

1. Click `Settings > AetherDSP Settings...` to open the AetherDSP Settings dialog.
2. Click the **NR2** tab.
3. Click **Reset Defaults**.

All NR2 parameters return to their defaults immediately.

### Reset NR4

1. Click `Settings > AetherDSP Settings...` to open the AetherDSP Settings dialog.
2. Click the **NR4** tab.
3. Click **Reset Defaults**.

All NR4 parameters return to their defaults immediately.

## What each control does

### NR2 defaults restored by Reset Defaults

| Control | Setting key | Default |
|---|---|---|
| Gain Method | `NR2GainMethod` | Gamma |
| NPE Method | `NR2NpeMethod` | OSMS |
| AE Filter (artifact elimination) | `NR2AeFilter` | Enabled |
| Reduction Depth: | `NR2GainMax` | 1.50 (range 0.50–2.00) |
| Smoothing: | `NR2GainSmooth` | 0.85 (range 0.50–0.98) |
| Voice Threshold: | `NR2Qspp` | 0.20 (range 0.05–0.50) |

### NR4 defaults restored by Reset Defaults

| Control | Setting key | Default |
|---|---|---|
| Noise Estimation Method | `NR4NoiseEstimationMethod` | SPP-MMSE |
| Adaptive Noise Estimation | `NR4AdaptiveNoise` | Enabled |
| Reduction (dB): | `NR4ReductionAmount` | 10.0 (range 0.0–40.0 dB) |
| Smoothing (%): | `NR4SmoothingFactor` | 0 (range 0–100) |
| Whitening (%): | `NR4WhiteningFactor` | 0 (range 0–100) |
| Masking Depth: | `NR4MaskingDepth` | 0.50 (range 0.00–1.00) |
| Suppression: | `NR4SuppressionStrength` | 0.50 (range 0.00–1.00) |

## Tips

- **Reset Defaults** applies only to the tab currently being reset. Clicking it on the NR2 tab does not affect NR4 settings, and vice versa.
- Changes take effect immediately; no confirmation is required and no additional save step is needed.

## Related

- [AetherDSP Settings overview](overview.md)
- [Tune NR2 reduction depth and voice threshold](tune-nr2-reduction-depth-and-voice-threshold.md)
- [Switch NR2 gain method between Linear, Log, Gamma and Trained](switch-nr2-gain-method-between-linear-log-gamma-and-trained.md)
- [Change NR2 noise power estimator (OSMS/MMSE/NSTAT)](change-nr2-noise-power-estimator-osms-mmse-nstat.md)
- [Adjust NR4 reduction amount in dB](adjust-nr4-reduction-amount-in-db.md)
- [Enable or disable NR4 adaptive noise estimation](enable-or-disable-nr4-adaptive-noise-estimation.md)
- [Tune NR4 masking depth and suppression strength](tune-nr4-masking-depth-and-suppression-strength.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
