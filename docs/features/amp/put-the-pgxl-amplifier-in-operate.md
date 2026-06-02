# Put the PGXL amplifier in OPERATE

This page explains how to switch a connected Power Genius XL amplifier from STANDBY to OPERATE using AetherSDR's Amplifier applet.

## Before you start

- AetherSDR must be connected to the radio. The Amplifier applet is hidden until a Power Genius XL is detected by the radio.
- The PGXL must be powered on and communicating with the Flex radio so that state telemetry has arrived. The OPERATE button is hidden until the first state update is received.

## Steps

1. Locate the AMP tray button on the right sidebar of the applet panel.
2. Click AMP to open the Amplifier applet.
3. Confirm the button in the applet reads "STANDBY". This means the PGXL is currently in standby.
4. Click STANDBY. The button label changes to "OPERATE" and turns green, indicating the amplifier is now in OPERATE.

## What each control does

| Control | Behavior                                                                                                                                                                                                                                                                | Notes                                                                                                                                                                                                                                                                                                                              |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OPERATE | Toggles the amplifier between OPERATE and STANDBY; emits operateToggled.                                                                                                                                                                                                | Hidden until setState arrives. Shows 'OPERATE' (green) for IDLE/OPERATE/TRANSMIT_* states, 'STANDBY' otherwise. In v0.9.8, setState is called from RadioModel::ampStateChanged (authoritative), preventing the button from staying stuck on the old label (#2437).                                                                 |
| STANDBY | When the button reads "STANDBY" (default style), the PGXL is in STANDBY, POWERUP, or FAULT. Click it to send the amplifier to OPERATE.                                                                                                                                  | Same button; label and color change with state.                                                                                                                                                                                                                                                                                    |
| PWR     | Left-side label showing the current forward power value (e.g., "PWR 1148"), followed by a horizontal bar gauge showing forward power output. Range: 0–2000 W. Bar turns red above 1500 W. Gauge uses ballistic smoothing: rises quickly, decays over ~800 ms.           | The gauge label was removed from the gauge interior; the live value appears in the PWR label to the left. Introduced in v26.6.1.                                                                                                                                                                                                   |
| SWR     | Left-side label showing the current SWR value (e.g., "SWR 1.2"), followed by a horizontal bar gauge showing SWR. Range: 1.0–3.0. Bar turns red above 2.5.                                                                                                               | The gauge label was removed from the gauge interior; the live value appears in the SWR label to the left. Introduced in v26.6.1.                                                                                                                                                                                                   |
| Id      | Left-side label showing the current drain current value (e.g., "Id 12.5"), followed by a horizontal bar gauge showing PGXL drain current. Range: 0–70 A. Bar turns red above 60 A.                                                                                      | Replaces the former Temp gauge. The temperature readout now appears in the info stack below. Introduced in v26.6.1.                                                                                                                                                                                                                |
| Temp    | Text label showing heatsink temperature in degrees Celsius (e.g., "— C" before data arrives). Appears in the info stack alongside Vdd and Vac.                                                                                                                           | Previously a horizontal gauge; now a text label in the bottom information area.                                                                                                                                                                                                                                                    |
| Vdd     | Text label showing PGXL drain voltage (e.g., "Vdd  50 V"). Appears in the info stack.                                                                                                                                                                                   | Replaces the former "Volts / Amps" indicator. Introduced in v26.6.1.                                                                                                                                                                                                                                                               |
| Vac     | Text label showing PGXL mains voltage (e.g., "Vac  240 V"). Appears in the info stack.                                                                                                                                                                                  | New in v26.6.1.                                                                                                                                                                                                                                                                                                                    |
| R       | Text label showing the data source (e.g., "● RADIO" in gray). Appears in the info stack below Vac.                                                                                                                                                                      | New in v26.6.1. Indicates that telemetry is coming from the radio/proxy.                                                                                                                                                                                                                                                           |
## Tips

- If the applet panel is not visible, go to `View > Applet Panel` to show it.
- The OPERATE button reflects the PGXL's reported state, not a locally tracked toggle. If the amplifier enters FAULT or POWERUP, the button reverts to "STANDBY" automatically.
- The PWR gauge uses ballistic smoothing: it rises quickly when RF is present, but decays over ~800 ms so brief transmissions remain visible. This matches the S-meter peak-hold feel.
- The info stack (Temp, Vdd, Vac, source indicator) only appears after the first telemetry data arrives from the PGXL.

## Troubleshooting

- **The AMP tray button does not appear** — No Power Genius XL has been detected by the radio. Confirm the PGXL is powered on and correctly connected to the Flex radio.
- **The OPERATE button is not visible inside the applet** — The applet has opened but no state telemetry has arrived yet from the PGXL. Wait a moment; the button appears after the first state update.
- **The button shows "STANDBY" immediately after clicking** — The PGXL may be in FAULT or POWERUP and cannot enter OPERATE. Check the amplifier's front panel for fault indicators.
- **The PWR or SWR gauge shows no value** — No telemetry has been received yet. Confirm the PGXL is communicating with the Flex radio.

## Related

- [Amplifier overview](overview.md)
- [Put the PGXL amplifier in STANDBY](put-the-pgxl-amplifier-in-standby.md)
- [Monitor forward power and SWR at the amplifier output](monitor-forward-power-and-swr-at-the-amplifier-output.md)
- [Watch PGXL temperature, drain current, and mains voltage](watch-pgxl-temperature-drain-current-and-mains-voltage.md)