# Choosing the right noise reduction: NR2, NR4, DFNR, MNR

AetherSDR provides four client-side noise-reduction engines. This page describes what each engine does, when to use it, and where to find its controls so you can pick the right one for your operating conditions.

## Before you start

- Open AetherDSP Settings via `Settings > AetherDSP Settings...`.
- The NR engine you configure here is client-side only; it does not require a radio connection.

## Steps

1. Go to `Settings > AetherDSP Settings...`.
2. Click the tab for the engine you want to use: **NR2**, **NR4**, **DFNR**, or **MNR**.
3. Adjust the controls on that tab (see the table below).
4. Close the dialog. Settings are saved automatically.

## What each control does

### NR2 — musical-noise reduction

A frequency-domain noise reducer designed to minimise the tonal "birdie" artefacts common in spectral subtraction. Good starting choice for SSB voice in moderate QRN.

| Control | Kind | Default | Range | Setting key |
|---|---|---|---|---|
| Gain Method | Radio buttons | Gamma | Linear \| Log \| Gamma \| Trained | `NR2GainMethod` |
| NPE Method | Radio buttons | OSMS | OSMS \| MMSE \| NSTAT | `NR2NpeMethod` |
| AE Filter (artifact elimination) | Checkbox | Enabled | — | `NR2AeFilter` |
| Reduction Depth: | Slider | 1.50 | 0.50–2.00 | `NR2GainMax` |
| Smoothing: | Slider | 0.85 | 0.50–0.98 | `NR2GainSmooth` |
| Voice Threshold: | Slider | 0.20 | 0.05–0.50 | `NR2Qspp` |
| Reset Defaults | Button | — | — | — |

**Gain Method** selects how NR2 maps noise estimates to gain reduction. Gamma matches typical speech amplitude patterns and is the default. Trained uses a model built from real speech and noise samples. Linear and Log trade perceptual accuracy for simpler computation.

**NPE Method** selects the noise power estimator. OSMS (Optimal Smoothing Minimum Statistics) tracks the noise floor using a running minimum and suits slowly varying noise. MMSE minimises expected estimation error. NSTAT adapts to noise that changes rapidly over time.

**AE Filter (artifact elimination)** applies a post-filter to reduce ringing and musical artefacts. Leave it enabled unless you are experimenting with very low Reduction Depth values.

**Reduction Depth:** controls maximum suppression. Higher values remove more noise but risk speech distortion. 1.50 is the default.

**Smoothing:** controls how quickly the noise estimate follows changes. Higher values are steadier but slower to adapt.

**Voice Threshold:** is the speech-presence-probability threshold. Lower values protect quiet speech but may allow more noise through.

**Reset Defaults** restores: Gamma / OSMS / AE Filter on / 1.50 / 0.85 / 0.20.

---

### NR4 — libspecbleach

A separate spectral-bleaching engine with its own noise estimator and additional shaping controls. Useful when NR2 leaves residual noise or when you want dB-calibrated reduction targets.

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

**Noise Estimation Method** — SPP-MMSE balances noise estimation with speech preservation. Brandt uses recursive smoothing over critical frequency bands and suits non-stationary noise. Martin uses running spectral minima and is robust for slowly varying noise floors.

**Adaptive Noise Estimation** enables continuous re-estimation of the noise floor. Disable it only if the noise environment is static and you want a fixed floor.

**Reduction (dB):** sets the maximum reduction in dB. Start at 10 dB and increase if noise remains.

**Smoothing (%):** applies time-domain smoothing to the noise estimate.

**Whitening (%):** flattens the residual noise spectral shape after reduction.

**Masking Depth:** controls the depth of spectral masking applied.

**Suppression:** sets the overall suppression strength. Higher values are more aggressive.

**Reset Defaults** restores: SPP-MMSE / Adaptive on / 10.0 dB / 0 / 0 / 0.50 / 0.50.

---

### DFNR — DeepFilterNet3

A neural-network-based noise filter. Suited for strong broadband noise where conventional spectral methods fall short. Has the highest CPU cost of the four engines.

| Control | Kind | Default | Range | Setting key |
|---|---|---|---|---|
| Attenuation Limit | Slider | 100 dB | 0–100 dB | `DfnrAttenLimit` |
| Post-Filter Beta | Slider | 0.00 | 0.00–0.30 | `DfnrPostFilterBeta` |

**Attenuation Limit** sets the maximum noise attenuation DeepFilterNet3 will apply. 0 is passthrough; 100 is maximum attenuation. Reduce this value if the neural filter over-suppresses weak signals.

**Post-Filter Beta** adds an extra suppression stage on top of the neural filter output. Leave at 0.00 unless residual noise remains after adjusting Attenuation Limit.

---

### MNR — macOS only

An MMSE-Wiener noise reducer with asymmetric gain smoothing, available only on macOS.

| Control | Kind | Default | Range | Setting key |
|---|---|---|---|---|
| Enable MNR (macOS only) | Checkbox | (read from audio engine) | — | `MnrEnabled` |
| Strength | Slider | 100 | 0–100 | `MnrStrength` |

**Enable MNR (macOS only)** turns the engine on or off. The initial state reflects the current audio engine state.

**Strength** sets aggressiveness. 0 is the mildest; 100 is maximum. Persisted internally as a normalised value of 0.00–1.00.

MNR is not available on Linux or Windows. The **MNR** tab is still present but **Enable MNR (macOS only)** will have no effect on non-macOS systems.

## Tips

- Run only one noise-reduction engine at a time. Chaining multiple engines can cause speech artefacts and adds CPU load.
- For SSB voice with moderate band noise, start with NR2 at its defaults before trying NR4 or DFNR.
- If you are on macOS and prefer a lighter CPU load, MNR is the lowest-overhead option.
- DFNR's Attenuation Limit at 100 dB can suppress very weak signals along with the noise. Reduce it to 40–60 dB on marginal paths.
- On the NR2 tab, if speech sounds hollow or "underwater", lower **Reduction Depth:** toward 0.80–1.00 or switch **Gain Method** from Gamma to Log.
- Use **Reset Defaults** on the NR2 or NR4 tab to recover a known-good starting point after experimental changes.

## Troubleshooting

- **Speech sounds hollow or musical artefacts are audible on NR2** — Reduce **Reduction Depth:** or confirm **AE Filter (artifact elimination)** is enabled.
- **NR4 is not reducing noise enough** — Increase **Reduction (dB):** and enable **Adaptive Noise Estimation** if it is off.
- **DFNR removes weak signals along with the noise** — Lower **Attenuation Limit** from 100 toward 40–60 dB.
- **MNR tab is present but has no effect** — MNR is macOS-only. On Linux or Windows, use NR2, NR4, or DFNR instead.
- **NR2 or NR4 settings did not persist after restart** — Settings are saved automatically on each control change. If values revert, click **Reset Defaults** and re-enter the desired values to force a save.

## Related

- [AetherDSP Settings overview](../../features/aether-dsp/overview.md)
- [Tune NR2 reduction depth and voice threshold](../../features/aether-dsp/tune-nr2-reduction-depth-and-voice-threshold.md)
- [Switch NR2 gain method between Linear, Log, Gamma and Trained](../../features/aether-dsp/switch-nr2-gain-method-between-linear-log-gamma-and-trained.md)
- [Change NR2 noise power estimator (OSMS/MMSE/NSTAT)](../../features/aether-dsp/change-nr2-noise-power-estimator-osms-mmse-nstat.md)
- [Adjust NR4 reduction amount in dB](../../features/aether-dsp/adjust-
