# Change NR2 noise power estimator (OSMS/MMSE/NSTAT)

The NR2 noise power estimator (NPE) controls how AetherSDR's NR2 engine measures the background noise floor before applying gain reduction. Switching between OSMS, MMSE, and NSTAT changes how the estimator tracks noise, which affects suppression quality on stationary versus rapidly changing noise sources.

## Before you start

- AetherSDR must be running. A radio connection is not required to change this setting.
- NR2 must be active on a receiver for changes to take audible effect immediately.

## Steps

1. Open `Settings > AetherDSP Settings...`.
2. Click the **NR2** tab.
3. In the **NPE Method** group, select one of the three radio buttons: **OSMS**, **MMSE**, or **NSTAT**.

The setting takes effect immediately and is saved automatically to `NR2NpeMethod`.

## What each control does

| Control | Kind | Default | Valid range | Setting key | Behavior |
|---|---|---|---|---|---|
| **NPE Method** — **OSMS** | Radio button | Default (0) | — | `NR2NpeMethod` | Optimal Smoothing Minimum Statistics. Tracks the noise floor using a running minimum estimate. Well-suited to stable, stationary noise. |
| **NPE Method** — **MMSE** | Radio button | — | — | `NR2NpeMethod` | Minimum Mean Squared Error. Minimizes expected noise estimation error. Good general-purpose choice. |
| **NPE Method** — **NSTAT** | Radio button | — | — | `NR2NpeMethod` | Non-Stationary estimation. Adapts to noise that changes over time, such as QRM or varying interference. |

`NR2NpeMethod` is stored as an integer: OSMS = 0, MMSE = 1, NSTAT = 2.

## Tips

- OSMS is the default and works well for steady background noise such as atmospheric hiss or white noise from the receiver itself.
- NSTAT is the better starting point when the noise floor changes rapidly, for example during a contest with varying band conditions or intermittent interference.
- If changing the NPE method introduces more musical noise artifacts, enable **AE Filter (artifact elimination)** on the same tab.
- Click **Reset Defaults** on the NR2 tab to return to OSMS along with all other NR2 parameters at once.

## Troubleshooting

- **Changing the NPE method produces no audible difference** — Confirm NR2 is enabled on the receiver. The AetherDSP Settings dialog adjusts parameters but does not itself activate NR2; NR2 must be switched on from the receiver controls.
- **NSTAT introduces more residual noise than OSMS** — NSTAT trades floor accuracy for faster adaptation. Reduce **Reduction Depth:** or increase **Smoothing:** on the NR2 tab to compensate.

## Related

- [Tune NR2 reduction depth and voice threshold](tune-nr2-reduction-depth-and-voice-threshold.md)
- [Switch NR2 gain method between Linear, Log, Gamma and Trained](switch-nr2-gain-method-between-linear-log-gamma-and-trained.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
