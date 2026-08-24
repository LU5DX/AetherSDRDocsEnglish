# AetherDSP Settings

The **AetherDSP Settings** dialog (`Settings > AetherDSP Settings...`) controls the client-side noise-reduction engines built into AetherSDR: NR2, NR4, MNR, RN2, BNR, and DFNR. Open it at any time; a radio connection is not required to change these parameters. All values are saved automatically when you close the dialog. The six DSP modules are selectable via a toggle row at the top; clicking a toggle also activates or bypasses that engine.

The dialog uses a custom frameless title bar with window controls matching the chrome family of NetworkDiagnosticsDialog and AetherialAudioStrip. Dialog position and size are persisted automatically between sessions. Drag the title bar to move the dialog; double-click the title bar to toggle maximize/restore. Drag any edge or corner to resize (6 px resize hit zone around the inner content widget).

The dialog and all its controls are themed using the current AetherSDR theme. The dialog background uses the `dialog/aetherDsp` theme color set, and sliders use the `applyPrimarySliderStyle()` style function instead of a hard-coded dark stylesheet.

## Before you start

- AetherSDR must be running.
- Decide which noise-reduction engine is active for your slice before tuning its parameters. Adjusting a disabled engine has no audible effect.

## Opening the dialog

1. Click `Settings > AetherDSP Settings...`.
2. The **AetherDSP Settings** dialog opens. Select the tab for the engine you want to adjust.

---

## NR2 tab

NR2 is the musical-noise-reduction engine. Click the **NR2** tab to access its controls.

### Controls

| Control                              | Kind                                                                                                        | Default                                                                                                        |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| **Gain Method**                      | Radio buttons                                                                                               | Gamma                                                                                                          |
| **NPE Method**                       | Radio buttons                                                                                               | OSMS                                                                                                           |
| **AE Filter (artifact elimination)** | Checkbox                                                                                                    | Enabled                                                                                                        |
| **Reduction:**                       | Slider                                                                                                      | 1.50                                                                                                           |
| **Smoothing:**                       | Slider                                                                                                      | 0.85                                                                                                           |
| **Threshold:**                       | Slider                                                                                                      | 0.20                                                                                                           |
| **Reset Defaults (↺ icon)**          | Button (flat icon)                                                                                          | —                                                                                                              |

### Control descriptions

**Gain Method** selects the gain-curve mapping NR2 uses. `NR2GainMethod` is stored as an integer: Linear = 0, Log = 1, Gamma = 2, Trained = 3. Gamma suits most voice modes.

**NPE Method** selects the noise power estimator. `NR2NpeMethod` is stored as an integer: OSMS = 0, MMSE = 1, NSTAT = 2.

**AE Filter (artifact elimination)** toggles the anti-artefact post-filter (`NR2AeFilter`). Leave this enabled unless you are specifically testing raw NR2 output.

**Reduction:** (`NR2GainMax`) sets the maximum reduction depth NR2 can apply. Higher values suppress more noise but can affect speech naturalness.

**Smoothing:** (`NR2GainSmooth`) controls how smoothly the noise estimate tracks changes. Higher values produce smoother but slower tracking.

**Threshold:** (`NR2Qspp`) sets the speech-presence-probability threshold below which NR2 treats audio as noise. Raise this if speech is being suppressed; lower it if noise breaks through during pauses.

**Reset Defaults (↺ icon)** restores the NR2 tab to its factory values: Gain Method = Gamma, NPE Method = OSMS, AE Filter = enabled, Reduction = 1.50, Smoothing = 0.85, Threshold = 0.20.

### Steps — adjust NR2 reduction depth

1. Open `Settings > AetherDSP Settings...`.
2. Click the **NR2** tab.
3. Drag the **Reduction:** slider to the desired value (default 1.50).
4. Close the dialog. The value is saved automatically.

---

## NR4 tab

NR4 uses the libspecbleach library. On Windows, NR4 requires LLVM (clang-cl) to compile; if LLVM is not installed, the NR4 toggle is dimmed with a tooltip instructing you to install LLVM from llvm.org and rebuild. Click the **NR4** tab to access its controls.

### Controls

| Control                              | Kind                                                                                                        | Default                                                                                                        |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| **Noise Estimation:**                | Radio buttons                                                                                               | MMSE                                                                                                           |
| **Adaptive Noise Estimation**        | Checkbox                                                                                                    | Enabled                                                                                                        |
| **Reduction (dB):**                  | Slider                                                                                                      | 10.0                                                                                                           |
| **Smoothing (%):**                   | Slider                                                                                                      | 0                                                                                                              |
| **Whitening (%):**                   | Slider                                                                                                      | 0                                                                                                              |
| **Masking Depth:**                   | Slider                                                                                                      | 0.50                                                                                                           |
| **Suppression:**                     | Slider                                                                                                      | 0.50                                                                                                           |
| **Reset Defaults (↺ icon)**          | Button (flat icon)                                                                                          | —                                                                                                              |

### Control descriptions

**Noise Estimation:** selects the noise-floor estimator NR4 uses. `NR4NoiseEstimationMethod` is stored as an integer: MMSE = 0, Brandt = 1, Martin = 2.

**Adaptive Noise Estimation** (`NR4AdaptiveNoise`) enables continuous re-estimation of the noise floor. Enable this when the noise floor varies rapidly.

**Reduction (dB):** (`NR4ReductionAmount`) sets the maximum noise reduction NR4 applies in decibels. At 0.0 dB NR4 applies no attenuation; at 40.0 dB it applies the maximum available suppression. The default of 10.0 dB suits most SSB conditions.

**Smoothing (%):** (`NR4SmoothingFactor`) applies time-domain smoothing to the NR4 noise estimate. If raising `NR4ReductionAmount` causes musical noise, try increasing this first.

