# AetherDSP Settings

The AetherDSP Settings dialog tunes the advanced parameters of AetherSDR's client-side noise-reduction engines (NR2, NR4, MNR, DFNR, RN2, BNR), letting operators dial in the tradeoff between noise suppression and speech fidelity. The six DSP modules are selectable via a toggle row at the top; clicking a toggle also activates or bypasses that engine.

## Before you start

- AetherSDR must be running. A radio connection is not required to change this setting.
- The DSP engine must be active on a receiver for changes to take audible effect immediately.

## Opening the dialog

1. Click `Settings > AetherDSP Settings...`.

The dialog appears as a frameless window with a gradient title bar. It remembers its size and position across sessions.

## Dialog controls overview

| Control | Description |
|---------|-------------|
| Title bar | Frameless 18 px gradient title bar with a grip glyph (⋮⋮) on the left and the dialog title. |
| — (Minimize) | Minimizes the dialog. |
| □ (Maximize) | Maximizes or restores the dialog. |
| × (Close) | Closes the dialog. |
| Drag-to-move | Click and drag the title bar to move the dialog. Double-click to toggle maximize/restore. |
| 8-axis resize | Click and drag any edge or corner of the dialog to resize. Cursor changes to indicate the resize direction. 6 px resize hit zone around the inner content widget. |

## NR2 tab

The NR2 tab controls the musical-noise-reduction engine.

### Controls

| Control | Kind | Default | Setting key | Behavior |
|---------|------|---------|-------------|----------|
| **NR2 (tab)** | Tab | — | — | Selects the NR2 page. Clicking the NR2 toggle button also activates or bypasses the NR2 engine. |
| **Gain Method** | Radio button (Linear, Log, Gamma, Trained) | Gamma | `NR2GainMethod` | Selects gain-curve mapping used by NR2. Stored as integer 0-3. |
| **NPE Method** | Radio button (OSMS, MMSE, NSTAT) | OSMS | `NR2NpeMethod` | Selects noise power estimator. Stored as integer 0-2. |
| **AE Filter (artifact elimination)** | Checkbox | True | `NR2AeFilter` | Toggles the anti-artefact post-filter. |
| **Reduction:** | Slider, 0.50–2.00 | 1.50 | `NR2GainMax` | Sets maximum NR2 reduction depth. Slider stores value*100 internally. |
| **Smoothing:** | Slider, 0.50–0.98 | 0.85 | `NR2GainSmooth` | Controls how smoothly the noise estimate tracks changes. |
| **Threshold:** | Slider, 0.05–0.50 | 0.20 | `NR2Qspp` | Sets speech-presence-probability threshold. |
| Reset Defaults (↺ icon) | Push button | — | — | Restores NR2 tab defaults (Gamma/OSMS/AE on, 1.50/0.85/0.20). |

### Changing the NPE method

1. Click the **NR2** tab.
2. In the **NPE Method** group, select one of the three radio buttons: **OSMS**, **MMSE**, or **NSTAT**.

The setting takes effect immediately and is saved automatically to `NR2NpeMethod`.

## NR4 tab

The NR4 tab controls the libspecbleach noise-reduction engine.

### Controls

| Control | Kind | Default | Setting key | Behavior |
|---------|------|---------|-------------|----------|
| **NR4 (tab)** | Tab | — | — | Selects the NR4 page. |
| **Noise Estimation:** | Radio button (MMSE, Brandt, Martin) | MMSE | `NR4NoiseEstimationMethod` | Selects noise-floor estimator. Stored as integer 0-2. |
| **Adaptive Noise Estimation** | Checkbox | True | `NR4AdaptiveNoise` | Enables continuous re-estimation of the noise floor. |
| **Reduction (dB):** | Slider, 0.0–40.0 | 10.0 | `NR4ReductionAmount` | Sets maximum reduction in dB. Slider stores value*10. |
| **Smoothing (%):** | Slider, 0–100 | 0 | `NR4SmoothingFactor` | Time-domain smoothing of noise estimate. |
| **Whitening (%):** | Slider, 0–100 | 0 | `NR4WhiteningFactor` | Flattens residual noise spectral shape. |
| **Masking Depth:** | Slider, 0.00–1.00 | 0.50 | `NR4MaskingDepth` | Controls spectral-masking depth. |
| **Suppression:** | Slider, 0.00–1.00 | 0.50 | `NR4SuppressionStrength` | Overall suppression strength. |
| Reset Defaults (↺ icon) | Push button | — | — | Restores NR4 defaults (MMSE/adaptive on, 10 dB, 0, 0, 0.50, 0.50). |

