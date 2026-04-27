# Watch PA temperature during long overs

The Meters applet shows a live PA Temp gauge that reads the radio's power amplifier temperature in real time. Keeping this visible during long transmit overs lets you catch thermal buildup before it becomes a problem.

## Before you start

- AetherSDR must be connected to the radio. The Meters applet requires an active radio connection.
- The applet panel must be visible. If it is hidden, use `View > Applet Panel` to show it.

## Steps

1. Locate the MTR tray button on the right sidebar of the applet panel.
2. Click MTR to toggle the Meters applet open.
3. Read the **PA Temp** gauge under the **Radio Hardware** section header.

The bar fills from left to right as temperature rises. The bar turns yellow above 55 °C and red above 70 °C.

## What each control does

| Label | Range | Red threshold | Behavior |
|-------|-------|---------------|----------|
| PA Temp | 0–120 °C | > 70 °C | Displays the PA temperature reported by the radio. Bar is green below 55 °C, yellow from 55–70 °C, red above 70 °C. |
| +13.8V | 10.0–16.0 V | > 15 V | Displays the supply voltage. |
| Main Fan | 0–3000 rpm | > 2500 rpm | Displays the main cooling fan speed. |

None of these controls have persisted settings keys. They are read-only telemetry displays.

## Tips

- The gauge uses smoothed ballistics, so brief peaks are visible without causing flicker. Sustained red-zone readings indicate a genuine thermal condition, not a transient spike.
- PA current is not shown. On FLEX-8000 series hardware the PA current meter clips under full PA draw, so it has been intentionally omitted.

## Troubleshooting

- **PA Temp gauge shows no movement** — The applet only receives data when connected to the radio. Verify the connection status and reconnect via `Settings > Connect to Radio...` if needed.

## Related

- [Meters overview](overview.md)
- [Check the radio's DC supply voltage](check-the-radio-s-dc-supply-voltage.md)
- [Monitor the main cooling fan speed](monitor-the-main-cooling-fan-speed.md)
