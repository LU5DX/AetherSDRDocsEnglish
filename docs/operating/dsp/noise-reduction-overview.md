# Choosing the right noise reduction: NR2, NR4, DFNR, MNR

AetherSDR provides four client-side noise reduction engines. This page explains what each engine does, when to use it, and where to find its controls.

## Before you start

- Open AetherDSP Settings via `Settings > AetherDSP Settings...`.
- Noise reduction engines are selected and activated separately from this dialog — the dialog only configures their parameters. Consult your slice receiver controls to enable a specific NR engine.

## Steps

1. Open `Settings > AetherDSP Settings...`.
2. Click the tab for the engine you want to configure: `NR2 (tab)`, `NR4 (tab)`, `MNR (tab)`, or `DFNR (tab)`.
3. Adjust parameters as described below.
4. Changes take effect immediately. No Apply or OK button is required.
5. To restore an engine to its factory state, click `Reset Defaults` on its tab.

## What each control does

### NR2

Spectral-domain musical-noise reduction. Use NR2 for SSB voice on moderate to heavy noise floors where preserving speech naturalness matters. Its `Voice Threshold:` control lets you protect quiet speech from being suppressed.

| Control | Default | Valid range | Setting key |
|---|---|---|---|
| Gain Method | Gamma | Linear / Log / Gamma / Trained | `NR2GainMethod` |
| NPE Method | OSMS | OSMS / MMSE / NSTAT | `NR2NpeMethod` |
| AE Filter (artifact elimination) | True (on) | on / off | `NR2AeFilter` |
| Reduction Depth: | 1.50 | 0.50–2.00 | `NR2GainMax` |
| Smoothing: | 0.85 | 0.50–0.98 | `NR2GainSmooth` |
| Voice Threshold: | 0.20 | 0.05–0.50 | `NR2Qspp` |

**Gain Method** selects how the gain curve is computed. Gamma matches typical speech amplitude patterns and is the recommended starting point. Trained uses a model trained on real speech and noise samples. Linear and Log are simpler mappings.

**NPE Method** selects the noise power estimator. OSMS tracks the noise floor using a running minimum estimate. MMSE minimises expected estimation error. NSTAT adapts to noise that changes over time.

**AE Filter (artifact elimination)** applies a post-filter that reduces ringing and musical artifacts common in frequency-domain NR. Leave it on unless you need to compare raw NR output.

**Reduction Depth:** sets the maximum suppression depth. Higher values remove more noise but risk distorting speech.

**Smoothing:** controls how quickly the noise estimate adapts. Higher values give a steadier estimate but slower response to changing noise.

**Voice Threshold:** sets the speech-presence-probability threshold. Lower values preserve quiet speech but may pass more noise.

---

### NR4

Libspecbleach-based reduction. Use NR4 when you want explicit dB-calibrated control over how much noise is removed, or when the noise floor is relatively stationary and you want to dial in whitening of residual noise.

| Control | Default | Valid range | Setting key |
|---|---|---|---|
| Noise Estimation Method | SPP-MMSE | SPP-MMSE / Brandt / Martin | `NR4NoiseEstimationMethod` |
| Adaptive Noise Estimation | True (on) | on / off | `NR4AdaptiveNoise` |
| Reduction (dB): | 10.0 | 0.0–40.0 dB | `NR4ReductionAmount` |
| Smoothing (%): | 0 | 0–100 | `NR4SmoothingFactor` |
| Whitening (%): | 0 | 0–100 | `NR4WhiteningFactor` |
| Masking Depth: | 0.50 | 0.00–1.00 | `NR4MaskingDepth` |
| Suppression: | 0.50 | 0.00–1.00 | `NR4SuppressionStrength` |

**Noise Estimation Method** selects the noise floor estimator. SPP-MMSE balances noise estimation with speech preservation. Brandt uses recursive smoothing over critical bands and suits non-stationary noise. Martin uses running spectral minima and is robust for slowly varying noise floors.

**Adaptive Noise Estimation** enables continuous re-estimation of the noise floor. Disable it if you want to lock the estimate taken at startup (useful on a very stable noise floor).

**Reduction (dB):** sets the maximum reduction depth in dB. 10 dB is a conservative starting point; values above 20 dB may introduce artifacts on voice.

