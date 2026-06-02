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

| Control               | Description                                        | Valid range |
|-----------------------|----------------------------------------------------|-------------|
| **AM Carrier** slider | Sets the AM carrier power level sent to the radio. Drag to adjust; tooltip shows percentage. | 0–100       |
| **VOX** button | Toggles voice-operated transmit on or off. | — |
| **VOX level** slider | Sets the VOX activation threshold. Drag to adjust; tooltip shows percentage. | 0–100 |
| **Delay** slider | Sets the VOX hang time before returning to receive. | 0–100 |
| **DEXP** button | Toggles the downward expander (noise gate). Stored as `DexpEnabled`. See note below. | — |
| **DEXP threshold** slider | Sets the DEXP gate threshold. Stored as `DexpLevel`. Default: 0. Drag to adjust; tooltip shows percentage. See note below. | 0–100 |
| **Low Cut < / >** | Adjusts the TX filter low-cut frequency in 50 Hz steps by snapping to the nearest 50 Hz multiple in the chosen direction. Default: 50 Hz. | 0 to (high-cut − 50) |
| **High Cut < / >** | Adjusts the TX filter high-cut frequency in 50 Hz steps by snapping to the nearest 50 Hz multiple in the chosen direction. Default: 3300 Hz. | (low-cut + 50) to 10000 |

> **Note — DEXP firmware limitation:** The **DEXP** toggle and **DEXP threshold** slider are non-functional on firmware v1.4.0.0. The radio returns error `0x5000002D` when these controls are used.

## How Low Cut and High Cut stepping works

As of v0.9.5.1, the **Low Cut < / >** and **High Cut < / >** buttons snap the filter frequency to the next multiple of 50 Hz in the chosen direction, rather than adding or subtracting a fixed 50 Hz from the current value. For example, if the current low-cut value is 87 Hz, clicking `>` sets it to 100 Hz and clicking `<` sets it to 50 Hz. You can also adjust either control with the mouse wheel. The radio accepts any integer Hz value; the snapping behaviour is a UI convenience only.

## Tips

- The numeric label next to the **AM Carrier** slider shows the current value in real time. Use it to set a precise level without guessing the slider position.
- The AM Carrier slider has no persisted setting key. Its value is read from the radio on connect and reset if you reconnect.
- Because **Low Cut** and **High Cut** now snap to 50 Hz multiples, clicking once from an off-grid value (for example, a value not divisible by 50) will first align to the nearest boundary before continuing to step in the expected direction.
- The Phone applet now supports theming. Its appearance automatically adapts to the selected theme, affecting colors of labels, sliders, and buttons.

## Related

- [Phone overview](overview.md)
- [Enable VOX and set trigger threshold](enable-vox-and-set-trigger-threshold.md)
- [Set the TX audio low-cut frequency](set-the-tx-audio-low-cut-frequency.md)
- [Set the TX audio high-cut frequency](set-the-tx-audio-high-cut-frequency.md)