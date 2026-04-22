# Change NR2 Noise Power Estimator (OSMS/MMSE/NSTAT)

The NR2 noise power estimator (NPE) determines how AetherSDR models the background noise floor before applying gain reduction. Switching between OSMS, MMSE, and NSTAT can improve noise suppression on signals where the noise character is stationary, slowly varying, or rapidly changing.

## Before you start

- AetherSDR must be running. A radio connection is not required to change this setting.
- NR2 noise reduction must be active on a slice receiver for the change to have an audible effect.

## Steps

1. Open `Settings > AetherDSP Settings...`.
2. Click the **NR2** tab.
3. Under **NPE Method**, click one of the three radio buttons: **OSMS**, **MMSE**, or **NSTAT**.
4. The setting takes effect immediately and is saved automatically to `NR2NpeMethod`.

## What each control does

| Control | Kind | Default | Valid values | Persisted key | Behavior |
|---|---|---|---|---|---|
| **NPE Method** | Radio button | OSMS | OSMS \| MMSE \| NSTAT | `NR2NpeMethod` | Selects the noise power estimator used by NR2. Stored as integer 0 (OSMS), 1 (MMSE), or 2 (NSTAT). |

**OSMS** — Optimal Smoothing Minimum Statistics. Tracks the noise floor using a running minimum estimate. Works well for stationary or slowly changing noise typical of band noise and interference.

**MMSE** — Minimum Mean Squared Error. Minimizes the expected noise estimation error. Generally produces smoother gain curves and may reduce musical noise artefacts on voice signals.

**NSTAT** — Non-Stationary estimation. Adapts to noise that changes over time. Use this when noise bursts, QRM, or other rapidly varying interference is present.

## Tips

- If you hear musical noise or residual burbling after NR2 processes a signal, try switching from OSMS to MMSE, then enable **AE Filter (artifact elimination)** if it is not already checked.
- For pile-up or contest conditions where interference changes rapidly, NSTAT may track the noise floor more accurately than OSMS.
- Changing the NPE method interacts with the **Smoothing:** slider (`NR2GainSmooth`, default 0.85). A lower smoothing value lets any estimator adapt faster; a higher value stabilises it.
- To restore OSMS along with all other NR2 defaults, click **Reset Defaults** on the NR2 tab.

## Related

- [Tune NR2 reduction depth and voice threshold](tune-nr2-reduction-depth-and-voice-threshold.md)
- [Switch NR2 gain method between Linear, Log, Gamma and Trained](switch-nr2-gain-method-between-linear-log-gamma-and-trained.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
