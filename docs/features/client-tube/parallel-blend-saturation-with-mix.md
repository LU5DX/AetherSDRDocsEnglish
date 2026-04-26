# Parallel-blend saturation with Mix

The Mix knob blends the dry (unprocessed) signal with the fully saturated tube output. Reducing Mix below 100 % lets you add harmonic richness while preserving some of the original signal's transient character — a technique called parallel saturation.

## Before you start

- The Tube stage must be enabled on the side you want to adjust (TX or RX). See [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md).
- Open the applet containing the Mix knob: **Aetherial Mic-PreAmp** (TX side) or **Aetherial Dynamic Tube** (RX side), found inside the Aetherial Audio (TXDSP) parent container.

## Steps

1. Locate the **Mix** knob — rightmost knob in the five-knob row, labelled **Mix**.
2. Turn **Mix** to set the dry/wet balance. The label displays the current value as a percentage (for example, `75 %`).
   - `100 %` — fully saturated signal, no dry blend (default).
   - `0 %` — dry signal only; tube saturation is inaudible.
   - Values between `0 %` and `100 %` blend dry and wet proportionally.
3. Adjust **Drive**, **Bias**, and **Tone** on the wet path as needed. The transfer curve and live input ball update to reflect the saturated signal regardless of the Mix position.
4. Use **Output** to compensate for any overall level change introduced by the blend. See [Compensate level changes with Output](compensate-level-changes-with-output.md).

Your setting is saved automatically each time you move the knob.

## What each control does

| Control | Default | Valid range | Persisted setting (TX / RX) |
|---------|---------|-------------|------------------------------|
| Mix | `100 %` | `0 %` to `100 %` (stored as 0.0 to 1.0) | `ClientTubeTxDryWet` / `ClientTubeRxDryWet` |

## Tips

- Start with **Mix** at `100 %`, dial in **Drive** and **Bias** for the tone you want, then back Mix down until the result sits comfortably in the audio — this is easier than trying to set all knobs simultaneously.
- Because the dry and wet signals are summed, heavy Drive settings at low Mix values can still produce audible harmonic content without overwhelming the source.
- The TX and RX Tube stages have fully independent Mix settings. Adjusting one side does not affect the other.

## Related

- [Aetherial Mic-PreAmp (TX) / Aetherial Dynamic Tube (RX) overview](overview.md)
- [Dial Drive until the curve starts to bend (TX warmth or RX tone shaping)](dial-drive-until-the-curve-starts-to-bend-tx-warmth-or-rx-tone-shaping.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md)
