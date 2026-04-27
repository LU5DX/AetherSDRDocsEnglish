# Compensate level changes with Output

The Output knob applies a post-tube gain trim to the processed signal. Use it to compensate for the level increase or decrease that Drive and Bias introduce, so the tube stage does not unintentionally push levels up or down in the rest of the chain.

## Before you start

- The Tube stage must be enabled on the side you want to adjust (TX or RX). See [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md).
- Open either the docked applet ("Aetherial Mic-PreAmp" for TX, "Aetherial Dynamic Tube" for RX) or the floating editor (double-click the TUBE stage in the CHAIN widget).

## Steps

1. Locate the **Output** knob in the five-knob row (fourth from the left: Drive, Tone, Bias, **Output**, Mix).
2. Turn **Output** clockwise to increase the post-tube level, or counter-clockwise to reduce it.
3. Release the knob when the output level matches your target. The label under the knob updates in real time and shows the current value in dB (for example, `0.0 dB`).

## What each control does

| Control | Default | Valid range | Persisted setting key |
|---|---|---|---|
| Output (TX) | 0.0 dB | −24.0 to 12.0 dB | `ClientTubeTxOutputGainDb` |
| Output (RX) | 0.0 dB | −24.0 to 12.0 dB | `ClientTubeRxOutputGainDb` |

Output is a post-tube make-up or trim gain. It acts after the Drive, Bias, and Tone stages, so it adjusts the final level without affecting the saturation character.

## Tips

- If raising Drive increases loudness more than desired, reduce Output by a matching amount to keep the net level consistent.
- Changes made in the floating editor and the docked applet stay in sync. A 30 Hz polling timer keeps both views updated, so adjusting Output in one location is reflected immediately in the other.

## Related

- [Dial Drive until the curve starts to bend (TX warmth or RX tone shaping)](dial-drive-until-the-curve-starts-to-bend-tx-warmth-or-rx-tone-shaping.md)
- [Parallel-blend saturation with Mix](parallel-blend-saturation-with-mix.md)
- [Aetherial Mic-PreAmp (TX) / Aetherial Dynamic Tube (RX) overview](overview.md)
