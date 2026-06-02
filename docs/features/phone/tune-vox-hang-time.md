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

| Control          | Description                                                                                                    | Valid range |
|------------------|----------------------------------------------------------------------------------------------------------------|-------------|
| **Delay** slider | Sets the VOX hang time — how long the radio remains in transmit after speech ends before returning to receive. | 0–100       |

No setting key is persisted for the Delay slider; the value is sent directly to the radio.

## Tips

- A Delay value that is too low causes the transmitter to drop in and out between words. Raise the value until tail drop-outs stop.
- A Delay value that is too high keeps the transmitter keyed well after you finish speaking, blocking other stations. Lower the value until the hang is just long enough to cover normal pauses.
- The VOX level threshold and Delay interact: a more sensitive (lower) VOX level may require a shorter Delay, and vice versa.

## TX filter cut-point stepping behavior

As of v0.9.5.1, the **Low Cut < / >** and **High Cut < / >** buttons snap the filter frequency to the nearest multiple of 50 Hz in the chosen direction, rather than adding or subtracting a fixed 50 Hz from the current value.

For example, if the low-cut is currently set to 87 Hz:

- Pressing **>** (increase) moves it to **100 Hz** (the next multiple of 50 above 87).
- Pressing **<** (decrease) moves it to **50 Hz** (the next multiple of 50 below 87).

This means a single button press always lands on a clean 50 Hz boundary regardless of the starting value. The mousewheel on each spinbox follows the same snap behavior. The radio accepts any integer Hz value, so the snapping is a UI convenience only and does not restrict what the radio will accept.

| Control            | Description                                                              | Default | Valid range                          |
|--------------------|--------------------------------------------------------------------------|---------|--------------------------------------|
| **Low Cut < / >**  | Sets the TX filter low-cut frequency; snaps to the next 50 Hz boundary. | 50 Hz   | 0 to (high-cut − 50), step 50 Hz    |
| **High Cut < / >** | Sets the TX filter high-cut frequency; snaps to the next 50 Hz boundary.| 3300 Hz | (low-cut + 50) to 10000, step 50 Hz |

Neither control has a persisted setting key; values are sent directly to the radio.

## Slider value formatting

As of v26.5.3, the **AM Carrier**, **VOX level**, and **DEXP threshold** sliders display their value as a percentage (e.g., "48%") when dragged. The numeric label next to the slider continues to show the raw 0–100 value without a percent sign.

## Theme support

As of v26.6.1, the Phone applet uses theme-aware colors instead of hardcoded hex values. The slider backgrounds, handle colors, button backgrounds, and text colors all follow the currently loaded theme. Themes are managed through `View > Theme Manager`.

## Related

- [Enable VOX and set trigger threshold](enable-vox-and-set-trigger-threshold.md)
- [Phone overview](overview.md)