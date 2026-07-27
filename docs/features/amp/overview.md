# Amplifier overview

The Amplifier applet provides real-time telemetry and OPERATE/STANDBY control for a connected Power Genius XL (PGXL) amplifier. Use it to monitor forward power, SWR, drain current, temperature, drain voltage, mains voltage, amplifier efficiency, and fan speed.

## Before you start

- AetherSDR must be connected to a Flex radio.
- A Power Genius XL amplifier must be detected by the radio. The applet and its tray button are hidden until the radio reports a PGXL.

## How it works

The Amplifier applet appears in the right-side applet panel when AetherSDR detects a PGXL amplifier on the network. Toggle it open or closed with the **AMP** tray button on the right sidebar.

All telemetry is pushed from the radio in real time. The gauges update as the PGXL reports new values; no polling or manual refresh is needed. The **OPERATE** / **STANDBY** button reflects the amplifier's current state and lets you switch between the two.

In v26.7.4, the temperature display gained a unit toggle. Click the temperature label to switch between Celsius (°C) and Fahrenheit (°F); the choice is persisted across sessions.

## What each control does

| Control             | Kind              | Behavior                                                                                                                                                                                                                                                                 |
|---------------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **PWR**             | Value + Gauge     | Shows PGXL forward power output as a numeric value and a gauge. The gauge bar rises quickly on RF bursts and decays over ~800 milliseconds, making brief transmissions still visible. The gauge is red above 1500 W. The SWR gauge resets to 1.0 when forward power drops below 5 W. |
| **SWR**             | Value + Gauge     | Shows PGXL SWR at the amplifier output as a numeric value and a gauge. The gauge is red above 2.5. The gauge only updates when forward power is 5 W or greater — SWR is not meaningful at idle.                                                                           |
| **Id**              | Value + Gauge     | Shows PGXL drain current as a numeric value and a gauge. The gauge is red above 60 A.                                                                                                                                                                                    |
| **Temp**            | Clickable text    | Shows PGXL heatsink temperature as `xx.x C` (default) or `xx.x F`. Click to toggle between Celsius and Fahrenheit. The preference is saved and restored next session. Added in v26.7.4.                                                                                    |
| **Vdd**             | Text indicator    | Shows PGXL drain voltage as `Vdd xx V`. When the drain supply is off (standby), shows `Vdd — V` instead of `0.0 V`.                                                                                                                                                  |
| **Vac**             | Text indicator    | Shows PGXL mains voltage as `Vac xx V`.                                                                                                                                                                                                                                 |
| **MEffA**           | Text indicator    | Shows the PGXL amplifier efficiency metric (meffa). Hidden until the first meffa telemetry arrives. Added in v26.5.1.                                                                                                                                                    |
| **● RADIO**         | Text indicator    | Shows the source of telemetry data. Appears after first telemetry arrives.                                                                                                                                                                                              |
| **Fan: Std** / **Fan: Contest** / **Fan: Bcast** | Button | Fan speed control button with textual label. Hidden until a direct PGXL connection delivers the first fan mode status. Click to cycle through STANDARD, CONTEST, and BROADCAST. In v26.7.4 the label was changed from a single letter (S/C/B) to a descriptive text. |
| **OPERATE**         | Button            | Toggles the amplifier between OPERATE and STANDBY. Hidden until the radio reports amplifier state. Shows **OPERATE** (green) when the PGXL is in IDLE, OPERATE, TRANSMIT_A, or TRANSMIT_B state. Shows **STANDBY** when the PGXL is in STANDBY, POWERUP, or FAULT state. |

The three gauges use a color-coded bar: green below the yellow threshold, yellow-amber in the caution zone, and red above the red threshold. Tick labels on each gauge are color-matched to their zone.

The temperature unit preference is the only persisted setting — all other values come live from the PGXL.

## Layout

The Amplifier applet displays telemetry in two sections:

1. **Top section:** Three rows, each with a label on the left and a gauge on the right:
   - **PWR** — forward power (0–2000 W, red > 1500 W)
   - **SWR** — SWR (1.0–3.0, red > 2.5)
   - **Id** — drain current (0–70 A, red > 60 A)

2. **Bottom section:** A text information stack on the left and the **OPERATE** button on the right:
   - Temperature (Temp, clickable to toggle °C/°F)
   - Drain voltage (Vdd)
   - Mains voltage (Vac)
   - Amplifier efficiency (MEffA)
   - Data source indicator (`● RADIO`)
   - Fan speed control button

The numeric value labels (PWR, SWR, Id) show the field name and live value in bold light-blue text.

## Temperature unit toggle

- Click the temperature label to switch between Celsius and Fahrenheit.
- The chosen unit persists across AetherSDR sessions.
- The label shows one decimal place regardless of unit.

## Accessibility

All gauges have accessible names set to "Forward power", "SWR", and "Drain current" respectively. The fan speed button sets its accessible name dynamically, for example "Fan speed: STANDARD". The temperature toggle button has an accessible description "Toggles amplifier temperature between Celsius and Fahrenheit" and can be reached with Tab key focus.

## Related

- [Put the PGXL amplifier in OPERATE](put-the-pgxl-amplifier-in-operate.md)
- [Put the PGXL amplifier in STANDBY](put-the-pgxl-amplifier-in-standby.md)
- [Monitor forward power and SWR at the amplifier output](monitor-forward-power-and-swr-at-the-amplifier-output.md)
- [Watch PGXL temperature, drain current, and mains voltage](watch-pgxl-temperature-drain-current-and-mains-voltage.md)
- Change PGXL fan speed