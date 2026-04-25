# Choosing the right noise reduction: NR2, NR4, DFNR, MNR

AetherSDR provides four client-side noise-reduction engines — NR2, NR4, DFNR, and MNR — each suited to different signal conditions and noise types. This page explains what each engine does and how to decide which one to use, then shows you where to configure it.

## Before you start

- No radio connection is required to open or adjust AetherDSP Settings.
- MNR is available on macOS only.
- DFNR uses DeepFilterNet3; confirm your system meets any CPU requirements before enabling it at high attenuation.

## Steps

1. Open `Settings > AetherDSP Settings...`.
2. Click the tab for the engine you want to use: **NR2**, **NR4**, **MNR**, or **DFNR**.
3. Adjust the controls for that engine (see the table below).
4. To return any engine to factory settings, click **Reset Defaults** at the bottom of its tab (available on NR2 and NR4).

## What each control does

### NR2 tab

NR2 is a frequency-domain musical-noise-reduction engine. Use it when you want fine control over how aggressively noise is suppressed relative to speech fidelity.

| Control | Kind | Default | Valid range | Setting key |
|---|---|---|---|---|
| Gain Method | Radio button | Gamma | Linear \| Log \| Gamma \| Trained | `NR2GainMethod` |
| NPE Method | Radio button | OSMS | OSMS \| MMSE \| NSTAT | `NR2NpeMethod` |
| AE Filter (artifact elimination) | Checkbox | On | — | `NR2AeFilter` |
| Reduction Depth: | Slider | 1.50 | 0.50–2.00 | `NR2GainMax` |
| Smoothing: | Slider | 0.85 | 0.50–0.98 | `NR2GainSmooth` |
| Voice Threshold: | Slider | 0.20 | 0.05–0.50 | `NR2Qspp` |

**Gain Method** selects the gain-curve mapping applied to each frequency bin. Gamma matches typical speech amplitude patterns and is the default. Trained uses a model built from real speech and noise samples, which can perform better on recognizable noise types. Linear and Log offer progressively simpler mappings.

**NPE Method** selects how NR2 estimates the noise floor. OSMS tracks the floor using a running minimum and works well with stationary noise. MMSE minimizes expected estimation error. NSTAT adapts to noise that changes over time.

**AE Filter (artifact elimination)** applies a post-filter that reduces ringing and musical noise artifacts. Leave this on unless you are testing the raw NR2 output.

**Reduction Depth:** sets how much NR2 can attenuate noise. Higher values suppress more noise but increase the risk of speech distortion.

**Smoothing:** controls how quickly the noise estimate reacts to changes. Higher values are steadier but slower to adapt.

**Voice Threshold:** sets the speech-presence-probability threshold below which a bin is treated as noise. Lower values preserve quiet speech but may let more noise through.

---

### NR4 tab

NR4 uses the libspecbleach library. It exposes separate controls for the noise estimation method, adaptive tracking, and spectral shaping. Use NR4 when you want explicit dB-calibrated reduction and control over residual noise colour.

| Control | Kind | Default | Valid range | Setting key |
|---|---|---|---|---|
| Noise Estimation Method | Radio button | SPP-MMSE | SPP-MMSE \| Brandt \| Martin | `NR4NoiseEstimationMethod` |
| Adaptive Noise Estimation | Checkbox | On | — | `NR4AdaptiveNoise` |
| Reduction (dB): | Slider | 10.0 dB | 0.0–40.0 dB | `NR4ReductionAmount` |
| Smoothing (%): | Slider | 0 | 0–100 | `NR4SmoothingFactor` |
| Whitening (%): | Slider | 0 | 0–100 | `NR4WhiteningFactor` |
| Masking Depth: | Slider | 0.50 | 0.00–1.00 | `NR4MaskingDepth` |
| Suppression: | Slider | 0.50 | 0.00–1.00 | `NR4SuppressionStrength` |

**Noise Estimation Method** selects the noise-floor estimator. SPP-MMSE balances noise estimation with speech preservation. Brandt uses recursive smoothing across critical frequency bands and handles non-stationary noise well. Martin tracks running spectral minima and is robust for slowly varying noise floors.

**Adaptive Noise Estimation** enables continuous re-estimation of the noise floor. Disable it only if the noise floor is stable and you want to lock in an initial estimate.

