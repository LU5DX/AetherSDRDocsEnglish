# Put the PGXL amplifier in OPERATE

This page explains how to switch a connected Power Genius XL amplifier from STANDBY to OPERATE using AetherSDR's Amplifier applet.

## Before you start

- AetherSDR must be connected to the radio. The Amplifier applet is hidden until a Power Genius XL is detected by the radio.
- The PGXL must be powered on and communicating with the FLEX-8600 so that state telemetry has arrived. The OPERATE button is hidden until the first state update is received.

## Steps

1. Locate the AMP tray button on the right sidebar of the applet panel.
2. Click AMP to open the Amplifier applet.
3. Confirm the button in the applet reads "STANDBY". This means the PGXL is currently in standby.
4. Click STANDBY. The button label changes to "OPERATE" and turns green, indicating the amplifier is now in OPERATE.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| OPERATE | When the button reads "OPERATE" (green), the PGXL is in IDLE, OPERATE, or a TRANSMIT state. Click it to send the amplifier to STANDBY. | Hidden until the first state update arrives from the radio. |
| STANDBY | When the button reads "STANDBY" (default style), the PGXL is in STANDBY, POWERUP, or FAULT. Click it to send the amplifier to OPERATE. | Same button; label and color change with state. |
| Fwd Pwr | Horizontal bar gauge showing forward power output. Range: 0–2000 W. Bar turns red above 1500 W. | |
| SWR | Horizontal bar gauge showing SWR. Range: 1.0–3.0. Bar turns red above 2.5. | |
| Temp | Horizontal bar gauge showing heatsink temperature. Range: 0–100 °C. Bar turns red above 80 °C. | |

## Tips

- If the applet panel is not visible, go to `View > Applet Panel` to show it.
- The OPERATE button reflects the PGXL's reported state, not a locally tracked toggle. If the amplifier enters FAULT or POWERUP, the button reverts to "STANDBY" automatically.

## Troubleshooting

- **The AMP tray button does not appear** — No Power Genius XL has been detected by the radio. Confirm the PGXL is powered on and correctly connected to the FLEX-8600.
- **The OPERATE button is not visible inside the applet** — The applet has opened but no state telemetry has arrived yet from the PGXL. Wait a moment; the button appears after the first state update.
- **The button shows "STANDBY" immediately after clicking** — The PGXL may be in FAULT or POWERUP and cannot enter OPERATE. Check the amplifier's front panel for fault indicators.

## Related

- [Amplifier overview](overview.md)
- [Put the PGXL amplifier in STANDBY](put-the-pgxl-amplifier-in-standby.md)
- [Monitor forward power and SWR at the amplifier output](monitor-forward-power-and-swr-at-the-amplifier-output.md)
- [Watch PGXL temperature, drain current, and mains voltage](watch-pgxl-temperature-drain-current-and-mains-voltage.md)
