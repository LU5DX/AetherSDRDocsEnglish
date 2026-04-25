# Switch NR2 gain method between Linear, Log, Gamma and Trained

The NR2 gain method controls how AetherSDR maps the estimated noise reduction gain onto the audio signal. Choosing the right method affects the balance between noise suppression and speech naturalness.

## Before you start

- AetherSDR must be running. A radio connection is not required to change this setting.
- NR2 must be active on the slice you want to affect.

## Steps

1. Click `Settings > AetherDSP Settings...`.
2. Click the **NR2** tab.
3. Under **Gain Method**, click one of the four radio buttons: **Linear**, **Log**, **Gamma**, or **Trained**.
4. Close the dialog. The setting takes effect immediately and is saved automatically.

## What each control does

| Control | Kind | Default | Valid values | Setting key | Behavior |
|---|---|---|---|---|---|
| **Gain Method** | Radio buttons | Gamma | Linear, Log, Gamma, Trained | `NR2GainMethod` | Selects the gain-curve mapping used by NR2. Stored as integer 0–3 matching the order above. |

**Gain Method options:**

- **Linear** — Applies gain on a linear amplitude scale. Direct, with no dynamic-range compression.
- **Log** — Uses a logarithmic amplitude scale, compressing the dynamic range of the applied gain.
- **Gamma** — Models speech amplitude as a Gamma distribution. This is the default and suits typical speech patterns.
- **Trained** — Uses a noise-reduction model trained on real speech and noise samples.

## Tips

- **Gamma** is the default and works well for most SSB voice contacts. Start here if you are unsure.
- **Trained** can sound more natural on clean speech but may behave differently on heavily distorted or weak signals.
- **Log** reduces the aggressiveness of gain transitions and can help if **Gamma** or **Trained** produce audible pumping.
- Click **Reset Defaults** on the NR2 tab to return **Gain Method** to **Gamma** along with all other NR2 parameters.

## Troubleshooting

- **Changing the gain method has no audible effect** — Confirm that NR2 is enabled on the active slice. The AetherDSP Settings dialog adjusts parameters only; NR2 must be switched on separately from the slice controls.
- **Speech sounds distorted after switching to Trained** — Try reducing **Reduction Depth:** from its default of 1.50 or increasing **Voice Threshold:** slightly. See [Tune NR2 reduction depth and voice threshold](tune-nr2-reduction-depth-and-voice-threshold.md).

## Related

- [Tune NR2 reduction depth and voice threshold](tune-nr2-reduction-depth-and-voice-threshold.md)
- [Change NR2 noise power estimator (OSMS/MMSE/NSTAT)](change-nr2-noise-power-estimator-osms-mmse-nstat.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
