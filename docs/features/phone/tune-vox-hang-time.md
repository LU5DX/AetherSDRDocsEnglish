# Tune VOX hang time

The VOX hang time controls how long the radio stays in transmit after your voice drops below the VOX trigger threshold. Adjusting it prevents choppy transmit drop-outs at the end of words while avoiding excessive dead air before returning to receive.

## Before you start

- AetherSDR must be connected to the radio. The Phone applet requires an active radio connection.
- VOX must be enabled. If VOX is not already on, enable it first — see [Enable VOX and set trigger threshold](enable-vox-and-set-trigger-threshold.md).

## Steps

1. Open the Phone applet by clicking the **PHNE** tray button in the right sidebar. If the applet panel is hidden, click the panel edge or use `View > Applet Panel` to show it.
2. Locate the **Delay:** row, directly below the VOX level row.
3. Drag the **Delay** slider left to shorten hang time or right to lengthen it. The numeric value to the right of the slider updates as you drag.

## What each control does

| Control            | Description                                                                                                    | Valid range |
|--------------------|----------------------------------------------------------------------------------------------------------------|-------------|
| **AM Carrier**     | Sets AM carrier power level. Displayed as a percentage (e.g., "48%") when dragged.                             | 0–100       |
| **VOX**            | Toggles voice-operated transmit on or off.                                                                     | —           |
| **VOX level**      | Sets the VOX activation threshold. Displayed as a percentage when dragged.                                     | 0–100       |
| **Delay**          | Sets the VOX hang time — how long the radio remains in transmit after speech ends before returning to receive. | 0–100       |
| **DEXP**           | Toggles the downward expander (noise gate) on or off.                                                          | —           |
| **DEXP threshold** | Sets the DEXP noise gate threshold.                                                                            | 0–100       |
| **Low Cut < / >**  | Sets the TX filter low-cut frequency; snaps to the next 50 Hz boundary.                                        | 50 Hz       |
| **High Cut < / >** | Sets the TX filter high-cut frequency; snaps to the next 50 Hz boundary.                                       | 3300 Hz     |

## Setting persistence

- The **DEXP** toggle and **DEXP threshold** slider values are sent directly to the radio. They are no longer persisted to AetherSDR settings.
- No other control in the Phone applet has a persisted setting key; all values are sent directly to the radio.

## Tips

- A Delay value that is too low causes the transmitter to drop in and out between words. Raise the value until tail drop-outs stop.
- A Delay value that is too high keeps the transmitter keyed well after you finish speaking, blocking other stations. Lower the value until the hang is just long enough to cover normal pauses.
- The VOX level threshold and Delay interact: a more sensitive (lower) VOX level may require a shorter Delay, and vice versa.

## TX filter cut-point stepping behavior

As of v26.8.4, the **Low Cut < / >** and **High Cut < / >** buttons snap the filter frequency to the next multiple of 50 Hz in the chosen direction, rather than adding or subtracting a fixed 50 Hz from the current value.

For example, if the low-cut is currently set to 87 Hz:

- Pressing **>** (increase) moves it to **100 Hz** (the next multiple of 50 above 87).
- Pressing **<** (decrease) moves it to **50 Hz** (the next multiple of 50 below 87).

This means a single button press always lands on a clean 50 Hz boundary regardless of the starting value. The mousewheel on each spinbox follows the same snap behavior. When the radio backend publishes a discrete list of allowed edge frequencies, the buttons step through that list instead. On radios that accept continuous integer Hz values, the snapping is a UI convenience only and does not restrict what the radio will accept.

### Direct numeric entry

As of v26.8.4, you can double-click either the **Low Cut** or **High Cut** value to type an exact frequency in Hz instead of stepping to it 50 Hz at a time. Press Enter to commit the value.

- A typed value is treated as a request for that exact frequency. On radios that support arbitrary integer Hz values, the exact value is sent to the radio.
- The step buttons still clamp to the radio's step grid (50 Hz multiples or the backend's discrete edge list). This asymmetry is deliberate: a step is a request to move by one increment, while a typed number is a request for a specific value.
- Out-of-range values are rejected, not clamped. The previous value is restored if you type an invalid frequency.
- When the backend publishes a discrete edge list, typed values not present in that list are rejected.

| Control            | Description                                                              | Default | Valid range                          |
|--------------------|--------------------------------------------------------------------------|---------|--------------------------------------|
| **Low Cut < / >**  | Sets the TX filter low-cut frequency; snaps to the next 50 Hz boundary. Double-click to type an exact Hz value. | 50 Hz   | 0 to (high-cut − 50), step 50 Hz    |
| **High Cut < / >** | Sets the TX filter high-cut frequency; snaps to the next 50 Hz boundary. Double-click to type an exact Hz value. | 3300 Hz | (low-cut + 50) to 10000, step 50 Hz |

Neither control has a persisted setting key; values are sent directly to the radio.

## Slider value formatting

As of v26.5.3, the **AM Carrier**, **VOX level**, and **DEXP threshold** sliders display their value as a percentage (e.g., "48%") when dragged. The numeric label next to the slider continues to show the raw 0–100 value without a percent sign.

## Theme support

As of v26.6.1, the Phone applet uses theme-aware colors instead of hardcoded hex values. The slider backgrounds, handle colors, button backgrounds, and text colors all follow the currently loaded theme. Themes are managed through `View > Theme Manager`.

## Related

- [Enable VOX and set trigger threshold](enable-vox-and-set-trigger-threshold.md)
- [Phone overview](overview.md)