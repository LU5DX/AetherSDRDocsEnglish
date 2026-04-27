# Monitor the Main Cooling Fan Speed

Use the Meters applet to watch the FLEX-8600's main cooling fan speed in real time. This helps you confirm the fan is running and catch unusually high speeds that may indicate thermal stress.

## Before you start

- AetherSDR must be connected to the radio. The Meters applet requires an active radio connection.
- The applet panel must be visible. If it is hidden, enable it via `View > Applet Panel`.

## Steps

1. Locate the **MTR** tray button on the right sidebar of the applet panel.
2. Click **MTR** to toggle the Meters applet open.
3. Read the **Main Fan** gauge under the **Radio Hardware** section header.

## What each control does

| Gauge | What it shows | Valid range | Red zone |
|---|---|---|---|
| **Main Fan** | Current cooling fan speed in rpm, read from the radio's MAINFAN meter | 0–3000 rpm | Above 2500 rpm |

The gauge bar is cyan in the normal operating range and turns red above 2500 rpm.

## Tips

- The **Main Fan** gauge updates as the radio reports new meter values. There may be a brief delay after the applet first opens while the meter index is resolved.
- The gauge uses smoothed animation for value changes, so rapid fluctuations will appear as a smooth sweep rather than an instant jump.

## Troubleshooting

- **Main Fan gauge shows no movement after opening the applet** — The fan meter index is resolved lazily on first update. Wait a few seconds for the radio to emit a meter reading. If the gauge remains at zero, verify the radio connection is active via `Settings > Connect to Radio...`.

## Related

- [Meters overview](overview.md)
- [Watch PA temperature during long overs](watch-pa-temperature-during-long-overs.md)
- [Check the radio's DC supply voltage](check-the-radio-s-dc-supply-voltage.md)
