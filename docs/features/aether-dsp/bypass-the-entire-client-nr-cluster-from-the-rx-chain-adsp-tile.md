# AetherDSP Settings

The AetherDSP Settings dialog provides advanced configuration for all client-side noise reduction engines in AetherSDR. It includes six DSP modules: NR2, NR4, MNR, DFNR, RN2, and BNR.

## Opening the dialog

- From the RX Chain strip, double-click the **ADSP** tile.
- From the VFO DSP grid, click the **ADSP** button.

## Dialog window

The dialog has a frameless title bar with a grip glyph (⋮⋮) on the left. The title bar includes three buttons:

- — (Minimize) — Minimizes the dialog.
- □ (Maximize) — Maximizes or restores the dialog.
- × (Close) — Closes the dialog.

Drag the title bar to move the dialog. Double-click the title bar to toggle maximize/restore. Drag any edge or corner to resize (6 px resize hit zone).

The dialog position and size are automatically persisted across sessions using the setting key `AetherDspDialogGeometry`.

The dialog uses theme-aware styling applied through the `ThemeManager`. Colors are derived from the active color theme rather than hardcoded values.

## Toggle row

The top of the dialog contains six toggle buttons that serve as both tab selectors and engine enable/disable controls:

- **NR2** — Musical-noise-reduction engine
- **NR4** — libspecbleach spectral noise reduction
- **MNR** — macOS MMSE-Wiener noise reduction (dimmed on Windows/Linux)
- **DFNR** — DeepFilterNet3 neural noise reduction
- **RN2** — RNNoise neural noise reduction
- **BNR** — NVIDIA Broadcast neural denoising (dimmed without NVIDIA Broadcast SDK)

Clicking a toggle activates that engine and selects its tab. Clicking it again deactivates the engine. Only one engine can be active at a time — NR2, NR4, and DFNR are mutually exclusive. MNR and BNR may stack in some builds.

Each toggle button has an accessible name that includes its label (e.g., "NR2 noise-reduction method") for assistive technology and automation bridge support.

The last active client NR engine is persisted in the `LastClientNr` setting. If DFNR is unavailable and was previously active, the preference is automatically cleared.

## NR2 tab

Controls for the musical-noise-reduction engine.

| Control                          | Type         | Default | Range                | Setting Key       | Behavior                                                        |
|----------------------------------|--------------|---------|----------------------|-------------------|-----------------------------------------------------------------|
| Gain Method                      | Radio button | Gamma   | Linear, Log, Gamma, Trained | `NR2GainMethod`   | Selects gain-curve mapping used by NR2. Stored as integer 0-3.  |
| NPE Method                       | Radio button | OSMS    | OSMS, MMSE, NSTAT    | `NR2NpeMethod`    | Selects noise power estimator. Stored as integer 0-2.           |
| AE Filter (artifact elimination) | Checkbox     | True    | —                    | `NR2AeFilter`     | Toggles the anti-artefact post-filter.                          |
| Reduction:                       | Slider       | 1.50    | 0.50-2.00            | `NR2GainMax`      | Sets maximum NR2 reduction depth. Slider stores value*100.      |
| Smoothing:                       | Slider       | 0.85    | 0.50-0.98            | `NR2GainSmooth`   | Controls how smoothly the noise estimate tracks changes.        |
| Threshold:                       | Slider       | 0.20    | 0.05-0.50            | `NR2Qspp`         | Sets speech-presence-probability threshold.                     |
| Reset Defaults (↺ icon)          | Push button  | —       | —                    | —                 | Restores NR2 tab defaults (Gamma/OSMS/AE on, 1.50/0.85/0.20).    |

Sliders on this tab use theme-aware styling via `applyPrimarySliderStyle()`.

## NR4 tab

Controls for the libspecbleach spectral noise reduction engine.

| Control | Type | Default | Range | Setting Key | Behavior |
|---------|------|---------|-------|-------------|----------|
| Noise Estimation: | Radio button | MMSE | MMSE, Brandt, Martin | `NR4NoiseEstimationMethod` | Selects noise-floor estimator (stored as integer 0-2). |
| Adaptive Noise Estimation | Checkbox | True | — | `NR4AdaptiveNoise` | Enables continuous re-estimation of the noise floor. |
| Reduction (dB): | Slider | 10.0 | 0.0-40.0 | `NR4ReductionAmount` | Sets maximum NR4 noise reduction in dB. |
| Smoothing (%): | Slider | 0 | 0-100 | `NR4SmoothingFactor` | Time-domain smoothing of NR4 noise estimate. |
| Whitening (%): | Slider | 0 | 0-100 | `NR4WhiteningFactor` | Flattens residual noise spectral shape. |
| Masking Depth: | Slider | 0.50 | 0.00-1.00 | `NR4MaskingDepth` | Controls spectral-masking depth. |
| Suppression: | Slider | 0.50 | 0.00-1.00 | `NR4SuppressionStrength` | Overall NR4 suppression strength. |
| Reset Defaults (↺ icon) | Push button | — | — | — | Restores NR4 defaults (MMSE/adaptive on, 10 dB, 0, 0, 0.50, 0.50). |

