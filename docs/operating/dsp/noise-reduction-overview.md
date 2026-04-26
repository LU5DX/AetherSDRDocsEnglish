# Choosing the right noise reduction: NR2, NR4, DFNR, MNR

AetherSDR provides four client-side noise-reduction engines. This page explains what each one does and how to decide which to use, so you can open the right tab in AetherDSP Settings and start tuning.

## Before you start

- Open `Settings > AetherDSP Settings...` to reach the AetherDSP Settings dialog.
- A radio connection is not required to configure these parameters.

## Steps

1. Open `Settings > AetherDSP Settings...`.
2. Click the tab for the engine you want to use: **NR2**, **NR4**, **DFNR**, or **MNR**.
3. Adjust the controls on that tab. Settings are saved immediately; there is no Apply button.
4. If you want to return a tab to its shipped defaults, click **Reset Defaults** at the bottom of the NR2 or NR4 tab.

## What each control does

### NR2 tab — musical-noise reduction

NR2 is a frequency-domain engine focused on suppressing the tonal "musical noise" artefacts that are common in SSB and weak-signal work. Use it when you hear a warbling, fluttery quality in the noise rather than a flat hiss.

| Control | Kind | Default | Range | Setting key |
|---|---|---|---|---|
| Gain Method | Radio buttons | Gamma | Linear \| Log \| Gamma \| Trained | `NR2GainMethod` |
| NPE Method | Radio buttons | OSMS | OSMS \| MMSE \| NSTAT | `NR2NpeMethod` |
| AE Filter (artifact elimination) | Checkbox | Enabled | — | `NR2AeFilter` |
| Reduction Depth: | Slider | 1.50 | 0.50–2.00 | `NR2GainMax` |
| Smoothing: | Slider | 0.85 | 0.50–0.98 | `NR2GainSmooth` |
| Voice Threshold: | Slider | 0.20 | 0.05–0.50 | `NR2Qspp` |
| Reset Defaults | Button | — | — | — |

**Gain Method** selects the curve used to calculate how much gain to apply to each spectral bin. Gamma is the default and suits most voice work. Trained uses a model built from real speech and noise samples and may perform better on weak DX signals. Linear and Log offer simpler mappings if you want predictable, auditable behaviour.

**NPE Method** controls how NR2 estimates the noise floor. OSMS tracks the floor using a running minimum and is robust on stable noise. MMSE minimises the mean squared estimation error. NSTAT adapts to noise that changes quickly over time.

**AE Filter (artifact elimination)** applies a post-filter to reduce ringing and musical-noise residuals. Leave it enabled unless you are deliberately comparing raw NR2 output.

**Reduction Depth:** sets how aggressively NR2 attenuates noise. Higher values suppress more noise but can distort speech.

**Smoothing:** controls how quickly the noise estimate follows changes. Higher values produce a steadier estimate but react more slowly to sudden noise bursts.

**Voice Threshold:** is the speech-presence-probability threshold below which NR2 treats a bin as noise. Lower values protect quieter speech but pass more noise.

---

### NR4 tab — libspecbleach broadband reduction

NR4 is built on libspecbleach and is suited to broadband noise: power-line hash, band noise, and atmospheric noise under SSB signals. It offers explicit dB-calibrated reduction and a whitening stage.

| Control | Kind | Default | Range | Setting key |
|---|---|---|---|---|
| Noise Estimation Method | Radio buttons | SPP-MMSE | SPP-MMSE \| Brandt \| Martin | `NR4NoiseEstimationMethod` |
| Adaptive Noise Estimation | Checkbox | Enabled | — | `NR4AdaptiveNoise` |
| Reduction (dB): | Slider | 10.0 dB | 0.0–40.0 dB | `NR4ReductionAmount` |
| Smoothing (%): | Slider | 0 | 0–100 | `NR4SmoothingFactor` |
| Whitening (%): | Slider | 0 | 0–100 | `NR4WhiteningFactor` |
| Masking Depth: | Slider | 0.50 | 0.00–1.00 | `NR4MaskingDepth` |
| Suppression: | Slider | 0.50 | 0.00–1.00 | `NR4SuppressionStrength` |
| Reset Defaults | Button | — | — | — |

**Noise Estimation Method** sets the noise-floor estimator. SPP-MMSE balances noise estimation with speech preservation. Brandt uses recursive smoothing across critical frequency bands and handles non-stationary noise well. Martin uses running spectral minima and is robust when the noise floor changes slowly.

