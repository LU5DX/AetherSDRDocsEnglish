# AetherDSP Settings overview

AetherDSP Settings gives you fine-grained control over AetherSDR's client-side noise-reduction engines. Use this dialog to tune the tradeoff between noise suppression and speech fidelity across six configurable engines: NR2, NR4, MNR, DFNR, RN2, and BNR.

## Before you start

- No radio connection is required to open or adjust AetherDSP Settings.
- Each engine must be enabled separately (from the applet panel or overlay menu) before its settings take effect.

## How it works

Open the dialog via `Settings > AetherDSP Settings...`. The dialog contains six tabs — **NR2**, **NR4**, **MNR**, **DFNR**, **RN2**, and **BNR** — each covering a different noise-reduction engine. Clicking a tab also activates or bypasses that engine; the six DSP toggles act as exclusive selectors and engine enable/disable controls. Settings are saved immediately when you change any control; no Apply or OK button is required.

The dialog has a frameless 18 px gradient title bar with a grip glyph (⋮⋮) on the left and window control buttons (—, □, ×) on the right, matching the chrome family of NetworkDiagnosticsDialog and AetherialAudioStrip. The controls inside the dialog are provided by an embedded `AetherDspWidget` in dialog mode, with all fonts scaled to 13 px. Dialog position and size are persisted across sessions using the `AetherDspDialogGeometry` setting key.

### NR2 tab

NR2 is a frequency-domain musical-noise-reduction engine. Its parameters control how aggressively noise is suppressed and how the engine identifies speech versus noise.

| Control | Type | Default | Range | Persisted key |
|---|---|---|---|---|
| Gain Method | Radio buttons | Gamma | Linear \| Log \| Gamma \| Trained | `NR2GainMethod` |
| NPE Method | Radio buttons | OSMS | OSMS \| MMSE \| NSTAT | `NR2NpeMethod` |
| AE Filter (artifact elimination) | Checkbox | Enabled | — | `NR2AeFilter` |
| Reduction: | Slider | 1.50 | 0.50–2.00 | `NR2GainMax` |
| Smoothing: | Slider | 0.85 | 0.50–0.98 | `NR2GainSmooth` |
| Threshold: | Slider | 0.20 | 0.05–0.50 | `NR2Qspp` |
| Reset Defaults (↺ icon) | Push button | — | — | — (no key) |

- **Gain Method** selects the gain-curve mapping applied during noise reduction. Gamma matches typical speech amplitude patterns; Trained uses a model built from real speech and noise samples.
- **NPE Method** selects the noise power estimator. OSMS tracks the noise floor using a running minimum; MMSE minimizes expected estimation error; NSTAT adapts to noise that changes over time.
- **AE Filter (artifact elimination)** toggles a post-filter that reduces ringing and musical artifacts common in frequency-domain processing.
- **Reduction:** sets the maximum suppression depth. Higher values suppress more noise but risk distorting speech.
- **Smoothing:** controls how quickly the noise estimate tracks changes. Higher values give steadier but slower adaptation.
- **Threshold:** sets the speech-presence-probability threshold. Lower values preserve quiet speech but may allow more noise through.
- **Reset Defaults** restores NR2 to: Gamma, OSMS, AE Filter on, Reduction 1.50, Smoothing 0.85, Threshold 0.20.

### NR4 tab

NR4 uses the libspecbleach library for spectral subtraction-based noise reduction, with independent control over suppression strength and spectral shaping. On Windows, NR4 requires the LLVM toolchain (clang-cl) to compile libspecbleach's C99 variable-length arrays. If AetherSDR was built without LLVM, the NR4 toggle is disabled and a tooltip explains the missing dependency.

| Control | Type | Default | Range | Persisted key |
|---|---|---|---|---|
| Noise Estimation: | Radio buttons | MMSE | MMSE \| Brandt \| Martin | `NR4NoiseEstimationMethod` |
| Adaptive Noise Estimation | Checkbox | Enabled | — | `NR4AdaptiveNoise` |
| Reduction (dB): | Slider | 10.0 | 0.0–40.0 dB | `NR4ReductionAmount` |
| Smoothing (%): | Slider | 0 | 0–100 | `NR4SmoothingFactor` |
| Whitening (%): | Slider | 0 | 0–100 | `NR4WhiteningFactor` |
| Masking Depth: | Slider | 0.50 | 0.00–1.00 | `NR4MaskingDepth` |
| Suppression: | Slider | 0.50 | 0.00–1.00 | `NR4SuppressionStrength` |
| Reset Defaults (↺ icon) | Push button | — | — | — (no key) |

- **Noise Estimation:** selects the noise-floor estimator. MMSE balances noise estimation with speech preservation; Brandt uses recursive smoothing across critical bands; Martin uses running spectral minima.
- **Adaptive Noise Estimation** enables continuous re-estimation of the noise floor as conditions change.
- **Reduction (dB):** sets the maximum noise reduction in decibels.
- **Smoothing (%):** applies time-domain smoothing to the noise estimate.
- **Whitening (%):** flattens the spectral shape of residual noise.
- **Masking Depth:** controls the depth of spectral masking applied.
- **Suppression:** sets overall NR4 suppression strength.
- **Reset Defaults** restores NR4 to: MMSE, Adaptive Noise Estimation on, Reduction 10.0 dB, Smoothing 0, Whitening 0, Masking Depth 0.50, Suppression 0.50.

### MNR tab

MNR is an MMSE-Wiener noise-reduction engine with asymmetric gain smoothing. It is available on macOS only; on Windows and Linux builds the MNR toggle is dimmed because the engine has no backend on those platforms.

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

The BNR tab covers NVIDIA noise reduction. Intensity is controlled from the overlay menu, not from this dialog. On builds without the NVIDIA Broadcast SDK the BNR toggle is dimmed.

## Window controls

The dialog's custom title bar provides these controls:

| Control | Behavior |
|---|---|
| Grip glyph (⋮⋮) | Visual indicator only; click and drag any part of the title bar to move the dialog |
| — (Minimize) | Minimizes the dialog |
| □ (Maximize) | Maximizes or restores the dialog |
| × (Close) | Closes the dialog |
| Double-click title bar | Toggles maximize/restore |

## Resizing

Click and drag any edge or corner of the dialog to resize it. The cursor changes to indicate the resize direction. A 6 px resize hit zone extends inward from each edge.

## Tips

- Changes take effect immediately; you can monitor the audio while adjusting sliders.
- On the NR2 tab, reducing **Threshold:** below its default (0.20) helps recover weak or low-power speech, but may increase noise breakthrough.
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