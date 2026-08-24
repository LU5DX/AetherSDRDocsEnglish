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

### Adjust the decoded text font size

As of v26.7.4, you can increase or decrease the font size of decoded CW text for better readability.

1. Locate the `A-` and `A+` buttons in the CW decode panel's button bar.
2. Click `A+` to increase the font size.
3. Click `A-` to decrease the font size.

The font size is persisted across sessions. Valid range is 8 to 32 pixels.

### Resize the CW decode panel

As of v26.7.4, you can drag the top edge of the CW panel to change its height, revealing more decoded text history.

1. Hover over the thin resize grip at the top of the CW decode panel. The cursor changes to a vertical resize cursor.
2. Click and drag up or down to resize the panel.

The panel height is persisted across sessions. Valid range is 60 to 600 pixels.

## What each control does

| Control                 | What it does                                                                                 | Default |
|-------------------------|----------------------------------------------------------------------------------------------|---------|
| `CPY ALL`               | Copies the full decoded text buffer to the clipboard.                                        | —       |
| `CPY VIS`               | Copies only the text currently visible in the scroll area to the clipboard.                  | —       |
| `CLR`                   | Clears the CW decode buffer entirely. Text cannot be recovered after clearing.               | —       |
| Right-click > **Clear** | Clears the CW decode buffer from the context menu of the text area. Equivalent to `CLR`.     | —       |
| `A-` / `A+` (v26.7.4)  | Decreases/increases the decoded-text font size. Persisted by `CwDecodeSettings::fontPx()`.   | 13 px   |
| Resize grip (v26.7.4)  | Drag up or down to change the panel height. Persisted by `CwDecodeSettings::panelHeight()`.  | 80 px   |
| Sens                    | Filters low-confidence decodes before they appear in the buffer. Higher values are stricter. | 30      |
| 🔒P (Lock Pitch)        | Locks the CW decoder pitch to the current tuned frequency.                                   | —       |
| 🔒S (Lock Speed)        | Locks the CW decoder speed to the current WPM.                                               | —       |
| Pitch range slider      | Double-handle slider that sets the decoder pitch search range (Lo to Hi) in Hz.              | 500–700 |
| WPM range slider        | Double-handle slider that sets the decoder speed search range (Lo to Hi) in WPM.             | 15–40   |

## CW stats display

The CW stats label shows the detected pitch and speed in the format `<hz> Hz  <wpm> WPM`. These values update in real time as the decoder processes signals.

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

## Panadapter title bar and canvas drag

When the panadapter is hosted on the workspace canvas (new in v26.8.4), the title bar (accessible name "panTitleBar") supports drag-to-move as a live gesture. A click (movement under 6 px before release) activates the panadapter; a press followed by movement beyond 6 px begins a drag that moves the panadapter on the canvas. The pop-out button remains visible for canvas items even in single-pan mode. Off-canvas, the button visibility reverts to the standard single-pan behavior.

## Tips

- Use `CPY VIS` when you want only a specific exchange or callsign that is visible on screen, without the surrounding session noise.
- Use `CPY ALL` when logging a full QSO or saving a complete decode session.
- Click `CLR` (or right-click the text area and choose **Clear**) before a new QSO to keep the buffer relevant. Note that clearing the buffer also removes text that `CPY ALL` would have captured.
- Decoded RX text is colour-coded by confidence: green is highest confidence, then yellow, orange, and red. TX text (your own sending) appears in cyan. Raising the Sens slider suppresses red and orange characters from appearing in the buffer. See [Tune CW decoder sensitivity to reject noise](tune-cw-decoder-sensitivity-to-reject-noise.md).
- Use the pitch range slider (embedded double-handle slider labelled "Pitch") to narrow the decoder's frequency search. Set the left handle for minimum pitch and the right handle for maximum pitch. The default range is 500–700 Hz.
- Use the WPM range slider (embedded double-handle slider labelled "WPM") to constrain the decoder's speed search. The default range is 15–40 WPM.
- Lock Pitch (`🔒P`) and Lock Speed (`🔒S`) buttons let you freeze the current detected values so the decoder no longer adjusts pitch or speed even if the signal varies.
- Use `A+` and `A-` to adjust the decoded text font for better readability, especially in small panadapter windows.
- Drag the resize grip at the top of the CW panel to show more decoded text history without scrolling.

## Related

- [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md)
- [Tune CW decoder sensitivity to reject noise](tune-cw-decoder-sensitivity-to-reject-noise.md)
- [Lock CW decoder pitch or speed once tracking is good](lock-cw-decoder-pitch-or-speed-once-tracking-is-good.md)