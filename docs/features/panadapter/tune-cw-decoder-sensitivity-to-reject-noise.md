# Tune CW decoder sensitivity to reject noise

The Sens slider controls how strictly the CW decoder filters out low-confidence decodes. Raising it reduces noise and garbage characters in the decode display; lowering it lets more uncertain characters through.

## Before you start

- The CW decode panel must be visible. If it is not, enable it first — see [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md).
- PC audio must be routed to AetherSDR. The panel displays "(requires PC Audio)" as a reminder when audio is absent.

## Steps

1. Locate the CW decode panel at the bottom of the panadapter.
2. Find the "Sens:" label and the short horizontal slider immediately to its right.
3. Drag the Sens slider to the right to increase sensitivity (stricter filtering, fewer noise characters). Drag left to decrease sensitivity (more permissive, more characters shown).
4. Watch the CW decode text area. Adjust until decoded text is readable without excess noise characters.

The setting is saved automatically. No confirmation step is needed.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Sens | 30 | 0–100 | `CwDecoderSensitivity` | Maps 0–100 to an internal cost threshold of 1.0–0.1. Higher values apply a stricter threshold, rejecting lower-confidence decodes. |

## Tips

- Decoded characters are coloured by confidence: green (highest confidence), yellow, orange, and red (lowest confidence). At lower Sens values, you will see more orange and red characters; raising Sens suppresses them.
- If a strong, clean signal is still producing noise characters, try also narrowing the pitch search range using the Lo and Hi sliders so the decoder is not tracking interference outside the signal's pitch.
- Once you find a Sens value that works for your noise floor, it persists across sessions via `CwDecoderSensitivity`.

## Troubleshooting

- **Raising Sens to maximum still shows noise characters** — The decoder may be tracking the wrong signal. Check that the Lo and Hi pitch sliders bracket only the CW signal's pitch, then consider using 🔒P (Lock Pitch) to hold the decoder on the correct frequency. See [Lock CW decoder pitch or speed once tracking is good](lock-cw-decoder-pitch-or-speed-once-tracking-is-good.md).
- **Sens is at 0 but almost nothing is decoded** — The cost threshold at 0 is 1.0, which accepts all decodes. If output is still sparse, the issue is likely audio routing rather than sensitivity. Verify PC audio is reaching AetherSDR.

## Related

- [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md)
- [Lock CW decoder pitch or speed once tracking is good](lock-cw-decoder-pitch-or-speed-once-tracking-is-good.md)
- [Copy decoded CW text to the clipboard](copy-decoded-cw-text-to-the-clipboard.md)
