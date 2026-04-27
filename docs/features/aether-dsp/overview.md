# AetherDSP Settings overview

AetherDSP Settings gives you fine-grained control over AetherSDR's client-side noise-reduction engines. Use this dialog to tune the tradeoff between noise suppression and speech fidelity across four configurable engines: NR2, NR4, MNR, and DFNR.

## Before you start

- No radio connection is required to open or adjust AetherDSP Settings.
- Each engine must be enabled separately (from the applet panel or overlay menu) before its settings take effect.

## How it works

Open the dialog via `Settings > AetherDSP Settings...`. The dialog contains six tabs — **NR2**, **NR4**, **MNR**, **DFNR**, **RN2**, and **BNR** — each covering a different noise-reduction engine. Settings are saved immediately when you change any control; no Apply or OK button is required.

### NR2 tab

NR2 is a frequency-domain musical-noise-reduction engine. Its parameters control how aggressively noise is suppressed and how the engine identifies speech versus noise.

| Control | Type | Default | Range | Persisted key |
|---|---|---|---|---|
| Gain Method | Radio buttons | Gamma | Linear, Log, Gamma, Trained | `NR2GainMethod` |
| NPE Method | Radio buttons | OSMS | OSMS, MMSE, NSTAT | `NR2NpeMethod` |
| AE Filter (artifact elimination) | Checkbox | Enabled | — | `NR2AeFilter` |
| Reduction Depth: | Slider | 1.50 | 0.50–2.00 | `NR2GainMax` |
| Smoothing: | Slider | 0.85 | 0.50–0.98 | `NR2GainSmooth` |
| Voice Threshold: | Slider | 0.20 | 0.05–0.50 | `NR2Qspp` |

- **Gain Method** selects the gain-curve mapping applied during noise reduction. Gamma matches typical speech amplitude patterns; Trained uses a model built from real speech and noise samples.
- **NPE Method** selects the noise power estimator. OSMS tracks the noise floor using a running minimum; MMSE minimizes expected estimation error; NSTAT adapts to noise that changes over time.
- **AE Filter (artifact elimination)** toggles a post-filter that reduces ringing and musical artifacts common in frequency-domain processing.
- **Reduction Depth:** sets the maximum suppression depth. Higher values suppress more noise but risk distorting speech.
- **Smoothing:** controls how quickly the noise estimate tracks changes. Higher values give steadier but slower adaptation.
- **Voice Threshold:** sets the speech-presence-probability threshold. Lower values preserve quiet speech but may allow more noise through.
- **Reset Defaults** restores NR2 to: Gamma, OSMS, AE Filter on, Reduction Depth 1.50, Smoothing 0.85, Voice Threshold 0.20.

### NR4 tab

NR4 uses the libspecbleach library for spectral subtraction-based noise reduction, with independent control over suppression strength and spectral shaping.

| Control | Type | Default | Range | Persisted key |
|---|---|---|---|---|
| Noise Estimation Method | Radio buttons | SPP-MMSE | SPP-MMSE, Brandt, Martin | `NR4NoiseEstimationMethod` |
| Adaptive Noise Estimation | Checkbox | Enabled | — | `NR4AdaptiveNoise` |
| Reduction (dB): | Slider | 10.0 | 0.0–40.0 dB | `NR4ReductionAmount` |
| Smoothing (%): | Slider | 0 | 0–100 | `NR4SmoothingFactor` |
| Whitening (%): | Slider | 0 | 0–100 | `NR4WhiteningFactor` |
| Masking Depth: | Slider | 0.50 | 0.00–1.00 | `NR4MaskingDepth` |
| Suppression: | Slider | 0.50 | 0.00–1.00 | `NR4SuppressionStrength` |

