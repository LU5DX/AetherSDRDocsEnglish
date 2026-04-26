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

| Control | Default | Range | Persisted key | Behavior |
|---|---|---|---|---|
| **Sens** slider | 30 | 0–100 | `CwDecoderSensitivity` | Maps 0–100 to an internal cost threshold of 1.0–0.1. Higher values mean stricter filtering: only high-confidence characters are shown. |
| CW decode text | — | — | — | Read-only rolling display coloured by confidence: green (highest), yellow, orange, red (lowest). |
| CW stats label | — | `<hz> Hz  <wpm> WPM` | — | Shows the pitch and speed the decoder is currently tracking. |

## Tips

- Start at the default of 30 and raise the slider gradually until red and orange characters disappear from the decode text.
- Character colour is a quick confidence gauge: if most output is green, the current sensitivity is well matched to signal conditions. If the display goes blank entirely, the slider is set too high — move it left until characters return.
- The **Lo** and **Hi** pitch sliders (default 500 Hz and 700 Hz, range 300–1200 Hz) constrain which pitches the decoder searches. Narrowing that range to match the received signal's sidetone pitch can reduce false triggers independently of **Sens**.

## Troubleshooting

- **Decoded text disappears completely after raising Sens** — the threshold is above the confidence level of the incoming signal. Lower the slider until output returns, then raise it more slowly.
- **Output remains noisy even at Sens 100** — the signal may be outside the pitch search window. Check the CW stats label for the reported pitch and adjust **Lo** and **Hi** to bracket it.
- **Sens resets to 30 after restart** — if `CwDecoderSensitivity` is missing from saved settings, AetherSDR uses the default of 30. Move the slider once to write the value; it is then saved on every change.

## Related

- [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md)
- [Lock CW decoder pitch or speed once tracking is good](lock-cw-decoder-pitch-or-speed-once-tracking-is-good.md)
- [Copy decoded CW text to the clipboard](copy-decoded-cw-text-to-the-clipboard.md)
