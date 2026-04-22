# Choosing the right noise reduction: NR2, NR4, DFNR, MNR

AetherSDR provides four client-side noise-reduction engines — NR2, NR4, DFNR, and MNR — each with different strengths. This page describes what each engine does and when to use one over another, so you can pick the right starting point before tuning parameters.

## Before you start

- No radio connection is required to open or adjust these settings.
- Open `Settings > AetherDSP Settings...` to reach all four engines.

## Steps

1. Open `Settings > AetherDSP Settings...`.
2. Click the tab for the engine you want to use: **NR2**, **NR4**, **DFNR**, or **MNR**.
3. Adjust controls as needed (see the table below).
4. Close the dialog. Settings are saved immediately when any control changes.

## What each control does

### NR2 tab — musical-noise reduction

NR2 uses a spectral-gain approach to suppress noise. It is tunable and works on all platforms.

| Control | Default | Range | Setting key | What it does |
|---|---|---|---|---|
| Gain Method | Gamma | Linear \| Log \| Gamma \| Trained | `NR2GainMethod` | Selects the gain-curve mapping. Gamma suits most speech signals. Trained uses a model built from real speech and noise samples. |
| NPE Method | OSMS | OSMS \| MMSE \| NSTAT | `NR2NpeMethod` | Selects the noise power estimator. OSMS tracks a running minimum; MMSE minimizes estimation error; NSTAT adapts to changing noise. |
| AE Filter (artifact elimination) | On | On / Off | `NR2AeFilter` | Reduces ringing and musical-noise artifacts. Leave on unless you hear side effects. |
| Reduction Depth: | 1.50 | 0.50–2.00 | `NR2GainMax` | Maximum suppression depth. Higher values remove more noise but risk distorting speech. |
| Smoothing: | 0.85 | 0.50–0.98 | `NR2GainSmooth` | How quickly the noise estimate tracks changes. Higher values are steadier but slower to adapt. |
| Voice Threshold: | 0.20 | 0.05–0.50 | `NR2Qspp` | Speech-presence-probability threshold. Lower values preserve quiet speech but may pass more noise. |
| Reset Defaults | — | — | — | Restores Gain Method to Gamma, NPE Method to OSMS, AE Filter on, and sliders to 1.50 / 0.85 / 0.20. |

### NR4 tab — libspecbleach

NR4 applies spectral bleaching and works well on continuous, broadband noise. Reduction depth is expressed in dB, giving precise control.

| Control | Default | Range | Setting key | What it does |
|---|---|---|---|---|
| Noise Estimation Method | SPP-MMSE | SPP-MMSE \| Brandt \| Martin | `NR4NoiseEstimationMethod` | Selects the noise-floor estimator. SPP-MMSE balances noise estimation with speech preservation; Brandt suits non-stationary noise; Martin suits slowly varying noise floors. |
| Adaptive Noise Estimation | On | On / Off | `NR4AdaptiveNoise` | Continuously re-estimates the noise floor as conditions change. |
| Reduction (dB): | 10.0 | 0.0–40.0 dB | `NR4ReductionAmount` | Maximum noise reduction in dB. |
| Smoothing (%): | 0 | 0–100 | `NR4SmoothingFactor` | Time-domain smoothing of the noise estimate. |
| Whitening (%): | 0 | 0–100 | `NR4WhiteningFactor` | Flattens residual noise spectral shape after reduction. |
| Masking Depth: | 0.50 | 0.00–1.00 | `NR4MaskingDepth` | Controls spectral-masking depth. |
| Suppression: | 0.50 | 0.00–1.00 | `NR4SuppressionStrength` | Overall NR4 suppression strength. |
| Reset Defaults | — | — | — | Restores SPP-MMSE, adaptive on, 10 dB, 0, 0, 0.50, 0.50. |

### DFNR tab — DeepFilterNet3

DFNR uses a deep neural network (DeepFilterNet3) for noise suppression. It is the most aggressive option and works best when the noise floor is continuous and the signal is speech.

| Control | Default | Range | Setting key | What it does |
|---|---|---|---|---|
| Attenuation Limit | 100 | 0–100 dB | `DfnrAttenLimit` | Maximum attenuation applied by DeepFilterNet3. Set to 0 for passthrough; 100 for maximum suppression. |
| Post-Filter Beta | 0.00 | 0.00–0.30 | `DfnrPostFilterBeta` | Applies an additional post-filter after DeepFilterNet3 for extra suppression. |

### MNR tab — macOS only

MNR is an MMSE-Wiener noise reduction engine with asymmetric gain smoothing, available on macOS only.

| Control | Default | Range | Setting key | What it does |
|---|---|---|---|---|
| Enable MNR (macOS only) | (read from audio engine) | On / Off | `MnrEnabled` | Enables MNR. |
| Strength | 100 | 0–100 | `MnrStrength` | Aggressiveness. 0 is mild; 100 is maximum. Persisted as a normalized 0.00–1.00 value. |

## Tips

- Use **NR2** when you want fine-grained control over speech detection and gain behavior, or when noise is intermittent.
- Use **NR4** when noise is broadband and steady and you want to set a precise dB reduction target.
- Use **DFNR** for the strongest suppression on speech signals, particularly in heavy QRM or atmospheric noise. Start with **Attenuation Limit** below 100 and raise it only as needed to avoid over-processing.
- Use **MNR** on macOS when a lighter, system-integrated option is preferred.
- Only one engine is active per receive path at a time; which engine is active is selected elsewhere in the UI, not in this dialog. This dialog only adjusts each engine's parameters.
- Click **Reset Defaults** on the NR2 or NR4 tab to recover a known-good baseline if adjustments produce unwanted artifacts.

## Related

- [AetherDSP Settings overview](../../features/aether-dsp/overview.md)
- [Tune NR2 reduction depth and voice threshold](../../features/aether-dsp/tune-nr2-reduction-depth-and-voice-threshold.md)
- [Switch NR2 gain method between Linear, Log, Gamma and Trained](../../features/aether-dsp/switch-nr2-gain-method-between-linear-log-gamma-and-trained.md)
- [Change NR2 noise power estimator (OSMS/MMSE/NSTAT)](../../features/aether-dsp/change-nr2-noise-power-estimator-osms-mmse-nstat.md)
- [Adjust NR4 reduction amount in dB](../../features/aether-dsp/adjust-nr4-reduction-amount-in-db.md)
- [Enable or disable NR4 adaptive noise estimation](../../features/aether-dsp/enable-or-disable-nr4-adaptive-noise-estimation.md)
- [Tune NR4 masking depth and suppression strength](../../features/aether-dsp/tune-nr4-masking-depth-and-suppression-strength.md)
- [Set DeepFilterNet3 attenuation limit for strong or weak signals](../../features/aether-dsp/set-deepfilternet3-attenuation-limit-for-strong-or-weak-signals.md)
- [Configure DFNR post-filter beta for extra suppression](../../features/aether-dsp/configure-dfnr-post-filter-beta-for-extra-suppression.md)
- [Enable MNR on macOS and set its strength](../../features/aether-dsp/enable-mnr-on-macos-and-set-its-strength.md)
- [Reset NR2 or NR4 parameters to defaults](../../features/aether-dsp/reset-nr2-or-nr4-parameters-to-defaults.md)
