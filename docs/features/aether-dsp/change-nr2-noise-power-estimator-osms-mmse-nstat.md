# Change NR2 noise power estimator (OSMS/MMSE/NSTAT)

The NR2 noise power estimator (NPE) controls how AetherSDR's NR2 engine measures the noise floor before applying suppression. Switching between OSMS, MMSE, and NSTAT can improve noise reduction quality depending on whether the noise on your band is stationary, slowly varying, or rapidly changing.

## Before you start

- No radio connection is required. AetherSDR's DSP settings take effect locally and can be changed while the radio is disconnected.
- NR2 must be active on your slice for changes to be audible. Enabling NR2 is done from the slice controls, not from this dialog.

## Steps

1. Open `Settings > AetherDSP Settings...`.
2. Click the **NR2** tab.
3. Under the **NPE Method** group, select one of the three radio buttons: **OSMS**, **MMSE**, or **NSTAT**.
4. Close the dialog. The setting takes effect immediately and is persisted automatically.

## What each control does

| Control | Description | Default | Valid values | Setting key |
|---|---|---|---|---|
| **OSMS** | Optimal Smoothing Minimum Statistics — tracks the noise floor using a running minimum estimate. Good for stationary or slowly drifting noise. | ✓ (default) | — | `NR2NpeMethod` = 0 |
| **MMSE** | Minimum Mean Squared Error — minimizes the expected noise estimation error. Tends to preserve speech more conservatively. | — | — | `NR2NpeMethod` = 1 |
| **NSTAT** | Non-Stationary estimation — adapts to noise that changes over time. Suits bands with impulsive or rapidly varying interference. | — | — | `NR2NpeMethod` = 2 |

The `NR2NpeMethod` setting is stored as an integer: 0 = OSMS, 1 = MMSE, 2 = NSTAT.

## Tips

- Start with **OSMS** (the default) on most HF bands where background noise is relatively steady. Switch to **NSTAT** if the noise floor is fluctuating or the band conditions are changing rapidly.
- If you want to return all NR2 parameters to their original state, click **Reset Defaults** on the NR2 tab. This restores NPE Method to **OSMS** along with the other NR2 defaults.

## Related

- [AetherDSP Settings overview](overview.md)
- [Tune NR2 reduction depth and voice threshold](tune-nr2-reduction-depth-and-voice-threshold.md)
- [Switch NR2 gain method between Linear, Log, Gamma and Trained](switch-nr2-gain-method-between-linear-log-gamma-and-trained.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
