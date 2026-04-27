# Tune NR4 masking depth and suppression strength

The NR4 engine's **Masking Depth:** and **Suppression:** sliders give you fine-grained control over how aggressively spectral masking is applied and how strongly noise is suppressed overall. Adjust these two parameters together to balance noise reduction against speech clarity.

## Before you start

- Open AetherSDR and enable NR4 on the receiver you want to adjust.
- Have a signal or noise source active so you can hear the effect of changes in real time.

## Steps

1. Click `Settings > AetherDSP Settings...`.
2. Click the **NR4** tab.
3. Locate the **Masking Depth:** slider. Drag it left to reduce spectral masking or right to increase it. The default is **0.50**; the valid range is **0.00–1.00**.
4. Locate the **Suppression:** slider directly below. Drag it left to reduce overall suppression or right to increase it. The default is **0.50**; the valid range is **0.00–1.00**.
5. Listen to the result. If speech sounds over-processed or hollow, reduce one or both sliders. If residual noise is too audible, increase them.
6. To undo all NR4 changes at once, click **Reset Defaults**. This restores **Masking Depth:** to **0.50** and **Suppression:** to **0.50**, along with the other NR4 defaults.

## What each control does

| Control | Default | Range | Persisted key | Behavior |
|---|---|---|---|---|
| **Masking Depth:** | 0.50 | 0.00–1.00 | `NR4MaskingDepth` | Controls how deeply spectral masking is applied to noise bins. Higher values suppress more noise but can affect tonal quality. |
| **Suppression:** | 0.50 | 0.00–1.00 | `NR4SuppressionStrength` | Sets the overall NR4 suppression strength. Higher values produce more aggressive noise reduction across the spectrum. |

## Tips

- **Masking Depth:** and **Suppression:** interact: raising both together produces maximum noise reduction but the highest risk of speech distortion. Raise them incrementally and test on a live or recorded signal.
- If you also have **Reduction (dB):** set high, lowering **Suppression:** slightly can recover naturalness without losing much noise floor reduction.
- The **Adaptive Noise Estimation** checkbox affects how quickly NR4 tracks a changing noise floor, which in turn affects how both sliders sound in practice. See [Enable or disable NR4 adaptive noise estimation](enable-or-disable-nr4-adaptive-noise-estimation.md).
- Click **Reset Defaults** to return all NR4 parameters — not just these two sliders — to their factory values before experimenting again.

## Troubleshooting

- **Speech sounds hollow or underwater after raising the sliders** — Both sliders at high values can over-suppress spectral components that overlap with speech. Reduce **Masking Depth:** first, then **Suppression:** until naturalness returns.
- **Noise floor is still audible even at maximum settings** — Ensure **Adaptive Noise Estimation** is enabled so NR4 can continuously re-estimate the noise floor. Also consider increasing **Reduction (dB):** via [Adjust NR4 reduction amount in dB](adjust-nr4-reduction-amount-in-db.md).
- **Slider snaps back or refuses to move** — The sliders use a guarded input model. Click directly on the slider handle rather than clicking in the groove.

## Related

- [Adjust NR4 reduction amount in dB](adjust-nr4-reduction-amount-in-db.md)
- [Enable or disable NR4 adaptive noise estimation](enable-or-disable-nr4-adaptive-noise-estimation.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
