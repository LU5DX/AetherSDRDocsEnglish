# Monitor Forward Power and SWR at the Amplifier Output

The Amplifier applet shows live forward power, SWR, drain current, and temperature readings from a connected Power Genius XL (PGXL) amplifier. Use these meters to confirm output power and antenna match during transmit, and to monitor amplifier health.

## Before you start

- AetherSDR must be connected to a Flex radio.
- A Power Genius XL amplifier must be detected by the radio. The AMP tray button does not appear until the PGXL is present.

## Steps

1. Locate the AMP tray button on the right sidebar of the applet panel.
2. Click AMP to open the Amplifier applet.
3. Transmit. Watch the PWR, SWR, and Id meters update in real time.

## What each control does

| Control             | What it shows                                                                                                                                                                            | Range                                                                                                                                                                 |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PWR                 | Shows PGXL forward power with a white peak tick held for 2.5 s after the last new peak; the numeric label only shows a value when power >= 5 W.                                         | 0–2000 W (red > 1500)                                                                                                                                                 |
| SWR                 | Shows PGXL SWR; the numeric label only appears when forward power >= 5 W.                                                                                                                | 1.0–3.0 (red > 2.5)                                                                                                                                                   |
| Id                  | Shows PGXL drain current; the numeric label only appears when current >= 0.5 A.                                                                                                          | 0–70 A (red > 60)                                                                                                                                                     |
| Temp (C/F button)   | Shows amp temperature (TEMP_A and TEMP_B if present) and toggles between Celsius and Fahrenheit on click. The choice persists to the `AmpApplet` settings object (tempFahrenheit field). | Celsius / Fahrenheit. Displays `tempA/tempB °C` when both sensors report, or `tempA °C` otherwise. Tooltip announces the unit clicking would switch to.               |
| Vdd (drain voltage) | Shows drain voltage `Vdd  x.x V` on a direct PGXL connection; shows a dash when the drain supply is off (vdd < 1 V) or when connected via the radio proxy.                               | Only updated on a direct connection; greyed out when proxied through the radio.                                                                                       |
| Vac (mains voltage) | Shows mains voltage `Vac  N V` on a direct PGXL connection.                                                                                                                              | Only updated on a direct connection; greyed out when proxied through the radio.                                                                                       |
| Source label        | Indicates whether telemetry is proxied through the radio (RADIO) or read directly from the PGXL (DIRECT).                                                                                | Vdd/Vac/fan mode are only available on the DIRECT path.                                                                                                               |
| Fan speed           | Selects the PGXL fan mode; emits `fanModeChanged` with the uppercase mode.                                                                                                               | STANDARD / CONTEST / BROADCAST                                                                                                                                        |
| OPERATE             | Toggles the amplifier between OPERATE and STANDBY; emits `operateToggled`.                                                                                                               | Hidden until `setState` arrives. Shows `OPERATE` (green) for IDLE/OPERATE/TRANSMIT_* states, `STANDBY` otherwise (kept in sync via `RadioModel::ampStateChanged`).     |

All three bar gauges (PWR, SWR, Id) display as horizontal bar gauges with a left-side label showing the field name and live value (e.g., "PWR 1148"). The filled bar turns red when the value enters the red zone. Tick labels are drawn along the top of each gauge at the following reference points:

- **PWR:** 0, 500, 1000, 1.5K, 2K
- **SWR:** 1, 1.5, 2, 2.5, 3
- **Id:** 0, 10, 20, 30, 40, 50, 60, 70

The PWR gauge has slow-release ballistics: the bar rises quickly on RF bursts but decays over approximately 800 ms, so brief transmissions remain visible. This gives a slow-release peak-hold feel matching the S-meter. The numeric value labels (PWR, SWR, Id) update at 10 Hz to avoid flicker.

**PWR gauge peak tick:** The forward-power gauge shows a white peak tick that is held for 2.5 seconds after the last new peak, making brief power peaks easy to read.

**SWR gauge behavior:** The SWR gauge only updates when forward power is at least 5.0 W. When forward power drops below 5.0 W, the SWR gauge resets to 1.0. This prevents stale or noise values from being displayed when the amplifier is idle. The cached value is restored when power resumes.

**Vdd label behavior:** When drain supply voltage (Vdd) drops below 1.0 V (indicating the drain supply is off during STANDBY), the Vdd label shows "Vdd — V" instead of "Vdd 0.0 V" for clarity.

**Fan speed selector:** The fan speed selector is a pull-down menu that appears only after a direct PGXL connection delivers the first fan mode status. Select STANDARD, CONTEST, or BROADCAST from the pull-down. The selector uses a guarded combo box, so accidental mouse-wheel scroll while hovering over the closed selector does not change fan mode; it only responds to wheel input when the dropdown is open.

**Temperature unit toggle:** The temperature display is a clickable button that toggles between Celsius and Fahrenheit. The button shows the current temperature with the unit symbol (e.g., "40.5 °C" or "104.9 °F"). Click the button to switch units. The setting is persisted and remembered across restarts.

None of the meters have a persisted settings key. Values are read-only telemetry from the PGXL.

## Tips

- The bar gauges use smoothed animation. A brief lag between the actual value and the displayed bar is normal during fast-changing conditions such as the start of a transmission.
- If SWR enters the red zone (above 2.5), check your antenna system before continuing to transmit at high power.
- The drain current (Id) gauge helps monitor amplifier health. If Id exceeds 60 A, consider reducing drive power.
- The MEffA field shows the PGXL amplifier efficiency metric. This field is hidden until telemetry arrives.
- The Volts / Amps text label is hidden until the first telemetry arrives.

## Troubleshooting

- **AMP tray button is not visible** — The PGXL has not been detected by the radio. Verify the amplifier is powered on and connected to the Flex radio. AetherSDR shows the AMP button only after the radio reports an amplifier is present.
- **PWR and SWR meters show no movement during transmit** — Confirm the amplifier is in OPERATE state, not STANDBY. See [Put the PGXL amplifier in OPERATE](put-the-pgxl-amplifier-in-operate.md).
- **Fan speed selector does not appear** — A direct PGXL connection is required. The selector becomes visible only after the first fan mode status is received from the amplifier.

## Related

- [Amplifier overview](overview.md)
- [Put the PGXL amplifier in OPERATE](put-the-pgxl-amplifier-in-operate.md)
- [Put the PGXL amplifier in STANDBY](put-the-pgxl-amplifier-in-standby.md)
- Watch PGXL temperature, drain voltage, and mains voltage