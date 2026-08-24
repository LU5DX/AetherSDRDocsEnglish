# Monitor the Main Cooling Fan Speed

Use the Meters applet to watch the FLEX-8600's main cooling fan speed in real time. This helps you confirm the fan is running and catch unusually high speeds that may indicate thermal stress. The applet also displays PA temperature and supply voltage gauges.

## Before you start

- AetherSDR must be connected to the radio. The Meters applet requires an active radio connection.
- The applet panel must be visible. If it is hidden, enable it via `View > Applet Panel`.

## Steps

1. Locate the **MTR** tray button on the right sidebar of the applet panel.
2. Click **MTR** to toggle the Meters applet open.
3. Read the **Main Fan** gauge under the **Radio Hardware** section header.
4. To toggle the PA temperature display between Celsius and Fahrenheit, click the **°C** or **°F** button in the header row next to the **Radio Hardware** label. The setting persists between sessions.

## What each control does

| Gauge                   | What it shows                                                                                                                                                                                                                                                                                                                                  | Valid range                                                           |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| **PA Temp**             | PA temperature, read from the radio's PATEMP meter. Displayed in Celsius by default; toggle to Fahrenheit using the **°C/°F** button in the header. The gauge label shows the live temperature value with the selected unit (e.g. **+55.0°C** or **+131.0°F**). The gauge has an accessible name of "PA temperature" for screen reader support. | 0–120 °C (32–248 °F); red above 70 °C (158 °F)                        |
| **°C / °F toggle**      | Toggles the PA temperature display between Celsius and Fahrenheit; the choice persists to the `MtrApplet` settings object (`tempFahrenheit` field). Located in the header row next to the **Radio Hardware** section label.                                                                                                                    | °C / °F                                                               |
| **+13.8V (supply voltage)** | Supply voltage in volts. The gauge label dynamically reflects the live radio-reported value (e.g. **+13.82V**) via `HGauge::setLabel`, instead of the static **+13.8V** placeholder. The gauge has an accessible name of "Supply voltage" for screen reader support.                                                                            | 10.0–16.0 V; red above 15 V                                           |
| **Main Fan**            | Current cooling fan speed in rpm, read from the radio's MAINFAN meter (resolved lazily by `MeterModel::findMeter`). The label shows the live rpm. The gauge has an accessible name of "Main fan speed" for screen reader support.                                                                                                              | 0–3000 rpm; red above 2500 rpm                                        |

Gauge bars are cyan in the normal operating range. The **PA Temp** gauge turns red above 70 °C (158 °F), the **+13.8V** gauge turns red above 15 V, and the **Main Fan** gauge turns red above 2500 rpm.

> **Note:** The **PACURRENT** meter is intentionally omitted from the Meters applet. The 10 A meter range clips under full PA draw on FLEX-8000 hardware.

## Controls

| Control | What it does |
|---------|--------------|
| **°C/°F** button | Toggles the PA temperature display between Celsius and Fahrenheit. The label updates to show the current unit. The setting persists across application restarts. |

## Tips

- The **Main Fan** gauge updates as the radio reports new meter values. There may be a brief delay after the applet first opens while the meter index is resolved.
- The gauge uses smoothed animation for value changes, so rapid fluctuations will appear as a smooth sweep rather than an instant jump.
- The **+13.8V** gauge label reflects the live voltage value reported by the radio. The label updates each time the radio sends a new meter reading, so the displayed voltage (for example, **+13.82V**) is always current.
- When you click the **°C/°F** button, the PA temperature gauge immediately updates to show values in the selected unit. The gauge scale and tick marks re-render instantly to match the selected scale, avoiding any animation across the unit jump.
- The **PA Temp** gauge is only updated when the radio reports a valid PA temperature reading; if the radio does not report one, the gauge retains its previous state rather than falling back to zero.

## Accessibility

- Each gauge has an accessible name set for screen reader compatibility:
  - **PA Temp** — "PA temperature"
  - **+13.8V** — "Supply voltage"
  - **Main Fan** — "Main fan speed"
- The **°C/°F** button has an accessible description: "Toggles PA temperature display between Celsius and Fahrenheit".

## Troubleshooting

- **Main Fan gauge shows no movement after opening the applet** — The fan meter index is resolved lazily on first update. Wait a few seconds for the radio to emit a meter reading. If the gauge remains at zero, verify the radio connection is active via `Settings > Connect to Radio...`.
- **Meters applet does not display correctly with certain themes** — The applet now applies theme styling via `applet/meter` container settings. If you experience visual issues, ensure you are using a compatible theme in `Settings > Appearance`.
- **PA temperature gauge shows "0" or does not update** — Verify the radio is transmitting and reporting PATEMP values. Some radios may not report temperature when idle. If the radio does not report a PATEMP value at all, the gauge will not update; this is expected behavior.

## Related

- [Meters overview](overview.md)
- [Watch PA temperature during long overs](watch-pa-temperature-during-long-overs.md)
- [Check the radio's DC supply voltage](check-the-radio-s-dc-supply-voltage.md)