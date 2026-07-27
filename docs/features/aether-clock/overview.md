# AetherClock overview

AetherClock is a precision timebase display and clock-alignment diagnostic applet for the AetherSDR application. It shows the radio's GNSS (GPS) lock status, measures clock drift between the radio and your local PC in nanoseconds, and allows you to align your PC clock to the radio's GPS-disciplined reference for sample-accurate timestamping.

## How it works

The AetherClock applet connects to your FLEX-8600 radio and displays three pieces of information:

- **GNSS lock status indicator** — Shows whether the radio's GPS receiver has a valid time fix. The possible states are:
  - **Locked** — The radio has a valid GNSS time reference.
  - **Unlocked** — No GNSS signal is available.
  - **Acquiring** — The radio is searching for a satellite fix.

- **Clock drift indicator** — The measured difference between the radio's GPS-disciplined clock and your local PC clock, displayed in nanoseconds. A small value (ideally under 1000 ns) indicates the clocks are well-aligned.

- **Align Clock button** — Triggers an alignment of your local PC clock to the radio's GPS reference. This synchronizes the local timebase so that timestamps applied to recorded or streamed IQ data are sample-accurate.

The applet requires an active connection to a FLEX-8600 radio. It does not persist any user settings.

## Opening the applet

Open the Applet Panel (typically docked at the bottom of the main window) and click the **AetherClock** tile (labeled **CLK**).

## What each control does

| Control | Kind | Behavior |
|---------|------|----------|
| GNSS lock indicator | Status indicator | Shows the radio's GPS/GNSS lock status (Locked, Unlocked, Acquiring). |
| Clock drift | Numeric display | Displays measured drift between radio's GPS clock and local PC clock in nanoseconds. |
| Align Clock | Push button | Triggers alignment of the local PC clock to the radio's GPS reference. |

## Related

- [Align the local clock to the radio's GPS timebase](align-the-local-clock-to-the-radio-s-gps-timebase.md)
- [Check the radio's GPS/GNSS lock status](check-the-radio-s-gps-gnss-lock-status.md)
- [Monitor clock drift between PC and radio](monitor-clock-drift-between-pc-and-radio.md)
