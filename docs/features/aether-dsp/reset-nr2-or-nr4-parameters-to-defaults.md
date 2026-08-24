# AetherDSP Settings

Use the **AetherDSP Settings** dialog to tune the advanced parameters of AetherSDR's client-side noise-reduction engines (NR2, NR4, MNR, DFNR, RN2, BNR). The six DSP modules are selectable via a toggle row at the top; clicking a toggle also activates or bypasses that engine.

## Opening AetherDSP Settings

1. Click `Settings > AetherDSP Settings...`.

The dialog opens with the currently active noise reduction tab selected.

## Dialog chrome

The AetherDSP Settings dialog uses a frameless 18 px gradient title bar with a grip glyph (⋮⋮) on the left and the dialog title "AetherDSP Settings". Three window-control buttons sit at the right:

- **— (Minimize)** — Minimizes the dialog.
- **□ (Maximize)** — Maximizes or restores the dialog. Double-clicking the title bar also toggles maximize/restore.
- **× (Close)** — Closes the dialog.

The dialog has a 6 px resize hit zone around the inner content widget. Drag the title bar to move the dialog. Resize the dialog by dragging any edge or corner (8-axis resize). The dialog geometry is persisted between sessions under the setting key `AetherDspDialogGeometry`.

The dialog uses themed styling applied through `ThemeManager` rather than a hardcoded stylesheet.

## Tab selector behavior

The six tabs at the top (NR2, NR4, MNR, DFNR, RN2, BNR) act as both tab selectors and engine enable/disable controls. Clicking a tab selects that page and activates the corresponding DSP engine. When a new engine is activated, AetherSDR cascades exclusion, disabling DFNR and other mutually exclusive modules.

Each toggle button has an object name in the format `dspMethodBtn` followed by the label text (e.g. `dspMethodBtnNR2`), and an accessible name that includes the label and "noise-reduction method". This allows screen readers and automation tools to identify each button.

The last active client-side noise reduction method is persisted under the setting key `LastClientNr`. On builds without the DFNR backend, any stored DFNR preference is automatically cleared.

**Platform notes:**

- **MNR (macOS only)** — The MNR tab is dimmed on Windows and Linux builds because the macOS MMSE-Wiener engine has no backend on those platforms.
- **BNR** — The BNR tab is dimmed on builds without the NVIDIA Broadcast SDK.
- **DFNR** — The DFNR tab shows a tooltip "DFNR requires DeepFilterNet to be set up and AetherSDR rebuilt." on builds without the DFNR backend.

## NR2 tab

Use the NR2 (musical-noise-reduction) engine for noise suppression that avoids musical artefacts.

### Controls

| Control                          | Default | Valid range | Setting key         |
|----------------------------------|---------|-------------|---------------------|
| Gain Method                      | Gamma   | Linear \| Log \| Gamma \| Trained | `NR2GainMethod` |
| NPE Method                       | OSMS    | OSMS \| MMSE \| NSTAT | `NR2NpeMethod` |
| AE Filter (artifact elimination) | Enabled | —           | `NR2AeFilter`       |
| Reduction:                       | 1.50    | 0.50–2.00   | `NR2GainMax`        |
| Smoothing:                       | 0.85    | 0.50–0.98   | `NR2GainSmooth`     |
| Threshold:                       | 0.20    | 0.05–0.50   | `NR2Qspp`           |

**Gain Method** — Selects the gain-curve mapping used by NR2. Stored as integer 0–3 matching the order above.
**NPE Method** — Selects the noise power estimator. Stored as integer 0–2.
**AE Filter** — Toggles the anti-artefact post-filter.
**Reduction:** — Sets the maximum NR2 reduction depth. Slider stores value×100 internally.
**Smoothing:** — Controls how smoothly the noise estimate tracks changes.
**Threshold:** — Sets the speech-presence-probability threshold.

### Reset NR2 defaults

1. Select the **NR2** tab.
2. Click **Reset Defaults** (↺ icon).

All NR2 controls return to Gamma, OSMS, AE Filter enabled, Reduction 1.50, Smoothing 0.85, Threshold 0.20.

## NR4 tab

Use the NR4 (libspecbleach) engine for speech-focused noise reduction with adaptive noise estimation.

### Controls

| Control | Default | Valid range | Setting key |
|---|---|---|---|
| Noise Estimation: | MMSE | MMSE \| Brandt \| Martin | `NR4NoiseEstimationMethod` |
| Adaptive Noise Estimation | Enabled | — | `NR4AdaptiveNoise` |
| Reduction (dB): | 10.0 | 0.0–40.0 dB | `NR4ReductionAmount` |
| Smoothing (%): | 0 | 0–100 | `NR4SmoothingFactor` |
| Whitening (%): | 0 | 0–100 | `NR4WhiteningFactor` |
| Masking Depth: | 0.50 | 0.00–1.00 | `NR4MaskingDepth` |
| Suppression: | 0.50 | 0.00–1.00 | `NR4SuppressionStrength` |

