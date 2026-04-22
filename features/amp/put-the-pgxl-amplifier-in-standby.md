# Put the PGXL amplifier in STANDBY

Use this page to move a connected Power Genius XL amplifier from OPERATE into STANDBY, stopping it from amplifying transmitted signals.

## Before you start

- AetherSDR must be connected to the radio. The AMP tray button appears only after a Power Genius XL is detected.
- The Amplifier applet must be open. If it is not visible, click the AMP tray button on the right sidebar to show it.
- The OPERATE button is hidden until the first state message arrives from the amplifier. Confirm it is visible before proceeding.

## Steps

1. Open the Amplifier applet by clicking the AMP tray button on the right sidebar if it is not already visible.
2. Confirm the OPERATE button shows the label "OPERATE" in green. This indicates the amplifier is currently in an operating state (IDLE, OPERATE, or TRANSMIT).
3. Click OPERATE.

The button label changes to "STANDBY" and the green background is replaced with the default dark style, confirming the amplifier has moved to STANDBY.

## What each control does

| Control | Behavior | States |
|---|---|---|
| OPERATE | Toggles the amplifier between OPERATE and STANDBY. | Shows "OPERATE" (green) when the amplifier state is IDLE, OPERATE, or TRANSMIT_A/TRANSMIT_B. Shows "STANDBY" (default dark style) when the state is STANDBY, POWERUP, or FAULT. |

## Troubleshooting

- **The AMP tray button is not visible** — The applet is hidden until a Power Genius XL is detected by the radio. Confirm the PGXL is powered on and connected to the FLEX-8600.
- **The OPERATE button is not visible** — The button is hidden until the first state message arrives from the amplifier. Wait a moment after the applet opens; if it does not appear, check the amplifier connection.
- **Clicking OPERATE has no effect** — Confirm AetherSDR is still connected to the radio. Disconnect and reconnect if needed.

## Related

- [Put the PGXL amplifier in OPERATE](put-the-pgxl-amplifier-in-operate.md)
- [Monitor forward power and SWR at the amplifier output](monitor-forward-power-and-swr-at-the-amplifier-output.md)
- [Watch PGXL temperature, drain current, and mains voltage](watch-pgxl-temperature-drain-current-and-mains-voltage.md)
- [Amplifier overview](overview.md)
