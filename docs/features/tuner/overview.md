# Tuner overview

The Tuner applet gives you control over a 4O3A Tuner Genius XL (TGXL) external antenna tuner directly from AetherSDR. From one panel you can run an autotune, monitor forward power and SWR, adjust individual relay banks, switch between antenna ports, and set the tuner's operating state.

## How it works

The Tuner applet is hidden until AetherSDR detects a connected TGXL. When the tuner is present, click the TUN tray button on the right sidebar to show or hide the applet.

The applet has three functional areas arranged top to bottom:

**Power and SWR meters** — Two horizontal gauges at the top display live readings reported by the TGXL. The forward power scale adjusts automatically based on your radio and amplifier configuration (see the table below). The SWR gauge turns red above 2.5.

**Relay bars and control buttons** — The relay bar area and the TUNE / OPERATE buttons occupy the lower portion side by side. The C1, L, and C2 bars show the current relay bank positions. When a direct TGXL connection is active, you can scroll the mousewheel over any bar to nudge that relay bank up or down. The TUNE and OPERATE buttons are always visible.

**Antenna switch row** — A row of three antenna buttons (ANT 1, ANT 2, ANT 3) appears below the relay bars only when a direct TGXL connection is active and the TGXL reports that a 3x1 antenna switch is present. The row is hidden otherwise.

## What each control does

| Control | Kind | Behavior | Range / States |
|---|---|---|---|
| Fwd Pwr | Meter | Displays TGXL-reported forward power. Scale adjusts by radio/amp configuration. | 0–200 W barefoot; 0–600 W Aurora; 0–2000 W with PGXL |
| SWR | Meter | Displays TGXL-reported SWR. Gauge turns red above 2.5. | 1.0–3.0 |
| C1 | Relay bar | Shows C1 relay bank position. Mousewheel scroll adjusts the relay when a direct TGXL connection is active. | 0–255 |
| L | Relay bar | Shows L relay bank position. Mousewheel scroll adjusts the relay when a direct TGXL connection is active. | 0–255 |
| C2 | Relay bar | Shows C2 relay bank position. Mousewheel scroll adjusts the relay when a direct TGXL connection is active. | 0–255 |
| TUNE | Button | Sends an autotune command to the TGXL. Button turns red and reads "TUNING..." during the tune. On completion, flashes the achieved SWR as "SWR x.xx" for 2.5 seconds, then returns to "TUNE". | TUNE / TUNING... / SWR x.xx |
| OPERATE | Button | Cycles the TGXL relay state. Each click advances to the next state: OPERATE (green) → BYPASS (orange) → STANDBY (default) → OPERATE. | OPERATE / BYPASS / STANDBY |
| ANT 1 | Button | Selects antenna port 1 on the TGXL 3x1 switch. Visible only when a direct TGXL connection is active and an antenna switch is present. | — |
| ANT 2 | Button | Selects antenna port 2. | — |
| ANT 3 | Button | Selects antenna port 3. | — |

## Tips

- The forward power scale is set automatically. Barefoot operation uses a 0–200 W scale with a red threshold at 125 W. An Aurora amplifier shifts the scale to 0–600 W (red above 500 W). A PGXL amplifier uses 0–2000 W (red above 1500 W).
- Mousewheel relay adjustment on C1, L, and C2 is only available when a direct TGXL connection is active. If scrolling has no effect, the connection type does not support manual relay control.
- After a tune completes, AetherSDR waits briefly before displaying the final SWR to allow the settled post-tune reading to arrive from the TGXL.

## Related

- [Run an autotune on the external TGXL](run-an-autotune-on-the-external-tgxl.md)
- [Put the tuner in OPERATE, BYPASS, or STANDBY](put-the-tuner-in-operate-bypass-or-standby.md)
- [Fine-tune the C1/L/C2 relays with the mousewheel](fine-tune-the-c1-l-c2-relays-with-the-mousewheel.md)
- [Switch between three antennas on a TGXL 3x1](switch-between-three-antennas-on-a-tgxl-3x1.md)
- [Read SWR immediately after a tune](read-swr-immediately-after-a-tune.md)
