# Set the TX audio low-cut frequency

Use the Low Cut control in the Phone applet to raise the lower edge of the TX audio passband, cutting rumble, breath noise, or low-frequency interference from your transmitted signal.

## Before you start

- Connect to a FLEX-8600 radio. The Phone applet requires an active radio connection.
- Make sure the Applet Panel is visible. If it is not, click `View > Applet Panel` to show it.

## Steps

1. Click the **PHNE** tray button on the right sidebar to open the Phone applet.
2. Locate the **Low Cut** section in the TX filter area at the bottom of the applet.
3. Click **<** to decrease the low-cut frequency or **>** to increase it. You can also scroll the mouse wheel over the value display to step in either direction.
4. Read the current value in the numeric display between the two buttons. The default is **50 Hz**.

## How the step buttons work

Each click of **<** or **>** snaps the low-cut frequency to the nearest multiple of 50 Hz in the chosen direction, rather than adding or subtracting a fixed 50 Hz from the current value. For example, if the current value is 87 Hz, clicking **>** sets it to 100 Hz and clicking **<** sets it to 50 Hz. If the value is already an exact multiple of 50 Hz, the buttons move it to the next multiple in the chosen direction.

This means a single click always lands on a clean 50 Hz boundary regardless of the starting value.

## What each control does

| Control               | Default | Valid range                             |
|-----------------------|---------|-----------------------------------------|
| **Low Cut** **<**     | —       | Snaps down to next lower 50 Hz multiple |
| **Low Cut** **>**     | —       | Snaps up to next higher 50 Hz multiple  |
| Low Cut value display | 50 Hz   | 0 Hz to (high-cut − 50 Hz), step 50 Hz |

## Tips

- The low-cut value cannot be set higher than the current high-cut frequency minus 50 Hz. If you are near that limit, lower the high-cut first or raise it to create room.
- For SSB voice, a typical low-cut of 100–200 Hz reduces low-frequency noise without noticeably affecting voice intelligibility.
- Because the buttons snap to multiples of 50 Hz, clicking once from any off-boundary value may move the frequency by less than 50 Hz. This is expected behaviour.

## Troubleshooting

- **Low Cut buttons do nothing** — Confirm the radio is connected. The TX filter controls require an active radio connection to send filter changes to the FLEX-8600.

## Related

- [Set the TX audio high-cut frequency](set-the-tx-audio-high-cut-frequency.md)
- [Phone overview](overview.md)
- [Enable VOX and set trigger threshold](enable-vox-and-set-trigger-threshold.md)

---

# Set the TX audio high-cut frequency

Use the High Cut control in the Phone applet to lower the upper edge of the TX audio passband, reducing sibilance, hiss, or high-frequency noise from your transmitted signal.

## Before you start

- Connect to a FLEX-8600 radio. The Phone applet requires an active radio connection.
- Make sure the Applet Panel is visible. If it is not, click `View > Applet Panel` to show it.

## Steps

1. Click the **PHNE** tray button on the right sidebar to open the Phone applet.
2. Locate the **High Cut** section in the TX filter area at the bottom of the applet.
3. Click **<** to decrease the high-cut frequency or **>** to increase it. You can also scroll the mouse wheel over the value display to step in either direction.
4. Read the current value in the numeric display between the two buttons. The default is **3300 Hz**.

## How the step buttons work

Each click of **<** or **>** snaps the high-cut frequency to the nearest multiple of 50 Hz in the chosen direction. For example, if the current value is 1234 Hz, clicking **>** sets it to 1250 Hz and clicking **<** sets it to 1200 Hz. If the value is already an exact multiple of 50 Hz, the buttons move it to the next multiple in the chosen direction.

This means a single click always lands on a clean 50 Hz boundary regardless of the starting value.

## What each control does

| Control                | Default | Valid range                                |
|------------------------|---------|--------------------------------------------|
| **High Cut** **<**     | —       | Snaps down to next lower 50 Hz multiple    |
| **High Cut** **>**     | —       | Snaps up to next higher 50 Hz multiple     |
| High Cut value display | 3300 Hz | (low-cut + 50 Hz) to 10000 Hz, step 50 Hz |

## Tips

- The high-cut value cannot be set lower than the current low-cut frequency plus 50 Hz. If you are near that limit, raise the low-cut first or lower it to create room.
- For SSB voice, a typical high-cut of 2700–3000 Hz reduces hiss while maintaining good intelligibility. For AM or FM, higher settings may be appropriate.
- Because the buttons snap to multiples of 50 Hz, clicking once from any off-boundary value may move the frequency by less than 50 Hz. This is expected behaviour.

## Troubleshooting

- **High Cut buttons do nothing** — Confirm the radio is connected. The TX filter controls require an active radio connection to send filter changes to the FLEX-8600.

## Related

- [Set the TX audio low-cut frequency](set-the-tx-audio-low-cut-frequency.md)
- [Phone overview](overview.md)
- [Enable VOX and set trigger threshold](enable-vox-and-set-trigger-threshold.md)

---

# Phone overview

The Phone applet provides voice transmit (TX) controls for the FLEX-8600 radio. Access it by clicking the **PHNE** tray button on the right sidebar.

## Controls

