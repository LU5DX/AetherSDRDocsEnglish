# Meters overview

The Meters applet displays live hardware telemetry from the connected FLEX-8600: PA temperature, DC supply voltage, and main cooling fan speed. Use it to keep an eye on the radio's thermal and electrical health during operation.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The applet does not display data without an active radio connection.
- The applet panel must be visible. If it is hidden, enable it with `View > Applet Panel`.

## How it works

The Meters applet is hidden by default. Click the **MTR** tray button on the right sidebar to show or hide it.

Once open, the applet shows three horizontal bar gauges under the **Radio Hardware** section heading. Each gauge fills from left to right and changes color as the reading climbs through normal, caution, and warning zones. The bar is cyan in the normal range, yellow in the caution zone, and red once the reading crosses the threshold.

Gauge values are smoothed with ballistic animation — the bar follows rapid changes with a brief settling motion rather than jumping instantly. This mirrors the feel of a physical meter movement.

PA temperature and supply voltage are delivered as cached telemetry from the radio. Fan speed is resolved separately once the radio reports its meter list; the fan gauge may read zero briefly at connection time until that lookup completes.

PA current is not shown. The FLEX-8000 series hardware reports PA current on a 10 A scale, which clips under full PA draw and produces a misleading reading.

## What each control does

| Gauge | What it shows | Normal range | Red above | Unit |
|---|---|---|---|---|
| **PA Temp** | Power amplifier temperature | 0–70 °C | 70 °C | °C |
| **+13.8V** | DC supply voltage | 10.0–15.0 V | 15 V | V |
| **Main Fan** | Main cooling fan speed | 0–2500 rpm | 2500 rpm | rpm |

Full scale values: PA Temp 120 °C, +13.8V 16.0 V, Main Fan 3000 rpm.

None of the gauges have persisted settings or user-adjustable controls. They are read-only displays of radio-reported values.

## Tips

- Watch **PA Temp** during long transmit overs or contest operating. A reading consistently above 70 °C warrants attention to ventilation around the radio.
- A **+13.8V** reading above 15 V or below about 12 V suggests a power supply problem worth investigating before further operation.
- **Main Fan** readings above 2500 rpm indicate the radio is working hard thermally; check airflow and ambient temperature.

## Related

- [Watch PA temperature during long overs](watch-pa-temperature-during-long-overs.md)
- [Check the radio's DC supply voltage](check-the-radio-s-dc-supply-voltage.md)
- [Monitor the main cooling fan speed](monitor-the-main-cooling-fan-speed.md)
