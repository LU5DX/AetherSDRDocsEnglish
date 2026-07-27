# Check the radio's GPS/GNSS lock status

Open the AetherClock applet to see whether the radio's GPS receiver has a valid time fix for its precision timebase.

## Before you start

- The radio must be connected to AetherSDR.

## Steps

1. Open the **Applet panel** (click the applet tray bar at the top or bottom of the main window).
2. Click the **AetherClock** tile (labeled "CLK").
3. Look at the **GNSS lock indicator** — it shows one of three states:
   - **Locked** — the radio's GPS receiver has a valid time fix.
   - **Unlocked** — no GPS fix available.
   - **Acquiring** — the receiver is searching for satellites.

## What each control does

| Control | Purpose |
|---------|---------|
| GNSS lock indicator | Shows the current GPS/GNSS lock state (Locked, Unlocked, Acquiring). |
| Clock drift | Displays the measured drift between the radio's GPS clock and your local PC clock, in nanoseconds. |
| Align Clock | Aligns the local PC clock to the radio's GPS-disciplined reference for sample-accurate timing. |

## Tips

- If the indicator shows **Unlocked** for more than a few minutes, check the radio's antenna connection and ensure it has a clear view of the sky.
- The **Acquiring** state is normal after a cold start; it may take several minutes to achieve a fix.

## Related

- [AetherClock overview](overview.md)
- [Align the local clock to the radio's GPS timebase](align-the-local-clock-to-the-radio-s-gps-timebase.md)
- [Monitor clock drift between PC and radio](monitor-clock-drift-between-pc-and-radio.md)
