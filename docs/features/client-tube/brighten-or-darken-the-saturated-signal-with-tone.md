# Brighten or darken the saturated signal with Tone

The Tone knob tilts the frequency balance of the tube-saturated signal toward brighter or darker character. Use it after setting Drive to shape the tonal color of the saturation without changing the overall output level.

## Before you start

- The Tube Saturator applet must be visible. It appears as the TUBE sub-container inside the PooDoo Audio (TXDSP) parent container.
- The tube stage must be enabled via the CHAIN widget. If the applet is hidden, enable the stage first so the TUBE sub-container appears.

## Steps

1. Locate the TUBE sub-container in the applet panel.
2. Find the **Tone** knob — the second knob from the left in the five-knob row, between Drive and Bias.
3. Turn **Tone** clockwise to brighten the saturated signal (toward `1.00`), or counter-clockwise to darken it (toward `-1.00`).
4. Watch the label beneath the knob; it displays the current value as a two-decimal number such as `0.25` or `-0.50`.
5. To return to neutral, double-click **Tone** to reset it to its default of `0.00`.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---------|---------|-------------|---------------|----------|
| Tone | `0.00` | `-1.0` to `1.0` | `ClientTubeTxTone` | Negative values darken, positive values brighten the saturated signal. Linear mapping across the range. |

## Tips

- The Tone knob affects only the saturated portion of the signal. If Mix is below 100 %, the dry path is unaffected, so the tonal shift will be proportionally blended.
- Changes made to Tone in the floating Tube editor are reflected in the applet knob within approximately 33 ms, and vice versa. You can adjust from either location.
- Small adjustments — values between `-0.30` and `0.30` — are usually sufficient. Extreme values can sound unnatural depending on Drive and Bias settings.

## Related

- [Tube Saturator overview](overview.md)
- [Dial Drive until the curve starts to bend](dial-drive-until-the-curve-starts-to-bend.md)
- [Shift Bias to tweak the even / odd harmonic balance](shift-bias-to-tweak-the-even-odd-harmonic-balance.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Parallel-blend saturation with Mix](parallel-blend-saturation-with-mix.md)
