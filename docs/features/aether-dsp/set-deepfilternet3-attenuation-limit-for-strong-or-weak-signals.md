# Set DeepFilterNet3 Attenuation Limit for Strong or Weak Signals

The `DfnrAttenLimit` setting caps how much noise DeepFilterNet3 is allowed to suppress. Lowering the limit preserves more signal character on strong, clean signals; raising it gives maximum noise removal on weak or noisy signals.

## Before you start

- AetherSDR must be running. A radio connection is not required to change this setting.
- DeepFilterNet3 (DFNR) must already be selected as your active noise reduction engine. See [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md) if you have not done this yet.

## Steps

1. Click `Settings > AetherDSP Settings...`.
2. In the AetherDSP Settings dialog, click the **DFNR** tab.
3. Drag the **Attenuation Limit** slider to the desired value.
4. Close the dialog. The value is saved immediately.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Attenuation Limit | 100 | 0–100 dB | `DfnrAttenLimit` | Sets the maximum noise attenuation DeepFilterNet3 may apply. 0 is passthrough (no attenuation); 100 is maximum attenuation. |
| Post-Filter Beta | 0.00 | 0.00–0.30 | `DfnrPostFilterBeta` | Applies an additional post-filter on top of DFNR for extra suppression. |

## Tips

- For strong signals where you want to preserve natural audio character, set **Attenuation Limit** to a lower value such as 20–40 dB.
- For weak or heavily noise-affected signals, leave **Attenuation Limit** at 100 to allow full suppression.
- Setting **Attenuation Limit** to 0 effectively bypasses DeepFilterNet3 without disabling the engine.

## Related

- [Configure DFNR post-filter beta for extra suppression](configure-dfnr-post-filter-beta-for-extra-suppression.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
- [AetherDSP Settings overview](overview.md)
