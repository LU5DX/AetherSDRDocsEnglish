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

Click **DEXP** to toggle the downward expander (noise gate) on or off.

**Note:** This control is non-functional on firmware v1.4.0.0 — the radio returns error 0x5000002D.

### DEXP threshold

Set the DEXP gate threshold by dragging the **DEXP threshold** slider. The slider range is 0 to 100. The slider displays the value as a percentage while dragging. This setting is persisted in AetherSDR's local settings under `DexpLevel`. The **DEXP** toggle state is persisted under `DexpEnabled`.

**Note:** This control has the same firmware limitation as the DEXP toggle on v1.4.0.0.

## TX Filter Low Cut

Adjust the TX filter low-cut frequency using the **Low Cut < / >** field. The default value is 50 Hz. The range is 0 to (high_cut − 50) Hz, stepping in 50 Hz increments.

## TX Filter High Cut

Adjust the TX filter high-cut frequency using the **High Cut < / >** field. The default value is 3300 Hz. The range is (low_cut + 50) to 10000 Hz, stepping in 50 Hz increments.

## Adjusting TX filter frequencies

1. Click **<** to decrease the frequency to the next lower multiple of 50 Hz.
2. Click **>** to increase the frequency to the next higher multiple of 50 Hz.
3. Scroll the mouse wheel over the value display to step in either direction.
4. Double-click the value display to type an exact Hz value. The typed value is honored on radios that accept it, while the radio's own readback is preserved elsewhere (issues #3627, #5064).

### Step behaviour and direct entry

The **<** and **>** buttons snap the value to the nearest multiple of 50 Hz in the chosen direction, rather than adding or subtracting a fixed 50 Hz from the current value. For example, if the current high-cut is 3275 Hz, clicking **>** sets it to 3300 Hz and clicking **<** sets it to 3250 Hz. This behaviour applies equally to the **Low Cut** controls.

Typed values are handled differently from steps:

- A **typed** number is treated as a request for that exact value. Out-of-range values or values not on the radio's supported step grid are **rejected**, and the previous value is restored.
- The **step buttons** clamp to the nearest valid value within the allowed range, stopping at the bound if it is reached.

When stepping, if the radio's backend publishes a discrete set of supported frequencies (an edge list), the buttons step to the next value in that list rather than to a multiple of 50 Hz. Otherwise, stepping snaps to multiples of 50 Hz.

The table below shows the difference:

| Action           | Behaviour                                                                 |
|------------------|---------------------------------------------------------------------------|
| Click **<**      | Moves to the next lower supported frequency. Clamps to the lower bound.  |
| Click **>**      | Moves to the next higher supported frequency. Clamps to the upper bound. |
| Type a value     | Requests that exact frequency. Rejects values outside the valid range or not on the radio's supported grid. |

The high-cut frequency cannot be set below the current low-cut frequency plus 50 Hz. For example, if low-cut is set to 100 Hz, the minimum high-cut value is 150 Hz. Similarly, the low-cut frequency cannot be set above the current high-cut frequency minus 50 Hz.

## What each control does

| Control                | Description                                                                      | Default | Setting Key |
|------------------------|----------------------------------------------------------------------------------|---------|-------------|
| **AM Carrier**         | Sets AM carrier power level (0-100).                                             | —       | None        |
| **VOX**                | Toggles voice-operated transmit on/off.                                          | —       | None        |
| **VOX level**          | Sets VOX activation threshold (0-100).                                           | —       | None        |
| **Delay**              | Sets VOX hang time before returning to receive (0-100).                          | —       | None        |
| **DEXP**               | Toggles downward expander (noise gate) on/off.                                   | —       | `DexpEnabled` |
| **DEXP threshold**     | Sets DEXP gate threshold (0-100). Persisted in `DexpLevel`.                      | 0       | `DexpLevel` |
| **Low Cut < / >**      | Adjusts TX filter low-cut frequency (0 to high_cut−50 Hz, step 50 Hz).           | 50 Hz   | None        |
| **High Cut < / >**     | Adjusts TX filter high-cut frequency (low_cut+50 to 10000 Hz, step 50 Hz).       | 3300 Hz | None        |

## Theme support

The Phone applet uses theme-aware colors for all UI elements. Labels, sliders, and buttons adapt to the active theme. The applet container applies the `applet/phone` theme style, and all previously hardcoded color values have been replaced with themed equivalents. This ensures consistent appearance across light and dark themes.

## Tips

- For larger changes, use the scroll wheel with rapid movement rather than repeated button clicks.
- A typical SSB passband uses a low-cut of 50 Hz and a high-cut of 3300 Hz. Reducing high-cut to around 2700–2800 Hz can improve intelligibility in noisy conditions by removing high-frequency hiss.
- The low-cut and high-cut settings are not persisted by AetherSDR's local settings — they are sent directly to the radio and stored in the radio's active profile.

## Related

- [Set the TX audio high-cut frequency](set-the-tx-audio-high-cut-frequency.md)
- [Phone overview](overview.md)

---

# Set the TX audio high-cut frequency

Use the Phone applet to raise or lower the upper boundary of the TX audio passband. Narrowing the high-cut reduces transmitted bandwidth; raising it passes more high-frequency audio content.

## Before you start

- AetherSDR must be connected to the radio. The Phone applet requires an active radio connection.
- The radio must be in a phone mode (SSB, AM, or similar) for TX filter changes to have audible effect.

