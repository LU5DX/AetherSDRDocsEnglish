# Drag the TX or RX filter cutoff guide line to move the radio passband

The EQ editor canvas shows dashed yellow vertical lines at the radio's current TX or RX filter cutoff edges. Dragging these lines moves the radio's passband in real time, letting you match your EQ shaping to the actual filter boundaries without leaving the EQ editor.

## Before you start

- AetherSDR must be connected to the radio.
- The floating editor for the relevant side (TX or RX) must be open. The guide lines are draggable only in the frameless editor canvas, not in the docked applet tile.
- To open the floating editor, double-click the EQ stage in the CHAIN widget on the TX or RX side. See [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md).

## Steps

1. Open the floating editor for the side you want to adjust: double-click the EQ stage in the CHAIN widget. The editor title bar reads "Aetherial Parametric EQ — TX" or "Aetherial Parametric EQ — RX".
2. Locate the dashed yellow vertical lines on the canvas. There are two: one at the low cutoff edge and one at the high cutoff edge of the radio's current passband.
3. Move the pointer toward one of the dashed yellow lines. When the pointer is close enough to the line, the cursor changes to a horizontal-resize arrow.
4. Click and drag the line left or right. The radio's corresponding filter cutoff updates in real time as you drag.
5. Release to set the new cutoff position.
6. Repeat for the other guide line if you want to adjust the opposite passband edge.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| Filter cutoff guide lines (TX) | Dashed yellow vertical lines on the TX editor canvas marking the radio's current TX low and high filter cutoffs. Drag in the editor to move the radio's TX passband in real time. | Cursor changes to a horizontal-resize arrow when hovering near a line. |
| Filter cutoff guide lines (RX) | Dashed yellow vertical lines on the RX editor canvas marking the active slice's RX passband edges (in the audio-frequency domain). Drag in the editor to move the radio's RX passband in real time. | Cursor changes to a horizontal-resize arrow when hovering near a line. |

## Tips

- The guide lines are visible in both the docked applet tile and the floating editor, but dragging is only active in the floating editor canvas.
- A guide line is absent when the corresponding cutoff value is 0 or not set by the radio.
- Watch the parameter text row at the bottom of the editor while dragging to confirm the resulting passband edges.

## Troubleshooting

- **Cursor does not change to a horizontal-resize arrow near the line** — You are hovering over the docked applet tile, not the floating editor canvas. Open the floating editor by double-clicking the EQ stage in the CHAIN widget, then try again.
- **No dashed yellow lines are visible on the canvas** — The radio has not reported filter cutoff values, or both cutoff values are 0. Verify the radio is connected and a slice is active.

## Related

- [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md)
- [Inspect the TX EQ curve and live spectrum](inspect-the-tx-eq-curve-and-live-spectrum.md)
- [Inspect the RX EQ curve and live spectrum](inspect-the-rx-eq-curve-and-live-spectrum.md)
- [Read exact freq / gain / Q values in the parameter text row](read-exact-freq-gain-q-values-in-the-parameter-text-row.md)
