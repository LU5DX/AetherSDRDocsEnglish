# Start a tune carrier to check SWR

Send a continuous carrier at reduced power to read SWR on your antenna system. Use this before a QSO or after changing antennas to confirm a good match.

## Before you start

- AetherSDR must be connected to the radio. The TX Controls applet is only active with a live radio connection.
- Make sure you are clear to transmit on the frequency (the band must be open to your station legally).
- Set the tune power to a level appropriate for your antenna system. The default is 10; see [Set tune-carrier power](set-tune-carrier-power.md).

## Steps

1. Click the TX tray button in the right sidebar to open the TX Controls applet if it is not already visible.
2. Check the **Tune Pwr** slider. The default is 10 (out of 100). Adjust if needed before transmitting.
3. Right-click the **TUNE** button to select the carrier shape for the next tune cycle. Choose **Mono Tone** or **Two Tone** from the context menu. The radio's tune mode is a transient one-shot — AetherSDR does not persist the choice.
4. Click **TUNE**.
   - The button label changes to **TUNING...** and the button background turns red while the carrier is active.
   - The **SWR** gauge updates in real time. The scale runs from 1.0 to 3.0; readings above 2.5 are shown in red.
   - The **RF Pwr** gauge shows forward power at the exciter output. A peak-hold bar tracks the peak envelope power (PEP) for 2 seconds, then decays toward the current reading.
5. Read the SWR value from the **SWR** gauge.
6. Click **TUNE** again to stop the carrier.
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
- The peak-hold bar on the **RF Pwr** gauge resets to zero immediately when the transmitter un-keys, so a held PEP reading does not linger across overs.

## ATU button behavior (v0.9.5.1)

Starting with v0.9.5.1, the **ATU** button behaves as a frequency-aware toggle rather than always starting a new tune cycle. The logic mirrors SmartSDR's per-frequency behavior:

- **First click (or after a frequency change)** — Starts a fresh ATU tune cycle.
- **Second click at the same frequency** — If the ATU has already reported a successful match (**Success** or **Mem** indicator lit) and the transmit frequency has not changed since that tune, clicking **ATU** switches the tuner to bypass instead of starting another cycle.
- **After any frequency change** — The saved tune frequency is cleared. The next **ATU** click always starts a fresh tune cycle, even if the previous result was successful.

When the ATU enters bypass, the tuned-frequency record is also cleared, so the next click will start a fresh tune regardless of frequency.

This change has no effect on the **MEM** button or the ATU status indicators (**Success**, **Byp**, **Mem**), which continue to behave as described below.

## ATU right-click menu (v26.5.2.1)

Right-click the **ATU** button to access the following actions:

- **Pre-tune bands…** — Opens the Pre-Tune Bands dialog to run a sweep across selected bands. This action is only available when MEM is enabled (the **MEM** button must be engaged). If MEM is off, the menu item is disabled with a tooltip explaining that MEM must be enabled first.
- **Clear ATU memories…** — Prompts for confirmation and then clears all stored ATU memories.

This matches SmartSDR Windows's hidden right-click menu on the ATU button.

## MOX and Quindar tones (v0.9.7)

Starting with v0.9.7, clicking **MOX** routes through the Quindar-tone coordinator rather than keying the transmitter directly. When the QUIN chip is enabled in the Audio Channel Strip and the active TX slice is on a phone mode, the K-tone plays on PTT engage and the BK-tone plays on PTT disengage. When Quindar is disabled or the active TX slice is not on a phone mode, the behavior is identical to previous versions.

This change affects only the **MOX** button in the TX Controls applet. Hardware PTT, VOX, and other PTT sources are not affected.

## Slider value display (v26.5.3)

Starting with v26.5.3, when dragging the **RF Pwr** or **Tune Pwr** slider, the slider thumb displays the current value in watts (e.g., "50 W") as a tooltip next to the thumb. This provides immediate visual feedback of the power level as you adjust the slider.

## Troubleshooting

- **TUNE button does nothing** — The applet requires an active radio connection. Check that AetherSDR shows the radio as connected before attempting to transmit.
- **SWR gauge does not move during TUNE** — Forward power may be at or near zero. Verify the **Tune Pwr** slider is above 0 and that the correct antenna port is selected for the current band.
- **Carrier does not stop** — Click **TUNE** once more. If the button remains in **TUNING...** state, check the radio connection; a dropped connection can leave the transmit state unacknowledged.
- **ATU button bypasses the tuner instead of retuning** — This is expected behavior when the ATU already holds a successful match at the current frequency. Change frequency or wait for the tuner to clear its result, then click **ATU** again to start a fresh tune cycle.
- **MOX keys the transmitter but no Quindar tones are heard** — Confirm that the QUIN chip is enabled in the Audio Channel Strip and that the active TX slice is set to a phone mode (USB, LSB, AM, FM, or similar). Quindar tones do not play on CW or digital modes.
- **Pre-tune bands menu item is grayed out** — Enable MEM by clicking the **MEM** button in the TX Controls applet before right-clicking **ATU**.
- **Peak-hold bar does not appear during tune** — The peak-hold bar only tracks when the transmitter is keyed. The bar decays after 2 seconds of holding a peak, and resets to zero on un-key.

## Related

- [Set tune-carrier power](set-tune-carrier-power.md)
- [Run the internal ATU](run-the-internal-atu.md)
- Pre-tune bands
- Clear ATU memories
- [Recall an ATU memory](recall-an-atu-memory.md)
- [Set RF output power](set-rf-output-power.md)
- [Toggle MOX to manually key the transmitter](toggle-mox-to-manually-key-the-transmitter.md)