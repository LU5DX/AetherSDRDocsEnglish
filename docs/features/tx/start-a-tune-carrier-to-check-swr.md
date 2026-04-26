# Start a tune carrier to check SWR

Use the TUNE function to transmit a steady carrier at reduced power, then read the SWR meter to verify your antenna system before making a contact.

## Before you start

- AetherSDR must be connected to the radio. See `Settings > Connect to Radio...` if not connected.
- The TX Controls applet must be visible. If it is not, click the **TX** tray button on the right sidebar.
- Set an appropriate tune power level. The default is 10 (out of 100). See [Set tune-carrier power](set-tune-carrier-power.md) if you need to change it.
- Confirm you are permitted to transmit on the current frequency (correct band, licence class, and any required inhibit settings).

## Steps

1. Open the TX Controls applet by clicking the **TX** tray button on the right sidebar if it is not already open.
2. Check the **Tune Pwr** slider. The default value is 10. Adjust if needed by dragging the slider.
3. Click **TUNE**.
4. The button label changes to **TUNING...** and the button background turns red. The radio is now transmitting a continuous carrier.
5. Read the **SWR** meter. The scale runs from 1.0 to 3.0; the display turns red above 2.5.
6. Click **TUNE** again to stop the carrier. The button label returns to **TUNE**.

## What each control does

| Control | Kind | Default | Valid range | Behaviour |
|---|---|---|---|---|
| **Tune Pwr** | Slider | 10 | 0–100 | Sets the power level of the tune carrier. |
| **TUNE** | Button | — | — | Click to start the tune carrier; click again to stop. Label shows **TUNING...** with a red background while active. |
| **SWR** | Meter | — | 1.0–3.0 (red above 2.5) | Displays standing wave ratio at the exciter during transmission. |
| **RF Pwr** | Meter | — | 0–120 W barefoot; 0–600 W Aurora 500W (red above 100 W / 500 W) | Displays forward power at the exciter output during the tune carrier. |

## Tips

- Keep **Tune Pwr** low (10 or below) to protect your finals and any downstream amplifier while checking SWR.
- The tune carrier runs at the **Tune Pwr** level, not the **RF Power** level. Changing **RF Power** during a tune has no effect on carrier power.
- If you want to suppress a specific TX output line during tuning, use `Settings > Inhibit during TUNE` to select ACC TX, TX1, TX2, or TX3 before clicking **TUNE**.

## Troubleshooting

- **TUNE button has no effect** — Verify the radio connection is active. The TX Controls applet requires a live radio connection; the **TX** tray button and all controls are disabled when the radio is offline.
- **SWR reads high immediately** — Check antenna connection, coax, and any switch positions. A reading at or above 2.5 triggers the red zone on the SWR meter.
- **TUNING... does not stop** — Click **TUNE** a second time to send the stop command. If the button does not respond, check for a network interruption to the radio.

## Related

- [Set tune-carrier power](set-tune-carrier-power.md)
- [Set RF output power](set-rf-output-power.md)
- [Run the internal ATU](run-the-internal-atu.md)
- [Toggle MOX to manually key the transmitter](toggle-mox-to-manually-key-the-transmitter.md)
- [TX Controls overview](overview.md)
