# Equalizer (Graphic) overview

The Equalizer (Graphic) applet provides an 8-band graphic equalizer that runs inside the Flex radio itself, applied via the radio's TCP/IP API. Use it to shape the frequency response of your received audio or your transmitted signal across eight fixed octave bands from 63 Hz to 8 kHz.

This equalizer is separate from any client-side parametric EQ in AetherSDR. Changes take effect in the radio's DSP, not in software on your computer.

## Before you start

- Connect AetherSDR to a Flex radio. The applet requires an active radio connection.
- Make the applet panel visible. If it is hidden, go to `View > Applet Panel` to show it.

## How it works

Click the EQ tray button in the right sidebar to toggle the Equalizer tile open or closed. The tile appears in the top row of the applet panel.

The applet always shows one path at a time — either RX or TX. Use the RX and TX buttons to switch which path you are viewing and editing. The applet opens on the TX view by default. AetherSDR remembers the last-selected view (RX or TX) between sessions — if you close the applet while viewing the RX equalizer, it will open on RX the next time you launch the program.

Each of the eight bands has a vertical slider. Moving a slider sends the new value to the radio immediately; the dB value below each slider updates live. While dragging a slider, a popup appears near the slider handle showing the current dB value (formatted with a sign, e.g. "+3 dB" or "-5 dB"). Enabling or disabling the equalizer with ON also takes effect immediately on the currently selected path.

When you adjust a slider using the keyboard (for example, via arrow keys), a drag-value popup flashes to show the new value, then lingers and fades with the same timeout as a mouse release. This allows you to read the final value after a keyboard step.

The RX and TX paths are independent. You can have different curves on each, and enable or disable them separately.

## What each control does

| Control | Kind | Default | Range | Behavior |
|---|---|---|---|---|
| ON | Toggle button | Off (unchecked) | On / Off | Enables or disables the equalizer for the currently selected path (RX or TX). Highlighted green when enabled. |
| Reset arc (revert icon) | Push button | — | — | Resets all 8 bands of the currently selected path to 0 dB. Tooltip: "Reset all bands to 0 dB". |
| RX | Toggle button | Off (unchecked) | On / Off | Selects the receive equalizer path for display and editing. Highlighted blue when active. Mutually exclusive with TX. |
| TX | Toggle button | On (checked) | On / Off | Selects the transmit equalizer path for display and editing. Highlighted blue when active. Mutually exclusive with RX. |
| 63 | Vertical slider | 0 dB | −10 to +10 dB | Trims the 63 Hz band for the selected path. Shows a drag-value popup while the slider is being moved or adjusted via keyboard. |
| 125 | Vertical slider | 0 dB | −10 to +10 dB | Trims the 125 Hz band for the selected path. Shows a drag-value popup while the slider is being moved or adjusted via keyboard. |
| 250 | Vertical slider | 0 dB | −10 to +10 dB | Trims the 250 Hz band for the selected path. Shows a drag-value popup while the slider is being moved or adjusted via keyboard. |
| 500 | Vertical slider | 0 dB | −10 to +10 dB | Trims the 500 Hz band for the selected path. Shows a drag-value popup while the slider is being moved or adjusted via keyboard. |
| 1k | Vertical slider | 0 dB | −10 to +10 dB | Trims the 1 kHz band for the selected path. Shows a drag-value popup while the slider is being moved or adjusted via keyboard. |
| 2k | Vertical slider | 0 dB | −10 to +10 dB | Trims the 2 kHz band for the selected path. Shows a drag-value popup while the slider is being moved or adjusted via keyboard. |
| 4k | Vertical slider | 0 dB | −10 to +10 dB | Trims the 4 kHz band for the selected path. Shows a drag-value popup while the slider is being moved or adjusted via keyboard. |
| 8k | Vertical slider | 0 dB | −10 to +10 dB | Trims the 8 kHz band for the selected path. Shows a drag-value popup while the slider is being moved or adjusted via keyboard. |
| Per-band value label | Indicator | 0 | −10 through +10 | Shows the current dB value of each band below its slider handle. Updates live as you move the slider. |
| +10 / 0 / −10 dB scale | Indicator | — | — | Reference labels on the left and right edges of the slider area showing the slider range. |

No band slider values from this applet are persisted in AetherSDR's local configuration; all slider values are stored in and retrieved from the radio. The RX/TX view selection is stored locally so the applet reopens on your last-used path.

## Theme support

The Equalizer applet fully supports live theme switching. When you change themes, the following visual elements update automatically:

- Slider groove background, handle color, and sub-page/add-page fill
- Band label colors
- Scale label colors (+10, 0, −10)
- Reset button background colors and accent color on press
- Overall applet container background

The slider handles use the theme's foreground (fill) accent color rather than the standard handle token to match the intended visual idiom. The groove sub-page and add-page areas remain the groove background color to prevent unwanted accent fills from the global slider style.

## Tips

- Because RX and TX are independent paths, you can leave TX equalization flat while shaping only the RX audio, or vice versa.
- Use ON to quickly compare equalized versus flat audio without moving any sliders. Toggle it off and on while listening to evaluate your curve.
- The reset arc button resets all eight bands at once. If you only want to adjust one band, move just that slider back to 0 manually.
- The drag-value popup appears near the slider handle while you are dragging. The popup lingers briefly after you release the mouse button so you can read the final value. When adjusting sliders via keyboard, a flash of the popup shows the new value, then fades with the same linger duration as a mouse release.
- The applet remembers whether you were on RX or TX when you last used it, even across program restarts.

## Related

- [Enable radio-side graphic EQ for TX](enable-radio-side-graphic-eq-for-tx.md)
- [Enable radio-side graphic EQ for RX](enable-radio-side-graphic-eq-for-rx.md)
- [Boost or cut specific octave bands (63 Hz to 8 kHz)](boost-or-cut-specific-octave-bands-63-hz-to-8-khz.md)
- [Reset all bands to flat with one click](reset-all-bands-to-flat-with-one-click.md)
- [Switch between shaping RX audio and TX audio](switch-between-shaping-rx-audio-and-tx-audio.md)
- [Compare EQ on vs EQ off quickly with the ON button](compare-eq-on-vs-eq-off-quickly-with-the-on-button.md)