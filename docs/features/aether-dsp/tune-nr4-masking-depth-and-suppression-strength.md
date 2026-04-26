# Tune NR4 masking depth and suppression strength

The NR4 tab in AetherDSP Settings exposes two controls that determine how aggressively NR4 (libspecbleach) shapes the residual noise floor after its main reduction stage: `NR4MaskingDepth` and `NR4SuppressionStrength`. Adjust these when you want finer control over the balance between noise suppression and audio naturalness.

## Before you start

- AetherSDR must be running. A radio connection is not required to change these settings.
- Open `Settings > AetherDSP Settings...` to reach the dialog.

## Steps

1. Click `Settings > AetherDSP Settings...`.
2. Click the **NR4** tab.
3. Move the **Masking Depth:** slider to the desired value between 0.00 and 1.00. The default is 0.50.
4. Move the **Suppression:** slider to the desired value between 0.00 and 1.00. The default is 0.50.
5. Close the dialog. Settings are saved immediately when each slider moves.

## What each control does

| Control | Default | Valid range | Setting key | Behavior |
|---|---|---|---|---|
| **Masking Depth:** | 0.50 | 0.00–1.00 | `NR4MaskingDepth` | Controls spectral-masking depth. Higher values apply deeper masking to noise components below the estimated noise floor. |
| **Suppression:** | 0.50 | 0.00–1.00 | `NR4SuppressionStrength` | Sets the overall NR4 suppression strength. Higher values reduce more noise; lower values preserve more of the original signal character. |

## Tips

- To return both controls to their defaults (0.50 and 0.50), click **Reset Defaults** at the bottom right of the NR4 tab. This also resets all other NR4 parameters to their defaults (SPP-MMSE, adaptive on, 10.0 dB reduction, 0% smoothing, 0% whitening).
- If the signal sounds over-processed or thin, reduce **Suppression:** first, then **Masking Depth:** if needed.
- These controls act on the output of the main reduction stage. Set **Reduction (dB):** to a reasonable value before fine-tuning masking and suppression. See [Adjust NR4 reduction amount in dB](adjust-nr4-reduction-amount-in-db.md).

## Troubleshooting

- **Sliders have no audible effect** — confirm that NR4 is the active noise-reduction engine for the receiver. AetherDSP engines are selected per-receiver from the panadapter overlay, not from this dialog.
- **Reset Defaults changes more than just these two sliders** — this is expected. **Reset Defaults** on the NR4 tab restores all NR4 parameters simultaneously.

## Related

- [Adjust NR4 reduction amount in dB](adjust-nr4-reduction-amount-in-db.md)
- [Enable or disable NR4 adaptive noise estimation](enable-or-disable-nr4-adaptive-noise-estimation.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
