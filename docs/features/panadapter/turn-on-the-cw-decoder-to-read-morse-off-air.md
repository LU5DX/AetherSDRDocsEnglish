# Turn on the CW decoder to read Morse off-air

The CW decode panel sits beneath the panadapter's spectrum and waterfall and displays decoded Morse text in real time. Use it to read CW stations without a separate decoding application.

## Before you start

- AetherSDR must be connected to the radio. The CW decoder requires an active radio connection.
- PC audio must be routed to AetherSDR. The panel shows "(requires PC Audio)" as a reminder — decoding will not work without it.
- Tune to a CW signal and set the slice mode to CW.

## Steps

1. Locate the panadapter containing the slice you want to decode.
2. Right-click the panadapter's spectrum or waterfall area to open the context menu, then select **Show CW Decoder**. The CW decode panel appears below the waterfall.
3. Confirm the panel is visible: it shows the label **CW**, the hint **(requires PC Audio)**, a **Sens** slider, and a scrolling text area.
4. Adjust the **Lo** slider to set the minimum pitch the decoder searches (default 500 Hz, range 300–1200 Hz).
5. Adjust the **Hi** slider to set the maximum pitch (default 700 Hz, range 300–1200 Hz). **Lo** is clamped ≤ **Hi** automatically.
6. Watch the **CW decode text** area. Decoded characters appear coloured by confidence: green (highest), yellow, orange, or red (lowest).
7. The **CW stats label** above the text area shows the detected pitch and speed in the format `<hz> Hz  <wpm> WPM` once the decoder is tracking a signal.
8. To close the panel when finished, click **✕** (close CW) at the right of the control bar.

## What each control does

| Control | What it does | Default | Range / values | Setting key |
|---|---|---|---|---|
| **Sens** slider | Filters low-confidence decodes. Higher values reject more noise. | 30 | 0–100 | `CwDecoderSensitivity` |
| **🔒P (Lock Pitch)** | Locks the decoder pitch to the current tuned frequency. | Off | On / Off | — |
| **🔒S (Lock Speed)** | Locks the decoder speed to the current WPM. | Off | On / Off | — |
| **Lo** slider | Minimum pitch the decoder searches (Hz). Clamped ≤ Hi. | 500 Hz | 300–1200 Hz | — |
| **Hi** slider | Maximum pitch the decoder searches (Hz). Clamped ≥ Lo. | 700 Hz | 300–1200 Hz | — |
| **CW stats label** | Displays detected pitch and speed. | — | `<hz> Hz  <wpm> WPM` | — |
| **CW decode text** | Read-only rolling display of decoded characters, coloured by confidence. | — | — | — |
| **CPY ALL** | Copies the full decoded text buffer to the clipboard. | — | — | — |
| **CPY VIS** | Copies only the text currently visible in the scroll area to the clipboard. | — | — | — |
| **CLR** | Clears the CW decode buffer. | — | — | — |
| **✕ (close CW)** | Hides the CW decode panel. | — | — | — |

## Tips

- Text confidence colours: green = cost < 0.15 (best), yellow = < 0.35, orange = < 0.60, red = ≥ 0.60. Raise **Sens** to suppress the orange and red characters when the band is noisy.
- If you know the station's pitch, narrow **Lo** and **Hi** around it and enable **🔒P (Lock Pitch)** to stop the decoder wandering to interference.
- Once the decoder is tracking speed reliably, click **🔒S (Lock Speed)** to stabilise it against QSB.
- The `CwDecoderSensitivity` value (0–100) is saved automatically each time you move the **Sens** slider and persists across sessions.

## Troubleshooting

- **No text appears despite a strong CW signal** — Check that PC audio is routed to AetherSDR. The "(requires PC Audio)" hint in the panel indicates audio is required for decoding.
- **Only red or orange text appears** — The signal confidence is low. Lower the **Sens** slider toward 0 to show more output, or check that **Lo** and **Hi** bracket the actual CW pitch shown in the **CW stats label**.
- **Stats label stays blank** — The decoder has not locked onto a signal. Widen the **Lo**/**Hi** range and ensure the slice is tuned to a CW signal with sufficient audio level.

## Related

- [Tune CW decoder sensitivity to reject noise](tune-cw-decoder-sensitivity-to-reject-noise.md)
- [Lock CW decoder pitch or speed once tracking is good](lock-cw-decoder-pitch-or-speed-once-tracking-is-good.md)
- [Copy decoded CW text to the clipboard](copy-decoded-cw-text-to-the-clipboard.md)
- [Panadapter overview](overview.md)
