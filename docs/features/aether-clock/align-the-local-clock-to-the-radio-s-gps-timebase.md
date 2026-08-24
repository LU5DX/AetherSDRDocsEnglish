# Align the local clock to the radio's GPS timebase

Use this procedure to synchronize your PC's clock to the FLEX-8600's GPS-disciplined precision timebase for sample-accurate timestamping across your station.

## Before you start

- Ensure the radio is connected to AetherSDR.
- Verify the radio has GPS/GNSS lock (see [Check the radio's GPS/GNSS lock status](check-the-radio-s-gps-gnss-lock-status.md)).

## Steps

1. Open the Applet panel and click the **AetherClock** tile.
2. Confirm the **GNSS lock indicator** shows "Locked".
3. Note the **Clock drift** value in nanoseconds — this is the current offset between the radio's GPS clock and your PC's clock.
4. Click **Align Clock**.

AetherSDR adjusts your local system clock to match the radio's GPS timebase. The **Clock drift** indicator should reset to near zero.

## What each control does

| Control | Purpose |
|---------|---------|
| **GNSS lock indicator** | Shows the radio's GPS/GNSS lock status: Locked, Unlocked, or Acquiring. |
| **Clock drift** | Displays measured drift between the radio's GPS clock and your PC's clock in nanoseconds. |
| **Align Clock** | Aligns the local PC clock to the radio's GPS-disciplined reference. |

## DAX channel selection

The DAX chooser in the AetherClock applet selects which DAX channel routes audio for the currently selected slice.

The number of DAX channels available matches the radio's slice capacity:

- On radios with 2 receivers, the chooser offers DAX 1 and DAX 2.
- On radios with 8 receivers, the chooser offers DAX 1 through DAX 8.
- **DAX Off** is always available as the first option.

If a selected slice has a DAX channel assigned that is out of range for the current radio, the chooser displays **DAX Off** rather than an invalid in-range value.

On radios that do not have a DAX plane at all, the DAX chooser is hidden, and the amber "no DAX channel" warning banner is suppressed because audio flows normally over the radio's built-in feed.

## Tips

- The radio must have GNSS lock before alignment will be accurate. If the indicator shows "Unlocked" or "Acquiring", wait until it shows "Locked".
- After alignment, the **Clock drift** value should remain near zero if the radio maintains lock.

## Troubleshooting

- **GNSS lock indicator shows "Unlocked"** — The radio's GPS receiver has no valid time fix. Ensure the radio has a clear view of the sky or sufficient satellite reception.
- **Clock drift remains high after clicking Align Clock** — Your system may require root/administrator privileges to change the system clock. On Linux, ensure your user has permission or run AetherSDR with the `CAP_SYS_TIME` capability.
- **DAX chooser is missing or shows fewer channels than expected** — The chooser is sized to the radio's slice capacity. On radios without a DAX plane, the control is hidden entirely.

## Related

- [Check the radio's GPS/GNSS lock status](check-the-radio-s-gps-gnss-lock-status.md)
- [Monitor clock drift between PC and radio](monitor-clock-drift-between-pc-and-radio.md)
- [AetherClock overview](overview.md)