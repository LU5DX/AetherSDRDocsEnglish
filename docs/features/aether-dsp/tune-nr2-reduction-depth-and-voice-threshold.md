# Tune NR2 Reduction Depth and Voice Threshold

Adjust how aggressively NR2 suppresses noise and how sensitively it detects speech. These two sliders control the tradeoff between noise removal and speech fidelity — useful when the default settings over-suppress quiet signals or leave too much noise.

## Before you start

- Open AetherSDR.
- NR2 must be active on the slice you are monitoring. These controls affect the NR2 engine parameters globally; they do not enable NR2 on a slice.

## Steps

1. Click `Settings > AetherDSP Settings...`.
2. Click the **NR2** tab.
3. Locate the **Reduction Depth:** slider. Drag it left to reduce suppression aggressiveness or right to increase it. The current value displays to the right of the slider.
4. Locate the **Voice Threshold:** slider. Drag it left to make speech detection more sensitive (preserves quieter speech, but may pass more noise) or right to raise the threshold (stricter speech detection).
5. Close the dialog. Changes take effect immediately.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| **Reduction Depth:** | 1.50 | 0.50–2.00 | `NR2GainMax` | Sets the maximum noise reduction depth. Higher values suppress more noise but increase the risk of speech distortion. |
| **Smoothing:** | 0.85 | 0.50–0.98 | `NR2GainSmooth` | Controls how smoothly the noise estimate tracks signal changes. Higher values give a steadier but slower-adapting estimate. |
| **Voice Threshold:** | 0.20 | 0.05–0.50 | `NR2Qspp` | Sets the speech-presence-probability threshold. Lower values preserve quiet speech; higher values apply reduction more aggressively during borderline signals. |
| **AE Filter (artifact elimination)** | Enabled | On / Off | `NR2AeFilter` | Applies an anti-artifact post-filter that reduces ringing and musical noise. Leave enabled unless testing. |
| **Gain Method** | Gamma | Linear / Log / Gamma / Trained | `NR2GainMethod` | Selects the gain-curve mapping used by NR2. See [Switch NR2 gain method between Linear, Log, Gamma and Trained](switch-nr2-gain-method-between-linear-log-gamma-and-trained.md). |
| **NPE Method** | OSMS | OSMS / MMSE / NSTAT | `NR2NpeMethod` | Selects the noise power estimator. See [Change NR2 noise power estimator (OSMS/MMSE/NSTAT)](change-nr2-noise-power-estimator-osms-mmse-nstat.md). |
| **Reset Defaults** | — | — | — | Restores all NR2 tab values to defaults: Gamma, OSMS, AE on, Reduction Depth 1.50, Smoothing 0.85, Voice Threshold 0.20. |

## Tips

- Start with **Reduction Depth:** at the default of 1.50. Move it toward 2.00 only on bands with heavy broadband noise; values above 1.80 can introduce audible artifacts on SSB speech.
- If NR2 cuts into the first syllable of a transmission, lower **Voice Threshold:** from 0.20 toward 0.05. The engine will then classify marginal signals as speech and hold back reduction sooner.
- If residual noise breaks through during pauses, raise **Voice Threshold:** toward 0.30–0.40. The engine will apply reduction more readily when speech is absent.
- Reducing **Smoothing:** below 0.70 makes the noise estimate react faster to changing noise floors but can cause pumping on SSB signals.
- Click **Reset Defaults** to return to the baseline before experimenting further.

## Troubleshooting

- **Speech sounds hollow or distorted** — **Reduction Depth:** is set too high. Lower it toward 1.00–1.50.
- **Noise returns during speech pauses but cuts abruptly when the station transmits** — **Voice Threshold:** is set too high. Lower it so the engine detects speech presence earlier.
- **NR2 reacts too slowly to a changing noise floor** — Lower **Smoothing:** to allow faster noise estimate adaptation.

## Related

- [Switch NR2 gain method between Linear, Log, Gamma and Trained](switch-nr2-gain-method-between-linear-log-gamma-and-trained.md)
- [Change NR2 noise power estimator (OSMS/MMSE/NSTAT)](change-nr2-noise-power-estimator-osms-mmse-nstat.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