**Whitening (%):** (`NR4WhiteningFactor`) flattens the spectral shape of residual noise after suppression.

**Masking Depth:** (`NR4MaskingDepth`) controls the spectral-masking depth.

**Suppression:** (`NR4SuppressionStrength`) sets overall NR4 suppression strength.

**Reset Defaults (↺ icon)** restores the NR4 tab to its factory values: Noise Estimation = MMSE, Adaptive Noise Estimation = enabled, Reduction = 10.0 dB, Smoothing = 0, Whitening = 0, Masking Depth = 0.50, Suppression = 0.50.

### Steps — adjust NR4 reduction amount

1. Open `Settings > AetherDSP Settings...`.
2. Click the **NR4** tab.
3. Drag the **Reduction (dB):** slider left to decrease suppression or right to increase it. The current value is shown to the right of the slider.
4. Close the dialog. The value is saved automatically.

### Tips

- Start near the default of 10.0 dB and increase in small steps while monitoring audio quality. Values above 25–30 dB can introduce processing artifacts on weaker signals.
- **Smoothing (%):** and **Suppression:** interact with the reduction amount. If raising `NR4ReductionAmount` causes musical noise, try increasing smoothing first.
- Enable **Adaptive Noise Estimation** when the noise floor varies rapidly so NR4 re-estimates the floor continuously.

---

## MNR tab

MNR is the MMSE-Wiener noise-reduction engine with asymmetric gain smoothing. It is available on macOS only. On Windows and Linux builds the MNR toggle is dimmed — the engine has no backend on those platforms. Click the **MNR** tab to access its controls.

### Controls

| Control                              | Kind                                                                                                        | Default                                                                                                        |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| **Enable MNR (macOS only)**          | Checkbox                                                                                                    | Read from audio engine                                                                                         |
| **Strength**                         | Slider                                                                                                      | 100                                                                                                            |

### Control descriptions

**Enable MNR (macOS only)** (`MnrEnabled`) enables the MMSE-Wiener noise reduction engine with asymmetric gain smoothing. The initial state of the checkbox reflects the current state of the audio engine at the time the dialog opens.

**Strength** (`MnrStrength`) adjusts MNR aggressiveness. 0 is mild suppression; 100 is maximum suppression. The value is persisted internally as a normalized 0.00–1.00 range.

---

## RN2 tab

The **RN2** tab (RNNoise engine) hosts a **Noise Floor** slider. Sets the percentage of the original signal that remains mixed under the denoised audio. Zero yields full suppression (silent between phrases); 10–20% keeps a steady quiet floor so the receiver still sounds alive.

### Controls

| Control                              | Kind                                                                                                        | Default                                                                                                        |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| **Noise Floor (RN2 dry mix)**        | Slider                                                                                                      | 0                                                                                                              |

### Control descriptions

**Noise Floor (RN2 dry mix)** (`Rn2SettingsModel`) mixes a percentage of the original signal under the denoised audio. Affects received audio only; the transmit denoiser is unchanged. The slider range is 0–100%, with 0 providing full suppression.

### Steps — adjust RN2 noise floor

1. Open `Settings > AetherDSP Settings...`.
2. Click the **RN2** tab.
3. Drag the **Noise Floor** slider to the desired percentage. Lower values give stronger suppression; higher values keep more of the original signal in the output.
4. Close the dialog. The value is saved automatically.

---

## BNR tab

The **BNR** tab displays information about the NVIDIA noise-reduction engine. BNR intensity is controlled from the overlay menu, not from this dialog. On builds without the NVIDIA Broadcast SDK the BNR toggle is dimmed.

---

## DFNR tab

DFNR uses the DeepFilterNet3 neural network for noise reduction. Click the **DFNR** tab to access its controls.

### Controls

| Control                              | Kind                                                                                                        | Default                                                                                                        |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| **Attenuation Limit**                | Slider                                                                                                      | 100                                                                                                            |
| **Post-Filter Beta**                 | Slider                                                                                                      | 0.00                                                                                                           |

### Control descriptions

**Attenuation Limit** (`DfnrAttenLimit`) sets the maximum noise attenuation DeepFilterNet3 may apply. At 0 the output is passed through unchanged; at 100 the maximum attenuation is applied.

**Post-Filter Beta** (`DfnrPostFilterBeta`) applies an additional post-filter for extra suppression beyond what DeepFilterNet3 provides on its own. At 0.00 the post-filter is inactive. The value is stored internally multiplied by 100.

---

## Troubleshooting

- **Slider has no audible effect** — confirm that the engine whose tab you are adjusting is the active noise-reduction engine for your slice. Enabling another engine simultaneously may mask its contribution.
- **Speech sounds hollow or distorted at high NR4 reduction values** — lower **Reduction (dB):** and enable **Adaptive Noise Estimation** so the noise floor estimate stays accurate.
- **MNR controls are grayed out** — MNR is available on macOS only. On Linux and Windows the MNR tab is informational.
- **NR4 toggle is grayed out on Windows** — NR4 requires LLVM (clang-cl) to compile. Install LLVM from llvm.org and rebuild AetherSDR to enable NR4.
- **Changes appear to reset** — each tab has a **Reset Defaults** button. Verify you have not accidentally clicked it.
- **Slider appearance does not match screenshots** — the dialog now uses themed slider styling via `applyPrimarySliderStyle()`. The slider colors follow the current theme rather than a hard-coded color scheme. To change slider appearance, change your active theme in AetherSDR's theme settings.

---

## Related

- [Enable or disable NR4 adaptive noise estimation](enable-or-disable-nr4-adaptive-noise-estimation.md)
- [Tune NR4 masking depth and suppression strength](tune-nr4-masking-depth-and-suppression-strength.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)