# Check the Radio's Live DC Supply Voltage

The Meters applet shows the supply voltage reported live by the radio. Use it to confirm your DC power source is within a healthy range during operation.

## Before you start

- AetherSDR must be connected to the radio. The Meters applet requires an active radio connection.
- The applet panel must be visible. If it is hidden, enable it via `View > Applet Panel`.

## Steps

1. Click the **MTR** tray button on the right sidebar to open the Meters applet.
2. Read the **+13.8V** gauge. The label in the center of the bar updates live to show the current voltage — for example, `+13.82V`.

## What each control does

| Gauge | Valid range | Red above | Behavior | Accessibility |
|-------|-------------|-----------|----------|---------------|
| +13.8V | 10.0–16.0 V | 15 V | Displays the supply voltage reported by the radio. The gauge label updates dynamically to reflect the live value (e.g. `+13.82V`). | Accessible name: "Supply voltage" |
| PA Temp | 0–120 °C | 70 °C | Displays PATEMP meter reading from the radio. The temperature unit (°C or °F) is toggled by the button next to the "Radio Hardware" header. | Accessible name: "PA temperature" |
| Main Fan | 0–3000 rpm | 2500 rpm | Displays MAINFAN meter value from the radio. | Accessible name: "Main fan speed" |

## Header row controls

The **Radio Hardware** header row includes a temperature unit toggle button.

| Control | Label | Behavior | Accessibility |
|---------|-------|----------|---------------|
| Temperature unit toggle button | `°C` or `°F` | Click to toggle the PA temperature display between Celsius and Fahrenheit. The setting is persisted and restored on next launch. | Accessible description: "Toggles PA temperature display between Celsius and Fahrenheit" |

## Persisted settings

The temperature unit preference is stored under the `MtrApplet` settings key:
- `tempFahrenheit` — stored as `"True"` or `"False"` to indicate Fahrenheit or Celsius display.

## Accessibility notes

Each gauge has an accessible name set for screen reader compatibility:
- PA Temp gauge: "PA temperature"
- Supply voltage gauge: "Supply voltage"
- Main Fan gauge: "Main fan speed"
- Temperature unit toggle button: Accessible description describes its function.

These names are announced when the gauge receives focus or is navigated to with assistive technology.

## Tips

- The gauge label changes on every telemetry update from the radio, so the value shown in the bar center is always current — it is not a static placeholder.
- The bar fills cyan in the normal range and turns red above 15 V. A red bar indicates a supply voltage that is above the expected operating range.
- The PA temperature gauge turns red above 70 °C. If this occurs, reduce transmit power or duty cycle.
- Click the temperature unit toggle button (next to "Radio Hardware") to switch between Celsius and Fahrenheit. The setting is remembered across sessions.
- The Main Fan gauge turns red above 2500 rpm. This is normal during high-power operation and indicates the cooling fan is working as expected.

## Troubleshooting

- **Gauge shows no movement or a fixed label** — The radio is not connected, or the telemetry stream has not started. Confirm the connection status and reconnect via `Settings > Connect to Radio...`.

## Related

- [Meters overview](overview.md)
- [Watch PA temperature during long overs](watch-pa-temperature-during-long-overs.md)
- [Monitor the main cooling fan speed](monitor-the-main-cooling-fan-speed.md)