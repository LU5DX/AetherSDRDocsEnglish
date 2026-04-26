# Compensate level changes with Output

The Output knob applies post-tube make-up or trim gain, letting you correct the level change that Drive and Bias introduce without altering the saturation character.

## Before you start

- The Tube stage must be enabled on the side you want to adjust (TX or RX). See [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md).
- The "Aetherial Mic-PreAmp" (TX) or "Aetherial Dynamic Tube" (RX) sub-container must be visible in the Applet Panel.

## Steps

1. Locate the five-knob row at the bottom of the "Aetherial Mic-PreAmp" (TX) or "Aetherial Dynamic Tube" (RX) sub-container.
2. Find the fourth knob, labelled **Output**.
3. Turn the Output knob to the desired gain value. The label below the knob updates in real time and shows the current value in dB (for example, `0.0 dB`).
   - Turn clockwise to increase output level.
   - Turn counter-clockwise to reduce output level.
4. Release the knob. The new value is saved automatically.

## What each control does

| Control | Default | Valid range | Persisted key (TX / RX) |
|---------|---------|-------------|--------------------------|
| Output | 0.0 dB | −24.0 to 12.0 dB | `ClientTubeTxOutputGainDb` / `ClientTubeRxOutputGainDb` |

Output applies a linear gain stage after the tube model. It does not affect Drive, Bias, or Tone — only the final signal level leaving the tube stage. The label format is `X.X dB`.

## Tips

- If heavy Drive or high Bias cause the output to clip downstream, pull Output down to compensate before reducing Drive.
- The Output knob on the applet and the Output knob in the floating editor ("Aetherial Tube — TX" / "— RX") share the same parameter. Changes in one are reflected in the other within approximately 33 ms.
- To restore the default of 0.0 dB, double-click the Output knob.

## Related

- [Dial Drive until the curve starts to bend (TX warmth or RX tone shaping)](dial-drive-until-the-curve-starts-to-bend-tx-warmth-or-rx-tone-shaping.md)
- [Shift Bias to tweak the even / odd harmonic balance](shift-bias-to-tweak-the-even-odd-harmonic-balance.md)
- [Parallel-blend saturation with Mix](parallel-blend-saturation-with-mix.md)
- [Aetherial Mic-PreAmp (TX) / Aetherial Dynamic Tube (RX) overview](overview.md)