## Steps

1. If the Phone applet is not visible, click the **PHNE** tray button in the right sidebar to show it.
2. Locate the **High Cut** column on the right side of the TX filter section, below the DEXP row.
3. Do one of the following:
   - Click **>** to increase the high-cut frequency to the next supported value, or click **<** to decrease it.
   - Scroll the mouse wheel over the value display to step in either direction.
   - Double-click the value display and type an exact Hz value.
4. Read the current value in the numeric display between the **<** and **>** buttons.

## What each control does

| Control                | Description                                                                      | Default |
|------------------------|----------------------------------------------------------------------------------|---------|
| **High Cut `<`**       | Decreases the TX filter high-cut frequency to the next lower supported value.    | —       |
| **High Cut `>`**       | Increases the TX filter high-cut frequency to the next higher supported value.   | —       |
| High Cut value display | Shows the current high-cut frequency in Hz. Double-click to type an exact value. | 3300 Hz |

The high-cut frequency cannot be set below the current low-cut frequency plus 50 Hz. For example, if low-cut is set to 100 Hz, the minimum high-cut value is 150 Hz.

## How stepping works

The **<** and **>** buttons snap the value to the next supported frequency in the chosen direction. On radios where the backend publishes a discrete list of supported frequencies, the buttons step through that list. Otherwise, they snap to the nearest multiple of 50 Hz. For example, on a continuous radio with a current high-cut of 3275 Hz, clicking **>** sets it to 3300 Hz and clicking **<** sets it to 3250 Hz. This behaviour applies equally to the **Low Cut** controls.

If the current value is already an exact supported value, the result is the same as a plain single-step movement.

## Direct numeric entry

Double-click the value display to type an exact Hz value. 

- Valid values are those within the range from the current low-cut plus 50 Hz up to the radio's maximum supported high-cut, and on the radio's supported frequency grid.
- Out-of-range or unsupported values are rejected, and the previous value is restored.
- A typed value is treated as a request for that exact frequency, not a step, so it is not clamped to the nearest supported value — it is either accepted as-is or rejected.

## Tips

- For larger changes, use the scroll wheel with rapid movement rather than repeated button clicks.
- A typical SSB passband uses a low-cut of 50 Hz and a high-cut of 3300 Hz. Reducing high-cut to around 2700–2800 Hz can improve intelligibility in noisy conditions by removing high-frequency hiss.
- The high-cut setting is not persisted by AetherSDR's local settings — it is sent directly to the radio and stored in the radio's active profile.

## Related

- [Set the TX audio low-cut frequency](set-the-tx-audio-low-cut-frequency.md)
- [Phone overview](overview.md)

---

# Set the TX audio low-cut frequency

Use the Phone applet to raise or lower the lower boundary of the TX audio passband. Raising the low-cut removes low-frequency rumble and sub-audio content from the transmitted signal; lowering it passes more low-frequency audio.

## Before you start

- AetherSDR must be connected to the radio. The Phone applet requires an active radio connection.
- The radio must be in a phone mode (SSB, AM, or similar) for TX filter changes to have audible effect.

## Steps

1. If the Phone applet is not visible, click the **PHNE** tray button in the right sidebar to show it.
2. Locate the **Low Cut** column on the left side of the TX filter section, below the DEXP row.
3. Do one of the following:
   - Click **>** to increase the low-cut frequency to the next supported value, or click **<** to decrease it.
   - Scroll the mouse wheel over the value display to step in either direction.
   - Double-click the value display and type an exact Hz value.
4. Read the current value in the numeric display between the **<** and **>** buttons.

## What each control does

| Control               | Description                                                                      | Default |
|-----------------------|----------------------------------------------------------------------------------|---------|
| **Low Cut `<`**       | Decreases the TX filter low-cut frequency to the next lower supported value.     | —       |
| **Low Cut `>`**       | Increases the TX filter low-cut frequency to the next higher supported value.    | —       |
| Low Cut value display | Shows the current low-cut frequency in Hz. Double-click to type an exact value.  | 50 Hz   |

The low-cut frequency cannot be set above the current high-cut frequency minus 50 Hz. For example, if high-cut is set to 3300 Hz, the maximum low-cut value is 3250 Hz.

## How stepping works

The **<** and **>** buttons snap the value to the next supported frequency in the chosen direction. On radios where the backend publishes a discrete list of supported frequencies, the buttons step through that list. Otherwise, they snap to the nearest multiple of 50 Hz. For example, on a continuous radio with a current low-cut of 87 Hz, clicking **>** sets it to 100 Hz and clicking **<** sets it to 50 Hz. This behaviour applies equally to the **High Cut** controls.

If the current value is already an exact supported value, the result is the same as a plain single-step movement.

## Direct numeric entry

Double-click the value display to type an exact Hz value. 

- Valid values are those within the range from the radio's minimum supported low-cut up to the current high-cut minus 50 Hz, and on the radio's supported frequency grid.
- Out-of-range or unsupported values are rejected, and the previous value is restored.
- A typed value is treated as a request for that exact frequency, not a step, so it is not clamped to the nearest supported value — it is either accepted as-is or rejected.

When you type a low-cut value that is very high, the radio's high-cut is **not** dragged upward to maintain the 50 Hz minimum separation. Instead