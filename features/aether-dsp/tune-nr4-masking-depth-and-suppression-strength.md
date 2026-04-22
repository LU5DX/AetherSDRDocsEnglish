# Tune NR4 masking depth and suppression strength

The **Masking Depth:** and **Suppression:** sliders in the NR4 tab control how aggressively AetherSDR's libspecbleach engine attenuates noise below the estimated noise floor. Adjusting these two parameters lets you trade between cleaner-sounding noise reduction and better preservation of weak or low-level speech detail.

## Before you start

- Open AetherSDR. A radio connection is not required to adjust DSP parameters.
- Confirm that NR4 is the active noise reduction engine for your receiver. If you are unsure which engine to use, see [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md).

## Steps

1. Click `Settings > AetherDSP Settings...`.
2. Click the **NR4 (tab)** tab.
3. Locate the **Masking Depth:** slider. Drag it left to reduce spectral masking or right to increase it. The valid range is 0.00–1.00; the default is 0.50. The value is persisted as `NR4MaskingDepth`.
4. Locate the **Suppression:** slider. Drag it left for lighter suppression or right for stronger suppression. The valid range is 0.00–1.00; the default is 0.50. The value is persisted as `NR4SuppressionStrength`.
5. Listen to the received audio and fine-tune both sliders until the balance between noise reduction and speech clarity is satisfactory.
6. Close the dialog. Settings are saved immediately when each slider is moved.

## What each control does

| Control | Default | Valid range | Setting key | Behavior |
|---|---|---|---|---|
| **Masking Depth:** | 0.50 | 0.00–1.00 | `NR4MaskingDepth` | Controls the depth of spectral masking applied during noise reduction. Higher values apply deeper masking below the estimated noise floor. |
| **Suppression:** | 0.50 | 0.00–1.00 | `NR4SuppressionStrength` | Sets the overall NR4 suppression strength. Higher values remove more noise; lower values preserve more of the original signal character. |

## Tips

- These two sliders interact. A high **Suppression:** value with a low **Masking Depth:** value produces broad but shallow attenuation. A high **Masking Depth:** value combined with a high **Suppression:** value produces the most aggressive noise removal and carries the greatest risk of distorting quiet speech.
- If the noise floor is changing rapidly (QSB, band noise), enable **Adaptive Noise Estimation** to keep the noise estimate current before pushing **Masking Depth:** and **Suppression:** higher. See [Enable or disable NR4 adaptive noise estimation](enable-or-disable-nr4-adaptive-noise-estimation.md).
- To return both sliders to their defaults (0.50) along with all other NR4 parameters, click **Reset Defaults** on the NR4 tab. See [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md).

## Troubleshooting

- **Speech sounds hollow or distorted after raising the sliders** — Reduce **Masking Depth:** first. Masking depth has a stronger effect on speech coloration than **Suppression:** does. Lower it toward 0.20–0.30 and reassess.
- **Noise reduction has no audible effect even at maximum values** — Check that NR4 is actually the active engine on the receiver. Also verify that **Reduction (dB):** is above 0.0 dB, since that slider gates how much headroom NR4 has to work with. See [Adjust NR4 reduction amount in dB](adjust-nr4-reduction-amount-in-db.md).

## Related

- [Adjust NR4 reduction amount in dB](adjust-nr4-reduction-amount-in-db.md)
- [Enable or disable NR4 adaptive noise estimation](enable-or-disable-nr4-adaptive-noise-estimation.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
