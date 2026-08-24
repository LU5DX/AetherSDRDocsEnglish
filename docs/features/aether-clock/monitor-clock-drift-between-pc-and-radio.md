# Monitor clock drift between PC and radio

The AetherClock applet displays the measured clock drift between your PC and the radio's GPS-disciplined timebase, allowing you to monitor timing accuracy for sample-accurate timestamping and diagnostics.

## Before you start

- Ensure AetherSDR is connected to a FLEX-8600 radio
- The radio must have GPS/GNSS capability for drift monitoring

## Steps

1. Open the Applet Panel tray.
2. Click the **AetherClock** tile (labeled "CLK").
3. Read the **Clock drift** indicator to see the measured drift in nanoseconds.
4. If the drift is high or inconsistent, check the **GNSS lock indicator** — drift monitoring is only valid when the radio's GPS receiver has lock.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| GNSS lock indicator | Indicator | Shows the radio's GPS/GNSS lock status: **Locked**, **Unlocked**, or **Acquiring**. Drift data is only meaningful when locked. |
| Clock drift | Indicator | Measured drift between the radio's GPS clock and the local PC clock, displayed in nanoseconds. |
| Align Clock | Push button | Aligns the local PC clock to the radio's GPS-disciplined reference for sample-accurate timing. |

## Troubleshooting

- **Clock drift reading is erratic or shows extreme values** — The radio may not have GPS/GNSS lock. Check the GNSS lock indicator; if it shows **Unlocked** or **Acquiring**, wait for lock before relying on the drift reading.
- **No drift reading visible** — Verify the radio is connected and has GPS capabilities. The AetherClock applet requires an active radio connection.

## Related

- [AetherClock overview](overview.md)
- [Align the local clock to the radio's GPS timebase](align-the-local-clock-to-the-radio-s-gps-timebase.md)
- [Check the radio's GPS/GNSS lock status](check-the-radio-s-gps-gnss-lock-status.md)