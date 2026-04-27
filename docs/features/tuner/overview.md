# Tuner overview

The Tuner applet gives you real-time control over a 4O3A Tuner Genius XL (TGXL) external antenna tuner directly from AetherSDR. From a single panel you can read forward power and SWR, trigger an autotune, adjust relay banks, set the tuner operating state, and — when a TGXL 3x1 antenna switch is connected — select between three antenna ports.

## Before you start

- A Tuner Genius XL must be detected by AetherSDR. The applet is hidden until the TGXL is found.
- AetherSDR must be connected to the radio.

## How it works

The Tuner applet appears in the right-side applet panel once a TGXL is detected. Toggle its visibility with the **TUN** tray button on the right sidebar.

The applet is divided into three areas:

**Meters (top)** — Two horizontal gauges report live readings from the TGXL.

**Relay bars and buttons (middle)** — Three relay-position bars (C1, L, C2) sit to the left; TUNE and OPERATE/BYPASS/STANDBY buttons sit to the right.

**Antenna switch row (bottom)** — Three antenna selection buttons appear only when a direct TGXL connection is active and the TGXL reports that an antenna switch is present. The row is hidden otherwise.

## What each control does

| Control | Kind | Behavior | Valid range / states |
|---|---|---|---|
| **Fwd Pwr** | Meter | Displays TGXL-reported forward power. Scale adjusts automatically based on whether a PGXL or Aurora amplifier is detected. | 0–200 W (barefoot); 0–600 W (Aurora); 0–2000 W (with PGXL) |
| **SWR** | Meter | Displays TGXL-reported SWR. Gauge turns red above 2.5. | 1.0–3.0 |
| **C1** | Relay bar | Shows the C1 relay bank position. Mousewheel scroll adjusts the relay when a direct TGXL connection is active. | 0–255 |
| **L** | Relay bar | Shows the L relay bank position. Mousewheel scroll adjusts the relay when a direct TGXL connection is active. | 0–255 |
| **C2** | Relay bar | Shows the C2 relay bank position. Mousewheel scroll adjusts the relay when a direct TGXL connection is active. | 0–255 |
| **TUNE** | Button | Triggers an autotune. The button turns red and reads **TUNING...** while tuning is in progress. When tuning completes, the button briefly displays **SWR x.xx** (the settled post-tune SWR) for 2.5 seconds, then returns to **TUNE**. | — |
| **OPERATE** / **BYPASS** / **STANDBY** | Button | Cycles the TGXL relay state: OPERATE → BYPASS → STANDBY → OPERATE. Label and color reflect the current state: **OPERATE** (green), **BYPASS** (orange), **STANDBY** (default). | — |
| **ANT 1** | Button | Selects antenna port 1 on the TGXL 3x1 switch. Visible only when a direct TGXL connection is active and an antenna switch is present. | — |
| **ANT 2** | Button | Selects antenna port 2 on the TGXL 3x1 switch. | — |
| **ANT 3** | Button | Selects antenna port 3 on the TGXL 3x1 switch. | — |

## Tips

- Mousewheel scrolling on C1, L, and C2 is only enabled when a direct TGXL connection is active. If scrolling has no effect, check the connection state.
- The post-tune SWR displayed on the **TUNE** button reflects the final settled value after a short capture window, not the SWR measured mid-sweep.
- The forward power gauge scale is set automatically. No manual configuration is required when switching between barefoot, Aurora, and PGXL setups.

## Related

- [Run an autotune on the external TGXL](run-an-autotune-on-the-external-tgxl.md)
- [Put the tuner in OPERATE, BYPASS, or STANDBY](put-the-tuner-in-operate-bypass-or-standby.md)
- [Fine-tune the C1/L/C2 relays with the mousewheel](fine-tune-the-c1-l-c2-relays-with-the-mousewheel.md)
- [Switch between three antennas on a TGXL 3x1](switch-between-three-antennas-on-a-tgxl-3x1.md)
- [Read SWR immediately after a tune](read-swr-immediately-after-a-tune.md)