Sliders on this tab use theme-aware styling via `applyPrimarySliderStyle()`.

**Note:** NR4 requires LLVM (clang-cl) on Windows. The toggle is dimmed if LLVM is not installed. Install LLVM from llvm.org and rebuild AetherSDR to enable NR4.

## MNR tab

Controls for the macOS MMSE-Wiener noise reduction engine. This tab and its controls are available only on macOS builds.

| Control | Type | Default | Range | Setting Key | Behavior |
|---------|------|---------|-------|-------------|----------|
| Enable MNR (macOS only) | Checkbox | — | — | `MnrEnabled` | Enables MMSE-Wiener noise reduction with asymmetric gain smoothing. Initial state read live from AudioEngine. |
| Strength | Slider | 100 | 0-100 | `MnrStrength` | Adjusts MNR aggressiveness (0 mild, 100 max). Persisted as normalized 0.00-1.00. |
| Reset Defaults (↺ icon) | Push button | — | — | — | Restores MNR defaults (Strength 100). |

## DFNR tab

Controls for the DeepFilterNet3 neural noise reduction engine.

**Note:** DeepFilterNet3 is an advanced neural-network-based noise reduction system that uses deep learning to suppress noise while preserving speech quality. It may require significant CPU resources. DFNR requires DeepFilterNet to be set up and AetherSDR rebuilt. If unavailable, the DFNR toggle shows a tooltip explaining this.

| Control | Type | Default | Range | Setting Key | Behavior |
|---------|------|---------|-------|-------------|----------|
| Attenuation Limit | Slider | 100 | 0-100 dB | `DfnrAttenLimit` | Sets maximum noise attenuation applied by DeepFilterNet3. 0 = passthrough; 100 = maximum suppression. |
| Post-Filter Beta | Slider | 0.00 | 0.00-0.30 | `DfnrPostFilterBeta` | Applies an additional post-filter for extra suppression. Slider stores value*100 internally. |
| Reset Defaults (↺ icon) | Push button | — | — | — | Restores DFNR defaults (Attenuation 100, Beta 0.00). |

## RN2 tab

Controls for the RNNoise neural noise reduction engine.

| Control | Type | Default | Range | Setting Key | Behavior |
|---------|------|---------|-------|-------------|----------|
| Noise Floor (RN2 dry mix) | Slider | 0 | 0-100 | — | Sets the percentage of the original signal RN2 leaves under the denoised audio. Zero yields full suppression (silent between phrases); 10-20% keeps a steady quiet floor so the receiver still sounds alive. Affects received audio only; the transmit denoiser is unchanged. Persisted by `Rn2SettingsModel` and exposed to the DSP chain via `AetherDspWidget`'s `rn2DryMixChanged` signal. |
| Reset Defaults (↺ icon) | Push button | — | — | — | Restores RN2 defaults (Noise Floor 0). |

## BNR tab

Selects the NVIDIA Broadcast neural denoising page. Intensity is controlled from the overlay menu. The toggle is dimmed on builds without the NVIDIA Broadcast SDK. The Reset Defaults button is a no-op on this tab.

## Bypassing all client NR engines

To quickly disable all client-side noise reduction without opening the AetherDSP Settings dialog:

1. Locate the **ADSP** tile in the RX Chain strip.
2. Double-click the **ADSP** tile to open AetherDSP Settings.
3. In the toggle row at the top, click each active (lit) noise reduction toggle to deactivate it.
4. Continue until all toggles are dimmed.

The ADSP tile updates to reflect the bypassed state. No client NR engines are now active, returning the audio to the raw sliced audio stream from the radio.

## Tips

- The six DSP toggles (NR2, NR4, MNR, DFNR, RN2, BNR) serve as both tab selectors and engine enable/disable controls.
- NR2, NR4, and DFNR are mutually exclusive — only one can be active at a time.
- MNR and BNR may stack with other engines in some builds.
- The Reset Defaults button (↺ icon) on each tab restores that engine's parameters to their default values.
- Settings are persisted across sessions.
- The dialog uses theme-aware styling. Colors are drawn from the active color theme rather than fixed values.
- The last active client NR engine is persisted; if DFNR becomes unavailable, the stored preference is automatically cleared.
- The NR2 tab includes a "Reduction:" slider (not "Reduction Depth:") and a "Threshold:" slider (not "Voice Threshold:").