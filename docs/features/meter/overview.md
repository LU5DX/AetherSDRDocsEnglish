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

## What each control does

| Gauge | What it shows | Valid range | Red above |
|---|---|---|---|
| **PA Temp** | Power amplifier temperature | 0–120 °C | 70 °C |
| **+13.8V** | DC supply voltage | 10.0–16.0 V | 15 V |
| **Main Fan** | Main cooling fan speed | 0–3000 rpm | 2500 rpm |

None of the gauges have persisted settings or user-adjustable controls. There are no `AppSettings` keys associated with this applet.

**Note:** PA current is not displayed. On FLEX-8000 series hardware the PA current meter is capped at 10 A, which causes the reading to clip under full PA draw, making it unreliable.

## Tips

- A PA Temp reading that regularly reaches the red zone (above 70 °C) during long transmissions may indicate inadequate ventilation around the radio.
- The +13.8V gauge red threshold is 15 V. Readings consistently above that value suggest a power supply regulation issue worth investigating.
- Main Fan speed will read zero until the radio publishes the MAINFAN meter. This is normal for the first few seconds after connecting.

## Related

- [Watch PA temperature during long overs](watch-pa-temperature-during-long-overs.md)
- [Check the radio's DC supply voltage](check-the-radio-s-dc-supply-voltage.md)
- [Monitor the main cooling fan speed](monitor-the-main-cooling-fan-speed.md)
