# AetherDSP Settings

The AetherDSP Settings dialog tunes the advanced parameters of AetherSDR's client-side noise-reduction engines (NR2, NR4, MNR, DFNR, RN2, BNR), letting operators dial in the tradeoff between noise suppression and speech fidelity. The six DSP modules are selectable via a toggle row at the top; clicking a toggle also activates or bypasses that engine.

## Before you start

- AetherSDR does not need to be connected to a radio to adjust DSP settings.
- The selected NR engine must already be active on your receive slice for these changes to have an audible effect.
- Some DSP engines (MNR, BNR, RN2) are platform-dependent or informational only. For details see [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md).

## Open AetherDSP Settings

1. Open `Settings > AetherDSP Settings...`.

The dialog appears as a frameless window with a custom title bar. Click and drag the title bar to move the dialog. Double-click the title bar to toggle maximize/restore. Click and drag any edge or corner to resize the dialog.

The title bar contains three window controls:
- **— (Minimize)**: Minimizes the dialog.
- **□ (Maximize)**: Maximizes or restores the dialog.
- **× (Close)**: Closes the dialog.

## Select a DSP engine

At the top of the dialog, six toggle tabs act as both selector and enable/disable controls:

- **NR2** – Musical-noise-reduction engine
- **NR4** – libspecbleach noise suppression
- **MNR** – macOS MMSE-Wiener (dimmed on Windows/Linux builds)
- **DFNR** – DeepFilterNet3 neural noise suppression
- **RN2** – RNNoise (informational only, no adjustable parameters)
- **BNR** – NVIDIA Broadcast (dimmed on builds without NVIDIA Broadcast SDK)

Click a toggle to select its parameter page and activate or bypass that engine. When NR2 is activated, AudioEngine cascades exclusion, disabling DFNR and other mutually exclusive modules.

## NR2 parameters

| Control | Default | Valid values | Setting key |
|---|---|---|---|
| **Gain Method** | Gamma | Linear \| Log \| Gamma \| Trained | `NR2GainMethod` |
| **NPE Method** | OSMS | OSMS \| MMSE \| NSTAT | `NR2NpeMethod` |
| **AE Filter (artifact elimination)** | Enabled (checked) | Checked / unchecked | `NR2AeFilter` |
| **Reduction:** | 1.50 | 0.50–2.00 | `NR2GainMax` |
| **Smoothing:** | 0.85 | 0.50–0.98 | `NR2GainSmooth` |
| **Threshold:** | 0.20 | 0.05–0.50 | `NR2Qspp` |

Click **Reset Defaults (↺ icon)** to restore NR2 defaults (Gamma/OSMS/AE on, 1.50/0.85/0.20).

## NR4 parameters

| Control | Default | Valid values | Setting key |
|---|---|---|---|
| **Noise Estimation:** | MMSE | MMSE \| Brandt \| Martin | `NR4NoiseEstimationMethod` |
| **Adaptive Noise Estimation** | Enabled (checked) | Checked / unchecked | `NR4AdaptiveNoise` |
| **Reduction (dB):** | 10.0 | 0.0–40.0 dB | `NR4ReductionAmount` |
| **Smoothing (%):** | 0 | 0–100 | `NR4SmoothingFactor` |
| **Whitening (%):** | 0 | 0–100 | `NR4WhiteningFactor` |
| **Masking Depth:** | 0.50 | 0.00–1.00 | `NR4MaskingDepth` |
| **Suppression:** | 0.50 | 0.00–1.00 | `NR4SuppressionStrength` |

Click **Reset Defaults (↺ icon)** to restore NR4 defaults (MMSE/adaptive on, 10 dB, 0, 0, 0.50, 0.50).

### Enable or disable NR4 adaptive noise estimation

With adaptive noise estimation enabled, NR4 tracks changes in the noise environment in real time; disabling it locks the noise-floor estimate to a static snapshot, which can suit highly stable noise conditions.

1. Open `Settings > AetherDSP Settings...`.
2. Click the **NR4** tab.
3. Check or uncheck **Adaptive Noise Estimation** to enable or disable continuous noise-floor re-estimation.

The setting takes effect immediately and is saved automatically to `NR4AdaptiveNoise`.

#### Tips

- If the noise floor on your band is stable and consistent, unchecking **Adaptive Noise Estimation** can prevent the estimator from following signal-level changes and misclassifying speech as noise.
- If the noise floor varies rapidly — such as during band openings or with impulse noise — leave **Adaptive Noise Estimation** checked so NR4 can track the changing conditions.
- The **Noise Estimation Method** selector (MMSE, Brandt, Martin) determines how NR4 builds its noise model regardless of whether adaptive mode is on or off. Changing the method can affect how well the static or adaptive estimate tracks your noise floor.
- Click **Reset Defaults** on the NR4 tab to return all NR4 controls to their factory values (adaptive on, MMSE, 10 dB, 0, 0, 0.50, 0.50).

## MNR parameters (macOS only)

| Control | Default | Valid values | Setting key |
|---|---|---|---|
| **Enable MNR (macOS only)** | Off | Checked / unchecked | `MnrEnabled` |
| **Strength** | 100 | 0–100 | `MnrStrength` |

The MNR toggle is dimmed on Windows/Linux builds. The **Enable MNR** checkbox enables MMSE-Wiener noise reduction with asymmetric gain smoothing.

## DFNR parameters

| Control | Default | Valid values | Setting key |
|---|---|---|---|
| **Attenuation Limit** | 100 | 0–100 dB | `DfnrAttenLimit` |
| **Post-Filter Beta** | 0.00 | 0.00–0.30 | `DfnrPostFilterBeta` |

**Attenuation Limit** sets the maximum noise attenuation applied by DeepFilterNet3. 0 = passthrough; 100 = maximum.

**Post-Filter Beta** applies an additional post-filter for extra suppression.

## RN2 tab

Selecting the RN2 tab displays informational content only. There are no adjustable parameters for RN2.

## BNR tab

Selecting the BNR tab displays NVIDIA Broadcast noise reduction controls. The BNR toggle is dimmed on builds without the NVIDIA Broadcast SDK. Intensity is controlled from the overlay menu.

## Related

- [Adjust NR4 reduction amount in dB](adjust-nr4-reduction-amount-in-db.md)
- [Tune NR4 masking depth and suppression strength](tune-nr4-masking-depth-and-suppression-strength.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)