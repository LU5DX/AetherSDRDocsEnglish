# Boost or cut specific octave bands (63 Hz to 8 kHz)

Use the Equalizer applet to raise or lower individual frequency bands on the radio's receive or transmit audio path. Each of the eight bands can be trimmed anywhere from −10 dB to +10 dB.

## Before you start

- AetherSDR must be connected to the radio. The Equalizer applet requires an active radio connection.
- Decide whether you are shaping the RX or TX path before moving sliders.

## Steps

1. Click the EQ tray button in the right sidebar applet panel to open the Equalizer tile.
2. Click TX to edit the transmit path, or click RX to edit the receive path. TX is selected by default when the applet opens. The last-selected view is remembered and restored the next time you open the applet.
3. Click ON to enable the equalizer for the selected path. ON highlights green when active.
4. Drag the slider for the band you want to adjust. Bands are labeled **63**, **125**, **250**, **500**, **1k**, **2k**, **4k**, and **8k** (Hz and kHz respectively). Drag up to boost, drag down to cut.
5. As you drag, a pop-up label appears near the slider handle showing the current dB value (e.g., "+3 dB" or "−5 dB"). Read the value label directly below each slider handle to confirm the dB amount. The label updates live as you drag.
6. You can also nudge a slider with the keyboard arrow keys (Up/Down or Left/Right) when a slider has focus. The pop-up label appears and lingers briefly after the key release, the same as after a mouse drag.
7. Repeat steps 4–6 for any other bands you want to adjust.

## What each control does

| Control | Type | Default | Range | Behavior |
|---|---|---|---|---|
| ON | Toggle button | Off (unchecked) | On / Off | Enables or disables the equalizer for the currently-selected path. Highlights green when enabled. |
| RX | Toggle button | Unchecked | — | Switches the applet to display and edit the receive equalizer bands. Highlights blue when active. |
| TX | Toggle button | Checked | — | Switches the applet to display and edit the transmit equalizer bands. Highlights blue when active. Starts checked — applet opens on the TX view. |
| Reset arc button | Push button | — | — | Resets all 8 bands of the currently-selected path to 0 dB. Tooltip: "Reset all bands to 0 dB". Drawn as a 3/4-circle arrow. |
| 63 | Vertical slider | 0 dB | −10 to +10 dB | Trims the 63 Hz band for the selected path. Drag up to boost, down to cut. A pop-up shows the exact value while dragging and lingers briefly after release. Keyboard arrow nudge also shows the pop-up. |
| 125 | Vertical slider | 0 dB | −10 to +10 dB | Trims the 125 Hz band for the selected path. Drag up to boost, down to cut. A pop-up shows the exact value while dragging and lingers briefly after release. Keyboard arrow nudge also shows the pop-up. |
| 250 | Vertical slider | 0 dB | −10 to +10 dB | Trims the 250 Hz band for the selected path. Drag up to boost, down to cut. A pop-up shows the exact value while dragging and lingers briefly after release. Keyboard arrow nudge also shows the pop-up. |
| 500 | Vertical slider | 0 dB | −10 to +10 dB | Trims the 500 Hz band for the selected path. Drag up to boost, down to cut. A pop-up shows the exact value while dragging and lingers briefly after release. Keyboard arrow nudge also shows the pop-up. |
| 1k | Vertical slider | 0 dB | −10 to +10 dB | Trims the 1 kHz band for the selected path. Drag up to boost, down to cut. A pop-up shows the exact value while dragging and lingers briefly after release. Keyboard arrow nudge also shows the pop-up. |
| 2k | Vertical slider | 0 dB | −10 to +10 dB | Trims the 2 kHz band for the selected path. Drag up to boost, down to cut. A pop-up shows the exact value while dragging and lingers briefly after release. Keyboard arrow nudge also shows the pop-up. |
| 4k | Vertical slider | 0 dB | −10 to +10 dB | Trims the 4 kHz band for the selected path. Drag up to boost, down to cut. A pop-up shows the exact value while dragging and lingers briefly after release. Keyboard arrow nudge also shows the pop-up. |
| 8k | Vertical slider | 0 dB | −10 to +10 dB | Trims the 8 kHz band for the selected path. Drag up to boost, down to cut. A pop-up shows the exact value while dragging and lingers briefly after release. Keyboard arrow nudge also shows the pop-up. |
| +10 / 0 / −10 dB scale | Reference labels | — | — | Left and right reference labels showing the +/-10 dB range of the sliders. |
| Per-band value label | Indicator | 0 | −10 through +10 | Shows the live dB value of the slider directly below its handle. |
| Drag pop-up | Indicator | None | −10 through +10 | Floating label that appears near the slider handle during drag operations or after a keyboard arrow nudge. Displays the current dB value with a sign (e.g., "+3 dB" or "−5 dB"). Lingers for a moment after releasing the mouse button or keyboard key. |

## Tips

- RX and TX settings are independent. Adjusting bands while TX is selected has no effect on the RX curve, and vice versa.
- The +10 / 0 / −10 dB scale labels on the left and right edges of the slider column give a visual reference for the slider midpoint (0 dB) and limits.
- To quickly return all bands to flat without moving each slider individually, click the Reset arc button.
- The applet remembers whether you last used RX or TX view. When you reopen the Equalizer tile, it shows the same view you were using before, saving you a click.
- The drag pop-up shows a signed dB value (e.g., "+3 dB" for positive values, "−3 dB" for negative values, "0 dB" for zero) to match the formatting used elsewhere in the application.
- The slider handle and groove colours adapt to the active theme. Handle colour uses the accent colour, while the groove background uses the slider track colour from the current theme.
- Moving the previous or next slider with the keyboard Tab key does not trigger the pop-up. Only arrow keys on a focused slider show the pop-up.

## Troubleshooting

- **Sliders move but audio is not affected** — Check that ON is highlighted green for the active path. The equalizer has no effect when ON is unchecked, even if the sliders are set to non-zero values.
- **Adjusting sliders on TX path changes what you hear on RX** — You may be on the wrong path. Click RX to confirm you are editing the receive bands, or click TX for transmit. The two paths are independent; only the currently-displayed path is being edited.

## Related

- [Equalizer (Graphic) overview](overview.md)
- [Enable radio-side graphic EQ for TX](enable-radio-side-graphic-eq-for-tx.md)
- [Enable radio-side graphic EQ for RX](enable-radio-side-graphic-eq-for-rx.md)
- [Reset all bands to flat with one click](reset-all-bands-to-flat-with-one-click.md)
- [Switch between shaping RX audio and TX audio](switch-between-shaping-rx-audio-and-tx-audio.md)
- [Compare EQ on vs EQ off quickly with the ON button](compare-eq-on-vs-eq-off-quickly-with-the-on-button.md)