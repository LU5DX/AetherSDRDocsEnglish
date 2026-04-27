# Set tune-carrier power

The "Tune Pwr" slider sets the power level of the continuous carrier transmitted when you press TUNE. Keeping this low protects your finals and antenna system during ATU tuning or SWR checks.

## Before you start

- AetherSDR must be connected to the radio. The TX applet is unavailable without an active radio connection.
- Open the TX Controls applet: click the TX tray button in the right sidebar if the applet is not already visible.

## Steps

1. Locate the "Tune Pwr:" slider in the TX Controls applet.
2. Drag the slider left to decrease or right to increase the tune-carrier power level. The numeric readout to the right of the slider updates immediately.
3. Release the slider. The new value is sent to the radio.

## What each control does

| Control | Description | Default | Valid range |
|---|---|---|---|
| Tune Pwr | Sets the power level of the tune carrier in watts. | 10 | 0–100 |

## Tips

- Set "Tune Pwr" to the minimum level that allows your ATU to find a match. Many operators use 10–20 W for ATU tuning.
- The "Tune Pwr" setting is independent of "RF Power", which controls normal transmit power. Adjusting one does not affect the other.
- You can set per-band tune power defaults in `Settings > TX Band Settings...`.

## Related

- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [Run the internal ATU](run-the-internal-atu.md)
- [Set RF output power](set-rf-output-power.md)
