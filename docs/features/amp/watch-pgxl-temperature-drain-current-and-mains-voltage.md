# Watch PGXL temperature, drain current, and mains voltage

The Amplifier applet displays live heatsink temperature, drain current, and mains voltage from a connected Power Genius XL. Use these readings to monitor amplifier health during a session.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- A Power Genius XL amplifier must be detected by the radio. The AMP tray button does not appear until the radio reports a PGXL.

## Steps

1. Locate the AMP tray button on the right sidebar of the applet panel.
2. Click AMP to open the Amplifier applet.
3. Read the **Temp** gauge for heatsink temperature. The bar turns red above 80 °C; valid range is 0–100 °C.
4. Read the **Volts / Amps** text indicator for mains voltage and drain current. The format is `Volts: xxxV  Amps: x.xA`. This indicator is hidden until the first telemetry arrives from the PGXL.

## What each control does

| Control | What it shows | Red threshold | Valid range |
|---|---|---|---|
| Temp | PGXL heatsink temperature | > 80 °C | 0–100 °C |
| Volts / Amps | Mains voltage (integer volts) and drain current (one decimal place, amps) | — | Integer volts; x.x A |

## Tips

- The **Volts / Amps** indicator remains hidden until the PGXL sends its first telemetry update. If it does not appear, the amplifier may not yet be transmitting telemetry — verify the PGXL is powered and communicating with the radio.
- The **Temp** gauge uses three color zones: green below 55 °C, yellow from 55 °C to 80 °C, and red above 80 °C.

## Troubleshooting

- **AMP tray button is not visible** — The radio has not detected a Power Genius XL. Confirm the PGXL is powered on and connected to the FLEX-8600.
- **Volts / Amps line does not appear** — The applet hides this indicator until the first telemetry arrives. Wait for the PGXL to send a telemetry update, or check the amplifier connection.

## Related

- [Amplifier overview](overview.md)
- [Monitor forward power and SWR at the amplifier output](monitor-forward-power-and-swr-at-the-amplifier-output.md)
