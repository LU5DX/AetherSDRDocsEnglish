# Compensate level changes with Output

The Output knob applies a post-tube gain trim, letting you restore or reduce the overall level after the tube stage shapes the signal. Use it to match the saturated output level to what you had before adding Drive, or to pull the signal back if heavy Drive causes it to run hot.

## Before you start

- The Tube Saturator stage must be enabled and visible. See [Bypass the tube from the chain](bypass-the-tube-from-the-chain.md) if the TUBE sub-container is not showing.
- Open the TUBE sub-container inside the PooDoo Audio (TXDSP) parent container, or double-click the Tube stage in the CHAIN widget to open the floating Tube editor.

## Steps

1. Locate the **Output** knob — the fourth knob in the five-knob row, labeled "Output".
2. Turn **Output** clockwise to increase post-tube gain, or counter-clockwise to reduce it.
3. Watch the transfer curve and your TX meter to confirm the output level is where you want it.

## What each control does

| Control | Default | Valid range | Persisted key |
|---------|---------|-------------|---------------|
| Output | 0.0 dB | −24.0 to 12.0 dB | `ClientTubeTxOutputGainDb` |

The knob label displays the current value as `X.X dB`. The gain is applied linearly after the tube model, functioning as a make-up or trim stage. It does not affect the shape of the transfer curve.

## Tips

- A common starting point: note your TX level with Drive at 0.0 dB, then increase Drive until the curve bends to taste, then trim Output downward until the TX level returns to the original reading.
- Output changes made in the floating Tube editor are reflected on the applet knob within approximately 33 ms, and vice versa.

## Related

- [Dial Drive until the curve starts to bend](dial-drive-until-the-curve-starts-to-bend.md)
- [Parallel-blend saturation with Mix](parallel-blend-saturation-with-mix.md)
- [Tube Saturator overview](overview.md)
