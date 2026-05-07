# AetherDSP Settings

AetherDSP Settings is a dialog that lets you tune the client-side noise-reduction engines available in AetherSDR: NR2, NR4, MNR, DFNR, RN2, and BNR. Each engine has its own tab. Open the dialog from `Settings > AetherDSP Settings...`.

From v0.9.8 the dialog uses a custom frameless chrome with a gradient title bar, window-control buttons, 8-axis resize, and drag-to-move. The dialog hosts an embedded `AetherDspWidget` that contains all controls. Existing signal connections to the dialog continue to work without change.

---

## NR2 tab

NR2 is AetherSDR's musical-noise-reduction engine.

### Steps

1. Click `Settings > AetherDSP Settings...`.
2. Click the **NR2** tab.
3. Select a **Gain Method** radio button.
4. Select an **NPE Method** radio button.
5. Check or uncheck **AE Filter (artifact elimination)** as needed.
6. Drag **Reduction:**, **Smoothing:**, and **Threshold:** to the desired values.
7. Click **Reset Defaults (↺ icon)** to return all NR2 controls to their factory values.

### What each control does

| Control | Kind | Default | Valid range | Setting key |
|---|---|---|---|---|
| Gain Method | Radio button | Gamma | Linear / Log / Gamma / Trained | `NR2GainMethod` |
| NPE Method | Radio button | OSMS | OSMS / MMSE / NSTAT | `NR2NpeMethod` |
| AE Filter (artifact elimination) | Checkbox | On | On / Off | `NR2AeFilter` |
| Reduction: | Slider | 1.50 | 0.50–2.00 | `NR2GainMax` |
| Smoothing: | Slider | 0.85 | 0.50–0.98 | `NR2GainSmooth` |
| Threshold: | Slider | 0.20 | 0.05–0.50 | `NR2Qspp` |
| Reset Defaults (↺ icon) | Push button | — | — | — |

`NR2GainMethod` is stored as an integer 0–3 (Linear=0, Log=1, Gamma=2, Trained=3). `NR2NpeMethod` is stored as an integer 0–2 (OSMS=0, MMSE=1, NSTAT=2). `NR2GainMax` is stored internally as value × 100.

### Tips

- **Gamma** gain method suits most SSB voice work. **Trained** can improve results on weak signals.
- Raise **Threshold:** if NR2 is suppressing speech. Lower it if noise breaks through during pauses.
- Click **Reset Defaults (↺ icon)** to restore: Gamma / OSMS / AE on / 1.50 / 0.85 / 0.20.

---

## NR4 tab

NR4 uses the libspecbleach engine.

### Steps

1. Click `Settings > AetherDSP Settings...`.
2. Click the **NR4** tab.
3. Select a **Noise Estimation:** radio button.
4. Check or uncheck **Adaptive Noise Estimation** as needed.
5. Adjust **Reduction (dB):**, **Smoothing (%)**:, **Whitening (%)**:, **Masking Depth:**, and **Suppression:** sliders.
6. Click **Reset Defaults (↺ icon)** to return all NR4 controls to their factory values.

### What each control does

| Control | Kind | Default | Valid range | Setting key |
|---|---|---|---|---|
| Noise Estimation: | Radio button | MMSE | MMSE / Brandt / Martin | `NR4NoiseEstimationMethod` |
| Adaptive Noise Estimation | Checkbox | On | On / Off | `NR4AdaptiveNoise` |
| Reduction (dB): | Slider | 10.0 | 0.0–40.0 | `NR4ReductionAmount` |
| Smoothing (%): | Slider | 0 | 0–100 | `NR4SmoothingFactor` |
| Whitening (%): | Slider | 0 | 0–100 | `NR4WhiteningFactor` |
| Masking Depth: | Slider | 0.50 | 0.00–1.00 | `NR4MaskingDepth` |
| Suppression: | Slider | 0.50 | 0.00–1.00 | `NR4SuppressionStrength` |
| Reset Defaults (↺ icon) | Push button | — | — | — |

`NR4NoiseEstimationMethod` is stored as an integer 0–2 (MMSE=0, Brandt=1, Martin=2). `NR4ReductionAmount` is stored internally as value × 10.

### Tips

