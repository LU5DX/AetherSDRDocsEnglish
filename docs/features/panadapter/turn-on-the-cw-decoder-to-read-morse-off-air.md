# Turn on the CW decoder to read Morse off-air

The CW decode panel appears beneath the panadapter and displays incoming Morse code as text in real time. Use it to copy off-air CW without manually listening or transcribing.

## Before you start

- AetherSDR must be connected to the radio. The CW decoder panel requires an active radio connection.
- PC audio must be routed to AetherSDR. The panel displays "(requires PC Audio)" as a reminder — decoding will not work without audio input.
- The slice bound to this panadapter should be set to CW mode on the radio.

## Steps

1. Locate the panadapter for the slice you want to decode.
2. Right-click the panadapter spectrum or waterfall to open the panadapter context menu, then select the option to show the CW decoder panel. The CW decode panel appears below the spectrum, showing "CW" in the header bar and "(requires PC Audio)".
3. Tune the radio to the CW signal. The CW stats label updates to show the detected pitch and speed in the format `<hz> Hz  <wpm> WPM`.
4. Watch the "CW decode text" area for decoded characters. Text is colour-coded by confidence: green is highest confidence, then yellow, then orange, then red.
5. Adjust the Sens slider if needed. The default is 30 (range 0–100). Move it right to reject low-confidence decodes; move it left to show more output. Your setting is saved as `CwDecoderSensitivity`.

## What each control does

| Control | What it does | Default | Range |
|---|---|---|---|
| CW stats label | Shows detected pitch and speed as `<hz> Hz  <wpm> WPM`. | — | — |
| Sens | Filters low-confidence decodes. Higher values are stricter. Saved as `CwDecoderSensitivity`. | 30 | 0–100 |
| 🔒P (Lock Pitch) | Locks the decoder pitch to the current tuned frequency. | Off | Toggle |
| 🔒S (Lock Speed) | Locks the decoder speed to the current detected WPM. | Off | Toggle |
| Lo (pitch min) | Minimum pitch the decoder searches, in Hz. Clamped to ≤ Hi. | 500 Hz | 300–1200 Hz |
| Hi (pitch max) | Maximum pitch the decoder searches, in Hz. Clamped to ≥ Lo. | 700 Hz | 300–1200 Hz |
| CW decode text | Read-only rolling display of decoded text, coloured by confidence. | — | — |
| CPY ALL | Copies the full decoded text to the clipboard. | — | — |
| CPY VIS | Copies only the text currently visible in the scroll area to the clipboard. | — | — |
| CLR | Clears the CW decode buffer. | — | — |
| ✕ (close CW) | Hides the CW decode panel. | — | — |

## Tips

- Decoded text colour indicates decode confidence: green means cost < 0.15 (highest confidence), yellow < 0.35, orange < 0.60, red ≥ 0.60.
- If the signal pitch drifts, leave 🔒P off so the decoder can track it. Once the pitch is stable, enable 🔒P to reduce false triggers from nearby signals.
- Narrow the Lo and Hi pitch range to bracket the signal you are copying. This reduces interference from other signals within the passband.
- Use CLR to clear accumulated text before a new over or contact begins.

## Troubleshooting

- **No text appears in the decode panel** — The CW decoder requires PC audio. Verify that audio is routed to AetherSDR. The "(requires PC Audio)" label in the panel header is a persistent reminder of this requirement.
- **Decoded text is mostly red or garbled** — Lower the Sens slider toward 0 to accept more output, then verify Lo and Hi pitch bounds bracket the actual signal tone. Check that the slice mode is CW on the radio.
- **Decoder tracks the wrong signal** — Enable 🔒P to lock the pitch to the target signal frequency. Narrow the Lo–Hi range to exclude other signal pitches.

## Related

- [Tune CW decoder sensitivity to reject noise](tune-cw-decoder-sensitivity-to-reject-noise.md)
- [Lock CW decoder pitch or speed once tracking is good](lock-cw-decoder-pitch-or-speed-once-tracking-is-good.md)
- [Copy decoded CW text to the clipboard](copy-decoded-cw-text-to-the-clipboard.md)
- [Panadapter overview](overview.md)
