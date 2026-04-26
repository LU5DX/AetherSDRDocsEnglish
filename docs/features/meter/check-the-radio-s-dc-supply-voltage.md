# Check the Radio's DC Supply Voltage

The Meters applet shows the radio's DC supply voltage in real time. Use this to confirm your power supply is delivering a stable voltage under load.

## Before you start

- AetherSDR must be connected to the radio. The Meters applet requires an active radio connection.
- The applet panel must be visible. If it is not, enable it via `View > Applet Panel`.

## Steps

1. Click the **MTR** tray button on the right sidebar to open the Meters applet.
2. Read the **+13.8V** gauge under the **Radio Hardware** section header.

The bar fills left to right. The gauge turns red when the reading exceeds 15 V.

## What each control does

| Control | What it shows | Valid range | Red above |
|---|---|---|---|
| +13.8V | DC supply voltage from the radio | 10.0–16.0 V | 15 V |

There is no persisted setting for this gauge. The value is read directly from the radio.

## Tips

- Watch the **+13.8V** gauge while transmitting. A significant voltage drop under TX load may indicate an undersized or failing power supply.
- The gauge uses smoothed ballistics, so rapid transients may not be visible at their peak instantaneous value.

## Related

- [Meters overview](overview.md)
- [Watch PA temperature during long overs](watch-pa-temperature-during-long-overs.md)
- [Monitor the main cooling fan speed](monitor-the-main-cooling-fan-speed.md)
