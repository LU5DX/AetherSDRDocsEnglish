# Turn on the CW decoder to read Morse off-air

The CW decode panel appears beneath the panadapter and displays incoming Morse code as readable text in real time. Use it to copy off-air CW without a separate decoding program.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- PC audio must be routed to AetherSDR. The panel itself shows the reminder "(requires PC Audio)" — decoding will not work without it.
- Tune to a CW signal and set the mode to CW on the active slice.

## Steps

1. In the panadapter title bar, confirm the correct slice is shown in the "Slice" title label (for example, "Slice A").
2. Open the CW decode panel. The panel appears below the spectrum/waterfall area and is hidden by default — look for a CW control or mode button that exposes it for the active slice. Once visible, the panel shows the label **CW** in blue alongside the hint **(requires PC Audio)**.
3. Watch the **CW decode text** area at the bottom of the panel. As the decoder tracks the signal, decoded characters roll in and are coloured by confidence: green (high), yellow, orange, or red (low).
4. Check the **CW stats label** above the text area. It shows the detected pitch and speed in the format `<Hz>  <WPM>`, for example `600 Hz  20 WPM`. Confirm these match the signal you are listening to before relying on the decode.

## What each control does

| Control | What it does | Default | Range / unit | Persisted key |
|---|---|---|---|---|
| **Sens** slider | Filters low-confidence characters. Higher values reject more uncertain decodes. | 30 | 0–100 | `CwDecoderSensitivity` |
| **🔒P (Lock Pitch)** toggle | Locks the decoder to the current detected pitch so it stops searching. | Off | On / Off | — |
| **🔒S (Lock Speed)** toggle | Locks the decoder to the current detected speed (WPM). | Off | On / Off | — |
| **Lo** slider | Minimum pitch the decoder searches. Clamped to be ≤ **Hi**. | 500 Hz | 300–1200 Hz | — |
| **Hi** slider | Maximum pitch the decoder searches. Clamped to be ≥ **Lo**. | 700 Hz | 300–1200 Hz | — |
| **CPY ALL** | Copies the entire decoded text buffer to the clipboard. | — | — | — |
| **CPY VIS** | Copies only the text currently visible in the scroll area to the clipboard. | — | — | — |
| **CLR** | Clears the CW decode buffer. | — | — | — |
| **× (close CW)** | Hides the CW decode panel. | — | — | — |
| **CW stats label** | Indicator showing detected pitch and speed. Read-only. | — | `<Hz>  <WPM>` | — |
| **CW decode text** | Rolling read-only display of decoded characters, coloured by confidence. | — | — | — |

## Tips

- If the text area fills with low-confidence (orange or red) characters, increase **Sens** to filter them out. Start around 50 and raise until noise characters disappear.
- Narrow the pitch search range with **Lo** and **Hi** to match the sidetone of the station you are copying. This reduces false triggers from nearby signals.
- Once the **CW stats label** settles on a stable pitch and speed, enable **🔒P (Lock Pitch)** and **🔒S (Lock Speed)** to prevent the decoder from drifting to another signal.
- Use **CLR** before a new QSO to keep the text area readable.

## Troubleshooting

- **No text appears in the decode area** — Verify PC audio is routed to AetherSDR. The panel shows "(requires PC Audio)" as a reminder. Without it the decoder receives no audio and produces no output.
- **Decode text is mostly red or orange** — The signal confidence is low. Increase **Sens**, or narrow the **Lo**/**Hi** pitch range to match the actual sidetone frequency shown in the **CW stats label**.
- **Wrong pitch or speed shown in CW stats label** — Do not engage **🔒P (Lock Pitch)** or **🔒S (Lock Speed)** until the stats label has stabilised on the target signal.

## Related

- [Tune CW decoder sensitivity to reject noise](tune-cw-decoder-sensitivity-to-reject-noise.md)
- [Lock CW decoder pitch or speed once tracking is good](lock-cw-decoder-pitch-or-speed-once-tracking-is-good.md)
- [Copy decoded CW text to the clipboard](copy-decoded-cw-text-to-the-clipboard.md)
- [Panadapter overview](overview.md)
