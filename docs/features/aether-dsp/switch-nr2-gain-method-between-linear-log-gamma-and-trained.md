# AetherDSP Settings

The AetherDSP Settings dialog tunes the advanced parameters of AetherSDR's client-side noise-reduction engines (NR2, NR4, MNR, DFNR, RN2, BNR), letting operators dial in the tradeoff between noise suppression and speech fidelity. The six DSP modules are selectable via a toggle row at the top; clicking a toggle also activates or bypasses that engine.

## Opening the dialog

1. Click **Settings > AetherDSP Settings...**.
2. The dialog opens with a frameless 18 px gradient title bar containing a grip glyph (⋮⋮) on the left and the dialog title.

The dialog can be moved by clicking and dragging the title bar. Double-click the title bar to toggle maximize/restore. Resize by clicking and dragging any edge or corner (6 px resize hit zone).

## Dialog controls

The title bar contains three window control buttons and a grip glyph:

| Button                    | Action                                                                                                                                                                                                       | Notes                                                                                                                                                                      |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **⋮⋮ (Grip glyph)**       | Visual reference indicator on the left of the title bar.                                                                                                                                                     |                                                                                                                                                                            |
| **— (Minimize)**          | Minimizes the dialog.                                                                                                                                                                                        |                                                                                                                                                                            |
| **□ (Maximize)**          | Maximizes or restores the dialog.                                                                                                                                                                            |                                                                                                                                                                            |
| **× (Close)**             | Closes the dialog.                                                                                                                                                                                           |                                                                                                                                                                            |
| Noise Floor (RN2 dry mix) | Sets the percentage of the original signal RN2 leaves under the denoised audio. Zero yields full suppression (silent between phrases); 10-20% keeps a steady quiet floor so the receiver still sounds alive. | Affects received audio only; the transmit denoiser is unchanged. Persisted by Rn2SettingsModel and exposed to the DSP chain via AetherDspWidget's rn2DryMixChanged signal. |
## DSP engine selection tabs

Click any of the six tabs (NR2, NR4, MNR, DFNR, RN2, BNR) to select that engine's page. Clicking a tab also activates or bypasses the corresponding engine. When NR2 is activated, AudioEngine cascades exclusion, disabling DFNR and other mutually exclusive modules.

### Tab availability

- **MNR** — Dimmed on Windows/Linux builds. The MNR engine has no backend on those platforms.
- **BNR** — Dimmed on builds without the NVIDIA Broadcast SDK.
- **RN2** — Adjustable Noise Floor slider (new in v26.8.4); previously purely informational.
- **DFNR** — Dimmed on builds without the DeepFilterNet SDK.

## NR2 tab

NR2 provides musical-noise reduction. Select it by clicking the **NR2** toggle.

### NR2 controls

| Control | Kind | Default | Range | Setting Key |
|---------|------|---------|-------|-------------|
| **Gain Method** | Radio buttons | Gamma | Linear, Log, Gamma, Trained | `NR2GainMethod` (stored as integer 0-3) |
| **NPE Method** | Radio buttons | OSMS | OSMS, MMSE, NSTAT | `NR2NpeMethod` (stored as integer 0-2) |
| **AE Filter (artifact elimination)** | Checkbox | True | - | `NR2AeFilter` |
| **Reduction:** | Slider | 1.50 | 0.50-2.00 | `NR2GainMax` (stored as value*100) |
| **Smoothing:** | Slider | 0.85 | 0.50-0.98 | `NR2GainSmooth` |
| **Threshold:** | Slider | 0.20 | 0.05-0.50 | `NR2Qspp` |
| **Reset Defaults (↺ icon)** | Push button | - | - | - |

### Gain Method descriptions

- **Linear** — Uses a linear audio amplitude scale for gain computation.
- **Log** — Uses a logarithmic amplitude scale, which compresses dynamic range.
- **Gamma** — Models gain on a gamma distribution that matches typical speech amplitude patterns. This is the default.
- **Trained** — Applies a noise reduction model trained on real speech and noise samples.

### NPE Method descriptions

- **OSMS** — Optimal smoothing and minimum statistics.
- **MMSE** — Minimum mean square error estimation.
- **NSTAT** — Noise statistics-based estimator.

### Reset Defaults (NR2)

Restores NR2 tab to Gamma/OSMS/AE on, Reduction 1.50, Smoothing 0.85, Threshold 0.20.

