# Tune CW decoder sensitivity to reject noise

The Sens slider controls how strictly the CW decoder filters out low-confidence decodes. Raising it reduces garbage characters caused by noise; lowering it lets through weaker or faster signals that the decoder is less certain about.

## Before you start

- The CW decode panel must be open. If it is not visible beneath the panadapter, see [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md).
- PC audio must be routed to AetherSDR. The panel displays "(requires PC Audio)" as a reminder if audio is not reaching the decoder.

## Steps

1. Locate the CW decode panel at the bottom of the panadapter.
2. Find the **Sens** slider in the panel's control bar.
3. Drag the slider right to increase sensitivity (stricter filtering, fewer low-confidence characters output) or left to decrease it (more permissive, more characters output including uncertain ones).
4. Watch the decoded text in the **CW decode text** area. Characters are coloured by confidence: green is highest confidence, then yellow, orange, and red. Raise Sens until red and orange characters drop to an acceptable level.

The setting is saved automatically. The next time AetherSDR starts, the slider restores to this value.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Sens | 30 | 0–100 | `CwDecoderSensitivity` | Filters low-confidence decodes. Higher values apply a stricter cost threshold, rejecting more uncertain characters. Maps 0–100 to an internal cost threshold of 1.0–0.1. |

## Tips

- A Sens value of 30 (the default) is a reasonable starting point on a quiet band. On a noisy band or with a weak signal, try values in the 50–70 range and watch whether the colour of decoded text shifts toward green.
- If a strong, clean signal is producing few decoded characters, lower Sens toward 10–20 to loosen the threshold.
- The **Lo** and **Hi** pitch sliders (300–1200 Hz, defaults 500 Hz and 700 Hz) narrow the frequency range the decoder searches. Constraining this range can help on its own before you need to raise Sens. See [Lock CW decoder pitch or speed once tracking is good](lock-cw-decoder-pitch-or-speed-once-tracking-is-good.md) to hold the decoder on a known pitch once it is tracking correctly.
- Use **CLR** to clear the decode buffer after adjusting Sens so you are reading only fresh output at the new setting.

## Troubleshooting

- **Decoder still outputs many garbage characters at high Sens** — Confirm PC audio is being received (the CW stats label should show a pitch in Hz and a speed in WPM). If the stats label is blank, the decoder is receiving no audio and sensitivity has no effect.
- **No characters appear at all** — Sens may be set too high (near 100), or the signal pitch may fall outside the Lo–Hi range. Lower Sens toward 20–30 and widen the Lo and Hi pitch range to cover the signal.

## Related

- [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md)
- [Lock CW decoder pitch or speed once tracking is good](lock-cw-decoder-pitch-or-speed-once-tracking-is-good.md)
- [Copy decoded CW text to the clipboard](copy-decoded-cw-text-to-the-clipboard.md)
