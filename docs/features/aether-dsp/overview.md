# AetherDSP Settings overview

AetherDSP Settings gives you direct access to the client-side noise-reduction engines built into AetherSDR. Use it to tune the tradeoff between noise suppression and speech fidelity across four adjustable engines: NR2, NR4, MNR, and DFNR.

## Before you start

- No radio connection is required to open this dialog or adjust its settings.
- Changes take effect immediately and are persisted automatically — there is no separate Save button.

## How it works

Open the dialog via `Settings > AetherDSP Settings...`. It contains six tabs, one per engine. Only NR2, NR4, MNR, and DFNR expose adjustable parameters; RN2 and BNR are informational or controlled elsewhere.

### NR2 tab

NR2 is a frequency-domain musical-noise-reduction engine. Its controls set how aggressively it suppresses noise and how carefully it tracks speech.

| Control | Kind | Default | Range | Setting key |
|---|---|---|---|---|
| Gain Method | Radio buttons | Gamma | Linear \| Log \| Gamma \| Trained | `NR2GainMethod` |
| NPE Method | Radio buttons | OSMS | OSMS \| MMSE \| NSTAT | `NR2NpeMethod` |
| AE Filter (artifact elimination) | Checkbox | Enabled | — | `NR2AeFilter` |
| Reduction Depth: | Slider | 1.50 | 0.50–2.00 | `NR2GainMax` |
| Smoothing: | Slider | 0.85 | 0.50–0.98 | `NR2GainSmooth` |
| Voice Threshold: | Slider | 0.20 | 0.05–0.50 | `NR2Qspp` |
| Reset Defaults | Button | — | — | — |

**Gain Method** selects the gain-curve mapping applied during noise reduction. Gamma matches typical speech amplitude patterns and is the default. Trained uses a model built from real speech and noise samples.

**NPE Method** selects the noise power estimator. OSMS tracks the noise floor using a running minimum. MMSE minimizes expected estimation error. NSTAT adapts to noise that changes over time.

**AE Filter (artifact elimination)** applies a post-filter to reduce ringing and musical artifacts common in frequency-domain noise reduction.

**Reduction Depth:** sets the maximum gain suppression applied. Higher values remove more noise but risk distorting speech.

**Smoothing:** controls how quickly the noise estimate follows changes in the signal. Higher values give a steadier but slower-adapting estimate.

**Voice Threshold:** sets the speech-presence-probability threshold below which NR2 treats the signal as noise. Lower values preserve quiet speech but may let more noise through.

**Reset Defaults** restores the NR2 tab to: Gain Method = Gamma, NPE Method = OSMS, AE Filter enabled, Reduction Depth = 1.50, Smoothing = 0.85, Voice Threshold = 0.20.

---

### NR4 tab

NR4 uses the libspecbleach library for spectral subtraction-based noise reduction. Its controls are expressed in dB and percentage terms.

| Control | Kind | Default | Range | Setting key |
|---|---|---|---|---|
| Noise Estimation Method | Radio buttons | SPP-MMSE | SPP-MMSE \| Brandt \| Martin | `NR4NoiseEstimationMethod` |
| Adaptive Noise Estimation | Checkbox | Enabled | — | `NR4AdaptiveNoise` |
| Reduction (dB): | Slider | 10.0 dB | 0.0–40.0 dB | `NR4ReductionAmount` |
| Smoothing (%): | Slider | 0 | 0–100 | `NR4SmoothingFactor` |
| Whitening (%): | Slider | 0 | 0–100 | `NR4WhiteningFactor` |
| Masking Depth: | Slider | 0.50 | 0.00–1.00 | `NR4MaskingDepth` |
| Suppression: | Slider | 0.50 | 0.00–1.00 | `NR4SuppressionStrength` |
| Reset Defaults | Button | — | — | — |

**Noise Estimation Method** selects the NR4 noise-floor estimator. SPP-MMSE balances noise estimation with speech preservation. Brandt uses recursive smoothing across critical frequency bands. Martin uses running spectral minima, suited to slowly varying noise floors.

**Adaptive Noise Estimation** enables continuous re-estimation of the noise floor as conditions change.

**Reduction (dB):** sets the maximum noise reduction applied, in decibels.

**Smoothing (%):** applies time-domain smoothing to the noise estimate.

**Whitening (%):** flattens the spectral shape of residual noise after reduction.

**Masking Depth:** controls the depth of spectral masking applied during reduction.

**Suppression:** sets the overall NR4 suppression strength.

**Reset Defaults** restores the NR4 tab to: Noise Estimation Method = SPP-MMSE, Adaptive Noise Estimation enabled, Reduction = 10.0 dB, Smoothing = 0, Whitening = 0, Masking Depth = 0.50, Suppression = 0.50.

---

### MNR tab

MNR is an MMSE-Wiener noise reduction engine with asymmetric gain smoothing. It is available on macOS only.

| Control | Kind | Default | Range | Setting key |
|---|---|---|---|---|
| Enable MNR (macOS only) | Checkbox | Read from audio engine | — | `MnrEnabled` |
| Strength | Slider | 100 | 0–100 | `MnrStrength` |

**Enable MNR (macOS only)** activates the MNR engine. Its initial state reflects whether MNR is currently active in the audio engine.

**Strength** adjusts MNR aggressiveness. 0 is the mildest setting; 100 is maximum suppression. The value is persisted as a normalized 0.00–1.00 internally.

---

### DFNR tab

DFNR uses the DeepFilterNet3 deep-learning model for noise reduction.

| Control | Kind | Default | Range | Setting key |
|---|---|---|---|---|
| Attenuation Limit | Slider | 100 | 0–100 dB | `DfnrAttenLimit` |
| Post-Filter Beta | Slider | 0.00 | 0.00–0.30 | `DfnrPostFilterBeta` |

**Attenuation Limit** caps the maximum noise attenuation DeepFilterNet3 applies. 0 passes the signal through unmodified; 100 allows maximum attenuation.

**Post-Filter Beta** applies an additional post-filter on top of DeepFilterNet3's output for extra suppression. 0.00 disables the post-filter.

---

### RN2 tab

The RN2 tab (RNNoise engine) is informational only. There are no adjustable parameters on this tab.

---

### BNR tab

The BNR tab (NVIDIA noise reduction) is informational only. BNR intensity is controlled from the overlay menu, not from this dialog.

---

## Tips

- All changes persist immediately. You do not need to close the dialog to hear the effect.
- Use **Reset Defaults** on the NR2 or NR4 tab to recover a known-good starting point before experimenting.
- On NR2, raising **Reduction Depth:** while lowering **Voice Threshold:** increases aggressiveness but increases the risk of speech artifacts. Enable **AE Filter (artifact elimination)** to mitigate this.
- On NR4, leave **Adaptive Noise Estimation** enabled for signals where the noise floor varies — for example, during band-opening conditions.
- DFNR's **Post-Filter Beta** range is 0.00–0.30. Small increments have a noticeable effect; start at 0.05 and increase gradually.

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
