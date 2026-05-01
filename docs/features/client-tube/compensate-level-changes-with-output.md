Looking at the diff, the changes are to `VfoWidget.cpp` and relate to NRL button visibility on 6000-series hardware. The catalog entry is for `LevelBar` with no controls, and the current documentation is about the Output knob/tube stage — none of this documentation is affected by the diff. The documentation should be returned unchanged.

# Compensate level changes with Output

The Output knob applies a post-tube gain trim to the processed signal. Use it to compensate for the level increase or decrease that Drive and Bias introduce, so the tube stage does not unintentionally push levels up or down in the rest of the chain.

## Before you start

- The Tube stage must be enabled on the side you want to adjust (TX or RX). See [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md).
- Open either the docked applet ("Aetherial Mic-PreAmp" for TX, "Aetherial Dynamic Tube" for RX) or the floating editor (double-click the TUBE stage in the CHAIN widget).

## Steps

1. Locate the **Output** knob in the five-knob row (fourth from the left: Drive, Tone, Bias, **Output**, Mix).
2. Turn **Output** clockwise to increase the post-tube level, or counter-clockwise to reduce it.
3. Release the knob when the output level matches your target. The label under the knob updates in real time and shows the current value in dB (for example, `0.0 dB`).
4. Optionally, watch the **OUT** level meter on the far right of the floating editor to confirm the post-saturation peak level. The meter is only visible in the floating editor, not in the docked applet tile.

## What each control does

| Control | Default | Valid range | Persisted setting key |
|---|---|---|---|
| Output (TX) | 0.0 dB | −24.0 to 12.0 dB | `ClientTubeTxOutputDb` |
| Output (RX) | 0.0 dB | −24.0 to 12.0 dB | `ClientTubeRxOutputDb` |

Output is a post-tube make-up or trim gain. It acts after the Drive, Bias, and Tone stages, so it adjusts the final level without affecting the saturation character.

## Output level meter

The floating editor includes an **OUT** peak level meter (the `ClientLevelMeter` widget) positioned at the far right of the editor panel. It shows the post-saturation peak level with fast-attack and slow-release ballistics and uses the following colour bands:

| Colour | Level range |
|---|---|
| Green | −60 to −12 dB |
| Lime | −12 to −6 dB |
| Amber | −6 to −3 dB |
| Red | Above −3 dB |

The meter is not present in the docked applet tile. It updates continuously alongside the knob controls whenever the floating editor is open.

## Tips

- If raising Drive increases loudness more than desired, reduce Output by a matching amount to keep the net level consistent.
- Use the **OUT** meter in the floating editor to verify that the post-tube signal stays below −3 dB (red) under normal operating conditions.
- Changes made in the floating editor and the docked applet stay in sync. A 30 Hz polling timer keeps both views updated, so adjusting Output in one location is reflected immediately in the other.

## Related

- [Dial Drive until the curve starts to bend (TX warmth or RX tone shaping)](dial-drive-until-the-curve-starts-to-bend-tx-warmth-or-rx-tone-shaping.md)
- [Parallel-blend saturation with Mix](parallel-blend-saturation-with-mix.md)
- [Aetherial Mic-PreAmp (TX) / Aetherial Dynamic Tube (RX) overview](overview.md)