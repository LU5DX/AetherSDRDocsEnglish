# Brighten or darken the saturated signal with Tone

The Tone knob shapes the tonal character of the saturated output. Use it to add air and presence (positive values) or to roll off harshness and warm the sound (negative values) after the tube stage has already colored the signal.

## Before you start

- The tube stage must be enabled for the relevant side (TX or RX). See [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md).
- The Aetherial Mic-PreAmp (TX) or Aetherial Dynamic Tube (RX) sub-container must be visible in the Applet Panel. If it is not visible, enable the Tube stage via the CHAIN widget on the matching side, or double-click the TUBE stage in the CHAIN widget to open the floating editor.

## Steps

1. Locate the five-knob row at the bottom of the Aetherial Mic-PreAmp (TX) or Aetherial Dynamic Tube (RX) applet. The knobs are, left to right: Drive, Tone, Bias, Output, Mix.
2. Turn the **Tone** knob to the right (positive) to brighten the saturated signal, or to the left (negative) to darken it.
3. Read the current value from the label beneath the knob. The label displays in the format `X.XX` (for example, `0.50` or `-0.75`).
4. Release the knob. The setting is saved automatically.

Alternatively, double-click the TUBE stage in the CHAIN widget to open the floating editor titled **Aetherial Tube — TX** or **Aetherial Tube — RX**, where the same Tone knob is available at a larger size.

## What each control does

| Control | Default | Valid range | Persisted setting key |
|---------|---------|-------------|-----------------------|
| Tone (TX) | `0.00` | −1.0 to 1.0 | `ClientTubeTxTone` |
| Tone (RX) | `0.00` | −1.0 to 1.0 | `ClientTubeRxTone` |

Negative values darken the saturated signal; positive values brighten it. The mapping is linear across the full range. A value of `0.00` applies no tonal correction.

## Tips

- Tone acts on the signal after the tube stage colors it with Drive and Bias. Set Drive and Bias first, then use Tone to trim the result rather than working in the opposite order.
- The transfer curve display updates in real time as you adjust Tone, giving a visual reference alongside the audible change.
- TX and RX instances are fully independent. Adjusting Tone on the TX side has no effect on the RX side and vice versa.

## Related

- [Aetherial Mic-PreAmp (TX) / Aetherial Dynamic Tube (RX) overview](overview.md)
- [Dial Drive until the curve starts to bend (TX warmth or RX tone shaping)](dial-drive-until-the-curve-starts-to-bend-tx-warmth-or-rx-tone-shaping.md)
- [Shift Bias to tweak the even / odd harmonic balance](shift-bias-to-tweak-the-even-odd-harmonic-balance.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md)