**Reduction (dB):** sets the maximum attenuation NR4 will apply. 10 dB is a conservative starting point; increase toward 40 dB for heavy noise, accepting more processing.

**Smoothing (%):** applies time-domain smoothing to the noise estimate. 0 means no additional smoothing beyond what the estimation method provides.

**Whitening (%):** flattens the spectral shape of residual noise. Higher values make leftover noise sound more uniform rather than tonal.

**Masking Depth:** controls how deeply spectral masking is applied to noise bins.

**Suppression:** sets the overall NR4 suppression strength across the spectrum.

---

### DFNR tab

DFNR runs DeepFilterNet3, a neural-network-based suppressor. It requires more CPU than NR2 or NR4 but can handle complex, non-stationary noise effectively. Use DFNR when the other engines leave audible structured noise.

| Control | Kind | Default | Valid range | Setting key |
|---|---|---|---|---|
| Attenuation Limit | Slider | 100 | 0–100 dB | `DfnrAttenLimit` |
| Post-Filter Beta | Slider | 0.00 | 0.00–0.30 | `DfnrPostFilterBeta` |

**Attenuation Limit** sets the maximum noise attenuation DeepFilterNet3 will apply. 0 is passthrough; 100 is maximum. Reduce this value if you hear over-processed or hollow-sounding audio.

**Post-Filter Beta** applies an additional post-filter on top of the neural network output for extra suppression. 0.00 disables the post-filter. Increase cautiously; higher values can introduce artifacts.

---

### MNR tab (macOS only)

MNR is an MMSE-Wiener noise reducer with asymmetric gain smoothing. It is only functional on macOS.

| Control | Kind | Default | Valid range | Setting key |
|---|---|---|---|---|
| Enable MNR (macOS only) | Checkbox | (read from audio engine) | — | `MnrEnabled` |
| Strength | Slider | 100 | 0–100 | `MnrStrength` |

**Enable MNR (macOS only)** turns the engine on or off. Its initial state reflects the current audio engine status.

**Strength** adjusts aggressiveness. 0 is mild; 100 is maximum suppression. `MnrStrength` is persisted as a normalized value between 0.00 and 1.00.

---

## Tips

- Start with NR2 at default settings (Gamma / OSMS / AE on / Reduction Depth 1.50) for typical SSB voice work. It preserves speech naturalness better than a flat dB cut.
- If the noise floor changes during a contact (QSB, band openings), enable **Adaptive Noise Estimation** in NR4 or switch **NPE Method** in NR2 to NSTAT.
- Use **Whitening (%)** in NR4 to reduce tonal or "fizzy" residual noise without increasing overall reduction.
- Set DFNR **Attenuation Limit** to a lower value (40–60) before experimenting upward; at 100 it applies maximum neural suppression, which can make weak signals sound processed.
- On macOS, you can stack MNR with NR2 or NR4 if needed, but start with one engine at a time to hear what each contributes.
- Click **Reset Defaults** on the NR2 or NR4 tab at any time to return to the factory values shown in the tables above.

## Troubleshooting

- **Speech sounds hollow or robotic** — Reduction is too high. On NR2, lower **Reduction Depth:** below 1.50. On NR4, reduce **Reduction (dB):** or lower **Suppression:**. On DFNR, reduce **Attenuation Limit**.
- **Musical noise or ringing remains after NR2** — Confirm **AE Filter (artifact elimination)** is checked.
- **MNR controls are grayed out** — MNR is macOS only. On Linux or Windows the tab is present but the engine is not available.
- **DFNR has no effect** — Check that **Attenuation Limit** is above 0. A value of 0 is passthrough.
- **NR4 noise estimate drifts on a quiet band** — Uncheck **Adaptive Noise Estimation** to lock the estimate, or switch **Noise Estimation Method** to Martin, which is designed for slowly varying floors.

## Related

- [AetherDSP Settings overview](../../features/aether-dsp/overview.md)
- [Tune NR2 reduction depth and voice threshold](../../features/aether-dsp/tune-nr2-reduction-depth-and-voice-threshold.md)
- [Switch NR2 gain method between Linear, Log, Gamma and Trained](../../features/aether-dsp/switch-nr2-gain-method-between-linear-log-gamma-and-trained.md)
- [Change NR
