# Copy decoded CW text to the clipboard

The CW decode panel provides two copy buttons that let you transfer decoded Morse text to the system clipboard — either the full decode history or only the text currently on screen.

## Before you start

- The CW decode panel must be open and actively decoding. If it is not visible, see [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md).
- PC audio must be routed to AetherSDR. The panel displays "(requires PC Audio)" as a reminder if audio is not flowing.

## Steps

1. Locate the CW decode panel beneath the panadapter spectrum and waterfall.
2. Choose which text to copy:
   - To copy everything in the decode buffer, click `CPY ALL`.
   - To copy only the text currently visible in the scroll area, click `CPY VIS`.
3. Paste into any application using your system's standard paste command.

To remove all decoded text from the buffer after copying, click `CLR`.

## What each control does

| Control | Behavior | Default | Range | Setting key |
|---|---|---|---|---|
| `CPY ALL` | Copies the full decoded text buffer to the clipboard. | — | — | — |
| `CPY VIS` | Copies only the text currently visible in the scroll area to the clipboard. | — | — | — |
| `CLR` | Clears the CW decode buffer. Does not affect the clipboard. | — | — | — |
| Sens | Filters low-confidence decodes; higher values reject more uncertain characters. | 30 | 0–100 | `CwDecoderSensitivity` |

## Tips

- Text in the decode display is colour-coded by confidence. Characters shown in red represent the lowest-confidence decodes and may contain errors. If accuracy matters, copy after tuning the Sens slider upward to suppress poor decodes — see [Tune CW decoder sensitivity to reject noise](tune-cw-decoder-sensitivity-to-reject-noise.md).
- `CPY VIS` is useful when you have scrolled back to a specific portion of a QSO and want only that excerpt on the clipboard.

## Related

- [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md)
- [Tune CW decoder sensitivity to reject noise](tune-cw-decoder-sensitivity-to-reject-noise.md)
- [Lock CW decoder pitch or speed once tracking is good](lock-cw-decoder-pitch-or-speed-once-tracking-is-good.md)
