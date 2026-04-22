# Monitor the Main Cooling Fan Speed

The Meters applet shows a live gauge of the FLEX-8600's main cooling fan speed. Use this to confirm the fan is spinning and to catch abnormally high speeds that may indicate thermal stress.

## Before you start

- AetherSDR must be connected to the radio. The Meters applet requires an active radio connection.
- The applet panel must be visible. If it is hidden, click the MTR tray button on the right sidebar to show it.

## Steps

1. Click the MTR tray button on the right sidebar. The Meters applet opens.
2. Look at the "Main Fan" gauge under the "Radio Hardware" header. The bar shows current fan speed in rpm.

## What each control does

| Label | Range | Red zone | Notes |
|---|---|---|---|
| Main Fan | 0–3000 rpm | above 2500 rpm | Bar turns red when fan speed exceeds 2500 rpm. No persisted setting. |

The gauge fills from left to right. The bar is green below 2500 rpm and turns red above 2500 rpm. Tick labels along the top read 0, 500, 1k, 1.5k, 2k, and 3k.

## Tips

- Fan speed is read from the radio's MAINFAN meter. The value updates in real time as the radio reports new readings; there is no manual refresh.
- A reading at or near 0 rpm while the radio is powered and transmitting warrants attention. Check physical connections and radio ventilation.
- Compare fan speed against the PA Temp gauge in the same applet. Rising temperature alongside high fan speed is normal during long transmissions; high temperature with low fan speed is not.

## Troubleshooting

- **Main Fan gauge shows no movement or stays at 0** — The meter index is resolved lazily after connection. Wait a few seconds for the radio to report its first MAINFAN reading. If the gauge remains at 0 while the radio is on and warm, verify the radio connection is active under `Settings > Connect to Radio...`.

## Related

- [Meters overview](overview.md)
- [Watch PA temperature during long overs](watch-pa-temperature-during-long-overs.md)
- [Check the radio's DC supply voltage](check-the-radio-s-dc-supply-voltage.md)