## NR4 tab

NR4 provides libspecbleach-based noise reduction. Select it by clicking the **NR4** toggle.

### NR4 controls

| Control | Kind | Default | Range | Setting Key |
|---------|------|---------|-------|-------------|
| **Noise Estimation:** | Radio buttons | MMSE | MMSE, Brandt, Martin | `NR4NoiseEstimationMethod` (stored as integer 0-2) |
| **Adaptive Noise Estimation** | Checkbox | True | - | `NR4AdaptiveNoise` |
| **Reduction (dB):** | Slider | 10.0 | 0.0-40.0 | `NR4ReductionAmount` (stored as value*10) |
| **Smoothing (%):** | Slider | 0 | 0-100 | `NR4SmoothingFactor` |
| **Whitening (%):** | Slider | 0 | 0-100 | `NR4WhiteningFactor` |
| **Masking Depth:** | Slider | 0.50 | 0.00-1.00 | `NR4MaskingDepth` |
| **Suppression:** | Slider | 0.50 | 0.00-1.00 | `NR4SuppressionStrength` |
| **Reset Defaults (↺ icon)** | Push button | - | - | - |

### Reset Defaults (NR4)

Restores NR4 tab to MMSE/adaptive on, Reduction 10 dB, Smoothing 0, Whitening 0, Masking Depth 0.50, Suppression 0.50.

## MNR tab (macOS only)

MNR provides macOS MMSE-Wiener noise reduction with asymmetric gain smoothing. Click the **MNR** toggle to access its controls.

**Note:** The MNR toggle is dimmed on Windows/Linux builds.

### MNR controls

| Control | Kind | Default | Range | Setting Key |
|---------|------|---------|-------|-------------|
| **Strength** | Slider | 100 | 0-100 | `MnrStrength` (persisted as normalized 0.00-1.00) |

## DFNR tab

DFNR provides DeepFilterNet3 noise reduction. Select it by clicking the **DFNR** toggle.

**Note:** The DFNR toggle is dimmed on builds without the DeepFilterNet SDK.

### DFNR controls

| Control | Kind | Default | Range | Setting Key |
|---------|------|---------|-------|-------------|
| **Attenuation Limit** | Slider | 100 | 0-100 dB | `DfnrAttenLimit` (0 = passthrough, 100 = maximum) |
| **Post-Filter Beta** | Slider | 0.00 | 0.00-0.30 | `DfnrPostFilterBeta` (stored as value*100) |
| **Reset Defaults (↺ icon)** | Push button | - | - | - |

## RN2 tab

RN2 provides RNNoise-based noise reduction. Select it by clicking the **RN2** toggle.

### RN2 controls

| Control | Kind | Default | Range | Setting Key |
|---------|------|---------|-------|-------------|
| **Noise Floor (RN2 dry mix)** | Slider | 0 | 0-100 | - |

The Noise Floor slider sets the percentage of the original signal RN2 leaves under the denoised audio. Zero yields full suppression (silent between phrases); 10-20% keeps a steady quiet floor so the receiver still sounds alive. Affects received audio only; the transmit denoiser is unchanged.

### Reset Defaults (RN2)

Restores RN2 tab to Noise Floor 0.

## BNR tab

BNR uses the NVIDIA Broadcast SDK. Intensity control is available from the overlay menu. The BNR toggle is dimmed on builds without the NVIDIA Broadcast SDK. No adjustable parameters — Reset Defaults is a no-op here.

## Tips

- **NR2** — **Gamma** gain method with **OSMS** NPE is the default and works well for most SSB voice contacts. Start here if you are unsure.
- **NR4** — **MMSE** noise estimation with adaptive noise enabled provides good baseline performance.
- **DFNR** — Attenuation Limit at 100 delivers maximum suppression. Lower values allow more noise through.
- **MNR** (macOS only) — Strength at 100 provides maximum aggressiveness. Reduce for more natural-sounding audio.
- **RN2** — Set Noise Floor to 10-20% to keep the receiver sounding alive between phrases; set to 0 for maximum suppression.
- After changing gain method or NPE method, re-adjust the reduction, smoothing, and threshold sliders to match the new characteristics.
- Each tab has its own **Reset Defaults** button to restore that engine's parameters to factory settings.

## Related

- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
- Enable NR2 on a slice
- Enable NR4 on a slice