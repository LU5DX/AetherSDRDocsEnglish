# Meters overview

The Meters applet displays real-time hardware telemetry from the connected FLEX-8600: PA temperature, DC supply voltage, and main cooling fan speed. Use it to watch radio health during operation without leaving the main AetherSDR window.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The applet requires an active radio connection.
- The applet panel must be visible. If it is hidden, enable it via `View > Applet Panel`.

## How it works

The Meters applet is hidden by default. Toggle it open or closed using the **MTR** tray button on the right sidebar.

Once open, the applet shows a "Radio Hardware" section containing three horizontal bar gauges. Each gauge fills from left to right and changes color as the value climbs through warning and alarm zones:

- The bar is **green** below the yellow threshold.
- The bar turns **yellow-amber** between the yellow and red thresholds.
- The bar turns **red** above the red threshold.

Tick labels along the top of each gauge are colored to match the zone they fall in. Values are smoothed with ballistic animation so rapid changes do not cause jarring jumps.

PA temperature and supply voltage are reported directly from the radio's hardware telemetry stream. Main fan speed is resolved by meter name when the radio first publishes it and updated as readings arrive.

The applet now applies the active application theme to the meters container using the theme manager. This ensures the meters area matches the look and feel of other applets in the current theme.

## What each control does

| Gauge        | What it shows               | Valid range |
|--------------|-----------------------------|-------------|
| **PA Temp**  | Power amplifier temperature | 0–120 °C or 32–248 °F |
| **+13.8V**   | DC supply voltage           | 10.0–16.0 V |
| **Main Fan** | Main cooling fan speed      | 0–3000 rpm  |

### PA Temp gauge

The PA Temp gauge displays the power amplifier temperature reading from the PATEMP meter. The gauge label dynamically updates to show the current temperature in the selected unit (e.g. "55.0°C" or "131.0°F").

Use the **°C/°F** toggle button in the header row to switch between Celsius and Fahrenheit display. Clicking the button toggles the temperature unit for all PA Temp readings. The setting is persisted in `MtrApplet.tempFahrenheit` and survives application restarts.

The gauge ticks adjust automatically when switching units:
- Celsius ticks: 0, 30, 55, 70, 90, 120 °C
- Fahrenheit ticks: 32, 86, 131, 158, 194, 248 °F

The red threshold is reached at 70 °C (158 °F).

### Supply voltage gauge

The label on the **+13.8V** gauge dynamically updates to reflect the live voltage value reported by the radio. For example, when the radio reports 13.82 V, the gauge label reads **+13.82V**. The gauge red threshold is 15 V.

### Main Fan gauge

The Main Fan gauge displays the MAINFAN meter value. The speed will read zero until the radio publishes the MAINFAN meter, which is normal for the first few seconds after connecting.

**Note:** PA current is not displayed. On FLEX-8000 series hardware the PA current meter is capped at 10 A, which causes the reading to clip under full PA draw, making it unreliable.

### Temperature unit toggle

A **°C/°F** button appears in the header row of the applet, to the right of the "Radio Hardware" label. This button toggles the PA temperature display unit. When you click it:

- The button label changes to the opposite unit.
- The PA Temp gauge value and tick labels update to the new unit.
- The setting is saved in the application configuration under the `MtrApplet.tempFahrenheit` key.

The toggle button has hover and focus styling consistent with the current theme. It includes an accessible description for screen readers: "Toggles PA temperature display between Celsius and Fahrenheit".

## Accessibility

Each gauge has a programmatic accessible name that screen readers can announce:

- **PA Temp** gauge: "PA temperature"
- **Supply voltage** gauge: "Supply voltage"
- **Main Fan** gauge: "Main fan speed"
- **Temperature unit toggle** button: "Toggles PA temperature display between Celsius and Fahrenheit"

These accessible names are set using the Qt accessibility framework and are available to assistive technology on all supported platforms.

## Tips

- A PA Temp reading that regularly reaches the red zone (above 70 °C / 158 °F) during long transmissions may indicate inadequate ventilation around the radio.
- The voltage gauge red threshold is 15 V. Readings consistently above that value suggest a power supply regulation issue worth investigating.
- Main Fan speed will read zero until the radio publishes the MAINFAN meter. This is normal for the first few seconds after connecting.

## Related

- [Watch PA temperature during long overs](watch-pa-temperature-during-long-overs.md)
- [Check the radio's DC supply voltage](check-the-radio-s-dc-supply-voltage.md)
- [Monitor the main cooling fan speed](monitor-the-main-cooling-fan-speed.md)