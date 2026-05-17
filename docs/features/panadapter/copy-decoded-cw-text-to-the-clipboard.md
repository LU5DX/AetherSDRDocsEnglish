# Copy decoded CW text to the clipboard

The CW decode panel provides two clipboard buttons that let you capture decoded Morse text — either the entire session buffer or only what is currently visible on screen.

## Before you start

- The CW decode panel must be open and actively decoding. If it is not visible, see [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md).
- PC audio must be routed to AetherSDR. The "(requires PC Audio)" indicator in the CW panel is a reminder that decoding stops without it.

## Steps

### Copy all decoded text

1. Locate the CW decode panel beneath the panadapter spectrum.
2. Click `CPY ALL`.

All text in the decode buffer is copied to the clipboard, including any text that has scrolled off screen.

### Copy only the visible text

1. Locate the CW decode panel beneath the panadapter spectrum.
2. Scroll the decode area to the portion of text you want.
3. Click `CPY VIS`.

Only the text currently visible in the scroll area is copied.

### Clear the buffer from the right-click menu

As of v0.9.2.1, the decoded text area has a context menu. Right-click anywhere in the CW decode text area to open it. The menu contains the standard text editing actions followed by a separator and a **Clear** item. Click **Clear** to erase the decode buffer. This is equivalent to clicking `CLR`.

## What each control does

| Control                 | What it does                                                                                 | Default |
|-------------------------|----------------------------------------------------------------------------------------------|---------|
| `CPY ALL`               | Copies the full decoded text buffer to the clipboard.                                        | —       |
| `CPY VIS`               | Copies only the text currently visible in the scroll area to the clipboard.                  | —       |
| `CLR`                   | Clears the CW decode buffer entirely. Text cannot be recovered after clearing.               | —       |
| Right-click > **Clear** | Clears the CW decode buffer from the context menu of the text area. Equivalent to `CLR`.     | —       |
| Sens                    | Filters low-confidence decodes before they appear in the buffer. Higher values are stricter. | 30      |

## Decoded text display

The CW decode panel shows decoded text from both received (RX) and transmitted (TX) keying in a single rolling display. Text is colour-coded so you can distinguish incoming Morse from your own sending:

| Colour       | Meaning                                                              |
|--------------|----------------------------------------------------------------------|
| Green        | RX text with high confidence (< 0.15 cost)                           |
| Yellow       | RX text with moderate confidence (< 0.35 cost)                       |
| Orange       | RX text with lower confidence (< 0.60 cost)                          |
| Red          | RX text with lowest confidence (>= 0.60 cost)                        |
| Cyan         | TX text (your own sending) — any confidence level                    |

A separator space is automatically inserted when the display switches between TX and RX text runs so the two coloured blocks do not visually merge.

## Tips

- Use `CPY VIS` when you want only a specific exchange or callsign that is visible on screen, without the surrounding session noise.
- Use `CPY ALL` when logging a full QSO or saving a complete decode session.
- Click `CLR` (or right-click the text area and choose **Clear**) before a new QSO to keep the buffer relevant. Note that clearing the buffer also removes text that `CPY ALL` would have captured.
- Decoded RX text is colour-coded by confidence: green is highest confidence, then yellow, orange, and red. TX text (your own sending) appears in cyan. Raising the Sens slider suppresses red and orange characters from appearing in the buffer. See [Tune CW decoder sensitivity to reject noise](tune-cw-decoder-sensitivity-to-reject-noise.md).

## Related

- [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md)
- [Tune CW decoder sensitivity to reject noise](tune-cw-decoder-sensitivity-to-reject-noise.md)
- [Lock CW decoder pitch or speed once tracking is good](lock-cw-decoder-pitch-or-speed-once-tracking-is-good.md)