# Brighten or darken the saturated signal with Tone

Use the Tone knob to tilt the spectral character of the saturated signal — negative values make it darker and warmer, positive values make it brighter and more present. Tone works on both the TX side (Aetherial Mic-PreAmp) and the RX side (Aetherial Dynamic Tube) independently.

## Before you start

- The tube stage must be enabled on the side you want to adjust (TX or RX). See [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md).
- The Aetherial Mic-PreAmp (TX) or Aetherial Dynamic Tube (RX) sub-container must be visible in the Applet Panel. Double-click the TUBE stage in the CHAIN widget to open the floating editor, or locate the sub-container directly in the panel.

## Steps

1. Locate the five-knob row at the bottom of the Aetherial Mic-PreAmp (TX) or Aetherial Dynamic Tube (RX) applet.
2. Find the knob labeled **Tone** — it is the second knob from the left, between Drive and Bias.
3. Turn the **Tone** knob left (toward −1.00) to darken the saturated signal, or right (toward +1.00) to brighten it.
4. Read the current value from the label beneath the knob. The label displays two decimal places (e.g. `−0.50` or `0.75`).
5. To reset Tone to its default, double-click the **Tone** knob.

## What each control does

| Control | Default | Valid range | Persisted setting key | Behavior |
|---|---|---|---|---|
| Tone (TX) | 0.00 | −1.0 to 1.0 | `ClientTubeTxTone` | Negative values darken, positive values brighten the saturated signal. |
| Tone (RX) | 0.00 | −1.0 to 1.0 | `ClientTubeRxTone` | Same behavior as TX Tone, applied to the receive path. |

## Tips

- Tone interacts with Drive: a high Drive value produces more saturation harmonics, so Tone adjustments become more audible as Drive increases. Dial in Drive first, then use Tone to shape the result.
- If you have the floating editor open alongside the applet, both reflect the same value. Changes made in one sync to the other within approximately 33 ms.
- A Tone value of 0.00 leaves the spectral balance of the saturated signal unchanged.

## Troubleshooting

- **Tone knob has no audible effect** — the tube stage may be bypassed. Confirm the stage is active in the CHAIN widget on the matching side. Also check that Mix is above 0 %; a fully dry signal (Mix at 0 %) passes through the tube model but blends none of the wet output.
- **Knob position does not match what you expect after reloading** — the value is saved automatically each time the knob changes. If `ClientTubeTxTone` or `ClientTubeRxTone` is missing or corrupted in your settings file, the value reverts to the default of 0.00.

## Related

- [Aetherial Mic-PreAmp (TX) / Aetherial Dynamic Tube (RX) overview](overview.md)
- [Dial Drive until the curve starts to bend (TX warmth or RX tone shaping)](dial-drive-until-the-curve-starts-to-bend-tx-warmth-or-rx-tone-shaping.md)
- [Shift Bias to tweak the even / odd harmonic balance](shift-bias-to-tweak-the-even-odd-harmonic-balance.md)
- [Parallel-blend saturation with Mix](parallel-blend-saturation-with-mix.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md)
