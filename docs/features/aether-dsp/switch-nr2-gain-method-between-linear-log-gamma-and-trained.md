# AetherDSP Settings

The AetherDSP Settings dialog tunes the advanced parameters of AetherSDR's client-side noise-reduction engines (NR2, NR4, MNR, DFNR, RN2, BNR), letting operators dial in the tradeoff between noise suppression and speech fidelity. The six DSP modules are selectable via a toggle row at the top; clicking a toggle also activates or bypasses that engine.

## Opening the dialog

1. Click **Settings > AetherDSP Settings...**.
2. The dialog opens with a frameless 18 px gradient title bar containing a grip glyph (⋮⋮) on the left and the dialog title.

The dialog can be moved by clicking and dragging the title bar. Double-click the title bar to toggle maximize/restore. Resize by clicking and dragging any edge or corner (6 px resize hit zone).

## Dialog controls

The title bar contains three window control buttons and a grip glyph:

| Button | Action |
|--------|--------|
| **⋮⋮ (Grip glyph)** | Visual reference indicator on the left of the title bar. |
| **— (Minimize)** | Minimizes the dialog. |
| **□ (Maximize)** | Maximizes or restores the dialog. |
| **× (Close)** | Closes the dialog. |

## DSP engine selection tabs

Click any of the six tabs (NR2, NR4, MNR, DFNR, RN2, BNR) to select that engine's page. Clicking a tab also activates or bypasses the corresponding engine. When NR2 is activated, AudioEngine cascades exclusion, disabling DFNR and other mutually exclusive modules.

### Tab availability

- **MNR** — Dimmed on Windows/Linux builds. The MNR engine has no backend on those platforms.
- **BNR** — Dimmed on builds without the NVIDIA Broadcast SDK.
- **RN2** — Purely informational; no adjustable parameters.
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
| **Floor:** | Slider | 0.00 | 0.00-1.00 | `NR2GainFloor` (stored as value*100) |
| **Smoothing:** | Slider | 0.85 | 0.50-0.98 | `NR2GainSmooth` |
| **Threshold:** | Slider | 0.20 | 0.05-0.50 | `NR2Qspp` |
| **Use Original Geometry** | Checkbox | False | - | `NR2UseOriginalGeometry` |
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

### Floor

Sets the minimum gain floor for NR2. Lower values allow more aggressive noise reduction.

### Use Original Geometry

When checked, uses the original geometric gain calculation method from earlier AetherSDR versions.

### Reset Defaults (NR2)

Restores NR2 tab to Gamma/OSMS/AE on, Reduction 1.50, Floor 0.00, Smoothing 0.85, Threshold 0.20, Use Original Geometry unchecked.

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
| **Enable MNR (macOS only)** | Checkbox | - | - | `MnrEnabled` (initial state read live from AudioEngine) |
| **Strength** | Slider | 100 | 0-100 | `MnrStrength` (persisted as normalized 0.00-1.00) |

## DFNR tab

DFNR provides DeepFilterNet3 noise reduction. Select it by clicking the **DFNR** toggle.

**Note:** The DFNR toggle is dimmed on builds without the DeepFilterNet SDK.

### DFNR controls

| Control | Kind | Default | Range | Setting Key |
|---------|------|---------|-------|-------------|
| **Attenuation Limit** | Slider | 100 | 0-100 dB | `DfnrAttenLimit` (0 = passthrough, 100 = maximum) |
| **Post-Filter Beta** | Slider | 0.00 | 0.00-0.30 | `DfnrPostFilterBeta` (stored as value*100) |

## RN2 tab

RN2 uses the RNNoise engine. This tab is purely informational with no adjustable parameters.

## BNR tab

BNR uses the NVIDIA Broadcast SDK. Intensity control is available from the overlay menu. The BNR toggle is dimmed on builds without the NVIDIA Broadcast SDK.

## Tips

- **NR2** — **Gamma** gain method with **OSMS** NPE is the default and works well for most SSB voice contacts. Start here if you are unsure. Enable **Use Original Geometry** if you prefer the previous gain calculation behavior.
- **NR4** — **MMSE** noise estimation with adaptive noise enabled provides good baseline performance.
- **DFNR** — Attenuation Limit at 100 delivers maximum suppression. Lower values allow more noise through.
- **MNR** (macOS only) — Strength at 100 provides maximum aggressiveness. Reduce for more natural-sounding audio.
- After changing gain method or NPE method, re-adjust the reduction, floor, smoothing, and threshold sliders to match the new characteristics.
- Each tab has its own **Reset Defaults** button to restore that engine's parameters to factory settings.

## Related

- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
- Enable NR2 on a slice
- Enable NR4 on a slice