# Tune NR2 Reduction Depth and Voice Threshold

Adjust how aggressively NR2 suppresses noise and how sensitively it detects speech. These two controls set the tradeoff between maximum noise removal and preserving quiet voice passages.

## Before you start

- AetherSDR does not need to be connected to a radio to change these settings.
- NR2 must be active on your slice for changes to take audible effect.

## Steps

1. Click `Settings > AetherDSP Settings...` to open the AetherDSP Settings dialog.
2. Click the **NR2** tab.
3. Locate the **Reduction Depth:** slider. Drag it left to reduce suppression or right to increase it. The default is **1.50**; the valid range is **0.50–2.00**.
4. Locate the **Voice Threshold:** slider. Drag it left to detect quieter speech (more noise may pass) or right to raise the threshold (stronger suppression between speech bursts). The default is **0.20**; the valid range is **0.05–0.50**.
5. Listen to the received audio and fine-tune both sliders until the balance between noise suppression and speech clarity is acceptable.
6. To undo all changes on this tab, click **Reset Defaults**. This restores Reduction Depth to **1.50** and Voice Threshold to **0.20**, along with all other NR2 defaults.

## What each control does

| Control | Default | Valid range | Persisted setting |
|---|---|---|---|
| **Reduction Depth:** slider | 1.50 | 0.50–2.00 | `NR2GainMax` |
| **Smoothing:** slider | 0.85 | 0.50–0.98 | `NR2GainSmooth` |
| **Voice Threshold:** slider | 0.20 | 0.05–0.50 | `NR2Qspp` |
| **AE Filter (artifact elimination)** checkbox | Enabled | — | `NR2AeFilter` |
| **Gain Method** radio buttons | Gamma | Linear \| Log \| Gamma \| Trained | `NR2GainMethod` |
| **NPE Method** radio buttons | OSMS | OSMS \| MMSE \| NSTAT | `NR2NpeMethod` |
| **Reset Defaults** button | — | — | — |

**Reduction Depth:** Sets the maximum gain reduction NR2 can apply. Higher values suppress more noise but increase the risk of speech distortion.

**Smoothing:** Controls how quickly the noise estimate follows changes in the noise floor. Higher values produce steadier but slower adaptation.

**Voice Threshold:** Sets the speech-presence-probability threshold. Lower values cause NR2 to treat more signal as speech and reduce suppression; higher values increase suppression during pauses.

**AE Filter (artifact elimination):** Applies a post-filter that reduces ringing and musical-noise artifacts. Leave this enabled unless you are comparing raw NR2 output.

## Tips

- On a quiet band with steady background noise, a **Reduction Depth:** of 1.50–2.00 and a **Voice Threshold:** of 0.15–0.25 works well for most SSB signals.
- If weak stations are being cut off at the start of syllables, lower **Voice Threshold:** toward 0.05 so NR2 opens up sooner.
- If musical noise (tonal artifacts) appears after increasing **Reduction Depth:**, verify that **AE Filter (artifact elimination)** is checked.
- Increasing **Smoothing:** can help on steady noise floors (RTTY interference, power-line hum) but slows NR2's reaction to rapidly changing noise.

## Troubleshooting

- **Slider changes have no audible effect** — NR2 may not be enabled on the active slice. Enable it from the slice controls, then return to this dialog.
- **Speech sounds distorted or robotic** — **Reduction Depth:** is set too high. Lower it toward 1.00–1.50 and confirm **AE Filter (artifact elimination)** is checked.
- **Noise breaks through between words** — **Voice Threshold:** may be too low. Raise it gradually toward 0.30–0.40 so NR2 applies stronger suppression during pauses.

## Related

- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
- [Switch NR2 gain method between Linear, Log, Gamma and Trained](switch-nr2-gain-method-between-linear-log-gamma-and-trained.md)
- [Change NR2 noise power estimator (OSMS/MMSE/NSTAT)](change-nr2-noise-power-estimator-osms-mmse-nstat.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Adjust NR4 reduction amount in dB](adjust-nr4-reduction-amount-in-db.md)
