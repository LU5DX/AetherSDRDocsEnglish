# Parallel-blend saturation with Mix

The Mix knob blends the dry (unprocessed) signal with the fully saturated (wet) output. Use it to add harmonic richness while keeping some of the original signal's transient character intact — a technique known as parallel compression or parallel saturation.

## Before you start

- The Tube Saturator stage must be enabled via the CHAIN widget. See [Bypass the tube from the chain](bypass-the-tube-from-the-chain.md).
- The TUBE sub-container must be visible inside the PooDoo Audio (TXDSP) parent container.

## Steps

1. Open the TUBE sub-container in the PooDoo Audio (TXDSP) parent container. If it is not visible, double-click the Tube stage in the CHAIN widget to open the floating Tube editor, or right-click the TUBE sub-container titlebar and select the appropriate option to show it.
2. Locate the Mix knob — the rightmost knob in the five-knob row at the bottom of the applet.
3. Turn Mix toward 0 % to increase the proportion of dry signal. Turn it toward 100 % to use more of the saturated signal.
4. Set Mix to the value where the transmitted audio sounds full without losing the original signal's clarity. A starting point of 50 % to 70 % is typical for parallel saturation.

## What each control does

| Control | Default | Valid range | Persisted setting |
|---------|---------|-------------|-------------------|
| Mix | 100 % | 0 % to 100 % (internal: 0.0 to 1.0) | `ClientTubeTxDryWet` |

At 100 % the output is entirely the saturated signal. At 0 % the tube stage is effectively bypassed in terms of audio content, though it remains active in the signal chain. Values between the two blend dry and wet proportionally.

## Tips

- Changes made to Mix in the floating Tube editor are reflected on the applet knob within approximately 33 ms, and vice versa.
- If the blended signal sounds louder than the dry signal alone, use the Output knob to trim the level back. See [Compensate level changes with Output](compensate-level-changes-with-output.md).
- For subtle warmth without obvious distortion, set Drive high to bend the curve, then pull Mix back to 20 %–40 %.

## Troubleshooting

- **Mix knob has no effect** — Confirm the Tube stage is enabled in the CHAIN widget. If the stage is bypassed, no wet signal is produced and the Mix knob cannot alter the output.
- **Knob position does not match what you set in the floating editor** — The applet syncs every ~33 ms. Wait a moment and the knob will update to reflect the current value.

## Related

- [Bypass the tube from the chain](bypass-the-tube-from-the-chain.md)
- [Dial Drive until the curve starts to bend](dial-drive-until-the-curve-starts-to-bend.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Tube Saturator overview](overview.md)
