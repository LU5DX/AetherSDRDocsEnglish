# Lock CW decoder pitch or speed once tracking is good

Once the CW decoder has acquired a signal, locking its pitch or speed stops it from drifting to another signal or re-estimating speed between overs.

## Before you start

- The CW decode panel must be open. See [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md).
- The CW stats label should be showing a stable reading, for example `600 Hz  20 WPM`, before you lock.

## Steps

1. Watch the CW stats label until the pitch (Hz) and speed (WPM) values settle on the signal you want.
2. To lock the pitch, click 🔒P. The button highlights when active.
3. To lock the speed, click 🔒S. The button highlights when active.
4. To unlock, click the active button again.

## What each control does

| Control | What it does | Default | Valid range | Setting key |
|---|---|---|---|---|
| CW stats label | Displays the currently detected pitch and speed as `<hz> Hz  <wpm> WPM`. | — | — | — |
| 🔒P (Lock Pitch) | Locks the decoder pitch to the current tuned frequency. Toggle off to resume tracking. | Off | On / Off | — |
| 🔒S (Lock Speed) | Locks the decoder speed to the current WPM. Toggle off to resume tracking. | Off | On / Off | — |
| Lo (pitch min) | Minimum pitch the decoder searches. Clamped ≤ Hi. | 500 Hz | 300–1200 Hz | — |
| Hi (pitch max) | Maximum pitch the decoder searches. Clamped ≥ Lo. | 700 Hz | 300–1200 Hz | — |
| Sens | Filters low-confidence decodes. Higher values are stricter. Maps 0–100 to a cost threshold of 1.0–0.1. | 30 | 0–100 | `CwDecoderSensitivity` |

## Tips

- If the decoder is jumping between signals, narrow the Lo/Hi pitch range around the signal before locking pitch. This constrains the search window before the lock takes effect.
- Lock speed when copying a single operator at a known WPM; unlock it when moving to a new QSO where the sending speed may differ.
- Locking both pitch and speed together gives the most stable decode in a crowded band segment.

## Troubleshooting

- **CW stats label shows no reading before locking** — The decoder has not acquired the signal yet. Check that PC audio is routed correctly (the CW panel displays a `(requires PC Audio)` reminder if audio is missing). Adjust Lo and Hi to bracket the signal's pitch, and lower Sens toward 0 to allow lower-confidence decodes through until the signal is acquired.
- **Decoded text quality drops after locking pitch** — The signal may have drifted. Unlock 🔒P, let the decoder re-acquire, then re-lock.

## Related

- [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md)
- [Tune CW decoder sensitivity to reject noise](tune-cw-decoder-sensitivity-to-reject-noise.md)
- [Copy decoded CW text to the clipboard](copy-decoded-cw-text-to-the-clipboard.md)