## MNR tab (macOS only)

The MNR tab controls the macOS MMSE-Wiener noise-reduction engine. The MNR toggle is dimmed on Windows/Linux builds — the engine has no backend on those platforms.

### Controls

| Control | Kind | Default | Setting key | Behavior |
|---------|------|---------|-------------|----------|
| **MNR (tab)** | Tab | — | — | Selects the MNR page. |
| **Enable MNR (macOS only)** | Checkbox | Read live from AudioEngine | `MnrEnabled` | Enables MMSE-Wiener noise reduction with asymmetric gain smoothing. |
| **Strength** | Slider, 0–100 | 100 | `MnrStrength` | Adjusts MNR aggressiveness (0 mild, 100 max). Persisted as normalized 0.00-1.00. |

## RN2 tab (informational)

The RN2 tab displays the RNNoise page. It is purely informational with no adjustable parameters. The RN2 engine is enabled via the toggle button at the top of the dialog.

## BNR tab (NVIDIA)

The BNR tab controls the NVIDIA Broadcast noise-reduction engine. Intensity is controlled from the overlay menu. The BNR toggle is dimmed on builds without the NVIDIA Broadcast SDK.

## DFNR tab

The DFNR tab controls the DeepFilterNet3 noise-reduction engine.

### Controls

| Control | Kind | Default | Setting key | Behavior |
|---------|------|---------|-------------|----------|
| **DFNR (tab)** | Tab | — | — | Selects the DeepFilterNet3 page. |
| **Attenuation Limit** | Slider, 0–100 dB | 100 | `DfnrAttenLimit` | Sets maximum noise attenuation. 0 = passthrough; 100 = maximum. |
| **Post-Filter Beta** | Slider, 0.00–0.30 | 0.00 | `DfnrPostFilterBeta` | Applies an additional post-filter for extra suppression. Slider stores value*100 internally. |

## Notes

- The six DSP toggles (NR2, NR4, MNR, DFNR, RN2, BNR) act as exclusive selectors and engine enable/disable controls. When NR2 is activated, AudioEngine cascades exclusion, disabling DFNR and other mutually exclusive modules.
- The dialog uses `PersistentDialog`, which automatically saves and restores its geometry across sessions. The dialog position and size are persisted using the `AetherDspDialogGeometry` setting key.
- All sliders in this dialog use the themable primary slider style, adapting to the current color theme.

## Tips

- NR2: OSMS works well for steady background noise such as atmospheric hiss or white noise. NSTAT is better for rapidly changing noise floors.
- NR2: If changing the NPE method introduces more musical noise artifacts, enable **AE Filter (artifact elimination)**.
- NR4: Adaptive noise estimation helps track changing noise conditions. Disable it if the noise floor is stable.
- DFNR: Post-Filter Beta adds extra suppression but may introduce artifacts at higher values.
- Click the Reset Defaults button (↺) on any tab to return all parameters on that tab to their factory defaults.

## Troubleshooting

- **Changing parameters produces no audible difference** — Confirm the DSP engine is enabled on the receiver. The AetherDSP Settings dialog adjusts parameters but does not itself activate the engine; the engine must be switched on from the receiver controls.
- **MNR tab is dimmed or unavailable** — MNR is only available on macOS. Windows and Linux builds do not include the MNR backend.
- **BNR tab is dimmed** — The NVIDIA Broadcast SDK is not installed on this system.

## Related

- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
- [Tune NR2 reduction depth and voice threshold](tune-nr2-reduction-depth-and-voice-threshold.md)
- [Switch NR2 gain method between Linear, Log, Gamma and Trained](switch-nr2-gain-method-between-linear-log-gamma-and-trained.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)