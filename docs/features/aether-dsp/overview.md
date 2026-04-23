# AetherDSP Settings overview

AetherDSP Settings gives you fine-grained control over AetherSDR's client-side noise-reduction engines. Use it to balance noise suppression against speech fidelity across four independent processing engines: NR2, NR4, MNR, and DFNR.

## Before you start

- No radio connection is required to open or adjust AetherDSP Settings.
- Decide which engine you want to tune. See [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md) if you are unsure.

## How it works

Open the dialog at `Settings > AetherDSP Settings...`. It presents six tabs — NR2, NR4, MNR, DFNR, RN2, and BNR — each corresponding to a separate noise-reduction engine. Adjustments take effect immediately and are persisted automatically; no explicit save step is required. Each tab contains a `Reset Defaults` button (where applicable) that restores that tab's parameters to their factory values.

- **NR2** — A frequency-domain engine focused on musical-noise reduction. Offers three algorithm knobs (Gain Method, NPE Method, AE Filter) and three level sliders.
- **NR4** — Built on libspecbleach. Provides dB-calibrated reduction control and several spectral shaping parameters.
- **MNR** — An MMSE-Wiener engine available on macOS only.
- **DFNR** — Uses the DeepFilterNet3 neural network. Two controls set the maximum attenuation and optional post-filtering.
- **RN2** — Uses RNNoise. This tab is informational; it has no adjustable parameters.
- **BNR** — Uses NVIDIA noise reduction. Intensity is controlled from the overlay menu, not from this dialog.

## What each control does

### NR2 tab

| Control | Kind | Default | Range | Setting key |
|---|---|---|---|---|
| Gain Method | Radio buttons | Gamma | Linear \| Log \| Gamma \| Trained | `NR2GainMethod` |
| NPE Method | Radio buttons | OSMS | OSMS \| MMSE \| NSTAT | `NR2NpeMethod` |
| AE Filter (artifact elimination) | Checkbox | Enabled | — | `NR2AeFilter` |
| Reduction Depth: | Slider | 1.50 | 0.50–2.00 | `NR2GainMax` |
| Smoothing: | Slider | 0.85 | 0.50–0.98 | `NR2GainSmooth` |
| Voice Threshold: | Slider | 0.20 | 0.05–0.50 | `NR2Qspp` |
| Reset Defaults | Button | — | — | — |

- **Gain Method** — Selects the gain-curve mapping applied by NR2. Gamma is the default and models typical speech amplitude patterns. Linear and Log offer simpler amplitude scaling. Trained uses a model built from speech and noise samples.
- **NPE Method** — Selects the noise power estimator. OSMS (Optimal Smoothing Minimum Statistics) tracks the noise floor via a running minimum. MMSE minimizes expected estimation error. NSTAT adapts to noise that changes over time.
- **AE Filter (artifact elimination)** — Toggles an anti-artefact post-filter that reduces ringing and musical noise typical of frequency-domain processing.
- **Reduction Depth:** — Sets the maximum NR2 reduction depth. Higher values suppress more noise but increase the risk of speech distortion.
- **Smoothing:** — Controls how smoothly the noise estimate tracks signal changes. Higher values give a steadier but slower-adapting estimate.
- **Voice Threshold:** — Sets the speech-presence-probability threshold. Lower values preserve quieter speech but may allow more noise through.
- **Reset Defaults** — Restores NR2 to: Gain Method = Gamma, NPE Method = OSMS, AE Filter = enabled, Reduction Depth = 1.50, Smoothing = 0.85, Voice Threshold = 0.20.

### NR4 tab

| Control | Kind | Default | Range | Setting key |
|---|---|---|---|---|
| Noise Estimation Method | Radio buttons | SPP-MMSE | SPP-MMSE \| Brandt \| Martin | `NR4NoiseEstimationMethod` |
| Adaptive Noise Estimation | Checkbox | Enabled | — | `NR4AdaptiveNoise` |
| Reduction (dB): | Slider | 10.0 | 0.0–40.0 dB | `NR4ReductionAmount` |
| Smoothing (%): | Slider | 0 | 0–100 | `NR4SmoothingFactor` |
| Whitening (%): | Slider | 0 | 0–100 | `NR4WhiteningFactor` |
| Masking Depth: | Slider | 0.50 | 0.00–1.00 | `NR4MaskingDepth` |
| Suppression: | Slider | 0.50 | 0.00–1.00 | `NR4SuppressionStrength` |
| Reset Defaults | Button | — | — | — |

