# Switch NR2 Gain Method Between Linear, Log, Gamma and Trained

The NR2 gain method controls how AetherSDR maps the estimated noise floor to a suppression gain curve. Changing this setting lets you trade off between natural-sounding speech and aggressive noise removal.

## Before you start

- No radio connection is required. The AetherDSP Settings dialog works offline.
- NR2 must be active on your receiver for changes to be audible.

## Steps

1. Open `Settings > AetherDSP Settings...`.
2. Click the **NR2** tab.
3. In the **Gain Method** group, click one of the four radio buttons: **Linear**, **Log**, **Gamma**, or **Trained**.
4. Close the dialog. The setting takes effect immediately and is saved automatically.

## What each control does

| Control | Kind | Default | Valid values | Setting key | Behavior |
|---|---|---|---|---|---|
| **Gain Method** | Radio buttons | Gamma | Linear, Log, Gamma, Trained | `NR2GainMethod` | Selects the gain-curve mapping used by NR2. Stored as integer 0–3 matching the order shown. |

### Gain method descriptions

- **Linear** — Applies a linear audio amplitude scale to gain computation.
- **Log** — Uses a logarithmic amplitude scale, compressing dynamic range.
- **Gamma** — Models speech amplitude patterns using a Gamma distribution. This is the default and suits most SSB and CW work.
- **Trained** — Applies a noise reduction model trained on real speech and noise samples.

## Tips

- **Gamma** is the factory default and works well for typical SSB signals. Try **Log** if Gamma over-suppresses weak stations.
- **Trained** may perform better on signals with consistent background noise but can sound less natural on rapidly varying noise floors.
- If you change the gain method and speech sounds worse, click **Reset Defaults** to restore Gamma along with all other NR2 parameters.

## Troubleshooting

- **Gain Method radio buttons appear but changing them has no effect** — Verify that NR2 is enabled on the receiver. The gain method setting is saved regardless, but is only applied when NR2 is active.

## Related

- [Change NR2 noise power estimator (OSMS/MMSE/NSTAT)](change-nr2-noise-power-estimator-osms-mmse-nstat.md)
- [Tune NR2 reduction depth and voice threshold](tune-nr2-reduction-depth-and-voice-threshold.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
