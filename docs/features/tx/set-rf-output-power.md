# Set RF output power

Use the TX Controls applet to adjust how much power the radio sends during transmit. Setting an appropriate level protects your finals, satisfies your license conditions, and keeps your signal clean.

## Before you start

- AetherSDR must be connected to the radio. The TX Controls applet requires an active radio connection.
- Open the TX Controls applet if it is not already visible: click the **TX** tray button on the right sidebar.

## Steps

1. Locate the **RF Power** slider in the TX Controls applet.
2. Drag the slider left to reduce power or right to increase it. The numeric readout to the right of the slider updates immediately.
3. Read the current output on the **RF Pwr** meter above the sliders to confirm the radio is delivering the expected power when transmitting.

## What each control does

| Control | Type | Default | Range | Behavior |
|---|---|---|---|---|
| **RF Power** | Slider | 100 | 0–100 | Sets the transmit RF power level sent to the radio. The numeric label to the right shows the current value. |
| **RF Pwr** | Meter | — | 0–120 W (barefoot); 0–600 W (Aurora 500 W) | Displays actual forward power at the exciter output. The scale changes automatically based on the connected radio model. Reads red above 100 W (barefoot) or 500 W (Aurora). |
| **SWR** | Meter | — | 1.0–3.0 | Displays standing wave ratio at the exciter. Reads red above 2.5. |

## Tips

- The **RF Pwr** meter only moves while the radio is transmitting (MOX keyed, TUNE active, or PTT asserted). Adjust the slider before transmitting, then verify the reading on air.
- Per-band power limits can be configured separately. See `Settings > TX Band Settings...` to set maximum TX power, tune power, and inhibit options for each band.
- The **Tune Pwr** slider controls the power used only during a tune cycle and does not affect normal transmit power. See [Set tune-carrier power](set-tune-carrier-power.md).

## Troubleshooting

- **RF Pwr meter stays at zero while transmitting** — Check that the antenna is connected and the SWR is within range. Extremely high SWR can cause the radio to fold back power to near zero.
- **RF Power slider moves but output does not change** — Confirm the radio is connected (the TX Controls applet requires an active connection). If the slider snaps back, the radio may be rejecting the command; check the radio's band settings or TX inhibit state.
- **RF Pwr scale shows 0–600 W unexpectedly** — This is normal if an Aurora 500 W module is detected. The red threshold shifts to 500 W on that scale.

## Related

- [TX Controls overview](overview.md)
- [Set tune-carrier power](set-tune-carrier-power.md)
- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [Run the internal ATU](run-the-internal-atu.md)
- [Switch TX profiles (e.g. SSB, Digital)](switch-tx-profiles-e-g-ssb-digital.md)
