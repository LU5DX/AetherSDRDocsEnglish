# Meters overview

The Meters applet displays live hardware telemetry from your Flex radio: PA temperature, DC supply voltage, and main cooling fan speed. Use it to keep an eye on radio health during operation without leaving the main AetherSDR window.

## Before you start

- AetherSDR must be connected to the radio. The Meters applet requires an active radio connection.
- The applet panel must be visible. If it is not, enable it with `View > Applet Panel`.

## How it works

The Meters applet is hidden by default. Click the MTR tray button on the right sidebar to show or hide it.

Once open, the applet displays a "Radio Hardware" section header above three horizontal bar gauges. Each gauge updates continuously from the radio's meter stream. The bar fills from left to right; color zones indicate normal (green), caution (yellow), and out-of-range (red) conditions. The gauge label is centred in the bar, and scale tick marks appear along the top edge.

The PA temperature and supply voltage readings come directly from the radio's hardware telemetry stream. The main fan speed is resolved from the radio's meter list on first update; there may be a brief delay before the fan gauge shows a reading after connection.

PA current is not shown. The FLEX-8000 series hardware caps that meter at 10 A, which causes the reading to clip under full PA draw, making it unreliable.

## What each control does

| Gauge | What it measures | Range | Red above |
|---|---|---|---|
| PA Temp | Power amplifier temperature | 0–120 °C | 70 °C |
| +13.8V | DC supply voltage | 10.0–16.0 V | 15 V |
| Main Fan | Main cooling fan speed | 0–3000 rpm | 2500 rpm |

None of these controls have persisted settings. They are read-only displays; no values can be adjusted from this applet.

## Tips

- The gauges use smoothed ballistics, so rapid fluctuations are averaged visually. A brief transient may not reach the red zone even if the instantaneous reading does.
- If the Main Fan gauge reads zero immediately after connecting, wait a moment. The fan meter index is resolved lazily on first update from the radio.

## Related

- [Watch PA temperature during long overs](watch-pa-temperature-during-long-overs.md)
- [Check the radio's DC supply voltage](check-the-radio-s-dc-supply-voltage.md)
- [Monitor the main cooling fan speed](monitor-the-main-cooling-fan-speed.md)
