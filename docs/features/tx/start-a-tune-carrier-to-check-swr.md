# Start a tune carrier to check SWR

Send a continuous carrier at reduced power to read SWR on your antenna system. Use this before a QSO or after changing antennas to confirm a good match.

## Before you start

- AetherSDR must be connected to the radio. The TX Controls applet is only active with a live radio connection.
- Make sure you are clear to transmit on the frequency (the band must be open to your station legally).
- Set the tune power to a level appropriate for your antenna system. The default is 10; see [Set tune-carrier power](set-tune-carrier-power.md).

## Steps

1. Click the TX tray button in the right sidebar to open the TX Controls applet if it is not already visible.
2. Check the **Tune Pwr** slider. The default is 10 (out of 100). Adjust if needed before transmitting.
3. Click **TUNE**.
   - The button label changes to **TUNING...** and the button background turns red while the carrier is active.
   - The **SWR** gauge updates in real time. The scale runs from 1.0 to 3.0; readings above 2.5 are shown in red.
   - The **RF Pwr** gauge shows forward power at the exciter output.
4. Read the SWR value from the **SWR** gauge.
5. Click **TUNE** again to stop the carrier.
   - The button label returns to **TUNE** and the red background clears.

## What each control does

| Control      | Kind        | Default |
|--------------|-------------|---------|
| **TUNE**     | Push button | —       |
| **Tune Pwr** | Slider      | 10      |
| **RF Pwr**   | Meter       | —       |
| **SWR**      | Meter       | —       |

## Tips

- Keep **Tune Pwr** low (10 or less) when testing an unknown antenna system. Raise it only after confirming a reasonable SWR.
- The **SWR** gauge turns red above 2.5. If it pegs at 3.0, stop the carrier and check your feedline and antenna connections before continuing.
- To run the internal ATU instead of checking SWR manually, click **ATU** after the tune carrier confirms the antenna is usable. See [Run the internal ATU](run-the-internal-atu.md).
- If you want to inhibit specific TX outputs (ACC TX, TX1, TX2, TX3) during tuning, configure them at `Settings > Inhibit during TUNE`.

## ATU button behavior (v0.9.5.1)

Starting with v0.9.5.1, the **ATU** button behaves as a frequency-aware toggle rather than always starting a new tune cycle. The logic mirrors SmartSDR's per-frequency behavior:

- **First click (or after a frequency change)** — Starts a fresh ATU tune cycle.
- **Second click at the same frequency** — If the ATU has already reported a successful match (**Success** or **Mem** indicator lit) and the transmit frequency has not changed since that tune, clicking **ATU** switches the tuner to bypass instead of starting another cycle.
- **After any frequency change** — The saved tune frequency is cleared. The next **ATU** click always starts a fresh tune cycle, even if the previous result was successful.

When the ATU enters bypass, the tuned-frequency record is also cleared, so the next click will start a fresh tune regardless of frequency.

This change has no effect on the **MEM** button or the ATU status indicators (**Success**, **Byp**, **Mem**), which continue to behave as described below.

## Troubleshooting

- **TUNE button does nothing** — The applet requires an active radio connection. Check that AetherSDR shows the radio as connected before attempting to transmit.
- **SWR gauge does not move during TUNE** — Forward power may be at or near zero. Verify the **Tune Pwr** slider is above 0 and that the correct antenna port is selected for the current band.
- **Carrier does not stop** — Click **TUNE** once more. If the button remains in **TUNING...** state, check the radio connection; a dropped connection can leave the transmit state unacknowledged.
- **ATU button bypasses the tuner instead of retuning** — This is expected behavior when the ATU already holds a successful match at the current frequency. Change frequency or wait for the tuner to clear its result, then click **ATU** again to start a fresh tune cycle.

## Related

- [Set tune-carrier power](set-tune-carrier-power.md)
- [Run the internal ATU](run-the-internal-atu.md)
- [Recall an ATU memory](recall-an-atu-memory.md)
- [Set RF output power](set-rf-output-power.md)
- [Toggle MOX to manually key the transmitter](toggle-mox-to-manually-key-the-transmitter.md)