# Set tune-carrier power

The "Tune Pwr" slider controls how much RF power the radio outputs when you press TUNE. Keeping this value low protects your antenna, tuner, and finals during routine ATU runs or SWR checks.

## Before you start

- AetherSDR must be connected to the radio. The TX Controls applet is not functional without a radio connection.
- The TX Controls applet must be visible. If it is not, click the TX tray button on the right sidebar to show it.

## Steps

1. Locate the "Tune Pwr:" row in the TX Controls applet.
2. Drag the "Tune Pwr" slider left or right to set the desired tune-carrier power level.
3. Read the numeric value displayed to the right of the slider to confirm your setting.

## What each control does

| Control | Description | Default | Valid range |
|---|---|---|---|
| Tune Pwr | Sets the power level of the tune carrier transmitted when TUNE is active. | 10 | 0–100 |

## Tips

- The numeric readout to the right of the "Tune Pwr" slider updates as you drag, so you can set an exact value before pressing TUNE.
- Many operators leave tune power at 10 or below to reduce wear on the finals and to satisfy ATU requirements. Raise it only if your tuner fails to find a match at lower power.
- The "Tune Pwr" setting is independent of the "RF Power" slider, which controls normal transmit power. Changing one does not affect the other.

## Related

- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [Run the internal ATU](run-the-internal-atu.md)
- [Set RF output power](set-rf-output-power.md)
