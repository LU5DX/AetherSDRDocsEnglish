# Watch PGXL telemetry and control OPERATE/STANDBY

The Amplifier applet displays live telemetry from a connected Power Genius XL: forward power, SWR, drain current, heatsink temperature, mains voltage, and amplifier efficiency. It also provides an OPERATE/STANDBY button to control the amplifier state.

## Before you start

- AetherSDR must be connected to a Flex radio.
- A Power Genius XL amplifier must be detected by the radio. The AMP tray button does not appear until the radio reports a PGXL.

## Steps

1. Locate the AMP tray button on the right sidebar of the applet panel.
2. Click AMP to open the Amplifier applet.
3. Read the **PWR** gauge for forward power. The bar turns red above 1500 W; valid range is 0–2000 W. The bar rises quickly on RF bursts and decays over ~800 ms to keep brief transmissions visible.
4. Read the **SWR** gauge. The bar turns red above 2.5; valid range is 1.0–3.0.
5. Read the **Id** gauge for drain current. The bar turns red above 60 A; valid range is 0–70 A.
6. Read the **Temp** text for heatsink temperature.
7. Read the **Vdd** text for drain voltage.
8. Read the **Vac** text for mains voltage.
9. Read the **MEffA** indicator for amplifier efficiency metric (added in v26.5.1). This indicator is hidden until the first telemetry arrives.
10. Click **OPERATE** to toggle the amplifier between OPERATE and STANDBY. The button shows "OPERATE" (green) when the amplifier is in IDLE, OPERATE, or TRANSMIT_* states, and "STANDBY" otherwise. The button is hidden until the first state report arrives.

## What each control does

| Control | What it shows | Red threshold | Notes |
|---|---|---|---|
| PWR | PGXL forward power | > 1500 W | Gauge with ballistic decay for brief transmissions |
| SWR | PGXL SWR | > 2.5 | — |
| Id | PGXL drain current | > 60 A | Added in v26.6.1, replaces separate Volts/Amps indicator |
| Temp | PGXL heatsink temperature | > 80 °C | Displayed as text label |
| Vdd | PGXL drain voltage | — | Displayed as text label |
| Vac | PGXL mains voltage | — | Displayed as text label |
| MEffA | PGXL amplifier efficiency metric | — | Hidden until first telemetry. Added in v26.5.1 |
| OPERATE | Toggle amplifier between OPERATE and STANDBY | — | Hidden until first state report. Green for OPERATE, default for STANDBY |

## Tips

- The **PWR** gauge uses ballistic decay to keep brief transmissions visible — the bar rises immediately on RF and decays over approximately 800 ms.
- The **MEffA** indicator remains hidden until the PGXL sends its first efficiency telemetry. If it does not appear, the amplifier may not yet be sending this metric.
- The **OPERATE** button stays in sync with the radio's authoritative state. If the PGXL state changes through the direct TCP path, the button updates immediately (v0.9.8+).
- The **Temp** gauge uses three color zones: green below 55 °C, yellow from 55 °C to 80 °C, and red above 80 °C.

## Troubleshooting

- **AMP tray button is not visible** — The radio has not detected a Power Genius XL. Confirm the PGXL is powered on and connected to the Flex radio.
- **MEffA indicator does not appear** — The applet hides this indicator until the first telemetry update. Wait for the PGXL to send an efficiency measurement, or check the amplifier connection.
- **OPERATE button does not appear** — The button is hidden until the amplifier sends its first state report. Wait for the PGXL to connect fully.
- **Old Volts/Amps indicator missing** — In v26.6.1, the Volts/Amps text indicator was replaced by separate Vdd, Vac, and Id gauges. Use the new Id gauge for drain current and the Vdd/Vac labels for voltage readings.

## Related

- [Amplifier overview](overview.md)
- [Monitor forward power and SWR at the amplifier output](monitor-forward-power-and-swr-at-the-amplifier-output.md)