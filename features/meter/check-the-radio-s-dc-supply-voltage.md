# Check the Radio's DC Supply Voltage

The Meters applet includes a live supply voltage gauge that shows the voltage the radio is receiving from its DC power source. Use this to confirm your power supply is delivering a healthy voltage before and during operation.

## Before you start

- AetherSDR must be connected to the radio. The Meters applet requires an active radio connection.
- The applet panel must be visible. If it is hidden, use `View > Applet Panel` to show it.

## Steps

1. Locate the `MTR` tray button on the right sidebar of the applet panel.
2. Click `MTR` to open the Meters applet.
3. Read the `+13.8V` gauge under the **Radio Hardware** section header.

The bar fills from left to right. The fill color is green in the normal operating range, transitions to yellow as voltage rises toward the warning zone, and turns red above 15.0 V.

## What each control does

| Control | Description | Valid range | Red threshold |
|---|---|---|---|
| `+13.8V` | Live DC supply voltage from the radio's power input | 10.0–16.0 V | > 15.0 V |

No setting key is associated with this gauge. The value is read directly from the radio and is not persisted.

## Tips

- A reading consistently below 13.0 V under transmit load suggests the power supply or cabling cannot sustain the radio's current draw. Check your supply's rated current and cable gauge.
- The gauge uses smoothed ballistics, so sudden brief voltage sags may appear slightly softened in the display.

## Troubleshooting

- **`+13.8V` gauge shows no movement or reads 0 V** — The radio may not yet have sent telemetry. Verify the radio connection is active. The gauge updates only when the radio sends hardware telemetry data.
- **Applet panel is missing** — Click `View > Applet Panel` to restore it, then click the `MTR` tray button.

## Related

- [Meters overview](overview.md)
- [Watch PA temperature during long overs](watch-pa-temperature-during-long-overs.md)
- [Monitor the main cooling fan speed](monitor-the-main-cooling-fan-speed.md)
