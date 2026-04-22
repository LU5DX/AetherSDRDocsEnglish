# Panadapter overview

The panadapter is AetherSDR's primary display for visualizing RF spectrum activity. It combines an FFT spectrum plot and a scrolling waterfall, and optionally shows a CW decode panel below the display for off-air Morse reading.

## Before you start

- Connect to a FLEX-8600 radio. The panadapter requires an active radio connection.
- If you want to use the CW decoder, PC audio routing to AetherSDR must be configured first. The panel shows a "(requires PC Audio)" reminder until audio is available.

## How it works

Each panadapter is bound to one slice (Slice A through Slice H). The slice title is shown in the panadapter's title bar. In single-panadapter mode, the title bar buttons for pop-out, maximize, and close are hidden. They appear when more than one panadapter is open.

**Spectrum and waterfall interaction**

Clicking anywhere on the spectrum/waterfall area activates that panadapter. You can drag to tune and scroll to zoom. By default, a double-click is required to retune; enable `View > Single-Click to Tune` to change this. When `View > Pan Follows VFO` is on (the default), the display pans automatically to keep the active VFO marker visible.

**CW decode panel**

The CW decode panel appears below the spectrum when the CW decoder is turned on. It runs an off-air Morse decoder against PC audio and displays rolling decoded text. Each character is colour-coded by decode confidence: green (highest confidence), yellow, orange, and red (lowest confidence). The panel can be hidden at any time with ✕.

## What each control does

### Title bar

| Control | Kind | Behavior | Notes |
|---|---|---|---|
| Slice title | Indicator | Shows the slice bound to this panadapter (e.g. "Slice A"). | — |
| ⬈ / ↩ (pop-out/dock) | Button | Pops the panadapter into a floating window or docks it back. | Hidden in single-pan mode. |
| □ (maximize) | Button | Maximizes this panadapter to fill the main layout area. | Hidden in single-pan mode. |
| × (close) | Button | Closes this panadapter. | Hidden in single-pan mode. |

### Spectrum / waterfall

| Control | Kind | Behavior |
|---|---|---|
| Spectrum / waterfall | Display and drag handle | Click to activate; drag to tune; scroll to zoom. |

### CW decode panel

| Control | Kind | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|---|
| CW stats label | Indicator | — | `<hz> Hz  <wpm> WPM` | — | Shows the pitch and speed currently detected by the decoder. |
| Sens | Slider | 30 | 0–100 | `CwDecoderSensitivity` | Filters low-confidence decodes. Higher values are stricter. Maps 0–100 to a cost threshold of 1.0–0.1. |
| 🔒P (Lock Pitch) | Toggle button | Off | — | — | Locks the decoder pitch to the current tuned frequency. |
| 🔒S (Lock Speed) | Toggle button | Off | — | — | Locks the decoder speed to the current WPM. |
| Lo (pitch min) | Slider | 500 Hz | 300–1200 Hz | — | Sets the minimum pitch the decoder searches. Clamped to ≤ Hi. |
| Hi (pitch max) | Slider | 700 Hz | 300–1200 Hz | — | Sets the maximum pitch the decoder searches. Clamped to ≥ Lo. |
| CPY ALL | Button | — | — | — | Copies the full decoded text buffer to the clipboard. |
| CPY VIS | Button | — | — | — | Copies only the text currently visible in the scroll area to the clipboard. |
| CLR | Button | — | — | — | Clears the CW decode buffer. |
| ✕ (close CW) | Button | — | — | — | Hides the CW decode panel. |
| CW decode text | Read-only text area | — | — | — | Rolling display of decoded Morse. Characters are coloured by confidence: green (<0.15), yellow (<0.35), orange (<0.60), red (≥0.60). |

## Tips

- Lo and Hi define the pitch search window. Narrowing the range around a known signal pitch reduces false decodes from adjacent interference.
- Setting Sens to 0 shows all decode attempts, including low-confidence ones. Raise it gradually until noise-driven garbage disappears.
- Use 🔒P and 🔒S once the decoder has locked onto a signal cleanly. This prevents the decoder from drifting if the signal temporarily weakens.

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
