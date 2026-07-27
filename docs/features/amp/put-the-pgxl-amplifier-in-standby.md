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
|---------|----------|--------|
| OPERATE | Toggles the amplifier between OPERATE and STANDBY; emits operateToggled. | Hidden until setState arrives. Shows 'OPERATE' (green) for IDLE/OPERATE/TRANSMIT_* states, 'STANDBY' otherwise. In v0.9.8, setState is called from RadioModel::ampStateChanged (authoritative), preventing the button from staying stuck on the old label (#2437). |
| Fan Speed | Button labelled with the current fan mode ("Fan: Std", "Fan: Contest", or "Fan: Bcast") that cycles the PGXL fan mode through STANDARD, CONTEST, and BROADCAST. | Hidden until a direct PGXL connection delivers the first fanmode status. Tooltip: "Fan Speed\nClick to cycle STANDARD / CONTEST / BROADCAST". Accessible name updates with current mode, e.g., "Fan speed: STANDARD". |
| Temperature unit toggle | Click the temperature display to toggle between Celsius (°C) and Fahrenheit (°F). The setting persists across application restarts. | Shows current temperature with one decimal place. Hidden until first telemetry arrives. |

## Telemetry indicators

The Amplifier applet displays telemetry values from the connected Power Genius XL amplifier. These indicators appear in the bottom section of the applet.

| Indicator | Display format | Range | Behavior | Notes |
|-----------|---------------|-------|----------|-------|
| PWR | Numeric value left of the Fwd Pwr gauge, e.g. "1148" | 0-2000 W | Shows PGXL forward power in watts. The gauge bar rises quickly on RF bursts but decays over approximately 800 ms, matching S-meter peak-hold feel. The gauge turns red above 1500 W. The SWR gauge clears to 1.0 when forward power drops below 5 W (idle). When forward power resumes above 5 W, the SWR gauge restores the cached value. | Added in v26.6.1. Value label replaces the previous "Fwd Pwr" label. |
| SWR | Numeric value left of the SWR gauge | 1.0-3.0 | Shows PGXL SWR. The gauge turns red above 2.5. The gauge only displays a value when forward power is 5 W or greater — SWR is not meaningful at idle and the radio/PGXL may report stale or noise values. | Added in v26.6.1. Value label replaces the previous standalone gauge label. |
| Id | Numeric value left of the gauge | 0-70 A | Shows PGXL drain current (Id). The gauge turns red above 60 A. | Added in v26.6.1. Replaces the previous "Amps" text display. |
| Temp | Clickable text label, e.g. "45.0 °C" or "113.0 °F" | — | Shows PGXL heatsink temperature. Click to toggle between Celsius and Fahrenheit. The setting persists across application restarts. | Hidden until first telemetry arrives. |
| Vdd | Text label, e.g. "Vdd 50 V" or "Vdd — V" | — | Shows PGXL drain voltage. Displays "Vdd — V" when the drain supply is off (voltage below 1.0 V) to clearly indicate the supply is off rather than reading zero. | Hidden until first telemetry arrives. |
| Vac | Text label, e.g. "Vac 120 V" | — | Shows PGXL mains voltage. | Hidden until first telemetry arrives. |
| MEffA | Text label | — | Displays the PGXL amplifier efficiency metric (meffa) forwarded from radio/proxy telemetry. | Hidden until setMeff is called. Added in v26.5.1. |
| ● RADIO | Source indicator | — | Shows the telemetry data source. Always displays "● RADIO". | Added in v26.6.1. |

## Layout changes in v26.6.1

Starting in v26.6.1, the Amplifier applet has a redesigned layout:

- **Top row**: PWR gauge with numeric value label on the left (e.g., "PWR 1148")
- **Second row**: SWR gauge with numeric value label on the left (e.g., "SWR 1.2")
- **Third row**: Id (drain current) gauge with numeric value label on the left (e.g., "Id 12.5")
- **Bottom row**: Temperature (Temp, clickable), drain voltage (Vdd), mains voltage (Vac), and source indicator stacked on the left, with the OPERATE button to the right

The gauge ballistics for PWR use a fast attack (30 ms) and slow release (800 ms) to keep brief transmissions visible on the meter.

## Fan speed control

The Fan Speed button appears only when a direct PGXL connection delivers the first fanmode status. The button is hidden until then.

- Click the button to cycle through fan speed modes: STANDARD → CONTEST → BROADCAST → STANDARD.
- The button text shows the mode label: "Fan: Std", "Fan: Contest", or "Fan: Bcast".
- The accessible name updates with the current mode, e.g., "Fan speed: STANDARD".

## Temperature unit toggle

The temperature display doubles as a control. Click it to switch between Celsius and Fahrenheit.

- The temperature is shown with one decimal place (e.g., "45.0 °C" or "113.0 °F").
- The setting persists across application restarts.
- The button has a visible focus indicator and hover effect.

## Troubleshooting

- **The AMP tray button is not visible** — The applet is hidden until a Power Genius XL is detected by the radio. Confirm the PGXL is powered on and connected to the Flex radio.
- **The OPERATE button is not visible** — The button is hidden until the first state message arrives from the amplifier. Wait a moment after the applet opens; if it does not appear, check the amplifier connection.
- **Clicking OPERATE has no effect** — Confirm AetherSDR is still connected to the radio. Disconnect and reconnect if needed.
- **Telemetry values show dashes** — Wait for the first telemetry packet to arrive from the amplifier. If values do not appear, check the amplifier connection and radio/proxy link.
- **The Fan Speed button is not visible** — The button is hidden until a direct PGXL connection delivers the first fanmode status. Wait for the connection to establish; if it does not appear, check that the PGXL is directly connected (not through a proxy).
- **SWR gauge shows no value** — The gauge only displays a value when forward power is 5 W or greater. This is normal; SWR is not meaningful when the amplifier is idle.

## Related

- [Put the PGXL amplifier in OPERATE](put-the-pgxl-amplifier-in-operate.md)
- [Monitor forward power and SWR at the amplifier output](monitor-forward-power-and-swr-at-the-amplifier-output.md)
- [Watch PGXL temperature, drain current, and mains voltage](watch-pgxl-temperature-drain-current-and-mains-voltage.md)
- [Amplifier overview](overview.md)