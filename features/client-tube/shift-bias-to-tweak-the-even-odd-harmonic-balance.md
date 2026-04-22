# Shift Bias to tweak the even / odd harmonic balance

The Bias knob shifts the operating point on the tube transfer curve. Moving it away from zero introduces asymmetry into the saturation, changing the ratio of even to odd harmonics in the processed signal.

## Before you start

- The Tube Saturator stage must be enabled. If the TUBE sub-container is not visible, enable the stage from the CHAIN widget or double-click the Tube stage in the CHAIN widget to open the floating Tube editor.
- Some Drive must be applied before Bias has an audible effect — a straight transfer curve produces no saturation regardless of Bias setting.

## Steps

1. Open the TUBE sub-container inside the PooDoo Audio (TXDSP) parent container.
2. Locate the Bias knob in the five-knob row.
3. Turn Bias clockwise to increase asymmetry. Watch the transfer curve — the curve bends asymmetrically as Bias rises.
4. Monitor the live input ball on the transfer curve to confirm the signal is riding the shaped portion of the curve.
5. Adjust to taste. Return Bias to 0 % to restore a symmetrical transfer curve.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Bias | 0 % | 0 % to 100 % (0.0 to 1.0) | `ClientTubeTxBiasAmount` | Shifts the operating point on the transfer curve. Higher values increase asymmetry, raising the proportion of even harmonics relative to odd. |
| Transfer curve | — | — | — | Draws the current tube transfer curve and updates in real time as Bias changes. |
| Live input ball | — | — | — | Dot tracks the current input level along the transfer curve, showing which portion of the curve the signal is using. |

## Tips

- Bias interacts with the active tube model. The effect of a given Bias value differs across Model A, Model B, and Model C because each model applies asymmetry differently.
- After increasing Bias, check the Output knob. Asymmetric saturation can shift the average output level; use Output to compensate.
- For subtle even-harmonic coloration, keep Bias low (under 25 %) and use moderate Drive.

## Related

- [Dial Drive until the curve starts to bend](dial-drive-until-the-curve-starts-to-bend.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Brighten or darken the saturated signal with Tone](brighten-or-darken-the-saturated-signal-with-tone.md)
- [Tube Saturator overview](overview.md)
