# Adjust NR4 reduction amount in dB

The `NR4ReductionAmount` setting controls how aggressively the NR4 (libspecbleach) engine attenuates noise. Raising it removes more noise; lowering it preserves more of the original signal character.

## Before you start

- AetherSDR must be running. A radio connection is not required to change this setting.
- Open the NR4 tab in AetherDSP Settings (see Steps below).

## Steps

1. Go to `Settings > AetherDSP Settings...`.
2. Click the **NR4 (tab)** tab.
3. Locate the **Reduction (dB):** slider.
4. Drag the slider left to reduce noise suppression or right to increase it. The current value in dB is displayed to the right of the slider.
5. Close the dialog. The value is saved immediately when you move the slider.

## What each control does

| Control | Default | Valid range | Persisted key |
|---|---|---|---|
| **Reduction (dB):** | 10.0 dB | 0.0–40.0 dB | `NR4ReductionAmount` |

**Reduction (dB):** Sets the maximum noise reduction applied by the NR4 engine, in decibels. At 0.0 dB, NR4 applies no attenuation. At 40.0 dB, it applies maximum suppression. Values between 10–20 dB work well for moderate band noise without audible speech artefacts.

## Tips

- If you hear the noise floor being removed but speech sounds hollow or watery, lower **Reduction (dB):** by 5–10 dB.
- **Reduction (dB):** interacts with **Suppression:** and **Masking Depth:** — see [Tune NR4 masking depth and suppression strength](tune-nr4-masking-depth-and-suppression-strength.md) for guidance on combining these controls.
- To return **Reduction (dB):** and all other NR4 parameters to factory values (10.0 dB), click **Reset Defaults** at the bottom of the NR4 tab — see [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md).
- Enabling **Adaptive Noise Estimation** lets NR4 continuously re-estimate the noise floor, which can make the reduction feel more consistent as band conditions change — see [Enable or disable NR4 adaptive noise estimation](enable-or-disable-nr4-adaptive-noise-estimation.md).

## Troubleshooting

- **Moving the slider has no audible effect** — confirm NR4 is the active noise reduction engine. Other engines (NR2, DFNR, MNR) have separate controls and do not share this setting.
- **Speech sounds distorted even at low values** — check that **Suppression:** (`NR4SuppressionStrength`) is not set near 1.00, as the two controls compound each other.

## Related

- [Enable or disable NR4 adaptive noise estimation](enable-or-disable-nr4-adaptive-noise-estimation.md)
- [Tune NR4 masking depth and suppression strength](tune-nr4-masking-depth-and-suppression-strength.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