- Leave **Adaptive Noise Estimation** on unless the noise floor is stable and you want to lock the estimate.
- Increase **Whitening (%):** to flatten residual colored noise after reduction.
- Click **Reset Defaults (↺ icon)** to restore: MMSE / adaptive on / 10 dB / 0 / 0 / 0.50 / 0.50.

---

## MNR tab

MNR is AetherSDR's MMSE-Wiener noise reduction engine, available on macOS only. The MNR toggle is dimmed on Windows and Linux builds.

### Before you start

- AetherSDR must be running on macOS. The **Enable MNR (macOS only)** checkbox is present only on macOS builds.
- No radio connection is required to adjust these settings.

### Steps

1. Click `Settings > AetherDSP Settings...`.
2. Click the **MNR** tab.
3. Check **Enable MNR (macOS only)** to activate the engine.
4. Drag the **Strength** slider to set aggressiveness. 0 is the mildest setting; 100 is maximum noise reduction.

### What each control does

| Control | Kind | Default | Valid range | Setting key |
|---|---|---|---|---|
| Enable MNR (macOS only) | Checkbox | *(read from audio engine at startup)* | On / Off | `MnrEnabled` |
| Strength | Slider | 100 | 0–100 | `MnrStrength` |

`MnrStrength` is persisted internally as a normalized value between 0.00 and 1.00.

### Tips

- Start with **Strength** at 100 and reduce it if you notice speech artifacts or a hollow sound. Lower values trade noise suppression for more natural voice reproduction.
- Because MNR's initial enabled state is read live from the audio engine at dialog open time, the checkbox reflects the current engine state rather than a fixed saved default.

### Troubleshooting

- **The MNR tab is visible but "Enable MNR (macOS only)" has no effect** — confirm you are running AetherSDR on macOS. The checkbox label explicitly notes macOS-only availability; on other platforms the engine is not active regardless of this setting.

---

## RN2 tab

The **RN2** tab displays information about the RNNoise engine. There are no adjustable parameters on this tab.

---

## BNR tab

The **BNR** tab displays information about the NVIDIA noise-reduction engine. Intensity is controlled from the overlay menu, not from this dialog. The BNR toggle is dimmed on builds without the NVIDIA Broadcast SDK.

---

## DFNR tab

DFNR uses the DeepFilterNet3 engine.

### Steps

1. Click `Settings > AetherDSP Settings...`.
2. Click the **DFNR** tab.
3. Drag **Attenuation Limit** to set the maximum noise attenuation. Set to 0 for passthrough; set to 100 for maximum attenuation.
4. Drag **Post-Filter Beta** to apply additional post-filtering suppression. Leave at 0.00 if no extra suppression is needed.

### What each control does

| Control | Kind | Default | Valid range | Setting key |
|---|---|---|---|---|
| Attenuation Limit | Slider | 100 | 0–100 dB | `DfnrAttenLimit` |
| Post-Filter Beta | Slider | 0.00 | 0.00–0.30 | `DfnrPostFilterBeta` |

`DfnrPostFilterBeta` is stored internally as value × 100.

### Tips

- Reduce **Attenuation Limit** if DeepFilterNet3 is over-suppressing and causing artifacts on voice peaks.
- Leave **Post-Filter Beta** at 0.00 unless residual noise remains after adjusting **Attenuation Limit**.

---

## Window controls

The AetherDSP Settings dialog uses a custom frameless title bar introduced in v0.9.8.

### Title bar

- 18 px tall with a blue gradient background (`#5a7494` to `#1e2e3e`).
- A grip glyph (⋮⋮) on the left and "AetherDSP Settings" in bold 10 px text.
- Three window-control buttons on the right: **—** (Minimize), **□** (Maximize/Restore), **×** (Close).

### Drag-to-move

- Click and drag the title bar to move the dialog.
- Double-click the title bar to toggle between maximized and restored states.

### 8-axis resize

- Click and drag any edge or corner of the dialog to resize. The cursor changes to indicate the resize direction.
- The resize hit zone extends 12 px from the edges of the dialog (the inner content widget has 6 px padding).

---

## Related

- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
- [AetherDSP Settings overview](overview.md)
- [Tune NR2 reduction depth and voice threshold](tune-nr2-reduction-depth-and-voice-threshold.md)