- **Noise Estimation Method** — Selects the NR4 noise-floor estimator. SPP-MMSE balances noise estimation with speech preservation. Brandt uses recursive smoothing across critical frequency bands and handles non-stationary noise well. Martin applies running spectral minima, suited to slowly varying noise floors.
- **Adaptive Noise Estimation** — When enabled, the noise floor is continuously re-estimated during reception.
- **Reduction (dB):** — Sets the maximum noise reduction NR4 will apply, in decibels.
- **Smoothing (%):** — Applies time-domain smoothing to the noise estimate.
- **Whitening (%):** — Flattens the spectral shape of residual noise after processing.
- **Masking Depth:** — Controls the depth of spectral masking applied during noise suppression.
- **Suppression:** — Sets the overall NR4 suppression strength.
- **Reset Defaults** — Restores NR4 to: SPP-MMSE, Adaptive Noise Estimation enabled, Reduction = 10.0 dB, Smoothing = 0, Whitening = 0, Masking Depth = 0.50, Suppression = 0.50.

### MNR tab

| Control | Kind | Default | Range | Setting key |
|---|---|---|---|---|
| Enable MNR (macOS only) | Checkbox | Read from audio engine | — | `MnrEnabled` |
| Strength | Slider | 100 | 0–100 | `MnrStrength` |

- **Enable MNR (macOS only)** — Enables MMSE-Wiener noise reduction with asymmetric gain smoothing. Available on macOS only.
- **Strength** — Sets MNR aggressiveness. 0 is mild; 100 is maximum suppression.

### DFNR tab

| Control | Kind | Default | Range | Setting key |
|---|---|---|---|---|
| Attenuation Limit | Slider | 100 | 0–100 dB | `DfnrAttenLimit` |
| Post-Filter Beta | Slider | 0.00 | 0.00–0.30 | `DfnrPostFilterBeta` |

- **Attenuation Limit** — Sets the maximum noise attenuation DeepFilterNet3 will apply. 0 passes the signal through unprocessed; 100 applies full attenuation.
- **Post-Filter Beta** — Applies an additional post-filter on top of DeepFilterNet3 output for extra suppression. Leave at 0.00 unless residual noise remains after adjusting Attenuation Limit.

### RN2 tab

This tab is informational. RNNoise has no user-adjustable parameters in AetherDSP Settings.

### BNR tab

This tab is informational. BNR (NVIDIA) intensity is controlled from the overlay menu, not from this dialog.

## Tips

- All changes persist immediately. You do not need to close the dialog to apply a setting.
- Use `Reset Defaults` on the NR2 or NR4 tab to recover a known-good baseline before comparing parameter changes.
- On the NR4 tab, start with only `Reduction (dB):` and `Suppression:` adjusted, leaving Smoothing, Whitening, and Masking Depth at their defaults, then refine from there.
- MNR is available on macOS only. The `Enable MNR (macOS only)` checkbox will reflect the current audio engine state when the dialog opens.

## Related

- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
- [Tune NR2 reduction depth and voice threshold](tune-nr2-reduction-depth-and-voice-threshold.md)
- [Switch NR2 gain method between Linear, Log, Gamma and Trained](switch-nr2-gain-method-between-linear-log-gamma-and-trained.md)
- [Change NR2 noise power estimator (OSMS/MMSE/NSTAT)](change-nr2-noise-power-estimator-osms-mmse-nstat.md)
- [Adjust NR4 reduction amount in dB](adjust-nr4-reduction-amount-in-db.md)
- [Enable or disable NR4 adaptive noise estimation](enable-or-disable-nr4-adaptive-noise-estimation.md)
- [Tune NR4 masking depth and suppression strength](tune-nr4-masking-depth-and-suppression-strength.md)
- [Enable MNR on macOS and set its strength](enable-mnr-on-macos-and-set-its-strength.md)
- [Set DeepFilterNet3 attenuation limit for strong or weak signals](set-deepfilternet3-at
