# Check the Radio's DC Supply Voltage

The Meters applet shows a live +13.8V supply voltage gauge sourced directly from the radio. Use this to confirm your power supply is delivering adequate voltage before or during operation.

## Before you start

- AetherSDR must be connected to the radio. The Meters applet requires an active radio connection.
- The applet panel must be visible. If it is hidden, enable it via `View > Applet Panel`.

## Steps

1. Locate the **MTR** tray button on the right sidebar of the applet panel.
2. Click **MTR** to toggle the Meters applet open.
3. Read the **+13.8V** gauge under the **Radio Hardware** section header.

## What each control does

| Label | What it shows | Valid range | Red above |
|-------|--------------|-------------|-----------|
| +13.8V | DC supply voltage from the radio's power input | 10.0–16.0 V | 15 V |

The gauge bar fills cyan in the normal operating range and turns red when the reading exceeds 15 V. The display updates in real time with smoothed ballistics.

## Tips

- A healthy supply typically reads near 13.8 V under receive conditions and may dip slightly under heavy TX load. A reading consistently below 12 V or above 15 V warrants attention to your power supply.
- The gauge scale marks are at 10.5, 12, 13.8, and 15 V for quick visual reference.

## Troubleshooting

- **+13.8V gauge shows no movement or reads 0** — The radio is not connected or the meter data has not been received yet. Verify the connection status and reconnect via `Settings > Connect to Radio...`.

## Related

- [Meters overview](overview.md)
- [Watch PA temperature during long overs](watch-pa-temperature-during-long-overs.md)
- [Monitor the main cooling fan speed](monitor-the-main-cooling-fan-speed.md)
