# Set RF output power

Use the RF Power slider in the TX Controls applet to set the transmit power level sent to your antenna. Adjusting this before transmitting prevents overdriving your amplifier or violating band power limits.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. If not, go to `Settings > Connect to Radio...`.
- The TX Controls applet must be visible. If it is not, click the **TX** tray button on the right sidebar to show it.

## Steps

1. Locate the **RF Power** slider in the TX Controls applet. It appears below the **SWR** gauge.
2. Drag the slider left or right to set your desired power level. The numeric readout to the right of the slider updates immediately.
3. Confirm the value shown in the readout is what you intend. The **RF Pwr** gauge will reflect actual forward power once you transmit.

## What each control does

| Control | Description | Default | Valid range |
|---|---|---|---|
| **RF Power** slider | Sets the transmit RF power level sent to the radio. | 100 | 0–100 |
| **RF Pwr** meter | Displays actual forward power at the exciter output. | — | 0–120 W (barefoot); 0–600 W (Aurora 500 W); red above 100 W / 500 W |
| **SWR** meter | Displays standing wave ratio at the exciter. | — | 1.0–3.0; red above 2.5 |

## Tips

- The **RF Pwr** meter scale changes automatically depending on your radio model. On a standard FLEX-8600 the red zone begins above 100 W.
- You can set per-band power limits independently of this slider. Go to `Settings > TX Band Settings...` to configure power, tune power, and inhibit settings for each band.
- The **RF Power** slider controls the exciter output level, not a separate amplifier. If you are running an external amplifier, set this slider to the drive level your amplifier expects.

## Troubleshooting

- **RF Pwr meter shows 0 W during transmit** — Confirm the radio is actually keyed. Check that MOX is active (the **MOX** button is red) or that your PTT line is asserted. Also verify the **RF Power** slider is not set to 0.
- **Slider moves but forward power does not change** — The radio connection may have dropped. Check the connection status and reconnect via `Settings > Connect to Radio...` if needed.

## Related

- [TX Controls overview](overview.md)
- [Set tune-carrier power](set-tune-carrier-power.md)
- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [Toggle MOX to manually key the transmitter](toggle-mox-to-manually-key-the-transmitter.md)
- [Switch TX profiles (e.g. SSB, Digital)](switch-tx-profiles-e-g-ssb-digital.md)
