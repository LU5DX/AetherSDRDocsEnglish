# Tune CW decoder sensitivity to reject noise

The Sens slider sets how strictly the CW decoder filters out low-confidence characters. Raising it reduces garbage characters caused by noise; lowering it recovers weak signals at the cost of more errors.

## Before you start

- The CW decode panel must be open in the Panadapter applet. If it is not visible, see [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md).
- PC audio must be routed to AetherSDR. The CW decode panel shows "(requires PC Audio)" as a reminder.

## Steps

1. Locate the CW decode panel at the bottom of the Panadapter applet.
2. Find the **Sens:** label and its slider immediately to the right.
3. Drag the **Sens** slider right to increase sensitivity (stricter filtering, fewer noise characters) or left to decrease it (more permissive, more characters pass through).
4. Watch the **CW decode text** area. Reduce the value if genuine characters are being dropped; raise it if noise characters are cluttering the output.

The new value is saved automatically to `CwDecoderSensitivity` and restored the next time AetherSDR starts.

## What each control does

| Control | Default | Range | Persisted key | Behavior |
|---|---|---|---|---|
| Sens | 30 | 0–100 | `CwDecoderSensitivity` | Filters low-confidence decodes. Higher values apply a stricter cost threshold, rejecting more characters. Maps 0–100 to an internal cost threshold of 1.0–0.1. |

## Tips

- The **CW decode text** area colours each decoded character by confidence: green (highest confidence), yellow, orange, and red (lowest). If you see mostly red or orange characters during a quiet period, raise Sens to suppress them.
- After finding a value that works for the current band conditions, consider locking pitch and speed to prevent the decoder from re-tracking on noise. See [Lock CW decoder pitch or speed once tracking is good](lock-cw-decoder-pitch-or-speed-once-tracking-is-good.md).
- The **Lo** and **Hi** sliders narrow the pitch search range (default 500–700 Hz), which also helps reject off-frequency noise independently of Sens.

## Troubleshooting

- **Raising Sens drops all decoded output** — The signal may be too weak or the pitch may be outside the Lo–Hi range. Lower Sens gradually and verify the **CW stats label** is showing a detected pitch and WPM figure. If the stats label is blank, the decoder is not locking onto any signal.
- **Sens is back at 30 after restarting** — The setting did not save. Check that AetherSDR has write permission to its configuration directory.

## Related

- [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md)
- [Lock CW decoder pitch or speed once tracking is good](lock-cw-decoder-pitch-or-speed-once-tracking-is-good.md)
- [Copy decoded CW text to the clipboard](copy-decoded-cw-text-to-the-clipboard.md)
