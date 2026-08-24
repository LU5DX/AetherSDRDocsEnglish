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

## DAX channel selection

The DAX chooser in the AetherClock applet lets you route the selected slice's audio to a DAX channel for recording or processing. The chooser's length matches the radio's slice capacity — a 6300 exposes two receivers, a 6700 eight. Available options are:

- **DAX Off** — disables DAX routing for the selected slice.
- **DAX 1** through **DAX N** — routes audio to the corresponding DAX channel, where N is the radio's slice capacity (1–8).

## DAX controls on seam-native radios

On radios that use a seam-native audio feed rather than a DAX plane, the DAX chooser and its related warning banner are hidden. On these radios:

- Audio flows normally over the seam-native feed without a DAX channel assignment.
- A zero DAX channel is the normal, correct state — it does not indicate a missing audio path.
- The amber "no DAX channel" warning banner does not appear, because it would describe a condition that is not the cause of any audio issue.

## What the DAX warning banner means

When the DAX controls are visible (on radios that support a DAX plane), a warning banner appears if a running, bound slice has no DAX channel selected. This banner indicates that the slice is running but its audio is not being routed to any DAX channel.

If the DAX chooser is hidden (seam-native radio), the banner does not appear because the slice's audio is flowing through the radio's native feed.

## Tips

- If the indicator shows **Unlocked** for more than a few minutes, check the radio's antenna connection and ensure it has a clear view of the sky.
- The **Acquiring** state is normal after a cold start; it may take several minutes to achieve a fix.
- If you select a DAX channel that is outside the radio's slice capacity, AetherSDR automatically sets the chooser to **DAX Off** rather than showing an invalid in-range value.

## Related

- [AetherClock overview](overview.md)
- [Align the local clock to the radio's GPS timebase](align-the-local-clock-to-the-radio-s-gps-timebase.md)
- [Monitor clock drift between PC and radio](monitor-clock-drift-between-pc-and-radio.md)