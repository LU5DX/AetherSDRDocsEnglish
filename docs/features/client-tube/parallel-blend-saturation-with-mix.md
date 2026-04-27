# Parallel-blend saturation with Mix

The Mix knob blends the dry (unprocessed) signal with the fully saturated tube output. Backing off Mix from 100 % lets you add harmonic color while preserving the transient character and dynamic feel of the original signal — a technique called parallel saturation.

## Before you start

- The Tube stage must be enabled on the side you want to adjust (TX or RX). See [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md).
- The Aetherial Mic-PreAmp (TX) or Aetherial Dynamic Tube (RX) sub-container must be visible inside the Aetherial Audio (TXDSP) parent container.

## Steps

1. Locate the five-knob row at the bottom of the applet — Drive, Tone, Bias, Output, Mix.
2. Find the rightmost knob, labeled **Mix**.
3. Turn **Mix** to set the dry/wet balance. At **100 %** only the saturated signal passes. At **0 %** only the dry signal passes. Intermediate values blend the two proportionally.
4. Watch the transfer curve and listen to the result. A value around 30–60 % is typical for parallel saturation.
5. If the blended level is louder or quieter than the dry signal, trim it with the **Output** knob. See [Compensate level changes with Output](compensate-level-changes-with-output.md).

## What each control does

| Control | Default | Valid range | Persisted setting key |
|---|---|---|---|
| Mix (TX) | 100 % | 0 % to 100 % (stored as 0.0–1.0) | `ClientTubeTxDryWet` |
| Mix (RX) | 100 % | 0 % to 100 % (stored as 0.0–1.0) | `ClientTubeRxDryWet` |

Mix operates as a linear dry/wet blend. The knob label displays the value as a percentage (e.g. `50 %`).

## Tips

- Mix adjustments made in the floating Aetherial Tube editor are reflected on the applet knob within approximately 33 ms, and vice versa. You do not need to reopen the editor after changing Mix in the applet.
- Mix applies after the tube stage but before nothing else in the chain — set Drive first to taste, then use Mix to dial back the intensity without losing the harmonic shape you dialed in.

## Related

- [Aetherial Mic-PreAmp (TX) / Aetherial Dynamic Tube (RX) overview](overview.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Dial Drive until the curve starts to bend (TX warmth or RX tone shaping)](dial-drive-until-the-curve-starts-to-bend-tx-warmth-or-rx-tone-shaping.md)
- [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md)
