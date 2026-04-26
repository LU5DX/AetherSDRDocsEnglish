# AetherDSP Settings overview

AetherDSP Settings is AetherSDR's client-side noise-reduction control center. It gives you fine-grained access to four DSP engines — NR2, NR4, MNR, and DFNR — so you can tune the tradeoff between noise suppression and speech fidelity without touching the radio.

## Before you start

- No radio connection is required. AetherDSP Settings can be opened at any time.
- Decide which engine you want to adjust. If you are unsure which engine fits your situation, see [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md).

## How it works

Open AetherDSP Settings via `Settings > AetherDSP Settings...`. The dialog contains six tabs: **NR2**, **NR4**, **MNR**, **DFNR**, **RN2**, and **BNR**. Each tab controls one engine independently. Changes take effect immediately and are persisted automatically — there is no global Save button.

### NR2 tab

NR2 is a frequency-domain musical-noise-reduction engine. Its controls let you select the gain curve, noise power estimator, and speech detection sensitivity.

| Control | Kind | Default | Valid range | Setting key |
|---|---|---|---|---|
| Gain Method | Radio buttons | Gamma | Linear, Log, Gamma, Trained | `NR2GainMethod` |
| NPE Method | Radio buttons | OSMS | OSMS, MMSE, NSTAT | `NR2NpeMethod` |
| AE Filter (artifact elimination) | Checkbox | Enabled | — | `NR2AeFilter` |
| Reduction Depth: | Slider | 1.50 | 0.50–2.00 | `NR2GainMax` |
| Smoothing: | Slider | 0.85 | 0.50–0.98 | `NR2GainSmooth` |
| Voice Threshold: | Slider | 0.20 | 0.05–0.50 | `NR2Qspp` |
| Reset Defaults | Button | — | — | — |

**Gain Method** selects the gain-curve mapping applied during noise reduction. **NPE Method** selects which algorithm estimates the noise power floor. **AE Filter (artifact elimination)** applies a post-filter that reduces ringing and musical artifacts. **Reduction Depth:** sets the maximum suppression depth — higher values suppress more noise but risk distorting speech. **Smoothing:** controls how quickly the noise estimate tracks signal changes — higher values give a steadier but slower response. **Voice Threshold:** sets the speech-presence-probability threshold — lower values preserve quiet speech but may let more noise through.

Click **Reset Defaults** to restore NR2 to: Gamma, OSMS, AE Filter on, Reduction Depth 1.50, Smoothing 0.85, Voice Threshold 0.20.

### NR4 tab

NR4 uses the libspecbleach library for spectral noise reduction. It exposes a noise estimation method, an adaptive mode, and several fine-tuning controls.

| Control | Kind | Default | Valid range | Setting key |
|---|---|---|---|---|
| Noise Estimation Method | Radio buttons | SPP-MMSE | SPP-MMSE, Brandt, Martin | `NR4NoiseEstimationMethod` |
| Adaptive Noise Estimation | Checkbox | Enabled | — | `NR4AdaptiveNoise` |
| Reduction (dB): | Slider | 10.0 dB | 0.0–40.0 dB | `NR4ReductionAmount` |
| Smoothing (%): | Slider | 0 | 0–100 | `NR4SmoothingFactor` |
| Whitening (%): | Slider | 0 | 0–100 | `NR4WhiteningFactor` |
| Masking Depth: | Slider | 0.50 | 0.00–1.00 | `NR4MaskingDepth` |
| Suppression: | Slider | 0.50 | 0.00–1.00 | `NR4SuppressionStrength` |
| Reset Defaults | Button | — | — | — |

**Noise Estimation Method** selects the algorithm used to estimate the noise floor. **Adaptive Noise Estimation** enables continuous re-estimation as conditions change. **Reduction (dB):** sets the maximum noise reduction applied. **Smoothing (%):** applies time-domain smoothing to the noise estimate. **Whitening (%):** flattens the spectral shape of any residual noise. **Masking Depth:** controls how deeply spectral masking is applied. **Suppression:** sets the overall NR4 suppression strength.

Click **Reset Defaults** to restore NR4 to: SPP-MMSE, Adaptive Noise Estimation on, 10.0 dB, Smoothing 0, Whitening 0, Masking Depth 0.50, Suppression 0.50.

### MNR tab

MNR is an MMSE-Wiener noise reduction engine with asymmetric gain smoothing. It is available on macOS only.

| Control | Kind | Default | Valid range | Setting key |
|---|---|---|---|---|
| Enable MNR (macOS only) | Checkbox | Read from audio engine | — | `MnrEnabled` |
| Strength | Slider | 100 | 0–100 | `MnrStrength` |

**Enable MNR (macOS only)** activates the engine. **Strength** adjusts aggressiveness: 0 is mild, 100 is maximum suppression.

### DFNR tab

DFNR uses DeepFilterNet3, a neural-network-based noise suppressor.

| Control | Kind | Default | Valid range | Setting key |
|---|---|---|---|---|
| Attenuation Limit | Slider | 100 dB | 0–100 dB | `DfnrAttenLimit` |
| Post-Filter Beta | Slider | 0.00 | 0.00–0.30 | `DfnrPostFilterBeta` |

**Attenuation Limit** caps the maximum noise attenuation DeepFilterNet3 applies. Setting it to 0 is effectively passthrough; 100 is maximum attenuation. **Post-Filter Beta** adds an additional post-filter stage for extra suppression beyond the neural network output.

### RN2 tab

The RN2 tab covers the RNNoise engine. It is informational only — there are no adjustable parameters on this tab.

### BNR tab

The BNR tab covers the NVIDIA noise suppression engine. Intensity is controlled from the overlay menu, not from this dialog.

## Tips

- All changes persist immediately. You do not need to close the dialog for settings to take effect.
- Each tab's **Reset Defaults** button affects only that tab's parameters, not the other engines.
- The MNR tab controls are active on macOS only. On other platforms the tab is visible but the engine will not be available.

## Related

- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
- [Switch NR2 gain method between Linear, Log, Gamma and Trained](switch-nr2-gain-method-between-linear-log-gamma-and-trained.md)
- [Change NR2 noise power estimator (OSMS/MMSE/NSTAT)](change-nr2-noise-power-estimator-osms-mmse-nstat.md)
- [Tune NR2 reduction depth and voice threshold](tune-nr2-reduction-depth-and-voice-threshold.md)
- [Adjust NR4 reduction amount in dB](adjust-nr4-reduction-amount-in-db.md)
- [Enable or disable NR4 adaptive noise estimation](enable-or-disable-nr4-adaptive-noise-estimation.md)
- [Tune NR4 masking depth and suppression strength](tune-nr4-masking-depth-and-suppression-strength.md)
- [Enable MNR on macOS and set its strength](enable-mnr-on-macos-and-set-its-strength.md)
- [Set DeepFilterNet3 attenuation limit for strong or weak signals](set-deepfilternet3-attenuation-limit-for-strong-or-weak-signals.md)
- [Configure DFNR post-filter beta for extra suppression](configure-dfnr-post-filter-beta-for-extra-suppression.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
