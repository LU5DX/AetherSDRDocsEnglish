# Monitor Forward Power and SWR at the Amplifier Output

The Amplifier applet shows live forward power and SWR readings from a connected Power Genius XL (PGXL) amplifier. Use these meters to confirm output power and antenna match during transmit.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- A Power Genius XL amplifier must be detected by the radio. The AMP tray button does not appear until the PGXL is present.

## Steps

1. Locate the AMP tray button on the right sidebar of the applet panel.
2. Click AMP to open the Amplifier applet.
3. Transmit. Watch the Fwd Pwr and SWR meters update in real time.

## What each control does

| Control | What it shows | Range | Red zone |
|---------|--------------|-------|----------|
| Fwd Pwr | Forward power at the PGXL output | 0–2000 W | Above 1500 W |
| SWR | Standing wave ratio at the PGXL output | 1.0–3.0 | Above 2.5 |

Both meters display as horizontal bar gauges. The filled bar turns red when the value enters the red zone. Tick labels are drawn along the top of each gauge at the following reference points:

- **Fwd Pwr:** 0, 500, 1000, 1.5k, 2k
- **SWR:** 1, 1.5, 2, 2.5, 3

Neither meter has a persisted settings key. Values are read-only telemetry from the PGXL.

## Tips

- The bar gauges use smoothed animation. A brief lag between the actual value and the displayed bar is normal during fast-changing conditions such as the start of a transmission.
- If SWR enters the red zone (above 2.5), check your antenna system before continuing to transmit at high power.

## Troubleshooting

- **AMP tray button is not visible** — The PGXL has not been detected by the radio. Verify the amplifier is powered on and connected to the FLEX-8600. AetherSDR shows the AMP button only after the radio reports an amplifier is present.
- **Fwd Pwr and SWR meters show no movement during transmit** — Confirm the amplifier is in OPERATE state, not STANDBY. See [Put the PGXL amplifier in OPERATE](put-the-pgxl-amplifier-in-operate.md).

## Related

- [Amplifier overview](overview.md)
- [Put the PGXL amplifier in OPERATE](put-the-pgxl-amplifier-in-operate.md)
- [Put the PGXL amplifier in STANDBY](put-the-pgxl-amplifier-in-standby.md)
- [Watch PGXL temperature, drain current, and mains voltage](watch-pgxl-temperature-drain-current-and-mains-voltage.md)
