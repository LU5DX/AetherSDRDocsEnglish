# Check the Radio's Live DC Supply Voltage

The Meters applet shows the supply voltage reported live by the radio. Use it to confirm your DC power source is within a healthy range during operation.

## Before you start

- AetherSDR must be connected to the radio. The Meters applet requires an active radio connection.
- The applet panel must be visible. If it is hidden, enable it via `View > Applet Panel`.

## Steps

1. Click the **MTR** tray button on the right sidebar to open the Meters applet.
2. Read the **+13.8V** gauge. The label in the center of the bar updates live to show the current voltage — for example, `+13.82V`.

## What each control does

| Gauge | Valid range | Red above | Behavior |
|-------|-------------|-----------|----------|
| +13.8V | 10.0–16.0 V | 15 V | Displays the supply voltage reported by the radio. The gauge label updates dynamically to reflect the live value (e.g. `+13.82V`). |

There is no persisted setting key for this gauge. It has no configurable default.

## Tips

- The gauge label changes on every telemetry update from the radio, so the value shown in the bar center is always current — it is not a static placeholder.
- The bar fills cyan in the normal range and turns red above 15 V. A red bar indicates a supply voltage that is above the expected operating range.

## Troubleshooting

- **Gauge shows no movement or a fixed label** — The radio is not connected, or the telemetry stream has not started. Confirm the connection status and reconnect via `Settings > Connect to Radio...`.

## Related

- [Meters overview](overview.md)
- [Watch PA temperature during long overs](watch-pa-temperature-during-long-overs.md)
- [Monitor the main cooling fan speed](monitor-the-main-cooling-fan-speed.md)
