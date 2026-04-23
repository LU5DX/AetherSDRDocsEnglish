# Copy decoded CW text to the clipboard

Use the CW decode panel to copy Morse text that has been decoded off-air — either the full decode buffer or only what is currently visible on screen.

## Before you start

- The CW decode panel must be open and actively decoding. If it is not visible, see [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md).
- The CW decoder requires PC audio routing to receive signal. The panel displays "(requires PC Audio)" as a reminder.

## Steps

1. Locate the CW decode panel at the bottom of the Panadapter applet.
2. To copy everything in the decode buffer, click `CPY ALL`. All text in the decode buffer is placed on the clipboard.
3. To copy only the text currently visible in the scroll area, click `CPY VIS`. Only the visible portion is placed on the clipboard.

## What each control does

| Control | Behavior | Default | Range | Setting key |
|---|---|---|---|---|
| CPY ALL | Copies the full decoded text buffer to the clipboard. | — | — | — |
| CPY VIS | Copies only the text currently visible in the scroll area to the clipboard. | — | — | — |
| CLR | Clears the CW decode buffer entirely. Does not affect the clipboard. | — | — | — |
| Sens | Filters low-confidence decodes. Higher values are stricter. | 30 | 0–100 | `CwDecoderSensitivity` |
| CW decode text | Read-only rolling display of decoded CW, coloured by confidence. Green = highest confidence; yellow, orange, and red indicate progressively lower confidence. | — | — | — |

## Tips

- If the buffer has accumulated a long session but you only want the most recent exchange, scroll the decode text to the portion you want and use `CPY VIS` rather than `CPY ALL`.
- Use `CLR` to reset the decode buffer before a new contact so that `CPY ALL` captures only that contact's text.
- Adjust the Sens slider to reduce noise characters in the buffer before copying. A value of 30 (the default) passes most readable text while rejecting the lowest-confidence decodes.

## Troubleshooting

- **CPY ALL places an empty string on the clipboard** — The decode buffer is empty. Check that the CW decoder is receiving audio and that the Sens slider is not set so high that all decodes are being filtered out.
- **CPY VIS copies less text than expected** — Only the text visible in the scroll area at the moment of the click is copied. Scroll the decode panel to show the desired text first.

## Related

- [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md)
- [Tune CW decoder sensitivity to reject noise](tune-cw-decoder-sensitivity-to-reject-noise.md)
- [Lock CW decoder pitch or speed once tracking is good](lock-cw-decoder-pitch-or-speed-once-tracking-is-good.md)
