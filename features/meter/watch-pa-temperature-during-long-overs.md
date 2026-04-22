# Watch PA temperature during long overs

The Meters applet shows a live PA Temp gauge fed directly from the radio. Use it during extended transmit periods to catch thermal buildup before it triggers the radio's protection circuits.

## Before you start

- AetherSDR must be connected to the radio. The Meters applet requires an active radio connection.
- The applet panel must be visible. If it is hidden, use `View > Applet Panel` to show it.

## Steps

1. Click the MTR tray button on the right sidebar. The Meters applet opens, showing the **Radio Hardware** section with three horizontal gauges.
2. Locate the **PA Temp** gauge at the top of the applet.
3. Begin your transmission. Watch the **PA Temp** bar as the over progresses.
4. If the bar enters the yellow zone (above 55 °C), consider shortening your overs. If it reaches the red zone (above 70 °C), end the transmission and allow the radio to cool.

## What each control does

| Control | What it shows | Range | Red threshold |
|---|---|---|---|
| PA Temp | Power amplifier temperature from the radio's PATEMP meter | 0–120 °C | above 70 °C |
| +13.8V | DC supply voltage | 10.0–16.0 V | above 15 V |
| Main Fan | Cooling fan speed | 0–3000 rpm | above 2500 rpm |

The bar fills cyan through yellow (above 55 °C) to red (above 70 °C). The gauge updates continuously while the radio is connected; no manual refresh is needed.

## Tips

- During a long over, glance at **Main Fan** alongside **PA Temp**. A fan reading well below the red zone (2500 rpm) while temperature climbs may indicate restricted airflow around the radio.
- The gauge uses smoothed ballistics, so the bar animates gradually toward the current reading rather than jumping. Brief thermal spikes may appear slightly softened.

## Troubleshooting

- **PA Temp gauge shows no movement after transmitting** — Confirm the radio connection is active. The Meters applet requires a live connection to receive telemetry; a disconnected state will leave all gauges static.

## Related

- [Meters overview](overview.md)
- [Monitor the main cooling fan speed](monitor-the-main-cooling-fan-speed.md)
- [Check the radio's DC supply voltage](check-the-radio-s-dc-supply-voltage.md)
