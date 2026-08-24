# Tune CW decoder sensitivity to reject noise

The **Sens** slider controls how strictly the CW decoder filters uncertain character decodes. Raising it suppresses garbled output caused by noise or weak signals; lowering it shows more characters at the cost of accuracy.

## Before you start

- The CW decode panel must be open in the Panadapter applet. If it is not visible, open it first.
- PC audio must be routed to AetherSDR. The panel displays "(requires PC Audio)" as a reminder.

## Steps

1. Locate the CW decode panel at the bottom of the Panadapter applet.
2. Find the **Sens:** label and the short horizontal slider immediately to its right.
3. Drag the **Sens** slider left to accept more decodes (lower threshold) or right to reject low-confidence decodes (higher threshold).
4. Watch the "CW decode text" area. Characters coloured red or orange indicate low confidence; reduce them by moving the slider right.
5. Release the slider. The value is saved automatically to `CwDecoderSensitivity`.

## What each control does

| Control             | Default     | Range                |
|---------------------|-------------|----------------------|
| **Sens** slider     | 30          | 0–100                |
| CW decode text      | —           | —                    |
| CW stats label      | —           | `<hz> Hz  <wpm> WPM` |
| **Pitch** range slider | 500–700 Hz | 300–1200 Hz        |
| **WPM** range slider   | 15–40 WPM  | 5–60 WPM            |
| **A-** button        | —           | —                    |
| **A+** button        | —           | —                    |
| CW panel resize grip | —           | —                    |
| **Lo** (pitch min) slider | 500 Hz  | 300–1200 Hz        |
| **Hi** (pitch max) slider | 700 Hz  | 300–1200 Hz        |
| **🔒P** (Lock Pitch) | —          | —                    |
| **🔒S** (Lock Speed) | —          | —                    |
| **CPY ALL** button   | —           | —                    |
| **CPY VIS** button   | —           | —                    |
| **CLR** button       | —           | —                    |
| **✕** (close CW) button | —        | —                    |

## CW decode text colouring

The decoded text uses colour to indicate confidence:

| Colour  | Cost threshold | Meaning                |
|---------|----------------|------------------------|
| Green   | < 0.15         | High confidence        |
| Yellow  | < 0.35         | Moderate confidence    |
| Orange  | < 0.60         | Low confidence         |
| Red     | >= 0.60        | Very low confidence    |

TX-side decoded text (your own sending) appears in cyan (`#5fc8ff`) so you can distinguish your sending from incoming CW. When switching from TX to RX, a separator space is inserted automatically to prevent the two coloured runs from merging.

## Locking the CW decoder pitch

Use **🔒P** (Lock Pitch) to fix the decoder's pitch search to the currently tuned frequency. This is useful once the decoder has locked onto a signal and you want to prevent it from wandering.

1. Click **🔒P** to enable pitch locking.
2. Click it again to disable locking and let the decoder search freely across the pitch range.

## Locking the CW decoder speed

Use **🔒S** (Lock Speed) to fix the decoder's speed search to the current WPM value. This prevents the decoder from switching between different character speeds while decoding a single transmission.

1. Click **🔒S** to enable speed locking.
2. Click it again to disable locking and let the decoder adapt to speed changes.

## Adjusting the CW decode text font size

The **A+** and **A-** buttons at the top of the CW decode panel let you increase or decrease the decoded text font size.

1. Click **A+** to enlarge the text; click **A-** to shrink it.
2. The font size is persisted between sessions. Valid range is 8–32 px.
3. Use larger text for better readability at a distance; use smaller text to see more history in the panel.

## Resizing the CW decode panel

Drag the thin horizontal grip at the top of the CW decode panel (just below the title bar) up or down to change the panel height. This reveals more or less decoded-text history.

1. Move your cursor over the 4-pixel-high resize bar until it becomes a vertical resize cursor.
2. Click and drag up to shrink the panel, or down to enlarge it. Valid range is 60–600 px.
3. The panel height is persisted between sessions.

## Copying decoded CW text

- Click **CPY ALL** to copy the entire decoded text buffer to the clipboard.
- Click **CPY VIS** to copy only the text currently visible in the scroll area.
- Right-clicking the CW decode text area also gives access to the standard text actions (Select All, Copy, and so on) alongside the **Clear** option.

## Clearing the CW decode buffer

Click **CLR** to erase all decoded text from the buffer. This is useful before a new transmission when you want a clean readout.

## Hiding the CW decode panel

Click the **✕** button at the top of the CW decode panel to hide it. The panel reappears when you switch the CW decoder on again.

## Tips

- Start at the default of 30 and raise the slider gradually until red and orange characters disappear from the decode text.
- Character colour is a quick confidence gauge: if most output is green, the current sensitivity is well matched to signal conditions. If the display goes blank entirely, the slider is set too high — move it left until characters return.
- The **Pitch** range slider (default 500–700 Hz, range 300–1200 Hz) constrains which pitches the decoder searches. Narrowing that range to match the received signal's sidetone pitch can reduce false triggers independently of **Sens**.
- The **WPM** range slider (default 15–40 WPM, range 5–60 WPM) constrains which speeds the decoder searches. Narrowing that range to match the received signal's sending speed improves decoding accuracy.
- Right-clicking the CW decode text area also gives access to the standard text actions (Select All, Copy, and so on) alongside the **Clear** option.
- Use **A+** and **A-** to find a comfortable reading size. The change takes effect immediately and is saved for next time.
- Lock both **🔒P** and **🔒S** once the decoder has locked onto a steady signal to produce the most consistent text.

## Troubleshooting

- **Decoded text disappears completely after raising Sens** — the threshold is above the confidence level of the incoming signal. Lower the slider until output returns, then raise it more slowly.
- **Output remains noisy even at Sens 100** — the signal may be outside the pitch search window. Check the CW stats label for the reported pitch and adjust the **Pitch** range slider to bracket it.
- **Sens resets to 30 after restart** — if `CwDecoderSensitivity` is missing from saved settings, AetherSDR uses the default of 30. Move the slider once to write the value; it is then saved on every change.
- **Font size resets after restart** — the font size is saved automatically. If it resets, ensure you have write permissions to the settings file.

## Related

- [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md)
- [Lock CW decoder pitch or speed once tracking is good](lock-cw-decoder-pitch-or-speed-once-tracking-is-good.md)
- [Copy decoded CW text to the clipboard](copy-decoded-cw-text-to-the-clipboard.md)