# Adjust NR4 Reduction Amount in dB

The `NR4ReductionAmount` setting controls how many decibels of noise reduction NR4 (libspecbleach) applies. Raising this value suppresses more noise; lowering it preserves more of the original signal character.

## Before you start

- AetherSDR must be running. A radio connection is not required to change this setting.
- Decide roughly how aggressive you want noise reduction to be. A value of 10.0 dB suits most SSB conditions; higher values (20–40 dB) suit very noisy bands but may affect speech fidelity.

## Steps

1. Click `Settings > AetherDSP Settings...` to open the AetherDSP Settings dialog.
2. Click the **NR4** tab.
3. Locate the **Reduction (dB):** slider.
4. Drag the slider left to reduce the amount or right to increase it. The current value is displayed to the right of the slider.
5. Close the dialog. The value is saved immediately; no separate Apply or Save step is needed.

## What each control does

| Control | Default | Valid range | Setting key |
|---|---|---|---|
| **Reduction (dB):** slider | 10.0 dB | 0.0–40.0 dB | `NR4ReductionAmount` |

Setting the slider to 0.0 dB disables NR4 reduction without turning off the NR4 engine. Setting it to 40.0 dB applies maximum suppression.

## Tips

- If you hear speech artifacts or a hollow quality, reduce the **Reduction (dB):** value in small steps rather than switching to a different noise reduction engine.
- The **Reduction (dB):** slider works together with **Suppression:** and **Masking Depth:**. If the overall result is still too aggressive after lowering **Reduction (dB):**, see [Tune NR4 masking depth and suppression strength](tune-nr4-masking-depth-and-suppression-strength.md).
- To return all NR4 parameters to their defaults (including **Reduction (dB):** back to 10.0 dB), click **Reset Defaults** at the bottom of the NR4 tab.

## Troubleshooting

- **Slider moves but noise level does not change** — NR4 may not be the active noise reduction engine for the current slice. Verify that NR4 is enabled in the audio path before adjusting its parameters.
- **Value resets to 10.0 after restarting AetherSDR** — The setting was not persisted. Confirm that AetherSDR has write access to its configuration directory and that no other instance is running that could be overwriting `NR4ReductionAmount`.

## Related

- [Enable or disable NR4 adaptive noise estimation](enable-or-disable-nr4-adaptive-noise-estimation.md)
- [Tune NR4 masking depth and suppression strength](tune-nr4-masking-depth-and-suppression-strength.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