**Smoothing (%):** applies time-domain smoothing to the noise estimate. 0 means no additional smoothing beyond the estimator's own behavior.

**Whitening (%):** flattens the spectral shape of residual noise. Increase this if you hear colored (tonal) residual noise after reduction.

**Masking Depth:** controls how aggressively spectral masking is applied.

**Suppression:** sets the overall suppression strength. Reduce this if NR4 sounds over-processed.

---

### MNR

MMSE-Wiener reduction with asymmetric gain smoothing. MNR is only active on macOS.

| Control | Default | Valid range | Setting key |
|---|---|---|---|
| Enable MNR (macOS only) | (read from audio engine) | on / off | `MnrEnabled` |
| Strength | 100 | 0–100 | `MnrStrength` |

**Enable MNR (macOS only)** activates the engine. The initial state reflects the current audio engine state.

**Strength** sets aggressiveness. 0 is mild; 100 is maximum suppression.

---

### DFNR

DeepFilterNet3 deep-learning noise reduction. Use DFNR for the highest suppression quality on voice modes, particularly when other engines leave residual noise or artifacts. DFNR requires more CPU than NR2 or NR4.

| Control | Default | Valid range | Setting key |
|---|---|---|---|
| Attenuation Limit | 100 | 0–100 dB | `DfnrAttenLimit` |
| Post-Filter Beta | 0.00 | 0.00–0.30 | `DfnrPostFilterBeta` |

**Attenuation Limit** caps the maximum noise attenuation. 0 is passthrough (no reduction); 100 is maximum. Lower this if DFNR suppresses too aggressively on weak signals.

**Post-Filter Beta** applies an additional post-filter on top of DeepFilterNet3's output for extra suppression. The default 0.00 disables it. Increase cautiously — high values can degrade speech quality.

---

### RN2 and BNR

The `RN2 (tab)` (RNNoise) and `BNR (tab)` (NVIDIA) tabs have no adjustable parameters in this dialog. RN2 has no controls. BNR intensity is controlled from the overlay menu.

## Tips

- Start with NR2 at its defaults (Gamma, OSMS, AE on, Reduction Depth 1.50) before reaching for DFNR. NR2 is lighter on CPU and works well on typical SSB noise.
- If NR2 leaves a residual musical tone, try switching `NPE Method` from OSMS to NSTAT, or enabling NR4 with a low `Whitening (%)` value.
- On macOS, MNR and DFNR can run alongside each other or alongside NR2/NR4; check CPU load before stacking multiple engines.
- DFNR `Attenuation Limit` at 100 can sound unnatural on CW or digital modes. Set it to 0 (passthrough) on those modes.
- Click `Reset Defaults` on any tab to return all parameters for that engine to factory values without affecting other engines.

## Troubleshooting

- **Voice sounds muffled or robotic after enabling NR2** — `Reduction Depth:` is set too high. Reduce it below 1.50, or lower `Voice Threshold:` to better protect speech.
- **NR4 appears to have no effect** — Check that `Reduction (dB):` is above 0.0 and `Suppression:` is above 0.00. Both default to values that produce audible reduction, but they may have been changed.
- **MNR tab controls are grayed out or missing** — MNR is only available on macOS. On Linux and Windows the tab is present but the engine is inactive.
- **DFNR produces no output** — `Attenuation Limit` set to 0 is passthrough. Increase it above 0.

## Related

- [AetherDSP Settings overview](../../features/aether-dsp/overview.md)
- [Tune NR2 reduction depth and voice threshold](../../features/aether-dsp/tune-nr2-reduction-depth-and-voice-threshold.md)
- [Switch NR2 gain method between Linear, Log, Gamma and Trained](../../features/aether-dsp/switch-nr2-gain-method-between-linear-log-gamma-and-trained.md)
- [Change NR2 noise power estimator (OSMS/MMSE/NSTAT)](../../features/aether-dsp/change-nr2-noise-power-estimator-osms-mmse-nstat.md)
- [Adjust NR4 reduction amount in dB](../../features/aether-dsp/adjust-nr4-reduction-amount-in-db.md)
- [Enable or disable NR4 adaptive noise estimation](../../features/aether-dsp/enable-or-disable-nr4-adaptive-noise-estimation.md)
- [Tune NR4 masking depth and suppression strength](../../features/aether-dsp/tune-nr4-masking-depth-and-suppression
