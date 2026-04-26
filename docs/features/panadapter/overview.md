# Panadapter overview

The panadapter is AetherSDR's main display: a live FFT spectrum and waterfall showing radio frequency activity across the tuned band. An optional CW decode panel underneath it can decode Morse code off-air in real time.

## Before you start

- Connect to a FLEX-8600 radio. The panadapter requires an active radio connection.
- If you intend to use the CW decoder, PC audio routing to AetherSDR must be active. The panel shows the reminder "(requires PC Audio)" until audio is available.

## How it works

AetherSDR opens with one panadapter visible in the centre of the main window. The title bar at the top of the panadapter shows which slice is bound to it (default: "Slice A", ranging from Slice A through Slice H). In multi-slice mode, each slice gets its own panadapter with its own title bar and controls.

### Spectrum and waterfall

The spectrum and waterfall area occupies the main body of the panadapter. Clicking it activates that panadapter. Dragging tunes the VFO; scrolling zooms the frequency span. With `View > Pan Follows VFO` enabled (the default), the display pans automatically to keep the VFO marker in view.

### Title bar controls

In single-pan mode, the ⬈ / ↩, □, and × buttons are hidden. They become visible when a second panadapter is added.

| Control | What it does |
|---|---|
| Slice title | Indicator showing which slice (Slice A–Slice H) is bound to this panadapter. |
| ⬈ / ↩ (pop-out/dock) | Pops the panadapter into a floating window, or docks it back. Hidden in single-pan mode. |
| □ (maximize) | Expands this panadapter to fill the main area in a multi-pan layout. Hidden in single-pan mode. |
| × (close) | Closes this panadapter. Hidden in single-pan mode. |

### CW decode panel

The CW decode panel appears below the spectrum when the CW decoder is turned on. It uses PC audio to detect and decode Morse code off-air, displaying decoded text coloured by confidence: green (highest confidence), yellow, orange, and red (lowest confidence). The detected pitch and speed are shown in the CW stats label in the format `<hz> Hz  <wpm> WPM`.

## What each control does

### CW decode panel controls

| Control | Default | Valid range | Persisted key | What it does |
|---|---|---|---|---|
| CW stats label | — | `<hz> Hz  <wpm> WPM` | — | Shows the pitch (Hz) and speed (WPM) detected by the decoder. |
| Sens | 30 | 0–100 | `CwDecoderSensitivity` | Filters out low-confidence decodes. Higher values are stricter. Maps the 0–100 range to an internal cost threshold of 1.0–0.1. |
| 🔒P (Lock Pitch) | Off | On / Off | — | Locks the decoder to the current detected pitch rather than tracking automatically. |
| 🔒S (Lock Speed) | Off | On / Off | — | Locks the decoder to the current WPM rather than tracking automatically. |
| Lo (pitch min) | 500 Hz | 300–1200 Hz | — | Sets the lower bound of the pitch range the decoder searches. Clamped to be no greater than Hi. |
| Hi (pitch max) | 700 Hz | 300–1200 Hz | — | Sets the upper bound of the pitch range the decoder searches. Clamped to be no less than Lo. |
| CPY ALL | — | — | — | Copies the full decoded text buffer to the clipboard. |
| CPY VIS | — | — | — | Copies only the text currently visible in the scroll area to the clipboard. |
| CLR | — | — | — | Clears the CW decode buffer. |
| × (close CW) | — | — | — | Hides the CW decode panel. |

## Tips

- The Lo and Hi pitch sliders constrain the frequency range the decoder searches. Narrowing this range around the signal's actual tone (visible on the spectrum) reduces false detections.
- Decoded text confidence is shown by colour: green is below a 0.15 cost threshold, yellow below 0.35, orange below 0.60, and red at 0.60 or above. Raising Sens discards the red and orange text.
- With `View > Single-Click to Tune` enabled, a single click on the spectrum retunes the VFO. Without it, a double-click is required.

## Related

- [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md)
- [Tune CW decoder sensitivity to reject noise](tune-cw-decoder-sensitivity-to-reject-noise.md)
- [Lock CW decoder pitch or speed once tracking is good](lock-cw-decoder-pitch-or-speed-once-tracking-is-good.md)
- [Copy decoded CW text to the clipboard](copy-decoded-cw-text-to-the-clipboard.md)
- [Pop a panadapter out into its own window](pop-a-panadapter-out-into-its-own-window.md)
- [Maximize one panadapter to fill the main area](maximize-one-panadapter-to-fill-the-main-area.md)
- [Close an extra panadapter](close-an-extra-panadapter.md)
- [Click the spectrum to activate a panadapter (multi-slice mode)](click-the-spectrum-to-activate-a-panadapter-multi-slice-mode.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)
