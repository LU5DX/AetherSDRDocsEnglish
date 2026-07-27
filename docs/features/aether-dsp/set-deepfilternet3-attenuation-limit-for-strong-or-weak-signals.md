# AetherDSP Settings

The AetherDSP Settings dialog (opened via `Settings > AetherDSP Settings...`) tunes the advanced parameters of AetherSDR's client-side noise-reduction engines (NR2, NR4, MNR, DFNR, RN2, BNR). It lets operators dial in the tradeoff between noise suppression and speech fidelity. The six DSP modules are selectable via a toggle row at the top; clicking a toggle also activates or bypasses that engine.

## Before you start

- AetherSDR must be running. A radio connection is not required to adjust DSP settings.
- Select a noise reduction engine by clicking its toggle in the dialog's tab row.

## Common controls

| Control                        | Behavior                                                                                                   | Notes                                                                                   |
|--------------------------------|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| Title bar — AetherDSP Settings | 18 px gradient title bar with grip glyph (⋮⋮) on the left and the dialog title.                            | Matching the chrome family of NetworkDiagnosticsDialog and AetherialAudioStrip.        |
| — (Minimize)                   | Minimizes the dialog.                                                                                      |                                                                                         |
| □ (Maximize)                   | Maximizes or restores the dialog.                                                                          |                                                                                         |
| × (Close)                      | Closes the dialog.                                                                                         |                                                                                         |
| Drag-to-move                   | Click and drag the title bar to move the dialog.                                                           | Double-click the title bar to toggle maximize/restore.                                  |
| 8-axis resize                  | Click and drag any edge or corner of the dialog to resize. Cursor changes to indicate the resize direction. | 6 px resize hit zone around the inner content widget.                                   |

## NR2 tab (Musical-Noise Reduction)

Selecting the NR2 tab activates or bypasses the NR2 engine. When NR2 is activated, AudioEngine cascades exclusion, disabling DFNR and other mutually exclusive modules.

### NR2 controls

| Control                        | Default       | Valid range    | Setting key           | Behavior                                                                                        | Notes                                                                                  |
|--------------------------------|---------------|----------------|-----------------------|-------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| Gain Method                    | Gamma         | Linear, Log, Gamma, Trained | `NR2GainMethod`       | Selects gain-curve mapping used by NR2.                                                        | Stored as integer 0-3 matching the order above.                                        |
| NPE Method                     | OSMS          | OSMS, MMSE, NSTAT | `NR2NpeMethod`        | Selects noise power estimator.                                                                 | Stored as integer 0-2.                                                                |
| AE Filter (artifact elimination) | True          | —              | `NR2AeFilter`         | Toggles the anti-artefact post-filter.                                                          |                                                                                        |
| Reduction:                     | 1.50          | 0.50-2.00      | `NR2GainMax`          | Sets maximum NR2 reduction depth.                                                              | Slider stores value*100 internally.                                                    |
| Gain Floor                     | 0.00          | 0.00-0.50      | `NR2GainFloor`        | Sets the minimum gain floor for NR2 processing.                                                 | Added in v26.7.4.                                                                      |
| Smoothing:                     | 0.85          | 0.50-0.98      | `NR2GainSmooth`       | Controls how smoothly the noise estimate tracks changes.                                        |                                                                                        |
| Threshold:                     | 0.20          | 0.05-0.50      | `NR2Qspp`             | Sets speech-presence-probability threshold.                                                    |                                                                                        |
| Use Original Spatial Geometry  | True          | —              | `NR2UseOriginalGeometry` | Toggles use of original spatial geometry instead of the cascade configuration.                 | Added in v26.7.4.                                                                      |
| Reset Defaults (↺ icon)       | —              | —              | —                     | Restores NR2 tab defaults (Gamma/OSMS/AE on, 1.50/0.00/0.85/0.20, Use Original Geometry on).    | Rendered as a flat icon button showing anticlockwise arrow (U+21BA).                   |

## NR4 tab (libspecbleach)

Selecting the NR4 tab activates or bypasses the NR4 engine.

### NR4 controls

