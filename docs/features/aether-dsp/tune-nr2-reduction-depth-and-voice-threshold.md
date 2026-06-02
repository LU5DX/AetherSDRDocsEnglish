# AetherDSP Settings

This page explains how to adjust AetherSDR's client-side noise-reduction engines (NR2, NR4, MNR, DFNR, RN2, BNR). The six DSP modules are selectable via toggle buttons at the top of the dialog; clicking a toggle also activates or bypasses that engine.

## Before you start

- AetherSDR must be running. A radio connection is not required to change these settings.
- The selected noise reduction engine must already be active on a receiver slice for changes to take audible effect immediately.
- MNR is only available on macOS builds. The MNR toggle is dimmed on Windows and Linux.
- BNR is only available on builds with the NVIDIA Broadcast SDK. The BNR toggle is dimmed otherwise.
- NR4 requires LLVM (clang-cl) on Windows. The NR4 toggle is dimmed on Windows builds compiled without LLVM. Install LLVM from llvm.org and rebuild to enable NR4.

## Opening the dialog

Click `Settings > AetherDSP Settings...`.

## Dialog overview

The AetherDSP Settings dialog features a custom title bar with a gradient background. From left to right it contains:

- A grip glyph (⋮⋮) — visual indicator only
- The dialog title "AetherDSP Settings"
- **—** (Minimize) button — minimizes the dialog
- **□** (Maximize) button — maximizes or restores the dialog
- **×** (Close) button — closes the dialog

Drag the title bar to move the dialog. Double-click the title bar to toggle maximize/restore. Drag any edge or corner to resize the dialog (8-axis resize with a 6 px hit zone).

The dialog stores its size and position between sessions using the geometry key `AetherDspDialogGeometry`.

## Selecting and activating a noise reduction engine

Six toggle buttons are arranged in a row at the top of the dialog. Clicking a toggle:

1. Selects that engine's parameter page
2. Activates the engine (if it was bypassed) or bypasses it (if it was active)

When NR2 is activated, the AudioEngine cascades exclusion, disabling DFNR and other mutually exclusive modules.

Available engines:

- **NR2** — Musical-noise-reduction engine
- **NR4** — libspecbleach-based engine (requires LLVM on Windows)
- **MNR** — macOS MMSE-Wiener engine (macOS only)
- **RN2** — RNNoise-based engine (informational only, no adjustable parameters)
- **BNR** — NVIDIA Broadcast SDK engine (NVIDIA SDK only)
- **DFNR** — DeepFilterNet3 engine

## NR2 parameters

Under the NR2 tab, use these controls:

| Control | Default | Valid Range | Setting Key | Description |
|---------|---------|-------------|-------------|-------------|
| **Gain Method** | Gamma | Linear / Log / Gamma / Trained | `NR2GainMethod` | Selects gain-curve mapping used by NR2. Stored as integer 0-3. |
| **NPE Method** | OSMS | OSMS / MMSE / NSTAT | `NR2NpeMethod` | Selects noise power estimator. Stored as integer 0-2. |
| **AE Filter (artifact elimination)** | On | On / Off | `NR2AeFilter` | Toggles the anti-artefact post-filter. |
| **Reduction:** | 1.50 | 0.50–2.00 | `NR2GainMax` | Sets maximum NR2 reduction depth. Slider stores value*100 internally. |
| **Smoothing:** | 0.85 | 0.50–0.98 | `NR2GainSmooth` | Controls how smoothly the noise estimate tracks changes. |
| **Threshold:** | 0.20 | 0.05–0.50 | `NR2Qspp` | Sets speech-presence-probability threshold. |

Click **Reset Defaults** (↺ icon) to restore all NR2 parameters to their defaults: Gamma/OSMS/AE on, Reduction 1.50, Smoothing 0.85, Threshold 0.20.

## NR4 parameters

Under the NR4 tab, use these controls:

| Control | Default | Valid Range | Setting Key | Description |
|---------|---------|-------------|-------------|-------------|
| **Noise Estimation:** | MMSE | MMSE / Brandt / Martin | `NR4NoiseEstimationMethod` | Selects noise-floor estimator used by NR4. Stored as integer 0-2. |
| **Adaptive Noise Estimation** | On | On / Off | `NR4AdaptiveNoise` | Enables continuous re-estimation of the noise floor. |
| **Reduction (dB):** | 10.0 | 0.0–40.0 | `NR4ReductionAmount` | Sets maximum NR4 noise reduction in dB. Slider stores value*10. |
| **Smoothing (%):** | 0 | 0–100 | `NR4SmoothingFactor` | Time-domain smoothing of NR4 noise estimate. |
| **Whitening (%):** | 0 | 0–100 | `NR4WhiteningFactor` | Flattens residual noise spectral shape. |
| **Masking Depth:** | 0.50 | 0.00–1.00 | `NR4MaskingDepth` | Controls spectral-masking depth. |
| **Suppression:** | 0.50 | 0.00–1.00 | `NR4SuppressionStrength` | Overall NR4 suppression strength. |

