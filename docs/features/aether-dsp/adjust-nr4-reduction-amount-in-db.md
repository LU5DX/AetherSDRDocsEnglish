# Adjust NR4 Reduction Amount in dB

The `NR4ReductionAmount` setting controls how many decibels of noise the NR4 engine (libspecbleach) can remove at maximum. Increasing this value suppresses more noise; decreasing it preserves more of the original signal character.

## Before you start

- AetherSDR must be running. A radio connection is not required to change this setting.
- Open the NR4 engine in your slice receiver before adjusting, so you can hear the effect in real time.

## Steps

1. Click `Settings > AetherDSP Settings...`.
2. Click the **NR4** tab.
3. Locate the **Reduction (dB):** slider.
4. Drag the slider left to reduce suppression or right to increase it. The current value is displayed to the right of the slider.
5. Close the dialog. The value is saved automatically.

## What each control does

| Control | Default | Valid range | Setting key |
|---|---|---|---|
| **Reduction (dB):** slider | 10.0 dB | 0.0–40.0 dB | `NR4ReductionAmount` |
| **Smoothing (%):** slider | 0 | 0–100 % | `NR4SmoothingFactor` |
| **Whitening (%):** slider | 0 | 0–100 % | `NR4WhiteningFactor` |
| **Masking Depth:** slider | 0.50 | 0.00–1.00 | `NR4MaskingDepth` |
| **Suppression:** slider | 0.50 | 0.00–1.00 | `NR4SuppressionStrength` |
| **Noise Estimation Method** radio buttons | SPP-MMSE | SPP-MMSE / Brandt / Martin | `NR4NoiseEstimationMethod` |
| **Adaptive Noise Estimation** checkbox | Enabled | On / Off | `NR4AdaptiveNoise` |
| **Reset Defaults** button | — | — | — |

**Reduction (dB):** sets the ceiling on how much NR4 attenuates noise. At 0 dB, suppression is effectively off. At 40 dB, the engine applies maximum attenuation to quiet noise floors.

## Tips

- Start at the default of 10.0 dB and increase in small steps while listening to a signal. Large values (above 25–30 dB) can introduce audible artifacts on weak or rapidly fading signals.
- If the noise floor returns between transmissions, enable **Adaptive Noise Estimation** so NR4 continuously updates its noise model. See [Enable or disable NR4 adaptive noise estimation](enable-or-disable-nr4-adaptive-noise-estimation.md).
- To return all NR4 parameters to factory defaults (including Reduction back to 10.0 dB), click **Reset Defaults** on the NR4 tab. See [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md).

## Troubleshooting

- **Slider has no audible effect** — confirm that NR4 is the active noise-reduction engine in your slice receiver. AetherSDR's client-side NR engines each require their own activation step in the receiver controls.
- **Noise returns immediately after quieting** — the noise floor may be changing faster than a fixed estimate can track. Enable **Adaptive Noise Estimation** and try the SPP-MMSE noise estimation method.
- **Speech sounds hollow or phasey at high reduction values** — lower **Reduction (dB):** toward 10–15 dB and raise **Masking Depth:** slightly. See [Tune NR4 masking depth and suppression strength](tune-nr4-masking-depth-and-suppression-strength.md).

## Related

- [Enable or disable NR4 adaptive noise estimation](enable-or-disable-nr4-adaptive-noise-estimation.md)
- [Tune NR4 masking depth and suppression strength](tune-nr4-masking-depth-and-suppression-strength.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
