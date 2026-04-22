# Parallel-blend saturation with Mix

The Mix knob blends the dry (unprocessed) signal with the fully saturated tube signal. Reducing Mix below 100 % lets you add harmonic character while preserving transient clarity and natural tone from the original signal — a technique called parallel saturation.

## Before you start

- The Tube Saturator stage must be enabled in the CHAIN widget. If it is not enabled, Mix has no audible effect.
- Open the TUBE sub-container inside the PooDoo Audio (TXDSP) parent container. If it is not visible, double-click the Tube stage in the CHAIN widget to open the floating Tube editor, or right-click the TUBE sub-container titlebar and choose to show it.

## Steps

1. Locate the Mix knob in the five-knob row at the bottom of the TUBE applet.
2. Turn Mix to set the dry/wet balance. The label displays the current value as a percentage (for example, `50 %`).
   - `100 %` — fully saturated signal only.
   - `0 %` — dry signal only; saturation is bypassed in effect.
   - Values between produce a proportional blend.
3. Adjust Drive, Output, or Tone as needed to compensate for level or tonal changes at the chosen blend point.

## What each control does

| Control | Default | Valid range | Persisted setting |
|---------|---------|-------------|-------------------|
| Mix | 100 % | 0 % to 100 % (stored as 0.0 to 1.0) | `ClientTubeTxDryWet` |

Mix is a linear dry/wet blend. At 100 % the output is the tube-processed signal. At 0 % the output is the unmodified input. Intermediate values sum both in proportion.

The applet synchronises with the floating Tube editor every 33 ms, so a value changed in either place is reflected in the other without any extra action.

## Tips

- Start with Drive set moderately (6–12 dB) before pulling Mix back. Low Drive with 100 % Mix produces less saturation than higher Drive blended to 30–50 % Mix, but the two approaches sound different — experiment to find the character you want.
- Use the Output knob to restore loudness after reducing Mix, since blending in dry signal typically lowers the perceived level of the saturation effect.
- The live input ball on the transfer curve still reflects the full Drive amount regardless of Mix setting. Use it to judge the saturation regime; use your ears to judge the blend.

## Related

- [Tube Saturator overview](overview.md)
- [Dial Drive until the curve starts to bend](dial-drive-until-the-curve-starts-to-bend.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Bypass the tube from the chain](bypass-the-tube-from-the-chain.md)
