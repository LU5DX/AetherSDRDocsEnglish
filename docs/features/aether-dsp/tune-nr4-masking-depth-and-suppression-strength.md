# AetherDSP Settings

AetherDSP Settings provides advanced control over AetherSDR's client-side noise-reduction engines: NR2, NR4, MNR, DFNR, RN2, and BNR. Each engine is selectable via a toggle row at the top of the dialog; clicking a toggle both selects that engine's page and activates or bypasses the engine.

## Opening AetherDSP Settings

1. Click `Settings > AetherDSP Settings...`.
2. The dialog opens.

## Dialog controls

The AetherDSP Settings dialog uses a custom frameless chrome with a gradient title bar, minimize/maximize/close buttons, drag-to-move, and 8-axis resize. The dialog geometry is persisted and restored across sessions.

| Control | Behavior |
|---------|----------|
| Title bar — AetherDSP Settings | 18 px gradient title bar with grip glyph (⋮⋮) on the left and the dialog title |
| — (Minimize) | Minimizes the dialog |
| □ (Maximize) | Maximizes or restores the dialog |
| × (Close) | Closes the dialog |
| Drag-to-move | Click and drag the title bar to move the dialog. Double-click to toggle maximize/restore |
| 8-axis resize | Click and drag any edge or corner to resize. Cursor changes to indicate direction. 6 px resize hit zone around the inner content widget |

## NR2 tab

The NR2 (musical-noise-reduction) engine uses a spectral-subtraction approach with configurable gain methods and noise power estimators.

| Control | Default | Range | Setting Key | Behavior |
|---------|---------|-------|-------------|----------|
| Gain Method | Gamma | Linear, Log, Gamma, Trained | `NR2GainMethod` | Selects gain-curve mapping. Stored as integer 0-3 |
| NPE Method | OSMS | OSMS, MMSE, NSTAT | `NR2NpeMethod` | Selects noise power estimator. Stored as integer 0-2 |
| AE Filter (artifact elimination) | Enabled | On/Off | `NR2AeFilter` | Toggles the anti-artefact post-filter |
| Reduction: | 1.50 | 0.50–2.00 | `NR2GainMax` | Sets maximum NR2 reduction depth. Slider stores value*100 internally |
| Smoothing: | 0.85 | 0.50–0.98 | `NR2GainSmooth` | Controls how smoothly the noise estimate tracks changes |
| Threshold: | 0.20 | 0.05–0.50 | `NR2Qspp` | Sets speech-presence-probability threshold |
| Use Original Geometry | Off | On/Off | `NR2UseOriginalGeometry` | When enabled, uses the original NR2 gain-curve geometry instead of the newer improved geometry. Off by default for best performance |
| Reset Defaults (↺ icon) | — | — | — | Restores NR2 defaults: Gamma, OSMS, AE on, 1.50, 0.85, 0.20, Use Original Geometry off |

## NR4 tab

The NR4 engine uses the libspecbleach library for noise reduction. It offers configurable noise estimation methods and spectral processing controls.

**Note:** On Windows, NR4 requires LLVM (clang-cl) to be installed when compiling the source. If LLVM is not present, the NR4 toggle is dimmed and displays the tooltip "NR4 requires LLVM (clang-cl) on Windows. Install LLVM from llvm.org and rebuild to enable NR4."

| Control | Default | Range | Setting Key | Behavior |
|---------|---------|-------|-------------|----------|
| Noise Estimation: | MMSE | MMSE, Brandt, Martin | `NR4NoiseEstimationMethod` | Selects noise-floor estimator. Stored as integer 0-2 |
| Adaptive Noise Estimation | Enabled | On/Off | `NR4AdaptiveNoise` | Enables continuous re-estimation of the noise floor |
| Reduction (dB): | 10.0 | 0.0–40.0 | `NR4ReductionAmount` | Sets maximum NR4 noise reduction in dB. Slider stores value*10 |
| Smoothing (%): | 0 | 0–100 | `NR4SmoothingFactor` | Time-domain smoothing of NR4 noise estimate |
| Whitening (%): | 0 | 0–100 | `NR4WhiteningFactor` | Flattens residual noise spectral shape |
| Masking Depth: | 0.50 | 0.00–1.00 | `NR4MaskingDepth` | Controls spectral-masking depth |
| Suppression: | 0.50 | 0.00–1.00 | `NR4SuppressionStrength` | Overall NR4 suppression strength |
| Reset Defaults (↺ icon) | — | — | — | Restores NR4 defaults: MMSE, adaptive on, 10 dB, 0, 0, 0.50, 0.50 |