**Adaptive Noise Estimation** enables continuous re-estimation of the noise floor. Disable it only if you want to lock the estimate to a snapshot.

**Reduction (dB):** is the main depth control. Start at the default 10.0 dB and increase only as needed; high values at wide bandwidths can hollow out voice quality.

**Smoothing (%):** applies time-domain smoothing to the noise estimate. Increase it to stabilise the estimate on burst noise.

**Whitening (%):** flattens the residual noise spectral shape after reduction, trading a coloured noise floor for a flatter hiss.

**Masking Depth:** controls how deeply spectral-masking suppression is applied.

**Suppression:** sets the overall NR4 suppression strength.

---

### DFNR tab — DeepFilterNet3

DFNR runs DeepFilterNet3, a neural-network filter. It operates on the audio stream and requires no noise-floor estimate. It is the most effective option for intelligibility on crowded bands but has the highest CPU cost of the four engines.

| Control | Kind | Default | Range | Setting key |
|---|---|---|---|---|
| Attenuation Limit | Slider | 100 dB | 0–100 dB | `DfnrAttenLimit` |
| Post-Filter Beta | Slider | 0.00 | 0.00–0.30 | `DfnrPostFilterBeta` |

**Attenuation Limit** caps how much attenuation DeepFilterNet3 can apply. At 0 it passes the signal through unchanged; at 100 it applies maximum attenuation. Reduce this on strong signals to prevent over-suppression.

**Post-Filter Beta** applies an additional post-filter on top of DeepFilterNet3's output for extra suppression. The default of 0.00 disables it. Increase cautiously; high values can degrade speech quality.

---

### MNR tab — macOS MMSE-Wiener reduction

MNR is an MMSE-Wiener filter with asymmetric gain smoothing. It is available on macOS only.

| Control | Kind | Default | Range | Setting key |
|---|---|---|---|---|
| Enable MNR (macOS only) | Checkbox | Read from audio engine | — | `MnrEnabled` |
| Strength | Slider | 100 | 0–100 | `MnrStrength` |

**Enable MNR (macOS only)** activates the engine. The initial state reflects what the audio engine reports, not a stored default.

**Strength** sets aggressiveness. 0 is mild; 100 is maximum suppression.

---

### Choosing between the engines

| Situation | Suggested engine |
|---|---|
| Musical-noise artefacts, warbling in SSB noise | NR2 |
| Broadband atmospheric or power-line noise | NR4 |
| Maximum intelligibility, CPU available | DFNR |
| macOS system audio path, light processing | MNR |

You are not limited to one engine at a time; the tray buttons for each engine activate them independently. Start with one and add a second only if the first is insufficient.

## Tips

- On the NR2 tab, click **Reset Defaults** to return to Gamma / OSMS / AE Filter on / 1.50 / 0.85 / 0.20 at any point.
- On the NR4 tab, click **Reset Defaults** to return to SPP-MMSE / adaptive on / 10.0 dB / 0 / 0 / 0.50 / 0.50.
- The MNR tab is present on all platforms but **Enable MNR (macOS only)** has no effect on Linux or Windows.
- Setting DFNR **Attenuation Limit** to 0 disables DeepFilterNet3 suppression without closing the dialog, which is useful for A/B comparison.

## Related

- [AetherDSP Settings overview](../../features/aether-dsp/overview.md)
- [Tune NR2 reduction depth and voice threshold](../../features/aether-dsp/tune-nr2-reduction-depth-and-voice-threshold.md)
- [Switch NR2 gain method between Linear, Log, Gamma and Trained](../../features/aether-dsp/switch-nr2-gain-method-between-linear-log-gamma-and-trained.md)
- [Change NR2 noise power estimator (OSMS/MMSE/NSTAT)](../../features/aether-dsp/change-nr2-noise-power-estimator-osms-mmse-nstat.md)
- [Adjust NR4 reduction amount in dB](../../features/aether-dsp/adjust-nr4-reduction-amount-in-db.md)
- [Enable or disable NR4 adaptive noise estimation](../../features/aether-dsp/enable-or-disable-nr4-adaptive-noise-estimation.md)
- [Tune NR4 masking depth and suppression strength](../../features/aether-dsp/tune-nr4-masking-depth-and-