**Noise Estimation:** — Selects the noise-floor estimator used by NR4. Stored as integer 0–2.
**Adaptive Noise Estimation** — Enables continuous re-estimation of the noise floor.
**Reduction (dB):** — Sets the maximum NR4 noise reduction in dB. Slider stores value×10.
**Smoothing (%):** — Time-domain smoothing of the NR4 noise estimate.
**Whitening (%):** — Flattens residual noise spectral shape.
**Masking Depth:** — Controls spectral-masking depth.
**Suppression:** — Overall NR4 suppression strength.

### Reset NR4 defaults

1. Select the **NR4** tab.
2. Click **Reset Defaults** (↺ icon).

All NR4 controls return to MMSE, Adaptive Noise Estimation enabled, Reduction 10.0 dB, Smoothing 0, Whitening 0, Masking Depth 0.50, Suppression 0.50.

## MNR tab (macOS only)

Use the MNR (macOS MMSE-Wiener) engine for noise reduction with asymmetric gain smoothing. This tab is only available on macOS builds.

### Controls

| Control | Default | Valid range | Setting key |
|---|---|---|---|
| Enable MNR (macOS only) | — | — | `MnrEnabled` |
| Strength | 100 | 0–100 | `MnrStrength` |

**Enable MNR** — Enables MMSE-Wiener noise reduction with asymmetric gain smoothing. Initial state read live from AudioEngine.
**Strength** — Adjusts MNR aggressiveness (0 mild, 100 max). Persisted as normalized 0.00–1.00.

### Reset MNR defaults

1. Select the **MNR** tab.
2. Click **Reset Defaults** (↺ icon).

The Strength slider returns to 100.

## DFNR tab

Use the DeepFilterNet3 engine for neural-network-based noise reduction.

### Controls

| Control | Default | Valid range | Setting key |
|---|---|---|---|
| Attenuation Limit | 100 | 0–100 dB | `DfnrAttenLimit` |
| Post-Filter Beta | 0.00 | 0.00–0.30 | `DfnrPostFilterBeta` |

**Attenuation Limit** — Sets maximum noise attenuation applied by DeepFilterNet3. 0 = passthrough; 100 = maximum.
**Post-Filter Beta** — Applies an additional post-filter for extra suppression. Slider stores value×100 internally.

### Reset DFNR defaults

1. Select the **DFNR** tab.
2. Click **Reset Defaults** (↺ icon).

Attenuation Limit returns to 100 and Post-Filter Beta returns to 0.00.

On builds without the DFNR backend, the DFNR tab shows a tooltip: "DFNR requires DeepFilterNet to be set up and AetherSDR rebuilt."

## RN2 tab

Use the RN2 (RNNoise) engine for real-time neural-network-based noise suppression.

### Controls

| Control | Default | Valid range | Setting key |
|---|---|---|---|
| Noise Floor (RN2 dry mix) | 0 | 0–100 | — |

**Noise Floor (RN2 dry mix)** — Sets the percentage of the original signal RN2 leaves under the denoised audio. Zero yields full suppression (silent between phrases); 10–20% keeps a steady quiet floor so the receiver still sounds alive. Affects received audio only; the transmit denoiser is unchanged. Persisted by Rn2SettingsModel and exposed to the DSP chain via AetherDspWidget's `rn2DryMixChanged` signal.

### Reset RN2 defaults

1. Select the **RN2** tab.
2. Click **Reset Defaults** (↺ icon).

The Noise Floor slider returns to 0.

## BNR tab

The BNR (NVIDIA Broadcast) tab uses the NVIDIA Broadcast SDK for AI-based noise reduction. The intensity is controlled from the overlay menu. The BNR tab is dimmed on builds without the NVIDIA Broadcast SDK. This tab has no adjustable parameters, so **Reset Defaults** is a no-op.

## Tips

- **Reset Defaults** affects only the tab where you click it. Resetting NR2 does not alter NR4 settings, and vice versa.
- Changes take effect immediately. If a noise reduction engine is active on a receive slice at the time, you will hear the engine change behaviour as soon as you adjust any control.
- The six DSP toggles act as exclusive selectors and engine enable/disable controls simultaneously. Activating one engine may disable other mutually exclusive modules.
- When AetherSDR restarts, it restores the last active client-side noise reduction method stored under the setting key `LastClientNr`.
- For RN2, setting the Noise Floor to 10–20% keeps a steady quiet floor so the receiver still sounds alive between phrases, while 0% yields full suppression.

## Related

- Tune NR2 reduction depth and threshold
- [Switch NR2 gain method between Linear, Log, Gamma and Trained](switch-nr2-gain-method-between-linear-log-gamma-and-trained.md)
- [Change NR2 noise power estimator (OSMS/MMSE/NSTAT)](change-nr2-noise-power-estimator-osms-mmse-nstat.md)
- [Adjust NR4 reduction amount in dB](adjust-nr4-reduction-amount-in-db.md)
- [Enable or disable NR4 adaptive noise estimation](enable-or-disable-nr4-adaptive-noise-estimation.md)
- [Tune NR4 masking depth and suppression strength](tune-nr4-masking-depth-and-suppression-strength.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
- [Set RN2 noise floor dry mix](set-rn2-noise-floor-dry-mix.md)