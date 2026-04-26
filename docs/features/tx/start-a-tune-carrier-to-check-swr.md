# Start a tune carrier to check SWR

Use the TUNE function to transmit a steady carrier at a reduced power level so you can read SWR without making a contact. This is the standard way to check your antenna match before operating.

## Before you start

- AetherSDR must be connected to the radio. The TX Controls applet is only functional when a radio connection is active.
- Confirm the frequency and mode are set to what you intend to check.
- Set "Tune Pwr" to a safe level for your antenna and any connected amplifier before transmitting.

## Steps

1. Click the TX tray button on the right sidebar to open the TX Controls applet if it is not already visible.
2. Adjust the "Tune Pwr" slider to the desired tune-carrier power level. The default is 10; valid range is 0–100.
3. Click TUNE. The button label changes to "TUNING..." and the button background turns red while the carrier is active.
4. Read the SWR meter. The "SWR" gauge displays the standing wave ratio at the exciter. The scale runs from 1.0 to 3.0; values above 2.5 are shown in red.
5. Click TUNE again (now labeled "TUNING...") to stop the carrier. The button returns to its normal "TUNE" label.

## What each control does

| Control | Kind | Default | Valid range | Behavior |
|---|---|---|---|---|
| TUNE | Push button | — | — | Starts or stops the tune carrier. Displays "TUNING..." with a red background while active. |
| Tune Pwr | Slider | 10 | 0–100 | Sets the tune-carrier power level sent to the radio. |
| SWR | Meter | — | 1.0–3.0 (red > 2.5) | Displays the standing wave ratio at the exciter while transmitting. |
| RF Pwr | Meter | — | 0–120 W barefoot; 0–600 W Aurora 500W (red > 100 W / > 500 W) | Displays forward power at the exciter output. |

## Tips

- Keep "Tune Pwr" at the minimum level needed to get a reliable SWR reading. A value of 10 is sufficient for most antenna analyzers and internal tuners.
- If you intend to run the internal ATU, you can start ATU tuning directly with the ATU button instead; the ATU cycle uses the tune carrier automatically. See [Run the internal ATU](run-the-internal-atu.md).

## Troubleshooting

- **TUNE button has no effect** — The TX Controls applet requires an active radio connection. Check that AetherSDR is connected to the FLEX-8600 via `Settings > Connect to Radio...`.
- **SWR gauge stays at 1.0 during tuning** — The radio may not be detecting reflected power. Verify the antenna connector and feedline are properly attached to the radio.
- **Carrier does not stop** — If clicking the button a second time does not stop the tune, the radio may have lost the command. Click MOX once to force the transmitter off, then click MOX again to return to receive.

## Related

- [Set tune-carrier power](set-tune-carrier-power.md)
- [Run the internal ATU](run-the-internal-atu.md)
- [Set RF output power](set-rf-output-power.md)
- [Toggle MOX to manually key the transmitter](toggle-mox-to-manually-key-the-transmitter.md)
