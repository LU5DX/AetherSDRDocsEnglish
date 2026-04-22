# Lock CW decoder pitch or speed once tracking is good

Once the CW decoder has locked onto a signal and is producing clean copy, you can freeze the pitch, the speed, or both so the decoder stops searching and stays on target.

## Before you start

- The CW decode panel must be open and active. See [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md).
- The CW stats label should be showing a stable reading — for example, `600 Hz  20 WPM` — before you lock.
- PC audio must be routed to AetherSDR; without it the decoder produces no output to lock onto.

## Steps

1. Tune to the CW signal and watch the CW stats label until the Hz and WPM readings settle.
2. To freeze the pitch, click 🔒P in the CW decode panel. The button highlights when active.
3. To freeze the speed, click 🔒S. The button highlights when active.
4. To unlock, click the same button again. The highlight clears and the decoder resumes tracking.

## What each control does

| Control | What it does | Default | Range | Setting key |
|---|---|---|---|---|
| CW stats label | Displays the currently detected pitch and speed as `<hz> Hz  <wpm> WPM`. | — | — | — |
| 🔒P (Lock Pitch) | Locks the decoder pitch to the frequency shown in the CW stats label. Toggle to unlock. | Off | On / Off | — |
| 🔒S (Lock Speed) | Locks the decoder speed to the WPM shown in the CW stats label. Toggle to unlock. | Off | On / Off | — |
| Lo (pitch min) | Sets the minimum pitch the decoder searches before a lock is established. Clamped ≤ Hi. | 500 Hz | 300–1200 Hz | — |
| Hi (pitch max) | Sets the maximum pitch the decoder searches before a lock is established. Clamped ≥ Lo. | 700 Hz | 300–1200 Hz | — |
| Sens | Filters low-confidence decodes. Higher values are stricter. | 30 | 0–100 | `CwDecoderSensitivity` |

## Tips

- Narrow Lo and Hi around the signal's actual pitch before locking. If the signal sits at 600 Hz, setting Lo to 550 and Hi to 650 gives the decoder less room to wander before you click 🔒P.
- You can lock pitch and speed independently. Locking speed alone is useful on a net where multiple stations send at the same rate but on slightly different offsets.
- If copy degrades after locking, the operator may have shifted pitch or changed speed. Unlock, let the decoder re-track, then lock again.

## Troubleshooting

- **CW stats label shows no reading** — The decoder has not detected a signal. Check that PC audio is routed correctly and that the signal falls within the Lo–Hi pitch range.
- **🔒P or 🔒S has no visible effect on the text** — The stats label was not stable when you locked. Unlock, wait for the reading to settle, then lock again.
- **Decoded text quality drops immediately after locking speed** — The WPM reading at the moment of locking was still converging. Unlock and wait for a steadier reading before locking again.

## Related

- [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md)
- [Tune CW decoder sensitivity to reject noise](tune-cw-decoder-sensitivity-to-reject-noise.md)
- [Copy decoded CW text to the clipboard](copy-decoded-cw-text-to-the-clipboard.md)
