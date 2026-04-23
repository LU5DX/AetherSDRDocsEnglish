# Amplifier overview

The Amplifier applet provides real-time telemetry and OPERATE/STANDBY control for a connected Power Genius XL (PGXL) amplifier. Use it to monitor forward power, SWR, temperature, drain current, and mains voltage without leaving AetherSDR.

## Before you start

- AetherSDR must be connected to a Flex radio.
- A Power Genius XL amplifier must be detected by the radio. The applet and its tray button are hidden until the radio reports a PGXL.

## How it works

The Amplifier applet appears in the right-side applet panel when AetherSDR detects a PGXL amplifier on the network. Toggle it open or closed with the **AMP** tray button on the right sidebar.

All telemetry is pushed from the radio in real time. The gauges update as the PGXL reports new values; no polling or manual refresh is needed. The **OPERATE** / **STANDBY** button reflects the amplifier's current state and lets you switch between the two.

## What each control does

| Control | Kind | Behavior | Range | Red threshold |
|---|---|---|---|---|
| **Fwd Pwr** | Gauge | Shows PGXL forward power output. | 0–2000 W | > 1500 W |
| **SWR** | Gauge | Shows PGXL SWR at the amplifier output. | 1.0–3.0 | > 2.5 |
| **Temp** | Gauge | Shows PGXL heatsink temperature. | 0–100 °C | > 80 °C |
| **Volts / Amps** | Text indicator | Displays mains voltage and drain current as `Volts: xxxV  Amps: x.xA`. Hidden until first telemetry arrives. | Integer volts, 0.1 A resolution | — |
| **MEffA** | Text indicator | Displays the PGXL MEffA value. Hidden until the radio reports a value. | — | — |
| **OPERATE** | Button | Toggles the amplifier between OPERATE and STANDBY. Hidden until the radio reports amplifier state. Shows **OPERATE** (green) when the PGXL is in IDLE, OPERATE, TRANSMIT_A, or TRANSMIT_B state. Shows **STANDBY** when the PGXL is in STANDBY, POWERUP, or FAULT state. | — | — |

The three gauges use a color-coded bar: green below the yellow threshold, yellow-amber in the caution zone, and red above the red threshold. Tick labels on each gauge are color-matched to their zone.

None of the controls have persisted settings — all values come live from the PGXL.

## Related

- [Put the PGXL amplifier in OPERATE](put-the-pgxl-amplifier-in-operate.md)
- [Put the PGXL amplifier in STANDBY](put-the-pgxl-amplifier-in-standby.md)
- [Monitor forward power and SWR at the amplifier output](monitor-forward-power-and-swr-at-the-amplifier-output.md)
- [Watch PGXL temperature, drain current, and mains voltage](watch-pgxl-temperature-drain-current-and-mains-voltage.md)
