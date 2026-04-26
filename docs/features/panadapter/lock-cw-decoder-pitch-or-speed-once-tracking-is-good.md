# Lock CW decoder pitch or speed once tracking is good

Once the CW decoder has settled on a signal's pitch and speed, locking those values prevents the decoder from drifting to interference or noise between transmissions.

## Before you start

- The CW decode panel must be open and decoding. See [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md).
- PC audio must be routed to AetherSDR. The CW panel shows "(requires PC Audio)" as a reminder if it is not.
- Watch the CW stats label (format: `<hz> Hz  <wpm> WPM`) and wait for stable, consistent readings before locking.

## Steps

1. Tune to the CW signal and watch the CW stats label until pitch and speed readings stabilize.
2. To lock pitch: click 🔒P in the CW panel. The button highlights when active.
3. To lock speed: click 🔒S in the CW panel. The button highlights when active.
4. To unlock, click the active button again.

## What each control does

| Control | What it does | Default | Range | Setting key |
|---|---|---|---|---|
| CW stats label | Shows detected pitch and speed as `<hz> Hz  <wpm> WPM`. | — | — | — |
| 🔒P | Locks the CW decoder pitch to the current tuned frequency. Toggle; highlighted when locked. | Off | — | — |
| 🔒S | Locks the CW decoder speed to the current WPM. Toggle; highlighted when locked. | Off | — | — |
| Lo | Minimum pitch the decoder searches. Clamped ≤ Hi. | 500 Hz | 300–1200 Hz | — |
| Hi | Maximum pitch the decoder searches. Clamped ≥ Lo. | 700 Hz | 300–1200 Hz | — |
| Sens | Filters low-confidence decodes. Higher values are stricter. | 30 | 0–100 | `CwDecoderSensitivity` |

## Tips

- Lock pitch and speed together when copying a single station through a pileup. The decoder will stop chasing other signals in the passband.
- If the signal drifts slightly, unlock 🔒P, let the decoder re-acquire, then re-lock.
- Narrow the Lo and Hi pitch range before locking to reduce the chance of the decoder latching onto the wrong signal in the first place.
- Decoded text is colour-coded by confidence: green is highest confidence, then yellow, orange, and red. Lock when you are seeing mostly green or yellow characters.

## Troubleshooting

- **🔒P or 🔒S does not appear** — The CW decode panel is not open. Open it first; see [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md).
- **Stats label shows no reading after locking** — PC audio is not routed to AetherSDR. The panel will show "(requires PC Audio)". Check your audio routing and unlock to allow the decoder to re-acquire.
- **Decoded text turns mostly orange or red after locking** — The locked pitch or speed no longer matches the signal. Click 🔒P or 🔒S to unlock, wait for the stats label to stabilize on the target signal, then re-lock.

## Related

- [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md)
- [Tune CW decoder sensitivity to reject noise](tune-cw-decoder-sensitivity-to-reject-noise.md)
- [Copy decoded CW text to the clipboard](copy-decoded-cw-text-to-the-clipboard.md)
