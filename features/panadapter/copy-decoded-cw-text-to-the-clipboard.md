# Copy decoded CW text to the clipboard

Use the CW decode panel's copy buttons to capture decoded Morse text into the system clipboard — either the full decode history or only the text currently visible on screen.

## Before you start

- The CW decode panel must be open and active. If it is not visible below the panadapter, see [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md).
- The decoder requires PC audio routing to produce any text. The panel shows "(requires PC Audio)" as a reminder if audio is not configured.

## Steps

1. Look at the CW decode text area at the bottom of the panadapter to confirm decoded text is present.
2. To copy everything the decoder has captured since the last clear, click `CPY ALL`.
3. To copy only the text currently visible in the scroll area, scroll to the portion you want, then click `CPY VIS`.
4. Paste into any application using your system's standard paste command.

## What each control does

| Control | Behavior | Default | Range | Setting key |
|---|---|---|---|---|
| `CPY ALL` | Copies the full decoded text buffer to the clipboard. | — | — | — |
| `CPY VIS` | Copies only the text currently visible in the scroll area to the clipboard. | — | — | — |
| `CLR` | Clears the CW decode buffer. Text already copied to the clipboard is unaffected. | — | — | — |
| Sens | Filters low-confidence decodes; higher values are stricter. | 30 | 0–100 | `CwDecoderSensitivity` |

## Tips

- Text in the decode display is colour-coded by confidence. Green indicates the highest confidence; yellow, orange, and red indicate progressively lower confidence. If most of your copied text appears orange or red, consider raising the Sens slider to filter out low-confidence characters before copying.
- If the buffer has grown long, use `CPY VIS` to copy only a specific passage by scrolling to it first, then clicking `CPY VIS`.
- Click `CLR` before a new contact to keep the buffer relevant, so `CPY ALL` captures only the current session.

## Related

- [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md)
- [Tune CW decoder sensitivity to reject noise](tune-cw-decoder-sensitivity-to-reject-noise.md)
- [Lock CW decoder pitch or speed once tracking is good](lock-cw-decoder-pitch-or-speed-once-tracking-is-good.md)