Click **Reset Defaults** (↺ icon) to restore all NR4 parameters to their defaults: MMSE/adaptive on, 10 dB, 0, 0, 0.50, 0.50.

## MNR parameters (macOS only)

Under the MNR tab, use these controls:

| Control | Default | Valid Range | Setting Key | Description |
|---------|---------|-------------|-------------|-------------|
| **Enable MNR (macOS only)** | Off | On / Off | `MnrEnabled` | Enables MMSE-Wiener noise reduction with asymmetric gain smoothing. Initial state read live from AudioEngine. |
| **Strength** | 100 | 0–100 | `MnrStrength` | Adjusts MNR aggressiveness (0 mild, 100 max). Persisted as normalized 0.00–1.00. |

The MNR tab and toggle are dimmed on Windows and Linux builds — the engine has no backend on those platforms.

## DFNR parameters

Under the DFNR tab, use these controls:

| Control | Default | Valid Range | Setting Key | Description |
|---------|---------|-------------|-------------|-------------|
| **Attenuation Limit** | 100 | 0–100 dB | `DfnrAttenLimit` | Sets maximum noise attenuation applied by DeepFilterNet3. 0 = passthrough; 100 = maximum. |
| **Post-Filter Beta** | 0.00 | 0.00–0.30 | `DfnrPostFilterBeta` | Applies an additional post-filter for extra suppression. Slider stores value*100 internally. |

## RN2 tab

The RN2 tab is informational only. It displays the currently active RNNoise model but provides no adjustable parameters. The engine is controlled exclusively through the main receiver toolbar toggle.

## BNR tab

The BNR tab displays the currently active NVIDIA Broadcast model. Intensity is controlled from the overlay menu, not from this dialog. The BNR toggle is dimmed on builds without the NVIDIA Broadcast SDK.

## Theme support

Starting in v26.6.1, the AetherDSP Settings dialog uses the theme system for styling. The dialog background and text colors follow the active theme. All sliders use the theme's primary slider style instead of hardcoded colors. Custom themes can override the appearance through the `{{color.background.0}}` and `{{color.text.primary}}` template variables.

## Tips

- For SSB voice operation with NR2, start with **Reduction:** at `1.50` and **Threshold:** at `0.20`. If speech sounds clipped or hollow, lower **Reduction:** toward `1.00`.
- Lowering **Threshold:** below `0.15` can cause residual noise to break through during speech pauses because more of the signal is classified as speech. Raise it if you notice this.
- If the noise estimate reacts too slowly to burst noise, lower **Smoothing:** toward `0.60`. If the noise gate sounds choppy, raise it toward `0.95`.
- Leaving **AE Filter (artifact elimination)** enabled is recommended for most conditions; disable it only if you notice the post-filter itself introducing artifacts.
- For NR4, start with default settings and adjust **Reduction (dB):** first. Raise **Masking Depth:** and **Suppression:** only if needed for particularly noisy conditions.
- MNR on macOS works best at **Strength** between 60-80 for SSB; higher values may introduce artifacts.

## Troubleshooting

- **Speech sounds hollow or over-processed** — **Reduction:** is too high or **Threshold:** is too high. Lower **Reduction:** and/or lower **Threshold:** so more speech components are preserved.
- **Noise is still audible during speech pauses** — **Threshold:** is too low, causing pauses to be classified as speech. Raise **Threshold:** toward `0.30`–`0.40`.
- **Noise estimate reacts sluggishly or the noise floor sounds unstable** — Adjust **Smoothing:** (see Tips above). Also verify the selected **NPE Method** suits your noise type; NSTAT adapts better to non-stationary noise.
- **MNR toggle is grayed out** — You are on Windows or Linux. MNR requires macOS.
- **BNR toggle is grayed out** — The NVIDIA Broadcast SDK is not installed or not detected.
- **NR4 toggle is grayed out on Windows** — LLVM (clang-cl) is not installed. Install LLVM from llvm.org and rebuild AetherSDR to enable NR4.
- **Can't find the dialog after minimizing** — Check the taskbar/dock. The dialog minimizes like any other window.

## Related

- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Switch NR2 gain method between Linear, Log, Gamma and Trained](switch-nr2-gain-method-between-linear-log-gamma-and-trained.md)
- [Change NR2 noise power estimator (OSMS/MMSE/NSTAT)](change-nr2-noise-power-estimator-osms-mmse-nstat.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)