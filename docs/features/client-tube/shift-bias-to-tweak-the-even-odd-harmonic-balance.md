# Shift Bias to tweak the even / odd harmonic balance

The Bias knob shifts the operating point on the tube transfer curve, changing the ratio of even to odd harmonics in the saturated signal. Use it to move between a warmer, rounder character and a grittier, more asymmetric one.

## Before you start

- The Tube stage must be enabled on the side you want to adjust (TX or RX). See [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md).
- The applet is visible inside the Aetherial Audio (TXDSP) parent container — "Aetherial Mic-PreAmp" for TX, "Aetherial Dynamic Tube" for RX.
- Some Drive applied (Drive > 0.0 dB) makes harmonic changes from Bias audible. See [Dial Drive until the curve starts to bend (TX warmth or RX tone shaping)](dial-drive-until-the-curve-starts-to-bend-tx-warmth-or-rx-tone-shaping.md).

## Steps

1. Locate the "Aetherial Mic-PreAmp" (TX) or "Aetherial Dynamic Tube" (RX) sub-container in the Aetherial Audio (TXDSP) parent container, or double-click the TUBE stage in the CHAIN widget to open the floating editor titled "Aetherial Tube — TX" or "Aetherial Tube — RX".
2. Find the **Bias** knob in the five-knob row (Drive, Tone, Bias, Output, Mix).
3. Turn the Bias knob. The label updates in real time, showing the current value as a percentage (for example, `50 %`).
4. Watch the transfer curve: as Bias increases, the curve shifts asymmetrically, increasing even harmonics relative to odd ones.
5. Stop at the value that gives the harmonic balance you want. The setting is saved automatically.

## What each control does

| Control | Default | Valid range | Persisted setting key |
|---|---|---|---|
| Bias (TX) | 0 % | 0 % to 100 % (internal: 0.0 to 1.0) | `ClientTubeTxBiasAmount` |
| Bias (RX) | 0 % | 0 % to 100 % (internal: 0.0 to 1.0) | `ClientTubeRxBiasAmount` |

The TX and RX instances are fully independent. Adjusting Bias on one side does not affect the other.

## Tips

- The transfer curve display and its live input ball update as you turn Bias, so you can see the operating point shift without transmitting or receiving a signal.
- Changes made in the floating editor and in the docked applet stay in sync. A 30 Hz timer keeps both views current, so you can adjust from either location.
- At 0 % Bias the tube operates symmetrically, favouring odd harmonics. Increasing Bias introduces asymmetry and raises even harmonics. The audible character changes most noticeably when Drive is several dB above its default.

## Related

- [Aetherial Mic-PreAmp (TX) / Aetherial Dynamic Tube (RX) overview](overview.md)
- [Dial Drive until the curve starts to bend (TX warmth or RX tone shaping)](dial-drive-until-the-curve-starts-to-bend-tx-warmth-or-rx-tone-shaping.md)
- [Brighten or darken the saturated signal with Tone](brighten-or-darken-the-saturated-signal-with-tone.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Parallel-blend saturation with Mix](parallel-blend-saturation-with-mix.md)
- [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md)
