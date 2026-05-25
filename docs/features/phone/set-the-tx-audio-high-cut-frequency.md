# Set the TX audio high-cut frequency

Use the Phone applet to raise or lower the upper boundary of the TX audio passband. Narrowing the high-cut reduces transmitted bandwidth; raising it passes more high-frequency audio content.

## Before you start

- AetherSDR must be connected to the radio. The Phone applet requires an active radio connection.
- The radio must be in a phone mode (SSB, AM, or similar) for TX filter changes to have audible effect.

## Steps

1. If the Phone applet is not visible, click the **PHNE** tray button in the right sidebar to show it.
2. Locate the **High Cut** column on the right side of the TX filter section, below the DEXP row.
3. Click **>** to increase the high-cut frequency to the next multiple of 50 Hz, or click **<** to decrease it to the next lower multiple of 50 Hz. You can also scroll the mouse wheel over the value display to step in either direction.
4. Read the current value in the numeric display between the **<** and **>** buttons.

## What each control does

| Control                | Description                                                                                      | Default |
|------------------------|--------------------------------------------------------------------------------------------------|---------|
| **High Cut `<`**       | Decreases the TX filter high-cut frequency to the next lower multiple of 50 Hz.                 | —       |
| **High Cut `>`**       | Increases the TX filter high-cut frequency to the next higher multiple of 50 Hz.                | —       |
| High Cut value display | Shows the current high-cut frequency in Hz.                                                      | 3300 Hz |

The high-cut frequency cannot be set below the current low-cut frequency plus 50 Hz. For example, if low-cut is set to 100 Hz, the minimum high-cut value is 150 Hz.

## How stepping works

The **<** and **>** buttons snap the value to the nearest multiple of 50 Hz in the chosen direction, rather than adding or subtracting a fixed 50 Hz from the current value. For example, if the current high-cut is 3275 Hz, clicking **>** sets it to 3300 Hz and clicking **<** sets it to 3250 Hz. This behaviour applies equally to the **Low Cut** controls.

The radio accepts any integer Hz value, so if the current value is already an exact multiple of 50 Hz the result is the same as a plain 50 Hz step.

## Tips

- For larger changes, use the scroll wheel with rapid movement rather than repeated button clicks.
- A typical SSB passband uses a low-cut of 50 Hz and a high-cut of 3300 Hz. Reducing high-cut to around 2700–2800 Hz can improve intelligibility in noisy conditions by removing high-frequency hiss.
- The high-cut setting is not persisted by AetherSDR's local settings — it is sent directly to the radio and stored in the radio's active profile.

## Related

- [Set the TX audio low-cut frequency](set-the-tx-audio-low-cut-frequency.md)
- [Phone overview](overview.md)

# Phone applet controls

The Phone applet provides voice transmit controls for AM carrier level, VOX settings, downward expander (noise gate) controls, and TX filter low-cut/high-cut frequency setters.

## Voice-Operated Transmit (VOX)

### VOX Enable

Click **VOX** to toggle voice-operated transmit on or off. When enabled, the radio will automatically begin transmitting when audio from the microphone exceeds the threshold set by the **VOX level** slider.

### VOX level

Set the VOX activation threshold by dragging the **VOX level** slider. The slider range is 0 to 100. Higher values require louder audio to trigger transmit. The slider displays the value as a percentage (e.g., "48%") while dragging.

### Delay

Set the VOX hang time by dragging the **Delay** slider. The slider range is 0 to 100. This controls how long the radio remains in transmit mode after audio stops before returning to receive.

## AM Carrier Level

Drag the **AM Carrier** slider to adjust the AM carrier power level. The slider range is 0 to 100. The slider displays the value as a percentage (e.g., "48%") while dragging. The current value is shown as a numeric label next to the slider.

## Downward Expander (DEXP)

### DEXP Enable

Click **DEXP** to toggle the downward expander (noise gate) on or off. Note: This control is non-functional on firmware v1.4.0.0 — the radio returns error 0x5000002D.

### DEXP threshold

Set the DEXP gate threshold by dragging the **DEXP threshold** slider. The slider range is 0 to 100. The slider displays the value as a percentage while dragging. This setting persists to the `DexpLevel` configuration key. Note: Same firmware limitation as the DEXP toggle.

## TX Filter Low Cut

Adjust the TX filter low-cut frequency using the **Low Cut < / >** spinbox. The default value is 50 Hz. The range is 0 to (high_cut − 50) Hz, stepping in 50 Hz increments. Click **<** to decrease, **>** to increase, or use the mouse wheel over the value display.

## TX Filter High Cut

Adjust the TX filter high-cut frequency using the **High Cut < / >** spinbox. The default value is 3300 Hz. The range is (low_cut + 50) to 10000 Hz, stepping in 50 Hz increments. Click **<** to decrease, **>** to increase, or use the mouse wheel over the value display.

## What each control does

| Control          | Description                                                                 | Default | Setting Key     |
|------------------|-----------------------------------------------------------------------------|---------|-----------------|
| **AM Carrier**   | Sets AM carrier power level (0-100).                                        | —       | None            |
| **VOX**          | Toggles voice-operated transmit on/off.                                     | —       | None            |
| **VOX level**    | Sets VOX activation threshold (0-100).                                      | —       | None            |
| **Delay**        | Sets VOX hang time before returning to receive (0-100).                     | —       | None            |
| **DEXP**         | Toggles downward expander (noise gate) on/off. Non-functional on fw v1.4.0.0| —       | `DexpEnabled`   |
| **DEXP threshold**| Sets DEXP gate threshold (0-100). Same firmware limitation as DEXP toggle. | 0       | `DexpLevel`     |
| **Low Cut < / >**| Adjusts TX filter low-cut frequency (0 to high_cut-50 Hz, step 50 Hz).      | 50 Hz   | None            |
| **High Cut < / >**| Adjusts TX filter high-cut frequency (low_cut+50 to 10000 Hz, step 50 Hz). | 3300 Hz | None            |