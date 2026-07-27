# AetherDSP Settings

The AetherDSP Settings dialog provides advanced control over all six client-side noise-reduction engines in AetherSDR: NR2, NR4, DFNR, MNR, RN2, and BNR. Each engine is selectable via a toggle row at the top of the dialog; clicking a toggle also activates or bypasses that engine.

## Opening AetherDSP Settings

1. Open `Settings > AetherDSP Settings...`.
2. The dialog opens with a frameless title bar by default.
3. The dialog can be opened without a radio connection, but the effect is only audible during live reception.

## Dialog layout and window controls

The AetherDSP Settings dialog uses custom chrome matching the NetworkDiagnosticsDialog and AetherialAudioStrip:

| Control | Description |
|---------|-------------|
| **Title bar** | 18 px gradient title bar with grip glyph (⋮⋮) on the left and dialog title. Added in v0.9.8 (#2425 refit). |
| **— (Minimize)** | Minimizes the dialog. |
| **□ (Maximize)** | Maximizes or restores the dialog. Double-click the title bar also toggles maximize/restore. |
| **× (Close)** | Closes the dialog. |
| **Drag-to-move** | Click and drag the title bar to move the dialog. |
| **8-axis resize** | Click and drag any edge or corner to resize. Cursor changes to indicate the resize direction. 6 px resize hit zone around the inner content widget. |

The dialog uses `PersistentDialog` with geometry stored in setting `AetherDspDialogGeometry`. The position and size are automatically restored when the dialog is reopened.

The dialog background, title bar colors, and slider styling use theme tokens from the active theme. Sliders now use `applyPrimarySliderStyle()` instead of hardcoded inline stylesheets, making them respect the user's chosen color scheme.

## Selecting and activating noise-reduction engines

The six DSP toggles (NR2, NR4, MNR, DFNR, RN2, BNR) act as both exclusive tab selectors and engine enable/disable controls. Click a toggle to select its settings page; the same click also activates or bypasses that engine.

When NR2 is activated, AudioEngine enforces cascade exclusion, disabling DFNR and other mutually exclusive modules.

Each toggle button has a stable object name (`dspMethodBtnNR2`, `dspMethodBtnNR4`, etc.) and accessible name for screen readers and automation tools.

## Tab: NR2 — Musical-noise reduction

The NR2 engine uses spectral subtraction with gain curve mapping and noise power estimation.

### Gain Method

Selects the gain-curve mapping used by NR2.

| Option | Description |
|--------|-------------|
| Linear | Linear gain curve |
| Log | Logarithmic gain curve |
| Gamma | Gamma-based gain curve (default) |
| Trained | Pre-trained gain curve |

Stored in setting `NR2GainMethod` as integer 0-3.

### NPE Method

Selects the noise power estimator.

| Option | Description |
|--------|-------------|
| OSMS | Optimal smoothing and minimum statistics (default) |
| MMSE | Minimum mean square error |
| NSTAT | Noise statistic-based estimation |

Stored in setting `NR2NpeMethod` as integer 0-2.

### AE Filter (artifact elimination)

- Toggle the anti-artefact post-filter.
- Default: On (`True`).
- Stored in setting `NR2AeFilter`.

### Reduction:

- Sets the maximum NR2 reduction depth.
- Default: 1.50
- Valid range: 0.50–2.00
- Stored in setting `NR2GainMax` (value * 100).

### Gain Floor:

- Sets the minimum gain floor for NR2, preventing over-suppression of weak signals.
- Default: 0.10
- Valid range: 0.00–0.50
- Stored in setting `NR2GainFloor`.

### Smoothing:

- Controls how smoothly the noise estimate tracks changes.
- Default: 0.85
- Valid range: 0.50–0.98
- Stored in setting `NR2GainSmooth`.

### Threshold:

- Sets the speech-presence-probability threshold.
- Default: 0.20
- Valid range: 0.05–0.50
- Stored in setting `NR2Qspp`.

### Use Original Geometry:

- When enabled, uses the original NR2 geometry for the noise estimate rather than the updated geometry algorithm.
- Default: Off (`False`).
- Stored in setting `NR2UseOriginalGeometry`.

### Reset Defaults (↺ icon)

- Restores NR2 tab defaults: Gamma, OSMS, AE on, Reduction 1.50, Gain Floor 0.10, Smoothing 0.85, Threshold 0.20, Use Original Geometry off.
- Rendered as a flat icon button with anticlockwise arrow (U+21BA).

## Tab: NR4 — Libspecbleach noise reduction

The NR4 engine uses the [libspecbleach](https://github.com/geraldmwangi/libspecbleach) library for spectral noise gating.

### Noise Estimation:

Selects the noise-floor estimator used by NR4.

| Option | Description |
|--------|-------------|
| MMSE | Minimum mean square error (default) |
| Brandt | Brandt noise estimator |
| Martin | Martin noise estimator |

Stored in setting `NR4NoiseEstimationMethod` as integer 0-2.

### Adaptive Noise Estimation

- Enables continuous re-estimation of the noise floor.
- Default: On (`True`).
- Stored in setting `NR4AdaptiveNoise`.

### Reduction (dB):

- Sets maximum NR4 noise reduction in dB.
- Default: 10.0
- Valid range: 0.0–40.0
- Stored in setting `NR4ReductionAmount` (value * 10).

### Smoothing (%):

- Time-domain smoothing of the NR4 noise estimate.
- Default: 0
- Valid range: 0–100
- Stored in setting `NR4SmoothingFactor`.

### Whitening (%):

- Flattens residual noise spectral shape.
- Default: 0
- Valid range: 0–100
- Stored in setting `NR4WhiteningFactor`.

### Masking Depth:

- Controls spectral-masking depth.
- Default: 0.50
- Valid range: 0.00–1.00
- Stored in setting `NR4MaskingDepth`.

### Suppression:

- Overall NR4 suppression strength.
- Default: 0.50
- Valid range: 0.00–1.00
- Stored in setting `NR4SuppressionStrength`.

### Reset Defaults (↺ icon)

- Restores NR4 defaults: MMSE, Adaptive on, 10 dB, 0, 0, 0.50, 0.50.
- Rendered as a flat icon button with anticlockwise arrow (U+21BA).

## Tab: MNR — MMSE-Wiener noise reduction

The MNR engine provides MMSE-Wiener noise reduction with asymmetric gain smoothing. **This tab is dimmed on Windows and Linux builds** — the engine has no backend on those platforms.

### Enable MNR (macOS only)

- Enables MMSE-Wiener noise reduction with asymmetric gain smoothing.
- Initial state is read live from the audio engine.
- Stored in setting `MnrEnabled`.

### Strength

- Adjusts MNR aggressiveness (0 mild, 100 max).
- Default: 100
- Valid range: 0–100
- Stored in setting `MnrStrength` (normalized as 0.00–1.00).

## Tab: RN2 — RNNoise

The RN2 (RNNoise) tab is **purely informational** — no adjustable parameters are available. The toggle activates or bypasses the RNNoise engine, but settings are managed elsewhere.

## Tab: BNR — NVIDIA Broadcast

The BNR (NVIDIA) tab shows intensity controlled from the overlay menu. **The BNR toggle is dimmed on builds without the NVIDIA Broadcast SDK.**

## Tab: DFNR — DeepFilterNet3

The DFNR tab provides controls for the DeepFilterNet3 noise reduction engine. **The DFNR toggle is dimmed on builds without the DeepFilterNet3 backend.**

### Attenuation Limit

- Sets maximum noise attenuation applied by DeepFilterNet3.
- Default: 100
- Valid range: 0–100 dB
- 0 = passthrough; 100 = maximum.
- Stored in setting `DfnrAttenLimit`.

### Post-Filter Beta

- Applies an additional post-filter for extra suppression beyond the attenuation limit.
- Default: 0.00
- Valid range: 0.00–0.30
- Stored in setting `DfnrPostFilterBeta` (value * 100).

## Tips

- Start with **Post-Filter Beta** at or below 0.10. Audible artefacts tend to appear before 0.30 is reached, especially on SSB voice signals.
- If you need stronger overall attenuation without touching the post-filter, increase **Attenuation Limit** first, then add **Post-Filter Beta** only for residual noise that remains.
- A value of 0.00 disables the post-filter entirely, leaving DeepFilterNet3's output unchanged.
- For NR2, start with default values and adjust Reduction upward gradually while checking for musical artefacts.
- The **Gain Floor** slider prevents NR2 from completely silencing weak signals. Increase it if signals drop out during pauses, decrease it if background noise is too prominent.

## Troubleshooting

- **Speech sounds hollow or phasey** — **Post-Filter Beta** is set too high. Reduce it toward 0.00 in small increments until naturalness returns.
- **No audible change when moving the slider** — The selected engine may not be active on the current slice. Confirm the engine toggle is selected and that parameters are not at minimum.
- **NR2 produces musical noise** — Reduce **Reduction** or enable **AE Filter** to suppress artefacts.
- **NR2 makes weak signals disappear** — Increase **Gain Floor** to prevent over-suppression.
- **MNR, BNR, or DFNR tabs are dimmed** — The required backend (macOS for MNR, NVIDIA Broadcast SDK for BNR, DeepFilterNet for DFNR) is not available on your platform.
- **DFNR tab is missing entirely** — AetherSDR was built without DeepFilterNet support. Rebuild with the DFNR backend to use this engine.
- **Colors appear mismatched with the rest of AetherSDR** — The dialog now uses theme-aware styling. Try switching themes in `Settings > Appearance` if the colors are not to your liking.

## Related

- [Tune NR2 reduction depth and voice threshold](tune-nr2-reduction-depth-and-voice-threshold.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
- [Configure DFNR post-filter beta for extra suppression](configure-dfnr-post-filter-beta-for-extra-suppression.md)
- [Set DeepFilterNet3 attenuation limit for strong or weak signals](set-deepfilternet3-attenuation-limit-for-strong-or-weak-signals.md)