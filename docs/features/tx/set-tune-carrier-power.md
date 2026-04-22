# Set tune-carrier power

The "Tune Pwr" slider sets the RF power level used when you key a tune carrier. Keeping tune power low protects your amplifier and antenna while still letting the ATU find a match.

## Before you start

- AetherSDR must be connected to the radio. The TX applet is not functional without a radio connection.
- The TX applet must be visible in the Applet Panel. If it is not visible, click the TX tray button on the right sidebar.

## Steps

1. Locate the "Tune Pwr" slider in the TX applet. It is the second slider row, below "RF Power".
2. Drag the slider left or right to set the desired tune-carrier power level. The numeric readout to the right of the slider updates immediately.

## What each control does

| Control | Description | Default | Valid range |
|---|---|---|---|
| Tune Pwr | Sets the power level of the tune carrier transmitted when TUNE is active. | 10 | 0–100 |

## Tips

- Set tune power before pressing TUNE. The value takes effect at the start of the next tune cycle.
- A low tune power (10–20) is sufficient for ATU matching in most cases and reduces stress on PA components.

## Related

- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [Run the internal ATU](run-the-internal-atu.md)
- [Set RF output power](set-rf-output-power.md)