| Control              | Type          | Description                                                                 |
|----------------------|---------------|-----------------------------------------------------------------------------|
| **AM Carrier**       | Slider        | Sets AM carrier power level from 0 to 100 percent. Drag while holding to see a percentage label (e.g. "48%"). |
| **VOX**              | Toggle button | Enables or disables voice-operated transmit.                                |
| **VOX level**        | Slider        | Sets the VOX activation threshold from 0 to 100 percent. Drag while holding to see a percentage label. |
| **Delay**            | Slider        | Sets VOX hang time from 0 to 100 (arbitrary units) before returning to receive. |
| **DEXP**             | Toggle button | Toggles the downward expander (noise gate). Non-functional on firmware v1.4.0.0 — radio returns error 0x5000002D. |
| **DEXP threshold**   | Slider        | Sets the DEXP gate threshold from 0 to 100 percent. Drag while holding to see a percentage label. Same firmware limitation as DEXP toggle. |
| **Low Cut < / >**    | Spin box      | Adjusts TX filter low-cut frequency by 50 Hz steps. Default 50 Hz. Range: 0 Hz to (high-cut − 50 Hz). |
| **High Cut < / >**   | Spin box      | Adjusts TX filter high-cut frequency by 50 Hz steps. Default 3300 Hz. Range: (low-cut + 50 Hz) to 10000 Hz. |

## Notes

- The AM Carrier slider and VOX level slider now show a percentage label when dragged (e.g. "48%"). This provides clearer visual feedback of the current value.
- The DEXP controls are present but non-functional on FLEX-8600 firmware versions earlier than 4.2. Attempting to use them will result in an error.
- All sliders in the Phone applet use the `GuardedSlider` class, which provides smooth drag behavior and visual feedback.

## Related

- [Set the TX audio low-cut frequency](set-the-tx-audio-low-cut-frequency.md)
- [Set the TX audio high-cut frequency](set-the-tx-audio-high-cut-frequency.md)
- [Enable VOX and set trigger threshold](enable-vox-and-set-trigger-threshold.md)

---

# Enable VOX and set trigger threshold

Use the VOX controls in the Phone applet to enable voice-operated transmit and adjust the sensitivity and hang time.

## Before you start

- Connect to a FLEX-8600 radio. The Phone applet requires an active radio connection.
- Make sure the Applet Panel is visible. If it is not, click `View > Applet Panel` to show it.

## Steps

1. Click the **PHNE** tray button on the right sidebar to open the Phone applet.
2. Click the **VOX** toggle button to enable voice-operated transmit. The button lights up green when active.
3. Adjust the **VOX level** slider to set the activation threshold:
   - Drag the slider right (higher value) to require louder audio to trigger transmit.
   - Drag the slider left (lower value) to allow quieter audio to trigger transmit.
   - While dragging, a percentage label appears (e.g. "45%") showing the current level.
4. Adjust the **Delay** slider to set how long transmit continues after you stop speaking:
   - Drag the slider right for a longer hang time.
   - Drag the slider left for a shorter hang time.

## What each control does

| Control         | Default    | Range    | Description                                      |
|-----------------|------------|----------|--------------------------------------------------|
| **VOX**         | Disabled   | —        | Toggles voice-operated transmit on/off           |
| **VOX level**   | —          | 0–100%   | Activation threshold for VOX                     |
| **Delay**       | —          | 0–100    | Hang time before returning to receive (arbitrary units) |

## Tips

- Start with a VOX level around 30–50% and adjust based on your microphone and speaking volume.
- A longer delay prevents the transmitter from dropping out between words or short pauses, but too long a delay can make the channel seem busy.
- The percentage label on the VOX level slider provides precise feedback when adjusting the threshold.

## Troubleshooting

- **VOX button does not turn on** — Confirm the radio is connected. VOX requires an active radio connection to function.
- **VOX triggers too easily or not at all** — Adjust the VOX level slider. Increase it to require louder audio, decrease it to allow quieter audio.
- **VOX drops out between words** — Increase the Delay slider to extend the hang time.

## Related

- [Phone overview](overview.md)
- [Set the TX audio low-cut frequency](set-the-tx-audio-low-cut-frequency.md)
- [Set the TX audio high-cut frequency](set-the-tx-audio-high-cut-frequency.md)

---

# Set the AM carrier level

Use the AM Carrier slider in the Phone applet to set the AM carrier power level for AM mode operation.

## Before you start

- Connect to a FLEX-8600 radio. The Phone applet requires an active radio connection.
- Make sure the Applet Panel is visible. If it is not, click `View > Applet Panel` to show it.

## Steps

1. Click the **PHNE** tray button on the right sidebar to open the Phone applet.
2. Locate the **AM Carrier** slider at the top of the applet.
3. Drag the slider to the desired level. The valid range is 0 to 100 percent.
4. While dragging, a percentage label appears (e.g. "48%") showing the current carrier level.

## Tips

- The AM carrier level should be set to match your transmitter's capabilities and the modulation depth you want to achieve.
- Typical AM carrier levels range from 20% to 80% depending on your radio and antenna system.
- The percentage label provides precise feedback when adjusting the carrier level.

## Troubleshooting

- **AM Carrier slider has no effect** — Confirm the radio is in AM mode. The slider only controls AM carrier level.
- **No percentage label appears when dragging** — This indicates an older version of the software. Update to v26.5.3 or later to see the label.

## Related

- [Phone overview](overview.md)
- [Set the TX audio low-cut frequency](set-the-tx-audio-low-cut-frequency.md)
- [Set the TX audio high-cut frequency](set-the-tx-audio-high-cut-frequency.md)