# Lock CW decoder pitch or speed once tracking is good

Once the CW decoder has latched onto a signal, use the lock controls to prevent the decoder from drifting to a different pitch or speed when band conditions change or other signals appear nearby.

## Before you start

- The CW decode panel must be visible. If it is not, see [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md).
- The decoder must be producing output. Watch the CW stats label until it shows a stable pitch and WPM reading before locking.

## Steps

1. Tune to the CW signal and watch the CW stats label until it settles on a consistent reading, for example `598 Hz  22 WPM`.
2. To hold the pitch at that frequency, click 🔒P (Lock Pitch). The button highlights when active.
3. To hold the speed at that WPM, click 🔒S (Lock Speed). The button highlights when active.
4. To release a lock, click the active button again. It returns to its unhighlighted state and the decoder resumes tracking freely.

## What each control does

| Control | What it does | Default | Notes |
|---|---|---|---|
| CW stats label | Displays the currently detected pitch and speed in the format `<hz> Hz  <wpm> WPM`. | — | Read-only indicator. |
| 🔒P (Lock Pitch) | Locks the decoder pitch to the frequency shown in the CW stats label at the moment you click. | Unlocked | Toggle button; highlighted when active. |
| 🔒S (Lock Speed) | Locks the decoder speed to the WPM shown in the CW stats label at the moment you click. | Unlocked | Toggle button; highlighted when active. |
| Lo (pitch min) | Sets the lower bound of the pitch range the decoder searches. | 500 Hz | Valid range: 300–1200 Hz. Clamped ≤ Hi. |
| Hi (pitch max) | Sets the upper bound of the pitch range the decoder searches. | 700 Hz | Valid range: 300–1200 Hz. Clamped ≥ Lo. |
| Sens | Filters low-confidence decodes. Higher values are stricter. | 30 | Range: 0–100. Persisted as `CwDecoderSensitivity`. |

## Tips

- Lock pitch and speed independently. You can lock only one if the other is still settling.
- Narrow the Lo and Hi pitch range sliders around the signal frequency before locking pitch. A tighter search window reduces the chance the decoder latches onto the wrong signal in the first place.
- If the decoded text becomes garbled after locking, the signal pitch or speed may have drifted. Click the active lock button to release it, wait for the stats label to re-stabilise, then lock again.

## Troubleshooting

- **CW stats label is blank or not updating** — The decoder has not acquired a signal. Check that PC audio is routed correctly (the hint label reads `(requires PC Audio)`), that the signal falls within the Lo–Hi pitch range, and that Sens is not set so high that all decodes are rejected.
- **Locked pitch produces no output after tuning away and back** — Locking pitch holds the decoder to the frequency at the time of locking. If you retuned the VFO, the signal pitch seen by the decoder may have shifted. Release 🔒P, retune, and re-lock once the stats label stabilises.

## Related

- [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md)
- [Tune CW decoder sensitivity to reject noise](tune-cw-decoder-sensitivity-to-reject-noise.md)
- [Copy decoded CW text to the clipboard](copy-decoded-cw-text-to-the-clipboard.md)
