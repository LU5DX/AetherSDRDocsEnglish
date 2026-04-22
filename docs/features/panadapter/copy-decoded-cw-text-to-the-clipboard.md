# Copy decoded CW text to the clipboard

Use the CW decode panel's copy buttons to transfer decoded Morse text to the system clipboard — either the full decode history or only what is currently on screen.

## Before you start

- The CW decode panel must be visible. If it is not, enable the CW decoder first.
- The radio must be connected and receiving audio. The CW stats label shows detected pitch and speed when the decoder is active.

## Steps

1. Look at the CW decode text area at the bottom of the panadapter.
2. Choose what to copy:
   - To copy everything in the decode buffer, click **CPY ALL**.
   - To copy only the text currently visible in the scroll area, click **CPY VIS**.
3. Paste from the clipboard into any other application as normal.

## What each control does

| Control | Behavior | Default | Range | Setting key |
|---|---|---|---|---|
| **CPY ALL** | Copies the full decoded text buffer to the clipboard. | — | — | — |
| **CPY VIS** | Copies only the text currently visible in the scroll area to the clipboard. | — | — | — |
| **CLR** | Clears the CW decode buffer. Does not affect the clipboard. | — | — | — |
| **Sens** | Filters low-confidence decodes; higher values are stricter. | 30 | 0–100 | `CwDecoderSensitivity` |

## Tips

- Text in the decode area is coloured by confidence. If much of the text is orange or red, raise the **Sens** slider to suppress low-confidence characters before copying.
- **CPY VIS** is useful when you want to capture only a specific exchange you have scrolled to, without including the entire session history.
- **CLR** clears the buffer on screen. If you want a clean capture starting from a known point, click **CLR** first, wait for the text you need, then click **CPY ALL**.

## Related

- [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md)
- [Tune CW decoder sensitivity to reject noise](tune-cw-decoder-sensitivity-to-reject-noise.md)
- [Lock CW decoder pitch or speed once tracking is good](lock-cw-decoder-pitch-or-speed-once-tracking-is-good.md)
