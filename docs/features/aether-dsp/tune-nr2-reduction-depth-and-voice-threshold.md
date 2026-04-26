# Tune NR2 Reduction Depth and Voice Threshold

Adjust how aggressively NR2 suppresses noise and how sensitively it detects speech. These two controls — **Reduction Depth:** and **Voice Threshold:** — set the core tradeoff between noise suppression and speech preservation.

## Before you start

- AetherSDR must be running. A radio connection is not required to adjust these settings.
- NR2 must be enabled on the slice you want to affect. These controls tune the engine parameters; they do not activate NR2 itself.

## Steps

1. Open `Settings > AetherDSP Settings...`.
2. Click the **NR2** tab.
3. Drag the **Reduction Depth:** slider to set how much noise NR2 can remove. Higher values suppress more noise; lower values preserve more natural sound at the cost of less reduction.
4. Drag the **Voice Threshold:** slider to set the speech-presence-probability threshold. Lower values cause NR2 to treat quieter signals as speech and apply less reduction to them; higher values require a stronger signal before NR2 backs off.
5. Changes take effect immediately. No confirmation step is needed.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| **Reduction Depth:** | 1.50 | 0.50 – 2.00 | `NR2GainMax` | Sets the maximum NR2 reduction depth. Lower values produce gentler reduction; higher values produce deeper noise suppression at greater risk of speech distortion. |
| **Voice Threshold:** | 0.20 | 0.05 – 0.50 | `NR2Qspp` | Sets the speech-presence-probability threshold. Lower values preserve quiet speech but may let more noise through; higher values suppress more noise but may clip low-level speech. |
| **Smoothing:** | 0.85 | 0.50 – 0.98 | `NR2GainSmooth` | Controls how quickly the noise estimate tracks changes. Higher values give a steadier but slower-reacting estimate. |
| **AE Filter (artifact elimination)** | On | On / Off | `NR2AeFilter` | Toggles the anti-artifact post-filter that reduces musical noise typical of frequency-domain NR. |
| **Gain Method** | Gamma | Linear / Log / Gamma / Trained | `NR2GainMethod` | Selects the gain-curve mapping used by NR2. |
| **NPE Method** | OSMS | OSMS / MMSE / NSTAT | `NR2NpeMethod` | Selects the noise power estimator. |
| **Reset Defaults** | — | — | — | Restores all NR2 tab values to their defaults: Gamma, OSMS, AE on, 1.50, 0.85, 0.20. |

## Tips

- Start with **Reduction Depth:** at the default of 1.50 and increase it only if noise remains clearly audible after enabling NR2.
- If speech sounds hollow or distorted after increasing **Reduction Depth:**, lower **Voice Threshold:** slightly so NR2 more readily identifies speech segments and backs off reduction.
- If you hear musical-noise artifacts (a warbling or bubbling quality in the residual noise), verify that **AE Filter (artifact elimination)** is checked.
- Click **Reset Defaults** to return the entire NR2 tab to its factory values if the settings become difficult to reason about.

## Troubleshooting

- **Noise is barely reduced even at maximum Reduction Depth:** — The NPE Method may be losing track of the noise floor. Try switching **NPE Method** to MMSE or NSTAT, or enable a slower-varying noise scenario by increasing **Smoothing:**.
- **Speech sounds clipped or over-processed** — **Reduction Depth:** is likely too high or **Voice Threshold:** is too high, causing speech frames to be treated as noise. Lower **Reduction Depth:** and reduce **Voice Threshold:** toward 0.05.
- **Settings revert after restart** — This should not occur as values are persisted immediately on change. If it does, check whether AetherSDR has write access to its settings storage location.

## Related

- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Switch NR2 gain method between Linear, Log, Gamma and Trained](switch-nr2-gain-method-between-linear-log-gamma-and-trained.md)
- [Change NR2 noise power estimator (OSMS/MMSE/NSTAT)](change-nr2-noise-power-estimator-osms-mmse-nstat.md)
- [Adjust NR4 reduction amount in dB](adjust-nr4-reduction-amount-in-db.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
