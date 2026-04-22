# Lock CW decoder pitch or speed once tracking is good

Once the CW decoder has found a signal and is tracking well, you can lock its pitch, speed, or both to prevent the decoder from drifting to a different signal or responding to noise.

## Before you start

- The CW decode panel must be open. See [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md).
- The CW stats label should be showing a stable pitch and WPM reading before you lock. The label displays values in the format `<hz> Hz  <wpm> WPM`.

## Steps

1. Watch the CW stats label until the pitch (Hz) and speed (WPM) values are stable and tracking the signal you want.
2. To lock the pitch, click 🔒P. The button highlights when active, indicating the decoder will no longer search for a new pitch.
3. To lock the speed, click 🔒S. The button highlights when active, indicating the decoder will hold the current WPM estimate.
4. To unlock either parameter, click the same button again. The highlight clears and the decoder resumes tracking.

## What each control does

| Control | What it does | Default | Valid range | Setting key |
|---|---|---|---|---|
| 🔒P (Lock Pitch) | Locks the CW decoder pitch to the current tuned frequency. Toggle off to resume tracking. | Off (unlocked) | On / Off | — |
| 🔒S (Lock Speed) | Locks the CW decoder speed to the current WPM. Toggle off to resume tracking. | Off (unlocked) | On / Off | — |
| CW stats label | Read-only display of detected pitch and speed: `<hz> Hz  <wpm> WPM`. | — | — | — |
| Lo (pitch min) | Minimum pitch the decoder searches. Clamped ≤ Hi. | 500 Hz | 300–1200 Hz | — |
| Hi (pitch max) | Maximum pitch the decoder searches. Clamped ≥ Lo. | 700 Hz | 300–1200 Hz | — |
| Sens | Filters low-confidence decodes. Higher values are stricter. Maps 0–100 to a cost threshold of 1.0–0.1. | 30 | 0–100 | `CwDecoderSensitivity` |

## Tips

- Narrow the Lo and Hi pitch range sliders around the signal's pitch before locking. This reduces the chance of the decoder latching onto the wrong signal in the first place.
- If the decoded text confidence drops (characters turn orange or red in the decode display) after locking, the transmitting station may have drifted. Unlock 🔒P temporarily to let the decoder reacquire, then re-lock.
- You can lock pitch and speed independently. Locking speed alone is useful on a band where QSB shifts the audio pitch but the operator's sending speed is consistent.

## Troubleshooting

- **CW stats label shows no pitch or WPM after locking** — The lock buttons only hold the last tracked values; if no signal was tracked before locking, there is nothing to hold. Click 🔒P or 🔒S again to unlock and allow the decoder to search.
- **Decoder ignores a new station after locking** — This is expected behavior. Unlock the relevant button to let the decoder retune to the new signal.

## Related

- [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md)
- [Tune CW decoder sensitivity to reject noise](tune-cw-decoder-sensitivity-to-reject-noise.md)
- [Copy decoded CW text to the clipboard](copy-decoded-cw-text-to-the-clipboard.md)
