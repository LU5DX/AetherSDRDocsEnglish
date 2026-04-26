# Shift Bias to tweak the even / odd harmonic balance

The Bias knob shifts the operating point on the tube transfer curve, changing the ratio of even to odd harmonics in the saturated signal. Use it to move from a symmetrical, odd-harmonic character toward a warmer, even-harmonic one — or anywhere in between.

## Before you start

- The Tube stage must be enabled on the side you want to adjust (TX or RX). See [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md) if the stage is currently bypassed.
- The applet must be visible. If it is not, open the Aetherial Audio (TXDSP) parent container and locate the "Aetherial Mic-PreAmp" (TX) or "Aetherial Dynamic Tube" (RX) sub-container.

## Steps

1. Locate the five-knob row at the bottom of the applet: Drive, Tone, Bias, Output, Mix.
2. Find the knob labeled **Bias** — the third knob in the row.
3. Turn the **Bias** knob to the desired value. The label beneath the knob displays the current value as a percentage (for example, `50 %`).
4. Watch the transfer curve above the knob row. The curve's operating point shifts as you turn the knob, visualising the change in harmonic balance.
5. The live input ball on the transfer curve moves in real time, showing where the current input level sits on the new curve.

To open the larger floating editor for finer control, double-click the TUBE stage in the CHAIN widget on the matching side. The editor is titled "Aetherial Tube — TX" or "Aetherial Tube — RX". The Bias knob is available there as well, and both the applet and the editor stay in sync.

## What each control does

| Control | Default | Valid range | Persisted setting |
|---|---|---|---|
| Bias (TX) | 0 % | 0 % to 100 % (internal: 0.0 to 1.0) | `ClientTubeTxBiasAmount` |
| Bias (RX) | 0 % | 0 % to 100 % (internal: 0.0 to 1.0) | `ClientTubeRxBiasAmount` |

At 0 % the operating point is centred, producing a predominantly odd-harmonic character. Increasing Bias moves the operating point off-centre, introducing even harmonics. The transfer curve in the applet reflects this shift visually.

## Tips

- Bias interacts with Drive. Higher Drive values push more signal into the curve, so the effect of a given Bias setting becomes more pronounced. Set Drive first, then fine-tune Bias.
- The applet knobs and the floating editor knobs share the same state and sync within approximately 33 ms of any change made in either location.
- Changes are saved immediately to `ClientTubeTxBiasAmount` or `ClientTubeRxBiasAmount` after each knob movement.

## Related

- [Aetherial Mic-PreAmp (TX) / Aetherial Dynamic Tube (RX) overview](overview.md)
- [Dial Drive until the curve starts to bend (TX warmth or RX tone shaping)](dial-drive-until-the-curve-starts-to-bend-tx-warmth-or-rx-tone-shaping.md)
- [Brighten or darken the saturated signal with Tone](brighten-or-darken-the-saturated-signal-with-tone.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Parallel-blend saturation with Mix](parallel-blend-saturation-with-mix.md)
- [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md)
