# Compare EQ on vs EQ off quickly with the ON button

Use the ON button to toggle the radio-side equalizer in and out while listening, so you can hear the difference between your current band settings and a flat response without moving any sliders.

## Before you start

- AetherSDR must be connected to the radio. The EQ applet requires an active radio connection.
- Open the Equalizer tile by clicking the EQ tray button in the right sidebar applet panel.
- Set your band sliders to a non-flat curve. Toggling ON when all bands are at 0 dB produces no audible difference.

## Steps

1. In the Equalizer tile, click RX or TX to select the path you want to evaluate.
2. Confirm the sliders show the curve you want to compare against flat.
3. Click ON. The button highlights green and the equalizer is applied to the selected path on the radio.
4. Listen to the audio.
5. Click ON again. The green highlight disappears and the equalizer is bypassed — the radio reverts to a flat response on that path.
6. Repeat steps 3–5 as many times as needed to compare.

## What each control does

| Control | Behavior | Default |
|---|---|---|
| ON | Enables or disables the equalizer for the currently-selected path (RX or TX). Highlights green when enabled. Slider positions are preserved while bypassed. | Off (unchecked) |
| Reset arc (revert icon) | Resets all 8 bands of the currently-selected path back to 0 dB. Drawn as a 3/4-circle arrow. Tooltip: "Reset all bands to 0 dB". | N/A |
| RX | Selects the receive path for display and editing. ON acts on the RX equalizer when RX is active. Highlights blue when active. | Unchecked |
| TX | Selects the transmit path for display and editing. ON acts on the TX equalizer when TX is active. Highlights blue when active. Applet opens on the TX view by default, or restores the last-selected view between sessions. | Checked |
| 63 | Trims the 63 Hz band for the selected path. Value label below the slider updates live. While dragging, a popup shows the signed dB value (+/-). | 0 dB |
| 125 | Trims the 125 Hz band for the selected path. While dragging, a popup shows the signed dB value (+/-). | 0 dB |
| 250 | Trims the 250 Hz band for the selected path. While dragging, a popup shows the signed dB value (+/-). | 0 dB |
| 500 | Trims the 500 Hz band for the selected path. While dragging, a popup shows the signed dB value (+/-). | 0 dB |
| 1k | Trims the 1 kHz band for the selected path. While dragging, a popup shows the signed dB value (+/-). | 0 dB |
| 2k | Trims the 2 kHz band for the selected path. While dragging, a popup shows the signed dB value (+/-). | 0 dB |
| 4k | Trims the 4 kHz band for the selected path. While dragging, a popup shows the signed dB value (+/-). | 0 dB |
| 8k | Trims the 8 kHz band for the selected path. While dragging, a popup shows the signed dB value (+/-). | 0 dB |
| +10 / 0 / -10 dB scale | Left and right reference labels showing the +/-10 dB range of the sliders. | N/A |

## Drag value popup

When you click and drag any EQ band slider, a small popup appears near the slider handle showing the exact dB value with a plus or minus sign (e.g., "+3 dB" or "-5 dB"). The popup follows the handle as you drag and disappears a short moment after you release the mouse button.

This makes it easy to see the exact value without looking at the number below the slider, especially when you are focusing on the audio changes.

## Tips

- ON is path-specific. Toggling ON while RX is selected does not affect the TX equalizer, and vice versa. Switch paths with RX or TX before toggling if you want to compare the other direction.
- Your band slider positions are not changed by toggling ON. You can safely toggle in and out repeatedly without losing your curve.
- The applet remembers which view (RX or TX) you last selected and restores it the next time you open the Equalizer tile. The TX view remains the default for first-time use.
- Use the Reset arc button to quickly flatten all bands for the selected path without clicking individual sliders.

## Related

- [Equalizer (Graphic) overview](overview.md)
- [Enable radio-side graphic EQ for RX](enable-radio-side-graphic-eq-for-rx.md)
- [Enable radio-side graphic EQ for TX](enable-radio-side-graphic-eq-for-tx.md)
- [Switch between shaping RX audio and TX audio](switch-between-shaping-rx-audio-and-tx-audio.md)
- [Boost or cut specific octave bands (63 Hz to 8 kHz)](boost-or-cut-specific-octave-bands-63-hz-to-8-khz.md)
- Reset all EQ bands to flat