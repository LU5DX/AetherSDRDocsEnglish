# Turn on the CW decoder to read Morse off-air

The CW decode panel displays decoded Morse text directly beneath a panadapter. Use it to read CW off-air without a separate application.

## Before you start

- AetherSDR must be connected to the radio. The CW decoder requires an active radio connection.
- PC Audio must be routed to AetherSDR. The panel shows "(requires PC Audio)" as a reminder — decoding will not work without an audio feed.
- The active slice must be in CW mode so the radio is passing the appropriate audio.

## Steps

1. Locate the panadapter for the slice you want to decode.
2. Right-click the spectrum or waterfall area of that panadapter to open the context menu, then select **CW Decoder**. The CW decode panel appears as a strip beneath the waterfall.
3. Confirm the panel is visible. It shows the label **CW** and the hint **(requires PC Audio)** on the left, followed by the **Sens** slider, 🔒P, 🔒S, **Lo**, **Hi**, **CPY ALL**, **CPY VIS**, **CLR**, and ✕ controls.
4. Tune to a CW signal. Decoded text appears in the rolling display at the bottom of the panel, coloured by confidence.
5. If no text appears, adjust the **Lo** and **Hi** sliders to bracket the pitch of the signal. Default search range is 500 Hz (**Lo**) to 700 Hz (**Hi**).
6. Watch the CW stats label — it shows the detected pitch and speed in the form `<hz> Hz  <wpm> WPM` once the decoder locks on.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| **Sens** | 30 | 0–100 | `CwDecoderSensitivity` | Filters low-confidence decodes. Higher values reject more uncertain characters. Maps 0–100 to a cost threshold of 1.0–0.1. |
| **🔒P (Lock Pitch)** | Off | On / Off | — | Locks the decoder to the current detected pitch so it stops scanning. |
| **🔒S (Lock Speed)** | Off | On / Off | — | Locks the decoder to the current detected WPM. |
| **Lo** | 500 Hz | 300–1200 Hz | — | Lower bound of the pitch range the decoder searches. Clamped ≤ **Hi**. |
| **Hi** | 700 Hz | 300–1200 Hz | — | Upper bound of the pitch range the decoder searches. Clamped ≥ **Lo**. |
| **CPY ALL** | — | — | — | Copies the entire decoded text buffer to the clipboard. |
| **CPY VIS** | — | — | — | Copies only the text currently visible in the scroll area to the clipboard. |
| **CLR** | — | — | — | Clears the decoded text buffer. |
| **✕** | — | — | — | Hides the CW decode panel. |
| CW stats label | — | `<hz> Hz  <wpm> WPM` | — | Shows the pitch and speed the decoder has detected. |
| CW decode text | — | — | — | Read-only rolling display. Text is coloured green (highest confidence) through yellow, orange, and red (lowest confidence). |

## Tips

- Start with the default **Lo** / **Hi** range of 500–700 Hz. Most CW operators use a sidetone in this range. Widen the window only if you know the signal is outside it.
- Once the stats label shows a stable pitch and speed, press **🔒P** and **🔒S** to prevent the decoder from drifting to noise.
- Raise **Sens** if garbage characters appear in the text. Lowering it admits more uncertain output, which can help on weak signals at the cost of more errors.
- Use **CLR** before a new QSO to keep the text display uncluttered, then **CPY ALL** afterward to save the exchange to the clipboard.

## Troubleshooting

- **No text appears despite a strong CW signal** — The decoder requires PC Audio routing. Verify that audio from the radio is reaching AetherSDR. The "(requires PC Audio)" hint in the panel confirms this dependency.
- **Decoded text is mostly garbage** — Raise the **Sens** slider toward 100 to reject low-confidence characters, and narrow the **Lo**/**Hi** range to surround only the signal's actual pitch shown in the stats label.
- **Stats label shows no pitch or speed** — The signal pitch is likely outside the **Lo**–**Hi** search window. Widen the window or set **Lo** and **Hi** to bracket the audible tone frequency.
- **CW panel has disappeared** — It was closed with ✕. Reopen it via the panadapter context menu.

## Related

- [Tune CW decoder sensitivity to reject noise](tune-cw-decoder-sensitivity-to-reject-noise.md)
- [Lock CW decoder pitch or speed once tracking is good](lock-cw-decoder-pitch-or-speed-once-tracking-is-good.md)
- [Copy decoded CW text to the clipboard](copy-decoded-cw-text-to-the-clipboard.md)
- [Panadapter overview](overview.md)
