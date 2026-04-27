# Switch NR2 gain method between Linear, Log, Gamma and Trained

NR2's gain method controls how the engine maps its noise estimate to an actual reduction curve. Switching between Linear, Log, Gamma, and Trained lets you trade off between aggressive noise suppression and natural-sounding speech.

## Before you start

- AetherSDR must be running. A radio connection is not required to change this setting.
- NR2 must be active on the slice you want to affect. This dialog configures the NR2 engine parameters; enabling NR2 on a slice is done from the main UI.

## Steps

1. Click `Settings > AetherDSP Settings...`.
2. Click the **NR2** tab.
3. In the **Gain Method** group, click one of the four radio buttons: **Linear**, **Log**, **Gamma**, or **Trained**.

The selection takes effect immediately and is saved to `NR2GainMethod`.

## What each control does

| Control | Kind | Default | Valid values | Setting key | Behavior |
|---|---|---|---|---|---|
| **Gain Method** | Radio buttons | Gamma | Linear, Log, Gamma, Trained | `NR2GainMethod` | Selects the gain-curve mapping used by NR2. Stored as integer 0–3 matching the order shown. |

### Gain method descriptions

- **Linear** — Uses a linear audio amplitude scale for gain computation.
- **Log** — Uses a logarithmic amplitude scale, which compresses dynamic range.
- **Gamma** — Models gain on a gamma distribution that matches typical speech amplitude patterns. This is the default.
- **Trained** — Applies a noise reduction model trained on real speech and noise samples.

## Tips

- **Gamma** is the default and works well for most SSB voice contacts. Start here if you are unsure.
- **Trained** may produce more natural-sounding speech on signals it was trained for, but results vary with signal type.
- **Log** reduces the dynamic range of the gain curve, which can help with very uneven noise floors.
- After changing the gain method, adjust **Reduction Depth:** (default 1.50, range 0.50–2.00) and **Voice Threshold:** (default 0.20, range 0.05–0.50) to match the new curve's characteristics. See [Tune NR2 reduction depth and voice threshold](tune-nr2-reduction-depth-and-voice-threshold.md).
- Click **Reset Defaults** on the NR2 tab to return the gain method to Gamma along with all other NR2 parameters to their defaults.

## Related

- [Change NR2 noise power estimator (OSMS/MMSE/NSTAT)](change-nr2-noise-power-estimator-osms-mmse-nstat.md)
- [Tune NR2 reduction depth and voice threshold](tune-nr2-reduction-depth-and-voice-threshold.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
