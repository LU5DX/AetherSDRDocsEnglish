# Brighten or darken the saturated signal with Tone

Use the Tone knob in the Tube Saturator applet to shift the tonal character of the saturated signal — negative values darken it, positive values brighten it.

## Before you start

- The Tube Saturator stage must be enabled via the CHAIN widget or the floating Tube editor. The TUBE applet is hidden until the stage is active.
- Open the TUBE sub-container inside the PooDoo Audio (TXDSP) parent container. If it is not visible, double-click the Tube stage in the CHAIN widget to open the floating editor, or right-click the TUBE sub-container titlebar and select the appropriate option.

## Steps

1. Locate the **Tone** knob in the five-knob row at the bottom of the TUBE applet.
2. Turn the knob left (toward −1.0) to darken the saturated signal, or right (toward +1.0) to brighten it.
3. Watch the transfer curve and the live input ball above the knobs to observe how the saturation regime changes as you adjust Tone.
4. Release the knob. The value is saved automatically to `ClientTubeTxTone`.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Tone | 0.00 | −1.0 to 1.0 | `ClientTubeTxTone` | Negative values darken the saturated signal; positive values brighten it. Label shows the value to two decimal places. |

## Tips

- A Tone value of 0.00 leaves the tonal character of the saturated signal unchanged relative to the tube model and Drive setting.
- Changes made here are reflected in the floating Tube editor within approximately 33 ms, and vice versa — both views stay in sync.
- After adjusting Tone, check the Output knob to compensate for any perceived level change introduced by the tonal shift.

## Related

- [Tube Saturator overview](overview.md)
- [Dial Drive until the curve starts to bend](dial-drive-until-the-curve-starts-to-bend.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Shift Bias to tweak the even / odd harmonic balance](shift-bias-to-tweak-the-even-odd-harmonic-balance.md)
- [Parallel-blend saturation with Mix](parallel-blend-saturation-with-mix.md)
- [Bypass the tube from the chain](bypass-the-tube-from-the-chain.md)
