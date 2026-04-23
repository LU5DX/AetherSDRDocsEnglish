# Switch NR2 Gain Method Between Linear, Log, Gamma and Trained

The NR2 engine's gain method controls how it maps estimated noise to a suppression curve. Changing it lets you trade off between aggressive noise removal and natural-sounding speech.

## Before you start

- No radio connection is required. AetherDSP Settings can be opened at any time.
- NR2 must be active on a receiver slice for changes to take effect on live audio.

## Steps

1. Open `Settings > AetherDSP Settings...`.
2. Click the **NR2** tab.
3. In the **Gain Method** group, click one of the four radio buttons: **Linear**, **Log**, **Gamma**, or **Trained**.

The setting takes effect immediately. AetherSDR persists the choice to `NR2GainMethod`.

## What each control does

| Control | Kind | Default | Valid values | Persisted key |
|---|---|---|---|---|
| **Gain Method** | Radio buttons | Gamma | Linear, Log, Gamma, Trained | `NR2GainMethod` |

**Gain Method options:**

- **Linear** — Maps gain using a linear audio amplitude scale. No compression of dynamic range.
- **Log** — Uses a logarithmic amplitude scale. Compresses dynamic range; tends to reduce musical noise artifacts at the cost of some speech naturalness.
- **Gamma** — Models speech amplitude using a Gamma distribution. Default. Generally the best balance between suppression and speech fidelity for SSB and CW work.
- **Trained** — Applies a noise reduction model trained on real speech and noise samples. May perform better on specific noise types but can sound processed on others.

The selection is stored as an integer: Linear = 0, Log = 1, Gamma = 2, Trained = 3.

## Tips

- Start with **Gamma** if you are unsure. It is the default and suits most HF conditions.
- If you hear residual musical noise with Gamma, try **Log**.
- If the noise type is consistent (for example, a steady fan or HVAC hum), **Trained** may give cleaner results.
- After switching methods, use the **Reduction Depth:** and **Voice Threshold:** sliders to re-optimize suppression for the new curve. See [Tune NR2 reduction depth and voice threshold](tune-nr2-reduction-depth-and-voice-threshold.md).
- To return all NR2 parameters to their defaults, click **Reset Defaults** on the NR2 tab. This restores Gain Method to **Gamma**. See [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md).

## Related

- [Tune NR2 reduction depth and voice threshold](tune-nr2-reduction-depth-and-voice-threshold.md)
- [Change NR2 noise power estimator (OSMS/MMSE/NSTAT)](change-nr2-noise-power-estimator-osms-mmse-nstat.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
