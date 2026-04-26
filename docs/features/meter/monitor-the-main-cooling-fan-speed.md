# Monitor the main cooling fan speed

The Meters applet includes a "Main Fan" gauge that shows the FLEX-8600's main cooling fan speed in real time. Use it to confirm the fan is running and to catch abnormally high speeds that may indicate thermal stress.

## Before you start

- AetherSDR must be connected to the radio. The Meters applet requires an active radio connection.
- The applet panel must be visible. If it is not, enable it via `View > Applet Panel`.

## Steps

1. Click the **MTR** tray button on the right sidebar to open the Meters applet.
2. Look at the **Main Fan** gauge under the "Radio Hardware" section header.
3. Read the current fan speed from the horizontal bar. The gauge range is 0–3000 rpm. The bar turns red above 2500 rpm.

## What each control does

| Control | Description | Valid range | Redline |
|---|---|---|---|
| Main Fan | Displays the radio's main cooling fan speed. | 0–3000 rpm | > 2500 rpm (bar turns red) |
| PA Temp | Displays the PA temperature. | 0–120 °C | > 70 °C |
| +13.8V | Displays the DC supply voltage. | 10.0–16.0 V | > 15 V |

## Tips

- The Main Fan gauge updates lazily: the first reading may appear a moment after the applet opens, once the radio reports the meter value.
- The bar fills cyan through a yellow zone and turns red past 2500 rpm. Sustained red readings during a long over may indicate inadequate ventilation around the radio.

## Troubleshooting

- **Main Fan gauge shows no movement** — The meter index is resolved after the radio connection is established. If the gauge remains blank, disconnect and reconnect to the radio, then reopen the Meters applet.

## Related

- [Meters overview](overview.md)
- [Watch PA temperature during long overs](watch-pa-temperature-during-long-overs.md)
- [Check the radio's DC supply voltage](check-the-radio-s-dc-supply-voltage.md)
