# Watch PA temperature during long overs

The Meters applet shows a live PA Temp gauge that reads the radio's power amplifier temperature in real time. Keeping this visible during long transmit overs lets you catch thermal buildup before it becomes a problem.

## Before you start

- AetherSDR must be connected to the radio. The Meters applet requires an active radio connection.
- The applet panel must be visible. If it is hidden, use `View > Applet Panel` to show it.

## Steps

1. Locate the MTR tray button on the right sidebar of the applet panel.
2. Click MTR to toggle the Meters applet open.
3. Read the **PA Temp** gauge under the **Radio Hardware** section header.

The bar fills from left to right as temperature rises. The bar turns red above 70 °C (158 °F). You can toggle the temperature display between Celsius (°C) and Fahrenheit (°F) using the unit button in the header row.

## What each control does

| Label                   | Range                                                                                                                                             | Behavior / Notes                                                                                                                                                                         |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PA Temp                 | 0–120 °C or 32–248 °F (red > 70 °C / 158 °F)                                                                                                      | Displays PATEMP meter reading from the radio; the gauge label shows the live value with the selected unit. Scale and tick marks re-render when the °C/°F toggle is used, snapping immediately to avoid animating across the unit jump. |
| °C / °F toggle          | °C / °F                                                                                                                                           | Toggles the PA temperature display between Celsius and Fahrenheit; the choice persists to the `MtrApplet` settings object (`tempFahrenheit` field). Located in the header row next to the **Radio Hardware** section label. |
| +13.8V (supply voltage) | 10.0–16.0 V (red > 15)                                                                                                                            | Displays supply voltage meter; label dynamically updates to show the live voltage value (e.g. `+13.82V`) via `HGauge::setLabel`.                                                        |
| Main Fan                | 0–3000 rpm (red > 2500)                                                                                                                            | Displays MAINFAN meter value (resolved lazily by `MeterModel::findMeter`); label shows the live rpm. PACURRENT intentionally omitted: the 10A meter range clips under full PA draw on FLEX-8000 hardware. |

None of these controls have persisted settings keys (except the °C/°F toggle). They are read-only telemetry displays.

## Temperature unit toggle

A **°C/°F** button appears in the **Radio Hardware** header row. Click it to switch the PA Temp gauge between Celsius and Fahrenheit. The setting persists between sessions.

- When toggling to Fahrenheit, gauge ticks, the label, and the displayed value all update to show °F.
- The accessible name and the underlying data source remain unchanged; only the presentation is converted.
- The gauge scale re-renders immediately when toggled, without animating across the unit change.

## Tips

- The gauge uses smoothed ballistics, so brief peaks are visible without causing flicker. Sustained red-zone readings indicate a genuine thermal condition, not a transient spike.
- The supply voltage gauge label reflects the live voltage value reported by the radio. The label updates each time a new reading arrives, so it always shows the current voltage to two decimal places (for example, `+13.82V`).
- PA current is not shown. On FLEX-8000 series hardware the PA current meter clips under full PA draw, so it has been intentionally omitted.
- Each gauge has an accessible name set for screen reader compatibility: "PA temperature", "Supply voltage", and "Main fan speed".
- The temperature unit setting is stored in the application settings under the key `MtrApplet.tempFahrenheit`.

## Troubleshooting

- **PA Temp gauge shows no movement** — The applet only receives data when connected to the radio. Verify the connection status and reconnect via `Settings > Connect to Radio...` if needed.

## Related

- [Meters overview](overview.md)
- [Check the radio's DC supply voltage](check-the-radio-s-dc-supply-voltage.md)
- [Monitor the main cooling fan speed](monitor-the-main-cooling-fan-speed.md)