## MNR tab (macOS only)

The MNR (macOS MMSE-Wiener) engine is available only on macOS builds. It provides asymmetric gain smoothing for noise reduction. The MNR toggle is dimmed on Windows and Linux builds — the engine has no backend on those platforms.

| Control | Default | Range | Setting Key | Behavior |
|---------|---------|-------|-------------|----------|
| Enable MNR (macOS only) | Disabled | On/Off | `MnrEnabled` | Enables MMSE-Wiener noise reduction with asymmetric gain smoothing. Initial state read live from AudioEngine |
| Strength | 100 | 0–100 | `MnrStrength` | Adjusts MNR aggressiveness (0 mild, 100 max). Persisted as normalized 0.00–1.00 |

## DFNR tab

The DFNR (DeepFilterNet3) engine uses a deep learning model for noise reduction.

| Control | Default | Range | Setting Key | Behavior |
|---------|---------|-------|-------------|----------|
| Attenuation Limit | 100 | 0–100 dB | `DfnrAttenLimit` | Sets maximum noise attenuation (0 = passthrough, 100 = maximum) |
| Post-Filter Beta | 0.00 | 0.00–0.30 | `DfnrPostFilterBeta` | Applies an additional post-filter for extra suppression. Slider stores value*100 internally |

## RN2 tab

The RN2 (RNNoise) tab is purely informational and has no adjustable parameters.

## BNR tab

The BNR (NVIDIA) tab's intensity is controlled from the overlay menu. The BNR toggle is dimmed on builds without the NVIDIA Broadcast SDK.

## Engine selection and mutual exclusion

The six DSP toggles (NR2, NR4, MNR, DFNR, RN2, BNR) act as both page selectors and engine enable/disable controls. When NR2 is activated, the AudioEngine cascades exclusion, disabling DFNR and other mutually exclusive modules. Only one engine can be active at a time.

## Persistence

The last-used client-side noise-reduction engine is persisted in `LastClientNr` and restored on next launch. If the stored engine (e.g., DFNR) is not available in the current build, the preference is silently cleared.

## Tips

- **Masking Depth:** and **Suppression:** on the NR4 tab interact: raising both together produces maximum noise reduction but the highest risk of speech distortion. Raise them incrementally and test on a live or recorded signal.
- If speech sounds over-processed or hollow, reduce Masking Depth: first, then Suppression: until naturalness returns.
- The **Adaptive Noise Estimation** checkbox affects how quickly NR4 tracks a changing noise floor, which in turn affects how both sliders sound in practice.
- The **Use Original Geometry** checkbox on the NR2 tab reverts to the legacy gain-curve geometry used in older AetherSDR versions. Leave it off for best results unless you have a specific reason to use the original curve.
- Click **Reset Defaults** on any tab to return all parameters on that tab to their factory values.

## Troubleshooting

- **Speech sounds hollow or underwater after raising the sliders** — Both sliders at high values can over-suppress spectral components that overlap with speech. Reduce **Masking Depth:** first, then **Suppression:** until naturalness returns.
- **Noise floor is still audible even at maximum settings** — Ensure **Adaptive Noise Estimation** is enabled so NR4 can continuously re-estimate the noise floor. Also consider increasing **Reduction (dB):** .
- **Slider snaps back or refuses to move** — Click directly on the slider handle rather than clicking in the groove.
- **NR4 toggle is dimmed on Windows** — The NR4 engine requires LLVM (clang-cl) to compile its C99 VLAs. Install LLVM from llvm.org and rebuild AetherSDR to enable NR4.
- **Last-used noise reduction engine does not restore across sessions** — If the persisted engine (e.g., DFNR) is not compiled into the current build, the preference is silently cleared. Select an available engine and restart to persist the new preference.

## Related

- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)