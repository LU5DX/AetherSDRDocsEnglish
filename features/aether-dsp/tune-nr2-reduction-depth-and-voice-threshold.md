# Tune NR2 Reduction Depth and Voice Threshold

This page explains how to adjust NR2's maximum noise reduction depth and speech-presence threshold in the AetherDSP Settings dialog. These two sliders control how aggressively NR2 suppresses noise and how sensitively it protects speech from being treated as noise.

## Before you start

- AetherSDR must be running. A radio connection is not required to change these settings.
- NR2 must be active on the slice you want to affect. This page covers parameter tuning only, not enabling NR2.

## Steps

1. Open `Settings > AetherDSP Settings...`.
2. Click the **NR2** tab.
3. Adjust the **Reduction Depth:** slider to set the maximum suppression depth. The default is **1.50**; the valid range is **0.50–2.00**. Higher values suppress more noise but increase the risk of speech distortion.
4. Adjust the **Voice Threshold:** slider to set the speech-presence-probability threshold. The default is **0.20**; the valid range is **0.05–0.50**. Lower values preserve quieter speech but may allow more noise through.
5. Settings are saved automatically when you move a slider. No additional confirmation step is needed.

## What each control does

| Control | Default | Valid Range | Persisted Setting | Behavior |
|---|---|---|---|---|
| **Reduction Depth:** | 1.50 | 0.50–2.00 | `NR2GainMax` | Sets the maximum NR2 reduction depth. Higher values suppress more noise; lower values preserve more signal character. |
| **Voice Threshold:** | 0.20 | 0.05–0.50 | `NR2Qspp` | Sets the speech-presence-probability threshold. Lower values detect quieter speech as voice, reducing suppression of weak signals. Higher values require stronger speech presence before holding back noise reduction. |
| **Smoothing:** | 0.85 | 0.50–0.98 | `NR2GainSmooth` | Controls how smoothly the noise estimate tracks changes. Higher values give a steadier estimate that reacts more slowly to rapid noise changes. |
| **AE Filter (artifact elimination)** | On | On / Off | `NR2AeFilter` | Toggles the anti-artifact post-filter that reduces ringing and musical noise. |
| **Gain Method** | Gamma | Linear / Log / Gamma / Trained | `NR2GainMethod` | Selects the gain-curve mapping used during suppression. |
| **NPE Method** | OSMS | OSMS / MMSE / NSTAT | `NR2NpeMethod` | Selects the noise power estimator. |
| **Reset Defaults** | — | — | — | Restores all NR2 controls to defaults: Gamma, OSMS, AE on, 1.50, 0.85, 0.20. |

## Tips

- If speech sounds hollow or distorted, reduce **Reduction Depth:** toward 1.00 or enable **AE Filter (artifact elimination)** if it is off.
- If noise breaks through on weak signals, try lowering **Voice Threshold:** toward 0.05 so that quiet speech is detected more readily and suppression is held back.
- If NR2 reacts too slowly when noise conditions change quickly, reduce **Smoothing:** toward 0.50 to make the noise estimate track faster.
- Use **Reset Defaults** to return to a known-good baseline before making a new round of adjustments.

## Troubleshooting

- **Speech sounds muffled or over-processed** — **Reduction Depth:** may be set too high. Lower it toward 1.00. Also verify **AE Filter (artifact elimination)** is checked, as it reduces the musical-noise artifacts that can accompany heavy suppression.
- **Noise is still audible even at maximum Reduction Depth:** (2.00)** — NR2 may not be the right engine for this noise type. See [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md).
- **Sliders snap back or do not hold their values** — This can indicate a settings-file permissions issue. Confirm AetherSDR has write access to its configuration directory and restart the application.

## Related

- [Switch NR2 gain method between Linear, Log, Gamma and Trained](switch-nr2-gain-method-between-linear-log-gamma-and-trained.md)
- [Change NR2 noise power estimator (OSMS/MMSE/NSTAT)](change-nr2-noise-power-estimator-osms-mmse-nstat.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Adjust NR4 reduction amount in dB](adjust-nr4-reduction-amount-in-db.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
