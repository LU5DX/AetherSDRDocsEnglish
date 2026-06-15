# Watch PGXL telemetry and control OPERATE/STANDBY

The Amplifier applet displays live telemetry from a connected Power Genius XL: forward power, SWR, drain current, heatsink temperature, mains voltage, and amplifier efficiency. It also provides an OPERATE/STANDBY button to control the amplifier state and a Fan Speed button to cycle through fan modes.

## Before you start

- AetherSDR must be connected to a Flex radio.
- A Power Genius XL amplifier must be detected by the radio. The AMP tray button does not appear until the radio reports a PGXL.

## Steps

1. Locate the AMP tray button on the right sidebar of the applet panel.
2. Click AMP to open the Amplifier applet.
3. Read the **PWR** gauge for forward power. The bar turns red above 1500 W; valid range is 0–2000 W. The bar rises quickly on RF bursts and decays over ~800 ms to keep brief transmissions visible.
4. Read the **SWR** gauge. The bar turns red above 2.5; valid range is 1.0–3.0. The gauge clears to 1.0 when forward power drops below 5 W and restores the cached value when power resumes.
5. Read the **Id** gauge for drain current. The bar turns red above 60 A; valid range is 0–70 A.
6. Read the **Temp** text for heatsink temperature.
7. Read the **Vdd** text for drain voltage. Shows a dash when drain supply is off (voltage below 1.0 V).
8. Read the **Vac** text for mains voltage.
9. Read the **MEffA** indicator for amplifier efficiency metric (added in v26.5.1). This indicator is hidden until the first telemetry arrives.
10. Click the **Fan Speed** button to cycle through STANDARD, CONTEST, and BROADCAST modes. The button shows a single letter (S, C, or B). The button is hidden until the first fan mode status arrives from a direct PGXL connection. Added in v26.6.3.
11. Click **OPERATE** to toggle the amplifier between OPERATE and STANDBY. The button shows "OPERATE" (green) when the amplifier is in IDLE, OPERATE, or TRANSMIT_* states, and "STANDBY" otherwise. The button is hidden until the first state report arrives.

## What each control does

| Control | What it shows | Red threshold | Notes |
|---|---|---|---|
| PWR | PGXL forward power | > 1500 W | Gauge with ballistic decay for brief transmissions; accessible name "Forward power" |
| SWR | PGXL SWR | > 2.5 | Clears to 1.0 when forward power drops below 5 W; accessible name "SWR" |
| Id | PGXL drain current | > 60 A | Accessible name "Drain current" |
| Temp | PGXL heatsink temperature | > 80 °C | Displayed as text label |
| Vdd | PGXL drain voltage | — | Shows dash when below 1.0 V |
| Vac | PGXL mains voltage | — | Displayed as text label |
| MEffA | PGXL amplifier efficiency metric | — | Hidden until first telemetry. Added in v26.5.1 |
| Fan Speed | Cycle STANDARD / CONTEST / BROADCAST | — | Hidden until direct PGXL connection delivers fan mode. Shows first letter of current mode (S/C/B). Added in v26.6.3 |
| OPERATE | Toggle amplifier between OPERATE and STANDBY | — | Hidden until first state report. Green for OPERATE, default for STANDBY |

## Tips

- The **PWR** gauge uses ballistic decay to keep brief transmissions visible — the bar rises immediately on RF and decays over approximately 800 ms.
- The **SWR** gauge automatically clears to 1.0 when forward power drops below 5 W because SWR is not meaningful at idle. The cached value restores when power resumes.
- The **MEffA** indicator remains hidden until the PGXL sends its first efficiency telemetry. If it does not appear, the amplifier may not yet be sending this metric.
- The **OPERATE** button stays in sync with the radio's authoritative state. If the PGXL state changes through the direct TCP path, the button updates immediately (v0.9.8+).
- The **Temp** gauge uses three color zones: green below 55 °C, yellow from 55 °C to 80 °C, and red above 80 °C.
- The **Fan Speed** button only appears when a direct PGXL connection is established and delivers the first fan mode status. Click to cycle through STANDARD, CONTEST, and BROADCAST modes.
- The **Vdd** label shows a dash when the drain supply is off (voltage below 1.0 V), making it clear the supply is off rather than reading zero.

## Troubleshooting

- **AMP tray button is not visible** — The radio has not detected a Power Genius XL. Confirm the PGXL is powered on and connected to the Flex radio.
- **MEffA indicator does not appear** — The applet hides this indicator until the first telemetry update. Wait for the PGXL to send an efficiency measurement, or check the amplifier connection.
- **OPERATE button does not appear** — The button is hidden until the amplifier sends its first state report. Wait for the PGXL to connect fully.
- **Fan Speed button does not appear** — The button is hidden until a direct PGXL connection delivers the first fan mode status. Ensure the PGXL is directly connected and sending fan mode telemetry.
- **Old Volts/Amps indicator missing** — In v26.6.1, the Volts/Amps text indicator was replaced by separate Vdd, Vac, and Id gauges. Use the new Id gauge for drain current and the Vdd/Vac labels for voltage readings.

## Related

- [Amplifier overview](overview.md)
- [Monitor forward power and SWR at the amplifier output](monitor-forward-power-and-swr-at-the-amplifier-output.md)