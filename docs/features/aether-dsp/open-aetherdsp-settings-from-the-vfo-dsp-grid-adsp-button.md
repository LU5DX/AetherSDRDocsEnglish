# Open AetherDSP Settings from the VFO DSP grid ADSP button

Opens the AetherDSP Settings dialog so you can tune client-side noise-reduction parameters without navigating through the menu system.

## Before you start

- A slice must be active in the panadapter so the VFO DSP grid is visible.

## Steps

1. In the per-slice VFO DSP grid, locate the **ADSP** button.
2. Click **ADSP**.

The AetherDSP Settings dialog opens, showing the noise-reduction engine tabs (NR2, NR4, MNR, DFNR, RN2, BNR).

## Tips

- The same dialog can also be opened from the menu: **Settings > AetherDSP Settings...**, or by double-clicking the ADSP tile in the RX Chain strip.
- Click the **ADSP** button again while the dialog is open — this does not toggle the dialog; it brings an already-open dialog to the front. To bypass all client-side noise reduction, see [Bypass the entire client NR cluster from the RX chain ADSP tile](bypass-the-entire-client-nr-cluster-from-the-rx-chain-adsp-tile.md).

## Dialog controls

The AetherDSP Settings dialog provides six noise-reduction engine tabs. Click a tab to select it; clicking the tab also activates or bypasses that engine.

### NR2 (musical-noise reduction)

| Control | Type | Default | Range | Setting Key | Description |
|---------|------|---------|-------|-------------|-------------|
| NR2 (tab) | tab | — | — | — | Selects the NR2 page. Clicking activates or bypasses the NR2 engine. When activated, AudioEngine cascades exclusion, disabling DFNR and other mutually exclusive modules. |
| Gain Method | radio_button | Gamma | Linear, Log, Gamma, Trained | `NR2GainMethod` | Selects the gain-curve mapping. Stored as integer 0-3. |
| NPE Method | radio_button | OSMS | OSMS, MMSE, NSTAT | `NR2NpeMethod` | Selects the noise power estimator. Stored as integer 0-2. |
| AE Filter | checkbox | True | — | `NR2AeFilter` | Toggles the anti-artefact post-filter. |
| Reduction: | slider | 1.50 | 0.50–2.00 | `NR2GainMax` | Sets maximum NR2 reduction depth. |
| Smoothing: | slider | 0.85 | 0.50–0.98 | `NR2GainSmooth` | Controls how smoothly the noise estimate tracks changes. |
| Threshold: | slider | 0.20 | 0.05–0.50 | `NR2Qspp` | Sets the speech-presence-probability threshold. |
| Reset Defaults (↺ icon) | push_button | — | — | — | Restores NR2 defaults: Gamma, OSMS, AE on, 1.50/0.85/0.20. |

### NR4 (libspecbleach spectral NR)

| Control | Type | Default | Range | Setting Key | Description |
|---------|------|---------|-------|-------------|-------------|
| NR4 (tab) | tab | — | — | — | Selects the NR4 page. |
| Noise Estimation: | radio_button | MMSE | MMSE, Brandt, Martin | `NR4NoiseEstimationMethod` | Selects the noise-floor estimator. Stored as integer 0-2. |
| Adaptive Noise Estimation | checkbox | True | — | `NR4AdaptiveNoise` | Enables continuous re-estimation of the noise floor. |
| Reduction (dB): | slider | 10.0 | 0.0–40.0 | `NR4ReductionAmount` | Sets maximum NR4 noise reduction in dB. |
| Smoothing (%): | slider | 0 | 0–100 | `NR4SmoothingFactor` | Time-domain smoothing of the NR4 noise estimate. |
| Whitening (%): | slider | 0 | 0–100 | `NR4WhiteningFactor` | Flattens residual noise spectral shape. |
| Masking Depth: | slider | 0.50 | 0.00–1.00 | `NR4MaskingDepth` | Controls spectral-masking depth. |
| Suppression: | slider | 0.50 | 0.00–1.00 | `NR4SuppressionStrength` | Overall NR4 suppression strength. |
| Reset Defaults (↺ icon) | push_button | — | — | — | Restores NR4 defaults: MMSE, adaptive on, 10 dB, 0, 0, 0.50, 0.50. |

### MNR (macOS MMSE-Wiener)

| Control | Type | Default | Range | Setting Key | Description |
|---------|------|---------|-------|-------------|-------------|
| MNR (tab) | tab | — | — | — | Selects the MNR page. The MNR toggle is dimmed on Windows and Linux builds — the engine requires a macOS backend. |
| Enable MNR | checkbox | — | — | `MnrEnabled` | Enables MMSE-Wiener noise reduction with asymmetric gain smoothing. |
| Strength | slider | 100 | 0–100 | `MnrStrength` | Adjusts MNR aggressiveness (0 mild, 100 max). Persisted as normalized 0.00–1.00. |

### RN2 (RNNoise)

| Control | Type | Default | Range | Setting Key | Description |
|---------|------|---------|-------|-------------|-------------|
| RN2 (tab) | tab | — | — | — | Selects the RN2 page. This page is purely informational — no adjustable parameters. |

### BNR (NVIDIA Broadcast)

| Control | Type | Default | Range | Setting Key | Description |
|---------|------|---------|-------|-------------|-------------|
| BNR (tab) | tab | — | — | — | Selects the BNR page. Intensity is controlled from the overlay menu. The BNR toggle is dimmed on builds without the NVIDIA Broadcast SDK. |

### DFNR (DeepFilterNet3)

| Control | Type | Default | Range | Setting Key | Description |
|---------|------|---------|-------|-------------|-------------|
| DFNR (tab) | tab | — | — | — | Selects the DeepFilterNet3 page. |
| Attenuation Limit | slider | 100 | 0–100 dB | `DfnrAttenLimit` | Sets maximum noise attenuation applied by DeepFilterNet3. 0 = passthrough, 100 = maximum. |
| Post-Filter Beta | slider | 0.00 | 0.00–0.30 | `DfnrPostFilterBeta` | Applies an additional post-filter for extra suppression. |

## Dialog chrome behavior

The dialog uses a frameless window style with a custom title bar. Dialog geometry and state are persisted across sessions via the `AetherDspDialogGeometry` setting key.

- **Title bar**: 18 px gradient title bar with grip glyph (⋮⋮) on the left and the dialog title.
- **Minimize (—)**: Minimizes the dialog.
- **Maximize (□)**: Maximizes or restores the dialog.
- **Close (×)**: Closes the dialog.
- **Drag-to-move**: Click and drag the title bar to move the dialog. Double-click the title bar to toggle maximize/restore.
- **8-axis resize**: Click and drag any edge or corner of the dialog to resize. Cursor changes to indicate the resize direction. Resize hit zone is 6 px around the inner content widget.

## Platform notes

- **NR4** requires LLVM (clang-cl) on Windows to compile its C99 VLAs. If LLVM is not installed when AetherSDR was built, the NR4 toggle is dimmed and shows the tooltip: "NR4 requires LLVM (clang-cl) on Windows. Install LLVM from llvm.org and rebuild to enable NR4."
- **MNR** is only available on macOS. On Windows and Linux builds, the MNR toggle is dimmed with the tooltip: "MNR is only available on macOS."
- **BNR** requires the NVIDIA Broadcast SDK at compile time. On builds without it, the BNR toggle is dimmed.