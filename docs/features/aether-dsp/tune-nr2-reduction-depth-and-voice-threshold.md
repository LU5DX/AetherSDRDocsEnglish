# Tune NR2 Reduction Depth and Voice Threshold

This page explains how to adjust NR2's maximum noise reduction depth and speech-presence threshold in AetherSDR. Changing these two sliders lets you balance how aggressively NR2 suppresses noise against how faithfully it preserves speech.

## Before you start

- AetherSDR must be running. A radio connection is not required to change these settings.
- NR2 must already be active on a receiver slice for changes to take audible effect immediately.

## Steps

1. Click `Settings > AetherDSP Settings...`.
2. In the AetherDSP Settings dialog, click the **NR2** tab.
3. Locate the **Reduction Depth:** slider. Drag it left to reduce suppression or right to increase it. The current value is shown to the right of the slider (default: `1.50`).
4. Locate the **Voice Threshold:** slider. Drag it left to make speech detection more sensitive (preserves quiet speech) or right to raise the threshold (passes less noise during pauses). The current value is shown to the right of the slider (default: `0.20`).
5. Changes take effect immediately and are saved automatically.

To restore both sliders to their defaults along with all other NR2 parameters, click **Reset Defaults** at the bottom right of the NR2 tab.

## What each control does

| Control | Default | Valid Range | Persisted Key | Behavior |
|---|---|---|---|---|
| **Reduction Depth:** | `1.50` | `0.50`–`2.00` | `NR2GainMax` | Sets the maximum depth of NR2 noise reduction. Higher values suppress more noise; values above `1.50` risk distorting speech. |
| **Voice Threshold:** | `0.20` | `0.05`–`0.50` | `NR2Qspp` | Sets the speech-presence-probability threshold. Lower values treat more signal as speech and preserve it; higher values treat more signal as noise and suppress it. |
| **Smoothing:** | `0.85` | `0.50`–`0.98` | `NR2GainSmooth` | Controls how quickly the noise estimate tracks changes. Higher values give a steadier estimate but slower adaptation to changing noise. |
| **AE Filter (artifact elimination)** | On | On / Off | `NR2AeFilter` | Toggles the anti-artifact post-filter that reduces musical noise and ringing. |
| **Gain Method** | Gamma | Linear / Log / Gamma / Trained | `NR2GainMethod` | Selects the gain-curve mapping used when computing suppression. |
| **NPE Method** | OSMS | OSMS / MMSE / NSTAT | `NR2NpeMethod` | Selects the noise power estimator. |
| **Reset Defaults** | — | — | — | Restores all NR2 tab parameters to defaults: Gamma, OSMS, AE on, `1.50`, `0.85`, `0.20`. |

## Tips

- For SSB voice operation, start with **Reduction Depth:** at `1.50` and **Voice Threshold:** at `0.20`. If speech sounds clipped or hollow, lower **Reduction Depth:** toward `1.00`.
- Lowering **Voice Threshold:** below `0.15` can cause residual noise to break through during speech pauses because more of the signal is classified as speech. Raise it if you notice this.
- If the noise estimate reacts too slowly to burst noise, lower **Smoothing:** toward `0.60`. If the noise gate sounds choppy, raise it toward `0.95`.
- Leaving **AE Filter (artifact elimination)** enabled is recommended for most conditions; disable it only if you notice the post-filter itself introducing artifacts.

## Troubleshooting

- **Speech sounds hollow or over-processed** — **Reduction Depth:** is too high or **Voice Threshold:** is too high. Lower **Reduction Depth:** and/or lower **Voice Threshold:** so more speech components are preserved.
- **Noise is still audible during speech pauses** — **Voice Threshold:** is too low, causing pauses to be classified as speech. Raise **Voice Threshold:** toward `0.30`–`0.40`.
- **Noise estimate reacts sluggishly or the noise floor sounds unstable** — Adjust **Smoothing:** (see Tips above). Also verify the selected **NPE Method** suits your noise type; NSTAT adapts better to non-stationary noise.

## Related

- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Switch NR2 gain method between Linear, Log, Gamma and Trained](switch-nr2-gain-method-between-linear-log-gamma-and-trained.md)
- [Change NR2 noise power estimator (OSMS/MMSE/NSTAT)](change-nr2-noise-power-estimator-osms-mmse-nstat.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
