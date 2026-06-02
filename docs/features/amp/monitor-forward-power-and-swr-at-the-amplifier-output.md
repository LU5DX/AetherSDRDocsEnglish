# Monitor Forward Power and SWR at the Amplifier Output

The Amplifier applet shows live forward power and SWR readings from a connected Power Genius XL (PGXL) amplifier. Use these meters to confirm output power and antenna match during transmit.

## Before you start

- AetherSDR must be connected to a Flex radio.
- A Power Genius XL amplifier must be detected by the radio. The AMP tray button does not appear until the PGXL is present.

## Steps

1. Locate the AMP tray button on the right sidebar of the applet panel.
2. Click AMP to open the Amplifier applet.
3. Transmit. Watch the Fwd Pwr and SWR meters update in real time.

## What each control does

| Control | What it shows                          | Range    |
|---------|----------------------------------------|----------|
| PWR     | Forward power at the PGXL output       | 0–2000 W |
| SWR     | Standing wave ratio at the PGXL output | 1.0–3.0  |
| Id      | Drain current                          | 0–70 A   |

All three meters display as horizontal bar gauges with a left-side label showing the field name and live value (e.g., "PWR 1148"). The filled bar turns red when the value enters the red zone. Tick labels are drawn along the top of each gauge at the following reference points:

- **PWR:** 0, 500, 1000, 1.5K, 2K
- **SWR:** 1, 1.5, 2, 2.5, 3
- **Id:** 0, 10, 20, 30, 40, 50, 60, 70

The PWR gauge has slow-release ballistics: the bar rises quickly on RF bursts but decays over approximately 800 ms, so brief transmissions remain visible. This matches the S-meter peak-hold feel.

Neither meter has a persisted settings key. Values are read-only telemetry from the PGXL.

## Tips

- The bar gauges use smoothed animation. A brief lag between the actual value and the displayed bar is normal during fast-changing conditions such as the start of a transmission.
- If SWR enters the red zone (above 2.5), check your antenna system before continuing to transmit at high power.
- The drain current (Id) gauge helps monitor amplifier health. If Id exceeds 60 A, consider reducing drive power.

## Troubleshooting

- **AMP tray button is not visible** — The PGXL has not been detected by the radio. Verify the amplifier is powered on and connected to the Flex radio. AetherSDR shows the AMP button only after the radio reports an amplifier is present.
- **PWR and SWR meters show no movement during transmit** — Confirm the amplifier is in OPERATE state, not STANDBY. See [Put the PGXL amplifier in OPERATE](put-the-pgxl-amplifier-in-operate.md).

## Related

- [Amplifier overview](overview.md)
- [Put the PGXL amplifier in OPERATE](put-the-pgxl-amplifier-in-operate.md)
- [Put the PGXL amplifier in STANDBY](put-the-pgxl-amplifier-in-standby.md)
- [Watch PGXL temperature, drain voltage, and mains voltage](watch-pgxl-temperature-drain-voltage-and-mains-voltage.md)