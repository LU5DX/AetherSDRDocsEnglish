# Change NR2 noise power estimator (OSMS/MMSE/NSTAT)

The NR2 noise power estimator (NPE) determines how AetherSDR's NR2 engine measures the background noise floor. Switching between OSMS, MMSE, and NSTAT lets you match the estimator to the type of noise you are dealing with.

## Before you start

- AetherSDR must be running. A radio connection is not required to change this setting.
- NR2 must be active on your slice for the change to have an audible effect.

## Steps

1. Click `Settings > AetherDSP Settings...`.
2. In the AetherDSP Settings dialog, click the **NR2** tab.
3. Under **NPE Method**, click one of the three radio buttons: **OSMS**, **MMSE**, or **NSTAT**.

The setting takes effect immediately and is saved automatically to `NR2NpeMethod`.

## What each control does

| Control | Kind | Default | Valid values | Setting key | Behavior |
|---|---|---|---|---|---|
| NPE Method — **OSMS** | radio button | ✓ default | — | `NR2NpeMethod` = 0 | Optimal Smoothing Minimum Statistics. Tracks the noise floor using a running minimum estimate. Best for steady, stationary noise. |
| NPE Method — **MMSE** | radio button | — | — | `NR2NpeMethod` = 1 | Minimum Mean Squared Error. Minimizes the expected noise estimation error. A balanced choice for mixed conditions. |
| NPE Method — **NSTAT** | radio button | — | — | `NR2NpeMethod` = 2 | Non-Stationary estimation. Adapts to noise that changes rapidly over time, such as QRM that varies in character. |

`NR2NpeMethod` is stored as an integer: 0 = OSMS, 1 = MMSE, 2 = NSTAT.

## Tips

- OSMS is the default and works well for consistent atmospheric or band noise.
- If the noise floor varies quickly (for example, switching stations or changing band conditions), try NSTAT, which re-adapts more aggressively.
- MMSE is a middle ground: it tends to leave less residual noise than OSMS in moderate conditions without the faster-moving artifacts that NSTAT can introduce.
- To return all NR2 parameters to their defaults (including NPE Method back to OSMS), click **Reset Defaults** at the bottom of the NR2 tab.

## Related

- [Tune NR2 reduction depth and voice threshold](tune-nr2-reduction-depth-and-voice-threshold.md)
- [Switch NR2 gain method between Linear, Log, Gamma and Trained](switch-nr2-gain-method-between-linear-log-gamma-and-trained.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