| Control                        | Default       | Valid range              | Setting key                    | Behavior                                                                                        | Notes                                                                                  |
|--------------------------------|---------------|--------------------------|--------------------------------|-------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| Noise Estimation:              | MMSE          | MMSE, Brandt, Martin     | `NR4NoiseEstimationMethod`     | Selects noise-floor estimator used by NR4.                                                      | Stored as integer 0-2.                                                                |
| Adaptive Noise Estimation      | True          | —                        | `NR4AdaptiveNoise`             | Enables continuous re-estimation of the noise floor.                                            |                                                                                        |
| Reduction (dB):                | 10.0          | 0.0-40.0                | `NR4ReductionAmount`           | Sets maximum NR4 noise reduction in dB.                                                         | Slider stores value*10.                                                                |
| Smoothing (%):                 | 0             | 0-100                   | `NR4SmoothingFactor`           | Time-domain smoothing of NR4 noise estimate.                                                    |                                                                                        |
| Whitening (%):                 | 0             | 0-100                   | `NR4WhiteningFactor`           | Flattens residual noise spectral shape.                                                         |                                                                                        |
| Masking Depth:                 | 0.50          | 0.00-1.00               | `NR4MaskingDepth`              | Controls spectral-masking depth.                                                                |                                                                                        |
| Suppression:                   | 0.50          | 0.00-1.00               | `NR4SuppressionStrength`       | Overall NR4 suppression strength.                                                               |                                                                                        |
| Reset Defaults (↺ icon)       | —              | —                        | —                              | Restores NR4 defaults (MMSE/adaptive on, 10 dB, 0, 0, 0.50, 0.50).                              | Rendered as a flat icon button showing anticlockwise arrow (U+21BA).                   |

## MNR tab (macOS MMSE-Wiener)

Selecting the MNR tab activates or bypasses the MNR engine. The MNR toggle is dimmed on Windows/Linux builds — the engine has no backend on those platforms.

### MNR controls

| Control                        | Default       | Valid range    | Setting key      | Behavior                                                                                        | Notes                                                                                  |
|--------------------------------|---------------|----------------|------------------|-------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| Enable MNR (macOS only)        | —             | —              | `MnrEnabled`     | Enables MMSE-Wiener noise reduction with asymmetric gain smoothing.                            | Initial state read live from AudioEngine::mnrEnabled().                               |
| Strength                       | 100           | 0-100          | `MnrStrength`    | Adjusts MNR aggressiveness (0 mild, 100 max).                                                   | Persisted as normalized 0.00-1.00.                                                     |

## DFNR tab (DeepFilterNet3)

Selecting the DFNR tab activates or bypasses the DeepFilterNet3 engine. DFNR is only available when AetherSDR is rebuilt after setting up DeepFilterNet.

### DFNR controls

| Control                        | Default       | Valid range    | Setting key           | Behavior                                                                                        | Notes                                                                                  |
|--------------------------------|---------------|----------------|-----------------------|-------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| Attenuation Limit              | 100           | 0-100 dB       | `DfnrAttenLimit`      | Sets maximum noise attenuation applied by DeepFilterNet3. 0 = passthrough; 100 = maximum.       |                                                                                        |
| Post-Filter Beta               | 0.00          | 0.00-0.30      | `DfnrPostFilterBeta`  | Applies an additional post-filter for extra suppression.                                        | Slider stores value*100 internally.                                                    |

## RN2 tab (RNNoise)

Selecting the RN2 tab activates or bypasses the RN2 engine. This page is purely informational — no adjustable parameters.

## BNR tab (NVIDIA)

Selecting the BNR tab activates or bypasses the BNR engine. Intensity is controlled from the overlay menu. The BNR toggle is dimmed on builds without the NVIDIA Broadcast SDK.

## Tips

- For strong, clean signals where preserving fidelity matters, reduce **Attenuation Limit** toward 0 to limit how much the engine can alter the audio.
- For weak or heavily noise-degraded signals, set **Attenuation Limit** to 100 and combine with a non-zero **Post-Filter Beta** for the most aggressive suppression.
- When using NR2, start with the defaults (Gamma/OSMS/AE on, 1.50/0.00/0.85/0.20) and adjust **Reduction:**, **Gain Floor**, and **Smoothing:** to find the best balance.
- The **Gain Floor** control prevents the NR2 engine from applying excessive attenuation to very faint signals; higher values keep more of the background noise, lower values allow deeper suppression.

## Troubleshooting

- **Audio sounds unaffected after moving the slider** — Confirm you are on the correct tab and that the corresponding noise reduction engine is active. Each engine has separate controls and is not affected by settings from other engines.
- **MNR tab is dimmed** — MNR is only available on macOS builds.
- **BNR tab is dimmed** — The NVIDIA Broadcast SDK is not detected on your system.
- **DFNR tab shows DFNR unavailable tooltip** — DFNR requires DeepFilterNet to be set up and AetherSDR rebuilt.

## Related

- [Configure DFNR post-filter beta for extra suppression](configure-dfnr-post-filter-beta-for-extra-suppression.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
- [AetherDSP Settings overview](overview.md)