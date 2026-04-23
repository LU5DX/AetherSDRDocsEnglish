# Change NR2 Noise Power Estimator (OSMS/MMSE/NSTAT)

The NR2 noise power estimator (NPE) controls how AetherSDR's NR2 engine measures the noise floor before applying gain. Switching between OSMS, MMSE, and NSTAT lets you match the estimator to the type of noise you are dealing with — steady, averaged, or rapidly changing.

## Before you start

- AetherSDR must be running. A radio connection is not required to change this setting.
- NR2 must be active on your slice for the change to have an audible effect.

## Steps

1. Click `Settings > AetherDSP Settings...`.
2. Click the **NR2** tab.
3. In the **NPE Method** group, click one of the three radio buttons: **OSMS**, **MMSE**, or **NSTAT**.

The selection takes effect immediately and is saved to `NR2NpeMethod`.

## What each control does

| Control | Kind | Default | Valid values | Setting key | Behavior |
|---|---|---|---|---|---|
| **NPE Method** | Radio buttons | OSMS | OSMS \| MMSE \| NSTAT | `NR2NpeMethod` | Selects the noise power estimator used by NR2. Stored as integer 0–2. |

**OSMS** — Optimal Smoothing Minimum Statistics. Tracks the noise floor using a running minimum estimate. Best for steady, slow-changing noise.

**MMSE** — Minimum Mean Squared Error. Minimizes the expected noise estimation error. A balanced general-purpose choice.

**NSTAT** — Non-Stationary estimation. Adapts to noise that changes over time. Use this when background noise is variable or intermittent.

## Tips

- If you hear musical noise artifacts after switching estimators, enable **AE Filter (artifact elimination)** on the same tab. Its setting is `NR2AeFilter` and it defaults to on.
- If you change the NPE method and are not satisfied, click **Reset Defaults** on the NR2 tab to restore OSMS along with all other NR2 parameters to their defaults (Gamma / OSMS / AE on / 1.50 / 0.85 / 0.20).

## Related

- [Tune NR2 reduction depth and voice threshold](tune-nr2-reduction-depth-and-voice-threshold.md)
- [Switch NR2 gain method between Linear, Log, Gamma and Trained](switch-nr2-gain-method-between-linear-log-gamma-and-trained.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
