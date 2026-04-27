# Set DeepFilterNet3 Attenuation Limit for Strong or Weak Signals

`DfnrAttenLimit` controls how aggressively DeepFilterNet3 suppresses noise. Lowering it preserves more of the original signal on strong signals; raising it maximizes noise removal on weak or noisy signals.

## Before you start

- AetherSDR must be running. A radio connection is not required to adjust DSP settings.
- DeepFilterNet3 (DFNR) must be selected as your active noise reduction engine.

## Steps

1. Click `Settings > AetherDSP Settings...`.
2. Click the **DFNR** tab.
3. Drag the **Attenuation Limit** slider to the desired value (0–100 dB).
4. Close the dialog. The setting takes effect immediately.

## What each control does

| Control | Default | Valid range | Setting key | Behavior |
|---|---|---|---|---|
| **Attenuation Limit** | 100 | 0–100 dB | `DfnrAttenLimit` | Sets the maximum noise attenuation applied by DeepFilterNet3. At 0 the engine passes audio through unmodified; at 100 it applies full attenuation. |
| **Post-Filter Beta** | 0.00 | 0.00–0.30 | `DfnrPostFilterBeta` | Applies an additional post-filter on top of the attenuation limit for extra suppression. |

## Tips

- For strong, clean signals where preserving fidelity matters, reduce **Attenuation Limit** toward 0 to limit how much the engine can alter the audio.
- For weak or heavily noise-degraded signals, set **Attenuation Limit** to 100 and combine with a non-zero **Post-Filter Beta** for the most aggressive suppression.

## Troubleshooting

- **Audio sounds unaffected after moving the slider** — Confirm you are on the **DFNR** tab and that DeepFilterNet3 is the active noise reduction engine. Other engines (NR2, NR4, MNR) have separate controls and are not affected by `DfnrAttenLimit`.

## Related

- [Configure DFNR post-filter beta for extra suppression](configure-dfnr-post-filter-beta-for-extra-suppression.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
- [AetherDSP Settings overview](overview.md)
