# Watch PGXL telemetry and control OPERATE/STANDBY

The Amplifier applet displays live telemetry from a connected Power Genius XL: forward power, SWR, drain current, heatsink temperature (toggleable C/F), drain and mains voltage (direct connection), fan speed mode, and operate/standby state. It also provides an OPERATE/STANDBY button to control the amplifier state and a fan speed selector.

## Before you start

- AetherSDR must be connected to a Flex radio.
- A Power Genius XL amplifier must be detected by the radio. The AMP tray button does not appear until the radio reports a PGXL.

## Steps

1. Locate the AMP tray button on the right sidebar of the applet panel.
2. Click AMP to open the Amplifier applet.
3. Read the **PWR** gauge for forward power. The bar turns red above 1500 W; valid range is 0–2000 W. The gauge shows a white peak tick held for 2.5 s after the last new peak. The numeric label only shows a value when power is at least 5 W.
4. Read the **SWR** gauge. The bar turns red above 2.5; valid range is 1.0–3.0. The gauge clears to 1.0 when forward power drops below 5 W and restores the cached value when power resumes. The numeric label only appears when forward power is at least 5 W.
5. Read the **Id** gauge for drain current. The bar turns red above 60 A; valid range is 0–70 A. The numeric label only appears when current is at least 0.5 A.
6. Read the **Temp** text for heatsink temperature. Click the temperature label to toggle between Celsius and Fahrenheit; the choice persists across sessions. The label shows "tempA/tempB °C" when both sensors report, or "tempA °C" otherwise.
7. Read the **Vdd** text for drain voltage on a direct PGXL connection. Shows a dash when the drain supply is off (voltage below 1.0 V) or when connected via the radio proxy.
8. Read the **Vac** text for mains voltage on a direct PGXL connection.
9. Read the **Source label** to see whether telemetry is proxied through the radio (● RADIO) or read directly from the PGXL (● DIRECT).
10. Select the **Fan Speed** dropdown to choose STANDARD, CONTEST, or BROADCAST fan mode. The dropdown is hidden until a direct PGXL connection delivers the first fan mode status.
11. Click **OPERATE** to toggle the amplifier between OPERATE and STANDBY. The button shows "OPERATE" (green) when the amplifier is in IDLE, OPERATE, or TRANSMIT_* states, and "STANDBY" otherwise. The button is hidden until the first state report arrives.

## What each control does

| Control | What it shows | Red threshold | Notes |
|---|---|---|---|
| PWR | PGXL forward power | > 1500 W | White peak tick held for 2.5 s; numeric label only when power ≥ 5 W; ballistics give a slow-release peak-hold feel matching the S-meter |
| SWR | PGXL SWR | > 2.5 | Clears to 1.0 when forward power drops below 5 W; numeric label only when power ≥ 5 W |
| Id | PGXL drain current | > 60 A | Numeric label only when current ≥ 0.5 A |
| Temp | PGXL heatsink temperature | — | Clickable button toggles between Celsius and Fahrenheit; persists to the `AmpApplet` settings object (`tempFahrenheit` field). Displays "tempA/tempB °C" when both sensors report, or "tempA °C" otherwise |
| Vdd | PGXL drain voltage | — | Shows "Vdd x.x V" on direct connection; dash when below 1.0 V or proxied through the radio. Greyed out when proxied |
| Vac | PGXL mains voltage | — | Shows "Vac N V" on direct connection. Greyed out when proxied |
| Source label | Telemetry source | — | "● RADIO" when proxied through the radio, "● DIRECT" when read directly from the PGXL |
| Fan Speed | Select STANDARD / CONTEST / BROADCAST | — | Combo box; hidden until direct connection delivers fan mode. Emits the uppercase mode for `sendCommand`. Uses a guarded combo so mouse-wheel scroll while hovering does not change the mode when the dropdown is closed |
| OPERATE | Toggle amplifier between OPERATE and STANDBY | — | Hidden until first state report. Shows "OPERATE" (green) for IDLE/OPERATE/TRANSMIT_* states, "STANDBY" otherwise |

## Tips

- Live value labels (PWR / SWR / Id) update at 10 Hz to avoid flicker.
- The **PWR** gauge shows a white peak tick held for 2.5 s after the last new peak. The gauge's ballistics give a slow-release peak-hold feel that matches the S-meter.
- The **SWR** gauge automatically clears to 1.0 when forward power drops below 5 W because SWR is not meaningful at idle. The cached value restores when power resumes.
- The **Fan Speed** combo box only appears when a direct PGXL connection is established and delivers the first fan mode status. Select the desired mode from the dropdown — no need to cycle through modes blind.
- The **Vdd** and **Vac** labels are only updated on a direct PGXL connection. When telemetry is proxied through the radio, they are greyed out. The **Source label** tells you which path is active.
- The **OPERATE** button stays in sync with the radio's authoritative state (`RadioModel::ampStateChanged`, #2437). If the PGXL state changes through the direct TCP path, the button updates immediately.
- The **Temp** tooltip announces the unit clicking would switch to.
- The **Temp** setting (Celsius/Fahrenheit) is saved per session and restored on restart.

## Troubleshooting

- **AMP tray button is not visible** — The radio has not detected a Power Genius XL. Confirm the PGXL is powered on and connected to the Flex radio.
- **OPERATE button does not appear** — The button is hidden until the amplifier sends its first state report. Wait for the PGXL to connect fully.
- **Fan Speed dropdown does not appear** — The dropdown is hidden until a direct PGXL connection delivers the first fan mode status. Ensure the PGXL is directly connected and sending fan mode telemetry.
- **Vdd/Vac labels are greyed out** — These values are only available on a direct PGXL connection. When telemetry is proxied through the radio, they are not updated.
- **Temp button does not respond** — Ensure you are clicking directly on the temperature text label, not the surrounding area. The button has a hover effect that highlights when active.
- **Old Volts/Amps indicator missing** — In v26.6.1, the Volts/Amps text indicator was replaced by separate Vdd, Vac, and Id gauges. Use the new Id gauge for drain current and the Vdd/Vac labels for voltage readings.

## Related

- [Amplifier overview](overview.md)
- [Monitor forward power and SWR at the amplifier output](monitor-forward-power-and-swr-at-the-amplifier-output.md)