- **Noise Estimation Method** selects how NR4 estimates the noise floor. SPP-MMSE balances noise estimation with speech preservation; Brandt uses recursive smoothing across critical bands; Martin uses running spectral minima.
- **Adaptive Noise Estimation** enables continuous re-estimation of the noise floor as conditions change.
- **Reduction (dB):** sets the maximum noise reduction in decibels.
- **Smoothing (%):** applies time-domain smoothing to the noise estimate.
- **Whitening (%):** flattens the spectral shape of residual noise.
- **Masking Depth:** controls the depth of spectral masking applied.
- **Suppression:** sets overall NR4 suppression strength.
- **Reset Defaults** restores NR4 to: SPP-MMSE, Adaptive Noise Estimation on, Reduction 10.0 dB, Smoothing 0, Whitening 0, Masking Depth 0.50, Suppression 0.50.

### MNR tab

MNR is an MMSE-Wiener noise-reduction engine with asymmetric gain smoothing. It is available on macOS only.

| Control | Type | Default | Range | Persisted key |
|---|---|---|---|---|
| Enable MNR (macOS only) | Checkbox | (read from audio engine) | — | `MnrEnabled` |
| Strength | Slider | 100 | 0–100 | `MnrStrength` |

- **Enable MNR (macOS only)** turns the engine on or off. The initial state reflects what the audio engine reports at the time the dialog opens.
- **Strength** sets aggressiveness from mild (0) to maximum (100). The value is persisted as a normalized 0.00–1.00 figure.

### DFNR tab

DFNR uses the DeepFilterNet3 neural network for deep noise suppression.

| Control | Type | Default | Range | Persisted key |
|---|---|---|---|---|
| Attenuation Limit | Slider | 100 | 0–100 dB | `DfnrAttenLimit` |
| Post-Filter Beta | Slider | 0.00 | 0.00–0.30 | `DfnrPostFilterBeta` |

- **Attenuation Limit** caps the maximum attenuation DeepFilterNet3 applies. 0 is passthrough; 100 is maximum.
- **Post-Filter Beta** applies an additional post-processing filter for extra suppression beyond what the neural network provides.

### RN2 tab

The RN2 tab covers the RNNoise engine. It is informational only; there are no adjustable parameters on this tab.

### BNR tab

The BNR tab covers NVIDIA noise reduction. Intensity is controlled from the overlay menu, not from this dialog.

## Tips

- Changes take effect immediately; you can monitor the audio while adjusting sliders.
- On the NR2 tab, reducing **Voice Threshold:** below its default (0.20) helps recover weak or low-power speech, but may increase noise breakthrough.
- On the NR4 tab, leaving **Smoothing (%):** and **Whitening (%):** at 0 gives the most natural-sounding output; increase them only if residual noise is objectionable.
- Use **Reset Defaults** on the NR2 or NR4 tab to recover a known-good baseline before experimenting.

## Related

- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
- [Tune NR2 reduction depth and voice threshold](tune-nr2-reduction-depth-and-voice-threshold.md)
- [Switch NR2 gain method between Linear, Log, Gamma and Trained](switch-nr2-gain-method-between-linear-log-gamma-and-trained.md)
- [Change NR2 noise power estimator (OSMS/MMSE/NSTAT)](change-nr2-noise-power-estimator-osms-mmse-nstat.md)
- [Adjust NR4 reduction amount in dB](adjust-nr4-reduction-amount-in-db.md)
- [Enable or disable NR4 adaptive noise estimation](enable-or-disable-nr4-adaptive-noise-estimation.md)
- [Tune NR4 masking depth and suppression strength](tune-nr4-masking-depth-and-suppression-strength.md)
- [Enable MNR on macOS and set its strength](enable-mnr-on-macos-and-set-its-strength.md)
- [Set DeepFilterNet3 attenuation limit for strong or weak signals](set-deepfilternet3-attenuation-limit-for-strong-or-weak-signals.md)
- [Configure DFNR post-filter beta for extra suppression](configure-dfnr-post-filter-beta-for-extra-suppression.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
