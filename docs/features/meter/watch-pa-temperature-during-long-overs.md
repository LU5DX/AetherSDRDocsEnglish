# Watch PA temperature during long overs

The Meters applet shows a live PA Temp gauge pulled directly from the radio. Use it to keep an eye on power amplifier temperature when running high-duty-cycle modes such as FT8, RTTY, or long CW overs.

## Before you start

- AetherSDR must be connected to the radio. The Meters applet requires an active radio connection.
- The applet panel must be visible. If it is hidden, enable it with `View > Applet Panel`.

## Steps

1. Locate the **MTR** tray button on the right sidebar of the applet panel.
2. Click **MTR** to toggle the Meters applet open.
3. Read the **PA Temp** gauge under the **Radio Hardware** section header.
4. Watch the bar colour as temperature rises: the bar is green below 55 °C, yellow from 55 °C to 70 °C, and red above 70 °C.

## What each control does

| Control | What it shows | Valid range | Red threshold |
|---|---|---|---|
| PA Temp | Power amplifier temperature from the radio | 0–120 °C | Above 70 °C |
| +13.8V | DC supply voltage | 10.0–16.0 V | Above 15 V |
| Main Fan | Main cooling fan speed | 0–3000 rpm | Above 2500 rpm |

No settings keys are associated with these meters. All values are read-only telemetry from the radio.

## Tips

- The gauge bar animates smoothly between readings — a sudden jump to red is a real hardware event, not a display glitch.
- If PA Temp is climbing toward 70 °C during a contest or digital over, reduce duty cycle or transmit power to allow the amplifier to cool.
- Checking Main Fan alongside PA Temp can help distinguish a ventilation problem from a high-power one.

## Troubleshooting

- **All gauges read zero or are unresponsive** — the applet requires an active radio connection. Confirm the radio is connected via `Settings > Connect to Radio...` before using the Meters applet.
- **PA Temp gauge stays at zero even when transmitting** — the radio may not yet have sent a telemetry update. Wait a few seconds after keying up. If it remains at zero, check your network connection to the radio.

## Related

- [Meters overview](overview.md)
- [Monitor the main cooling fan speed](monitor-the-main-cooling-fan-speed.md)
- [Check the radio's DC supply voltage](check-the-radio-s-dc-supply-voltage.md)
