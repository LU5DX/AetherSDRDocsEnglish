# Tune CW decoder sensitivity to reject noise

The Sens slider controls how strictly the CW decoder filters low-confidence decodes. Raising it reduces noise and garbled output at the cost of occasionally dropping weak but valid characters.

## Before you start

- The CW decode panel must be open and visible beneath the panadapter. If it is not visible, see [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md).
- PC audio must be routed to AetherSDR. The panel shows "(requires PC Audio)" as a reminder.

## Steps

1. Locate the CW decode panel at the bottom of the panadapter.
2. Find the label "Sens:" and the short horizontal slider immediately to its right.
3. Drag the slider right to increase sensitivity (stricter filtering, fewer noise decodes) or left to decrease it (more permissive, shows lower-confidence characters).
4. Watch the decoded text in the CW decode text area to confirm the noise level changes as expected.

The new value is saved immediately to `CwDecoderSensitivity` and persists across restarts.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Sens | 30 | 0–100 | `CwDecoderSensitivity` | Maps to an internal cost threshold: 0 = threshold 1.0 (show everything); 100 = threshold 0.1 (high confidence only). Higher values reject more noise. |

## Tips

- Decoded characters are coloured by confidence. Green indicates cost below 0.15; yellow below 0.35; orange below 0.60; red at 0.60 and above. If you see mostly red or orange, raise Sens until the output turns predominantly green or yellow.
- On a clean signal with a strong CW note, a Sens value of 30–50 is usually sufficient. In a noisy band or with a weak signal, experiment at lower values first to avoid losing characters before raising Sens to suppress noise.
- If the decoder still tracks poorly after adjusting Sens, consider narrowing the pitch search window with Lo and Hi, or locking the pitch once the decoder has found the tone. See [Lock CW decoder pitch or speed once tracking is good](lock-cw-decoder-pitch-or-speed-once-tracking-is-good.md).

## Troubleshooting

- **Raising Sens removes all output, including what appears to be a good signal** — The decoder's internal cost for that signal exceeds the threshold. Lower Sens slightly until valid characters reappear, then increase it again in small steps.
- **Output is unchanged after moving the slider** — Confirm the CW decode panel is active and PC audio is being received. The "(requires PC Audio)" hint in the panel header indicates audio is not yet reaching the decoder.

## Related

- [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md)
- [Lock CW decoder pitch or speed once tracking is good](lock-cw-decoder-pitch-or-speed-once-tracking-is-good.md)
- [Copy decoded CW text to the clipboard](copy-decoded-cw-text-to-the-clipboard.md)
