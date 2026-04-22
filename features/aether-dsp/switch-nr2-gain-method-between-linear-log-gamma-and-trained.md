# Switch NR2 gain method between Linear, Log, Gamma and Trained

The NR2 gain method controls how AetherSDR maps noise estimates to gain reduction curves. Choosing the right method lets you balance noise suppression against speech fidelity for different band conditions.

## Before you start

- AetherSDR must be running. A radio connection is not required to change this setting.
- NR2 must be active on your receive slice for the change to have an audible effect.

## Steps

1. Click `Settings > AetherDSP Settings...`.
2. Click the **NR2** tab.
3. Under **Gain Method**, click one of the four radio buttons: **Linear**, **Log**, **Gamma**, or **Trained**.
4. Close the dialog. The setting takes effect immediately and is saved automatically.

## What each control does

| Control | Kind | Default | Valid values | Setting key | Behavior |
|---|---|---|---|---|---|
| **Gain Method** | Radio buttons | Gamma | Linear, Log, Gamma, Trained | `NR2GainMethod` | Selects the gain-curve mapping used by NR2. Stored as integer 0–3 matching the order above. |

**Gain method descriptions:**

- **Linear** — Uses a linear audio amplitude scale for gain computation.
- **Log** — Uses a logarithmic amplitude scale, compressing dynamic range.
- **Gamma** — Models gain using a Gamma distribution matching typical speech amplitude patterns. This is the default.
- **Trained** — Applies a noise reduction model trained on real speech and noise samples.

## Tips

- **Gamma** suits most SSB contacts. Start here if you are unsure.
- **Trained** may perform better on noisy bands with recognizable speech patterns, but can sound over-processed on weak signals.
- **Log** can help reduce musical noise artifacts when **Linear** produces an uneven noise floor residual.
- After changing the gain method, adjust **Reduction Depth:** and **Voice Threshold:** on the same tab to match. See [Tune NR2 reduction depth and voice threshold](tune-nr2-reduction-depth-and-voice-threshold.md).
- Click **Reset Defaults** on the NR2 tab to return to Gamma and all other NR2 defaults at once.

## Troubleshooting

- **Changing the method has no audible effect** — Confirm NR2 is enabled on your receive slice. The AetherDSP Settings dialog configures parameters only; enabling NR2 is done from the slice controls.
- **Speech sounds distorted after switching to Trained** — Lower **Reduction Depth:** from its default of 1.50 toward 1.00, or switch back to **Gamma**.

## Related

- [Change NR2 noise power estimator (OSMS/MMSE/NSTAT)](change-nr2-noise-power-estimator-osms-mmse-nstat.md)
- [Tune NR2 reduction depth and voice threshold](tune-nr2-reduction-depth-and-voice-threshold.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
