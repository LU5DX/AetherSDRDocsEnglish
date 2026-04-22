# AetherDSP Settings overview

The AetherDSP Settings dialog exposes the advanced parameters for AetherSDR's client-side noise-reduction engines. Use it to balance noise suppression against speech fidelity across four configurable engines: NR2, NR4, MNR, and DFNR.

## Before you start

- No radio connection is required. The dialog can be opened at any time.
- Identify which noise-reduction engine you want to tune. See [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md) if you are unsure.

## How it works

Open the dialog with `Settings > AetherDSP Settings...`. The dialog contains six tabs — **NR2**, **NR4**, **MNR**, **DFNR**, **RN2**, and **BNR** — each covering a separate processing engine. Changes take effect immediately and are persisted automatically; no Save button is required. Each tab also provides a **Reset Defaults** button (NR2 and NR4) to restore factory values.

### NR2 tab

NR2 is a frequency-domain musical-noise-reduction engine. It applies a gain curve to suppress noise while attempting to preserve speech.

| Control | Kind | Default | Valid range | Setting key |
|---|---|---|---|---|
| Gain Method | Radio button | Gamma | Linear \| Log \| Gamma \| Trained | `NR2GainMethod` |
| NPE Method | Radio button | OSMS | OSMS \| MMSE \| NSTAT | `NR2NpeMethod` |
| AE Filter (artifact elimination) | Checkbox | Enabled | — | `NR2AeFilter` |
| Reduction Depth: | Slider | 1.50 | 0.50–2.00 | `NR2GainMax` |
| Smoothing: | Slider | 0.85 | 0.50–0.98 | `NR2GainSmooth` |
| Voice Threshold: | Slider | 0.20 | 0.05–0.50 | `NR2Qspp` |

- **Gain Method** selects the gain-curve mapping applied during noise reduction. Gamma matches typical speech amplitude patterns and is the default. Linear and Log offer simpler mappings; Trained uses a model trained on real speech and noise samples.
- **NPE Method** selects the noise power estimator. OSMS (Optimal Smoothing Minimum Statistics) tracks the noise floor using a running minimum. MMSE minimizes expected estimation error. NSTAT adapts to noise that changes over time.
- **AE Filter (artifact elimination)** toggles a post-filter that reduces ringing and musical artifacts common in frequency-domain noise reduction.
- **Reduction Depth:** sets the maximum gain reduction NR2 can apply. Higher values suppress more noise but increase the risk of speech distortion.
- **Smoothing:** controls how quickly the noise estimate tracks signal changes. Higher values give a steadier but slower-adapting estimate.
- **Voice Threshold:** sets the speech-presence-probability threshold. Lower values preserve quiet speech but may allow more noise to pass.
- **Reset Defaults** restores all NR2 controls to: Gain Method = Gamma, NPE Method = OSMS, AE Filter enabled, Reduction Depth = 1.50, Smoothing = 0.85, Voice Threshold = 0.20.

### NR4 tab

NR4 uses the libspecbleach library for spectral subtraction-based noise reduction. It offers more direct control over reduction depth in dB.

| Control | Kind | Default | Valid range | Setting key |
|---|---|---|---|---|
| Noise Estimation Method | Radio button | SPP-MMSE | SPP-MMSE \| Brandt \| Martin | `NR4NoiseEstimationMethod` |
| Adaptive Noise Estimation | Checkbox | Enabled | — | `NR4AdaptiveNoise` |
| Reduction (dB): | Slider | 10.0 | 0.0–40.0 dB | `NR4ReductionAmount` |
| Smoothing (%): | Slider | 0 | 0–100 | `NR4SmoothingFactor` |
| Whitening (%): | Slider | 0 | 0–100 | `NR4WhiteningFactor` |
| Masking Depth: | Slider | 0.50 | 0.00–1.00 | `NR4MaskingDepth` |
| Suppression: | Slider | 0.50 | 0.00–1.00 | `NR4SuppressionStrength` |

- **Noise Estimation Method** selects the noise-floor estimator. SPP-MMSE balances noise estimation with speech preservation. Brandt uses recursive smoothing across critical frequency bands, suited to non-stationary noise. Martin uses running spectral minima, suited to slowly varying noise floors.
- **Adaptive Noise Estimation** enables continuous re-estimation of the noise floor as conditions change.
- **Reduction (dB):** sets the maximum noise reduction NR4 will apply, in decibels.
- **Smoothing (%):** applies time-domain smoothing to the noise estimate.
- **Whitening (%):** flattens the spectral shape of residual noise after reduction.
- **Masking Depth:** controls the depth of spectral masking applied during suppression.
- **Suppression:** sets NR4's overall suppression strength.
- **Reset Defaults** restores all NR4 controls to: Noise Estimation Method = SPP-MMSE, Adaptive Noise Estimation enabled, Reduction = 10.0 dB, Smoothing = 0, Whitening = 0, Masking Depth = 0.50, Suppression = 0.50.

### MNR tab

MNR is an MMSE-Wiener noise reducer with asymmetric gain smoothing. It is available on macOS only.

| Control | Kind | Default | Valid range | Setting key |
|---|---|---|---|---|
| Enable MNR (macOS only) | Checkbox | Read from audio engine | — | `MnrEnabled` |
| Strength | Slider | 100 | 0–100 | `MnrStrength` |

- **Enable MNR (macOS only)** toggles the MNR engine. The initial state reflects the current audio engine status.
- **Strength** adjusts aggressiveness. 0 is mild; 100 is maximum suppression. Persisted internally as a normalized value of 0.00–1.00.

### DFNR tab

DFNR uses the DeepFilterNet3 deep-learning model for noise reduction.

| Control | Kind | Default | Valid range | Setting key |
|---|---|---|---|---|
| Attenuation Limit | Slider | 100 | 0–100 dB | `DfnrAttenLimit` |
| Post-Filter Beta | Slider | 0.00 | 0.00–0.30 | `DfnrPostFilterBeta` |

- **Attenuation Limit** sets the maximum noise attenuation DeepFilterNet3 will apply. 0 is passthrough; 100 is maximum attenuation.
- **Post-Filter Beta** applies an additional post-filter on top of DeepFilterNet3's output for extra suppression. 0.00 disables the post-filter.

### RN2 tab

The RN2 tab covers the RNNoise engine. It is informational only; there are no adjustable parameters on this tab.

### BNR tab

The BNR tab covers the NVIDIA noise-reduction engine. Intensity for BNR is controlled from the overlay menu, not from this dialog.

## Tips

- Adjust one parameter at a time and monitor the effect on a live signal before changing another.
- On the NR2 tab, if you hear musical noise artifacts after increasing Reduction Depth, ensure **AE Filter (artifact elimination)** is enabled.
- On the NR4 tab, if the noise floor changes rapidly (e.g. mobile operation), enable **Adaptive Noise Estimation** and try the Brandt or SPP-MMSE estimator.
- **Reset Defaults** on either the NR2 or NR4 tab is a quick way to recover a known-good starting point without reopening the dialog from scratch.

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
