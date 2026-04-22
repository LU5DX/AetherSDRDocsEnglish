# Compensate level changes with Output

Adding Drive or Bias changes the overall level of the saturated signal. The Output knob applies a post-tube gain trim so you can restore the original level or set a deliberate target level before the signal continues down the TX chain.

## Before you start

- The Tube Saturator stage must be enabled. See [Bypass the tube from the chain](bypass-the-tube-from-the-chain.md) for how to enable it.
- Open the TUBE sub-container inside the PooDoo Audio (TXDSP) parent container. If it is not visible, double-click the Tube stage in the CHAIN widget to open the floating Tube editor.

## Steps

1. Transmit a steady signal or use a tone source so the live input ball on the transfer curve is moving.
2. Locate the Output knob — the fourth knob in the row, labeled **Output**.
3. Turn Output clockwise to increase the post-tube level, or counter-clockwise to reduce it.
4. Stop adjusting when the downstream level meter reads the same as it did before you added saturation, or at whatever level your TX chain requires.

## What each control does

| Control | Default | Valid range | Persisted setting |
|---|---|---|---|
| Output | 0.0 dB | −24.0 to 12.0 dB | `ClientTubeTxOutputGainDb` |

Output applies a linear make-up or trim gain after the tube model. It does not affect the shape of the transfer curve — Drive, Tone, and Bias remain unchanged. The knob label displays the current value as `X.X dB`.

## Tips

- A good starting point is to set Drive first until the transfer curve bends noticeably, then use Output to bring the level back to 0.0 dB. Adjust from there to taste.
- Output changes are reflected immediately on the transfer curve widget's live input ball position, which lets you verify the signal is still operating in the intended saturation regime.
- If you are using the floating Tube editor at the same time as the TUBE applet, the knobs in both views stay in sync automatically.

## Related

- [Dial Drive until the curve starts to bend](dial-drive-until-the-curve-starts-to-bend.md)
- [Shift Bias to tweak the even / odd harmonic balance](shift-bias-to-tweak-the-even-odd-harmonic-balance.md)
- [Parallel-blend saturation with Mix](parallel-blend-saturation-with-mix.md)
- [Brighten or darken the saturated signal with Tone](brighten-or-darken-the-saturated-signal-with-tone.md)
