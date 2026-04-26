# Turn on the CW decoder to read Morse off-air

The CW decoder panel lets you read incoming Morse code as text directly below the panadapter. Use it when you want a visual decode of a CW signal without external software.

## Before you start

- Connect to a FLEX-8600 radio. The panadapter requires an active radio connection.
- Route PC audio from the radio to AetherSDR. The CW panel displays a "(requires PC Audio)" reminder — the decoder works on the audio stream, not the raw RF data.
- Tune the active slice to a CW signal.

## Steps

1. Locate the panadapter for the slice you want to decode. The slice is identified in the title bar (for example, "Slice A").
2. Right-click the panadapter spectrum or waterfall to open the context menu, then select **Show CW Decoder**. The CW decode panel appears as a fixed strip below the waterfall.
3. Watch the **CW decode text** area at the bottom of the panel. Decoded characters roll in as they are received, coloured by confidence.
4. Check the **CW stats label** in the top bar of the panel. It shows the detected pitch and speed in the format `<hz> Hz  <wpm> WPM` once the decoder is tracking a signal.
5. If you see too many noise characters, drag the **Sens** slider to the right to raise the threshold. If valid characters are being suppressed, drag it to the left.
6. Adjust the **Lo** slider to set the minimum pitch the decoder searches (default 500 Hz, range 300–1200 Hz), and the **Hi** slider to set the maximum (default 700 Hz, range 300–1200 Hz). Set both to bracket the tone of the station you are copying.
7. To close the panel when you are done, click **✕** in the CW panel bar.

## What each control does

| Control | Default | Range | Persisted key | Behavior |
|---|---|---|---|---|
| **CW stats label** | — | `<hz> Hz  <wpm> WPM` | — | Shows detected pitch and speed. |
| **Sens** | 30 | 0–100 | `CwDecoderSensitivity` | Filters low-confidence decodes. Higher values are stricter. Maps 0–100 to an internal cost threshold of 1.0–0.1. |
| **🔒P (Lock Pitch)** | off | on / off | — | Locks the decoder pitch to the current tuned frequency. |
| **🔒S (Lock Speed)** | off | on / off | — | Locks the decoder speed to the current WPM. |
| **Lo** | 500 Hz | 300–1200 Hz | — | Minimum pitch the decoder searches. Clamped ≤ Hi. |
| **Hi** | 700 Hz | 300–1200 Hz | — | Maximum pitch the decoder searches. Clamped ≥ Lo. |
| **CPY ALL** | — | — | — | Copies the full decoded text to the clipboard. |
| **CPY VIS** | — | — | — | Copies only the text currently visible in the scroll area. |
| **CLR** | — | — | — | Clears the CW decode buffer. |
| **✕** | — | — | — | Hides the CW decode panel. |
| **CW decode text** | — | read-only | — | Rolling display of decoded CW. Text is coloured by confidence: green (best) through yellow and orange to red (lowest). |

## Tips

- Decoded text colour indicates confidence. Green characters are high confidence; yellow and orange are marginal; red characters are low confidence and are the first to disappear when you raise **Sens**.
- If the station's tone sits outside the 500–700 Hz default pitch window, the decoder will not track it. Widen **Lo** and **Hi** before concluding the decoder is not working.
- Once the **CW stats label** shows a stable Hz and WPM reading, use **🔒P** and **🔒S** to prevent the decoder from drifting if QRM appears on an adjacent frequency. See [Lock CW decoder pitch or speed once tracking is good](lock-cw-decoder-pitch-or-speed-once-tracking-is-good.md).
- Use **CLR** before copying to clipboard so that you capture only the current QSO rather than accumulated text from earlier.

## Troubleshooting

- **CW decode text area is blank despite a strong CW signal** — The decoder requires PC audio routing. Confirm audio from the radio is reaching AetherSDR. The "(requires PC Audio)" label in the panel is a reminder of this requirement.
- **Decodes are garbled or full of noise characters** — Drag the **Sens** slider to the right to raise the confidence threshold. Also check that **Lo** and **Hi** bracket the actual tone of the signal shown in the **CW stats label**.
- **No Hz or WPM value appears in the CW stats label** — The decoder is not detecting a signal. Verify the signal is within the **Lo**–**Hi** pitch window and that the slice mode is set to CW.

## Related

- [Tune CW decoder sensitivity to reject noise](tune-cw-decoder-sensitivity-to-reject-noise.md)
- [Lock CW decoder pitch or speed once tracking is good](lock-cw-decoder-pitch-or-speed-once-tracking-is-good.md)
- [Copy decoded CW text to the clipboard](copy-decoded-cw-text-to-the-clipboard.md)
- [Panadapter overview](overview.md)
