# Tuner overview

The Tuner applet gives you control over a 4O3A Tuner Genius XL (TGXL) external antenna tuner directly from AetherSDR. From one panel you can run an autotune, monitor forward power and SWR, inspect or trim the C1/L/C2 relay positions, set the tuner's operating state, and select among three antenna ports.

## Before you start

- Connect to a Flex radio. The applet is hidden until a Tuner Genius XL is detected.
- Confirm the TGXL is powered and communicating with the radio or directly with AetherSDR.

## How it works

When a Tuner Genius XL is detected, the `TUN` tray button appears on the right sidebar. Click `TUN` to open or close the Tuner applet.

The applet has three sections arranged top to bottom:

1. **Power and SWR meters** — live readings reported by the TGXL.
2. **Relay bars and mode buttons** — C1, L, and C2 relay positions on the left; TUNE and OPERATE/BYPASS/STANDBY buttons on the right.
3. **Antenna switch row** — ANT 1, ANT 2, and ANT 3 buttons. This row is hidden unless a direct TGXL connection is active and the TGXL reports an antenna switch.

Mousewheel scrolling on the relay bars is enabled only when a direct TGXL connection is active.

## What each control does

| Control | Kind | Behavior | Range / States |
|---|---|---|---|
| Fwd Pwr | Meter | Displays TGXL-reported forward power. Scale adjusts based on radio and amplifier configuration. | 0–200 W (barefoot); 0–600 W (Aurora); 0–2000 W (with PGXL) |
| SWR | Meter | Displays TGXL-reported SWR. Gauge turns red above 2.5. | 1.0–3.0 |
| C1 | Relay bar | Shows the C1 relay bank position. Scroll the mousewheel to adjust (direct connection required). | 0–255 |
| L | Relay bar | Shows the L relay bank position. Scroll the mousewheel to adjust (direct connection required). | 0–255 |
| C2 | Relay bar | Shows the C2 relay bank position. Scroll the mousewheel to adjust (direct connection required). | 0–255 |
| TUNE | Button | Sends an autotune command to the TGXL. Button turns red and reads "TUNING..." during the tune cycle. When complete, flashes the captured SWR as "SWR x.xx" for 2.5 seconds, then returns to "TUNE". | TUNE / TUNING... / SWR x.xx |
| OPERATE | Button | Cycles the tuner state: OPERATE (green) → BYPASS (orange) → STANDBY (default) → OPERATE. | OPERATE / BYPASS / STANDBY |
| ANT 1 | Button | Selects antenna port 1 on the TGXL 3x1 switch. | — |
| ANT 2 | Button | Selects antenna port 2 on the TGXL 3x1 switch. | — |
| ANT 3 | Button | Selects antenna port 3 on the TGXL 3x1 switch. | — |

## Tips

- The SWR value shown after a tune is captured during a short window after the tune cycle ends, giving the TGXL time to report its final settled reading. The value displayed reflects the post-tune SWR, not the peak SWR seen during the sweep.
- The antenna switch row and relay bar scrolling both require a direct TGXL connection. If you do not see the ANT 1/2/3 buttons or cannot scroll the relay bars, the applet is communicating through the radio rather than a direct connection.

## Related

- [Run an autotune on the external TGXL](run-an-autotune-on-the-external-tgxl.md)
- [Put the tuner in OPERATE, BYPASS, or STANDBY](put-the-tuner-in-operate-bypass-or-standby.md)
- [Fine-tune the C1/L/C2 relays with the mousewheel](fine-tune-the-c1-l-c2-relays-with-the-mousewheel.md)
- [Read SWR immediately after a tune](read-swr-immediately-after-a-tune.md)
- [Switch between three antennas on a TGXL 3x1](switch-between-three-antennas-on-a-tgxl-3x1.md)
