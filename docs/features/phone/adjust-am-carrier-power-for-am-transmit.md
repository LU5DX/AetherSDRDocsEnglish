# Adjust AM carrier power for AM transmit

Use this page to set the AM carrier power level when transmitting in AM mode. Adjusting the carrier level controls how much power the radio outputs as the AM carrier before audio modulation is applied.

## Before you start

- Connect to a FLEX-8600 radio. The Phone applet requires an active radio connection.
- Set the slice to AM mode before transmitting.

## Steps

1. Open the Phone applet by clicking the **PHNE** tray button in the right sidebar. If the applet panel is not visible, click **View > Applet Panel** to show it.
2. Locate the **AM Carrier** row at the top of the Phone applet.
3. Drag the **AM Carrier** slider left to decrease or right to increase the carrier power level. The numeric label to the right of the slider updates immediately to show the current value (for example, `48`). While dragging, the tooltip shows the value as a percentage (for example, `48%`).

## What each control does

| Control                   | Description                                                                                                                                  | Valid range             |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| **AM Carrier** slider     | Sets the AM carrier power level sent to the radio. Drag to adjust; tooltip shows percentage.                                                 | 0–100                   |
| **VOX** button            | Toggles voice-operated transmit on or off.                                                                                                   | —                       |
| **VOX level** slider      | Sets the VOX activation threshold. Drag to adjust; tooltip shows percentage.                                                                 | 0–100                   |
| **Delay** slider          | Sets the VOX hang time before returning to receive.                                                                                          | 0–100                   |
| **DEXP** button           | Toggles the downward expander (noise gate). Stored as `DexpEnabled`.                                                                         | —                       |
| **DEXP threshold** slider | Sets the DEXP gate threshold. Stored as `DexpLevel`. Default: 0. Drag to adjust; tooltip shows percentage.                                   | 0–100                   |
| **Low Cut < / >**         | Adjusts the TX filter low-cut frequency. Step buttons move in 50 Hz increments using the model's reported range; double-click to type an exact value. Default: 50 Hz.    | 0 to (high-cut − 50), step 50 Hz    |
| **High Cut < / >**        | Adjusts the TX filter high-cut frequency. Step buttons move in 50 Hz increments using the model's reported range; double-click to type an exact value. Default: 3300 Hz. | (low-cut + 50) to 10000, step 50 Hz |

## How Low Cut and High Cut stepping works

The **Low Cut < / >** and **High Cut < / >** buttons snap the filter frequency to the next multiple of 50 Hz in the chosen direction, rather than adding or subtracting a fixed 50 Hz from the current value. For example, if the current low-cut value is 87 Hz on a radio that accepts continuous values, clicking `>` sets it to 100 Hz and clicking `<` sets it to 50 Hz. You can also adjust either control with the mouse wheel.

Some radios publish a discrete list of valid edge frequencies. When the radio provides such a list, the step buttons move to the nearest valid value in the chosen direction rather than to a 50 Hz multiple. The stepping behavior is a UI convenience; the radio ultimately enforces the actual limits.

## Direct numeric entry for Low Cut and High Cut

As of v26.8.4, you can double-click the **Low Cut** or **High Cut** value label to type an exact frequency in Hz instead of stepping to it 50 Hz at a time:

1. Double-click the value label for **Low Cut** or **High Cut**.
2. Type the desired frequency in Hz.
3. Press Enter to apply the value.

Typed values are validated against the current model range and are **rejected** (not clamped) if out of range. For example, typing a low-cut value at or above the current high-cut minus the minimum filter width is ignored and the previous value is restored. On radios that publish a discrete edge list, typed values must be present in that list to be accepted.

This behavior differs deliberately from the step buttons: a step is a request to move by one increment, so stopping at a bound is sensible; a typed number is a request for that exact value, so it is either honored or rejected entirely.

## Tips

- The numeric label next to the **AM Carrier** slider shows the current value in real time. Use it to set a precise level without guessing the slider position.
- The AM Carrier slider has no persisted setting key. Its value is read from the radio on connect and reset if you reconnect.
- Because **Low Cut** and **High Cut** step to valid boundaries, clicking once from an off-grid value (for example, a value not divisible by 50) will first align to the nearest boundary before continuing to step in the expected direction.
- The Phone applet now supports theming. Its appearance automatically adapts to the selected theme, affecting colors of labels, sliders, and buttons.
- The **DEXP** controls no longer persist settings to disk. Their state is communicated directly to the radio and reset on reconnect.

## Related

- [Phone overview](overview.md)
- [Enable VOX and set trigger threshold](enable-vox-and-set-trigger-threshold.md)
- [Set the TX audio low-cut frequency](set-the-tx-audio-low-cut-frequency.md)
- [Set the TX audio high-cut frequency](set-the-tx-audio-high-cut-frequency.md)