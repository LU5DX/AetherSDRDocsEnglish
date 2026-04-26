# Set tune-carrier power

The "Tune Pwr" slider controls how much RF power the radio outputs when you press TUNE. Keeping this low protects your antenna system and any connected amplifier during tuning.

## Before you start

- AetherSDR must be connected to your FLEX-8600 radio.
- The TX applet must be visible in the Applet Panel. If it is not, click the TX tray button on the right sidebar.

## Steps

1. Locate the "Tune Pwr:" slider in the TX applet.
2. Drag the slider left to decrease power or right to increase power. The numeric readout to the right of the slider updates immediately.
3. Release the slider. The new value is sent to the radio.

## What each control does

| Control | Default | Valid range | Behavior |
|---|---|---|---|
| Tune Pwr | 10 | 0–100 | Sets the power level of the tune carrier. The value is applied the next time TUNE is pressed. |

## Tips

- A setting of 10 is enough for the internal ATU to find a match on most bands. Raise it only if the ATU needs more power to measure SWR accurately.
- The "Tune Pwr:" slider is independent of the "RF Power:" slider, which controls normal transmit power. Changing one does not affect the other.
- You can also set tune power per band using `Settings > TX Band Settings...`, which overrides the global slider for each individual band.

## Related

- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [Run the internal ATU](run-the-internal-atu.md)
- [Set RF output power](set-rf-output-power.md)
- [TX Controls overview](overview.md)
