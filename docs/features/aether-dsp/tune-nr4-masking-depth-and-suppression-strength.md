# Tune NR4 masking depth and suppression strength

The NR4 tab in AetherDSP Settings exposes two controls — `NR4MaskingDepth` and `NR4SuppressionStrength` — that together govern how aggressively NR4 (libspecbleach) attenuates noise between speech syllables. Adjusting these lets you trade residual noise against speech naturalness.

## Before you start

- AetherSDR must be running. No radio connection is required to change these settings.
- NR4 must be the active noise-reduction engine on the slice you are listening to. If you have not yet enabled NR4, the sliders take effect as soon as you do.

## Steps

1. Open `Settings > AetherDSP Settings...`.
2. Click the **NR4** tab.
3. Locate the **Masking Depth:** slider. Drag it left or right to set spectral-masking depth (range 0.00–1.00, default 0.50). The current value is shown to the right of the slider.
4. Locate the **Suppression:** slider. Drag it left or right to set overall suppression strength (range 0.00–1.00, default 0.50). The current value is shown to the right of the slider.
5. Monitor the audio in real time. Adjust until residual noise is acceptably low without audible speech degradation.
6. Close the dialog. Values are saved immediately when each slider moves; no separate Save action is needed.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| **Masking Depth:** | 0.50 | 0.00–1.00 | `NR4MaskingDepth` | Controls how deeply spectral masking suppresses bins estimated to contain noise. Higher values increase masking at the risk of muffling weak signals. |
| **Suppression:** | 0.50 | 0.00–1.00 | `NR4SuppressionStrength` | Sets the overall NR4 suppression strength. Higher values remove more noise; very high values may introduce processing artifacts. |

## Tips

- These two controls interact: a high **Suppression:** value with a low **Masking Depth:** tends to produce a drier, flatter residual, whereas matching both at moderate levels (around 0.50) generally preserves the most natural speech character.
- If you want to return to a known-good baseline, click **Reset Defaults** on the NR4 tab. This restores **Masking Depth:** to 0.50 and **Suppression:** to 0.50, along with all other NR4 parameters.
- Changes take effect immediately without restarting AetherSDR or reconnecting to the radio.

## Troubleshooting

- **Increasing Suppression: makes voices sound hollow or phasey** — reduce **Suppression:** toward 0.30–0.40 and verify that **Adaptive Noise Estimation** is enabled so the noise floor estimate stays current. See [Enable or disable NR4 adaptive noise estimation](enable-or-disable-nr4-adaptive-noise-estimation.md).
- **Sliders have no audible effect** — NR4 may not be the active noise-reduction engine on the current slice, or the overall **Reduction (dB):** amount may be set to 0.0. See [Adjust NR4 reduction amount in dB](adjust-nr4-reduction-amount-in-db.md).

## Related

- [Adjust NR4 reduction amount in dB](adjust-nr4-reduction-amount-in-db.md)
- [Enable or disable NR4 adaptive noise estimation](enable-or-disable-nr4-adaptive-noise-estimation.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
