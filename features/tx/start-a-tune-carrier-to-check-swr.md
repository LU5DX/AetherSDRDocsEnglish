# Start a tune carrier to check SWR

Transmit a continuous carrier at reduced power so you can read SWR on the meter before making a contact or running the ATU.

## Before you start

- AetherSDR must be connected to the radio. The TX Controls applet requires an active radio connection.
- The antenna and feed line must be connected to the radio.
- Set "Tune Pwr" to a safe level for your antenna system before keying the carrier. The default is 10.

## Steps

1. Click the **TX** tray button on the right sidebar to open the TX Controls applet.
2. Check the **Tune Pwr** slider. The default value is 10. Adjust it if you need a different output level (valid range: 0–100).
3. Click **TUNE**.
   The button label changes to **TUNING...** and the button background turns red. The radio transmits a continuous carrier.
4. Read the **SWR** meter. The scale runs from 1.0 to 3.0; the indicator turns red above 2.5.
5. Click **TUNING...** to stop the carrier.
   The button returns to the **TUNE** label.

## What each control does

| Control | Kind | Default | Valid range | Behavior |
|---|---|---|---|---|
| **Tune Pwr** | Slider | 10 | 0–100 | Sets the output power level used during the tune carrier. |
| **TUNE** | Button | — | — | First click starts the carrier (label becomes **TUNING...**). Click again to stop. |
| **SWR** | Meter | — | 1.0–3.0 (red above 2.5) | Displays standing wave ratio at the exciter output while the carrier is on. |
| **RF Pwr** | Meter | — | 0–120 W barefoot; 0–600 W Aurora 500W (red above 100 W / 500 W) | Displays forward power at the exciter output. |

## Tips

- Keep **Tune Pwr** low (10–20) for an initial check. Raise it only if your SWR meter needs more drive to give a stable reading.
- The **SWR** meter is active any time the radio is transmitting, not only during **TUNE**. You can also read it while using **MOX**.
- To inhibit specific TX outputs during tuning, use `Settings > Inhibit during TUNE` and select the outputs to suppress.

## Troubleshooting

- **TUNE button is greyed out** — The radio is not connected. Check the connection status and see `Settings > Connect to Radio...`.
- **SWR meter reads 1.0 and RF Pwr reads 0 during TUNE** — The carrier started but no power is reaching the meter. Verify the antenna port selection in `Settings > Radio Setup...` and confirm the feed line is attached.
- **Carrier does not stop when clicking TUNING...** — Click the button once firmly. If it persists, click **MOX** to force the radio out of transmit, then verify the radio firmware is 4.1.5.

## Related

- [Set tune-carrier power](set-tune-carrier-power.md)
- [Run the internal ATU](run-the-internal-atu.md)
- [Set RF output power](set-rf-output-power.md)
- [Toggle MOX to manually key the transmitter](toggle-mox-to-manually-key-the-transmitter.md)
- [TX Controls overview](overview.md)
