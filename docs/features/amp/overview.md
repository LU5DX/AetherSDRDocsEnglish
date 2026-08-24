# Amplifier overview

The Amplifier applet provides real-time telemetry and OPERATE/STANDBY control for a connected Power Genius XL (PGXL) amplifier. Use it to monitor forward power, SWR, drain current, temperature, drain voltage, mains voltage, and fan speed.

## Before you start

- AetherSDR must be connected to a Flex radio.
- A Power Genius XL amplifier must be detected by the radio. The applet and its tray button are hidden until the radio reports a PGXL.

## How it works

The Amplifier applet appears in the right-side applet panel when AetherSDR detects a PGXL amplifier on the network. Toggle it open or closed with the **AMP** tray button on the right sidebar.

All telemetry is pushed from the radio in real time. The gauges update as the PGXL reports new values; no polling or manual refresh is needed. Live value labels (PWR, SWR, Id) update at 10 Hz to avoid flicker, and the gauge's ballistics give a slow-release peak-hold feel that matches the S-meter. The **OPERATE** / **STANDBY** button reflects the amplifier's current state and lets you switch between the two.

In v26.7.4, the temperature display gained a unit toggle. Click the temperature label to switch between Celsius (°C) and Fahrenheit (°F); the choice is persisted across sessions. In v26.8.4, the fan speed control changed from a cycle button to a pull-down menu that surfaces all three modes.

## What each control does

| Control                                          | Kind                                                                                                                                                                                     | Behavior                                                                                                                                                                                                                                                                             |
|--------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **PWR**                                          | Value + Gauge                                                                                                                                                                            | Shows PGXL forward power output as a numeric value and a gauge. The gauge shows a white peak tick held for 2.5 s after the last new peak. The numeric label only shows a value when power >= 5 W. The gauge is red above 1500 W. The SWR gauge resets to 1.0 when forward power drops below 5 W. |
| **SWR**                                          | Value + Gauge                                                                                                                                                                            | Shows PGXL SWR at the amplifier output as a numeric value and a gauge. The gauge is red above 2.5. The numeric label only appears when forward power is 5 W or greater — SWR is not meaningful at idle.                                                                               |
| **Id**                                           | Value + Gauge                                                                                                                                                                            | Shows PGXL drain current as a numeric value and a gauge. The numeric label only appears when current >= 0.5 A. The gauge is red above 60 A.                                                                                                                                           |
| **Temp**                                         | Clickable text                                                                                                                                                                           | Shows PGXL heatsink temperature as `xx.x C` (default) or `xx.x F`. Click to toggle between Celsius and Fahrenheit. The preference is saved and restored next session. Displays `tempA/tempB °C` when both sensors report, or `tempA °C` otherwise. Added in v26.7.4.                     |
| **Vdd**                                          | Text indicator                                                                                                                                                                           | Shows PGXL drain voltage as `Vdd xx V` on a direct PGXL connection. Shows a dash when the drain supply is off (vdd < 1 V) or when connected via the radio proxy. Greyed out when proxied through the radio.                                                                           |
| **Vac**                                          | Text indicator                                                                                                                                                                           | Shows PGXL mains voltage as `Vac xx V` on a direct PGXL connection. Only updated on a direct connection; greyed out when proxied through the radio.                                                                                                                                   |
| **● RADIO** / **● DIRECT**                       | Text indicator                                                                                                                                                                           | Shows the source of telemetry data. `● RADIO` when proxied through the radio, `● DIRECT` when read directly from the PGXL. Vdd/Vac/fan mode are only available on the DIRECT path.                                                                                                    |
| **Fan speed** (combo box)                        | Drop-down list                                                                                                                                                                           | Selects the PGXL fan mode from STANDARD, CONTEST, and BROADCAST. Hidden until a direct PGXL connection delivers the first fan mode status. Uses GuardedComboBox so accidental mouse-wheel scroll while hovering does not change fan mode when the dropdown is closed (#3905).          |
| **OPERATE**                                      | Button                                                                                                                                                                                   | Toggles the amplifier between OPERATE and STANDBY. Hidden until the radio reports amplifier state. Shows **OPERATE** (green) when the PGXL is in IDLE, OPERATE, TRANSMIT_A, or TRANSMIT_B state. Shows **STANDBY** when the PGXL is in STANDBY, POWERUP, or FAULT state.             |

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
   - Data source indicator (`● RADIO` / `● DIRECT`)
   - Fan speed control (drop-down)

The numeric value labels (PWR, SWR, Id) show the field name and live value in bold light-blue text.

## Temperature unit toggle

- Click the temperature label to switch between Celsius and Fahrenheit.
- The chosen unit persists across AetherSDR sessions.
- The label shows one decimal place regardless of unit.
- The tooltip announces the unit clicking would switch to.

## Fan speed control

- Select the fan mode from the **Fan speed** drop-down: STANDARD, CONTEST, or BROADCAST.
- The control is hidden until a direct PGXL connection delivers the first fan mode status.
- The drop-down prevents accidental fan mode changes from mouse-wheel scrolling while hovering over the control when the dropdown is closed.

## Accessibility

All gauges have accessible names set to "Forward power", "SWR", and "Drain current" respectively. The fan speed control sets its accessible name dynamically, for example "Fan speed: STANDARD". The temperature toggle button has an accessible description "Toggles amplifier temperature between Celsius and Fahrenheit" and can be reached with Tab key focus.

## Related

- [Put the PGXL amplifier in OPERATE](put-the-pgxl-amplifier-in-operate.md)
- [Put the PGXL amplifier in STANDBY](put-the-pgxl-amplifier-in-standby.md)
- [Monitor forward power and SWR at the amplifier output](monitor-forward-power-and-swr-at-the-amplifier-output.md)
- [Watch PGXL temperature, drain current, and mains voltage](watch-pgxl-temperature-drain-current-and-mains-voltage.md)
- Change PGXL fan speed