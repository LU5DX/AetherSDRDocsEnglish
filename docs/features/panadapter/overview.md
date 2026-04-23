# Panadapter overview

The panadapter displays a live FFT spectrum and waterfall for a bound slice, and optionally decodes Morse code from audio. This page describes every control in the panadapter and its CW decode panel; follow the links at the bottom for step-by-step task instructions.

## Before you start

- AetherSDR must be connected to a Flex radio. The panadapter requires an active radio connection.
- PC audio must be routed to AetherSDR for the CW decoder to produce output.

## How it works

Each panadapter is a self-contained display bound to one slice (Slice A through Slice H). The main area shows the FFT spectrum on top and the waterfall below, drawn by the SpectrumWidget. Click anywhere on the spectrum or waterfall to activate that panadapter; drag to tune; scroll to zoom.

In the default single-panadapter layout, only one panadapter is visible and its title bar buttons (pop-out, maximize, close) are hidden. When you add slices, each panadapter gets its own title bar and those buttons become available.

Underneath the spectrum sits an optional CW decode panel. It is hidden by default and appears when you enable CW decoding. The decoder listens to PC audio and uses the ggmorse engine to identify Morse; decoded text scrolls in a read-only display and is colour-coded by confidence.

## What each control does

### Title bar

| Control | Kind | Behavior |
|---|---|---|
| Slice title | Indicator | Shows the slice bound to this panadapter. Default: `Slice A`. Range: Slice A–Slice H. |
| ⬈ / ↩ (pop-out/dock) | Button | Pops the panadapter into a floating window, or docks it back. Hidden in single-pan mode. |
| □ (maximize) | Button | Maximizes this panadapter to fill the main area in a multi-pan layout. Hidden in single-pan mode. |
| × (close) | Button | Closes this panadapter. Hidden in single-pan mode. |

### Spectrum and waterfall

| Control | Kind | Behavior |
|---|---|---|
| Spectrum / waterfall | Display / drag handle | Click to activate this panadapter. Drag left or right to tune. Scroll to zoom in or out. |

### CW decode panel

| Control | Kind | Default | Range | Setting key | Behavior |
|---|---|---|---|---|---|
| CW stats label | Indicator | — | `<hz> Hz  <wpm> WPM` | — | Shows the pitch and speed currently detected by the decoder. |
| Sens | Slider | 30 | 0–100 | `CwDecoderSensitivity` | Filters low-confidence decodes. Higher values are stricter. Internally maps 0–100 to a cost threshold of 1.0–0.1. |
| 🔒P (Lock Pitch) | Toggle button | Off | On / Off | — | Locks the decoder pitch to the currently tuned frequency. |
| 🔒S (Lock Speed) | Toggle button | Off | On / Off | — | Locks the decoder speed to the current WPM value. |
| Lo (pitch min) | Slider | 500 Hz | 300–1200 Hz | — | Sets the minimum pitch the decoder searches. Clamped to be no greater than Hi. |
| Hi (pitch max) | Slider | 700 Hz | 300–1200 Hz | — | Sets the maximum pitch the decoder searches. Clamped to be no less than Lo. |
| CPY ALL | Button | — | — | — | Copies the entire decoded text buffer to the clipboard. |
| CPY VIS | Button | — | — | — | Copies only the text currently visible in the scroll area to the clipboard. |
| CLR | Button | — | — | — | Clears the CW decode buffer. |
| × (close CW) | Button | — | — | — | Hides the CW decode panel. |
| CW decode text | Read-only display | — | — | — | Rolling display of decoded Morse. Text is colour-coded by decode confidence: green (best) through yellow and orange to red (poorest). |

## Tips

- Lo and Hi define the pitch search window. Narrowing this range around the actual signal pitch reduces false decodes.
- The CW stats label shows `(requires PC Audio)` when audio is not yet routed. If you see only this hint and no pitch or WPM, check your PC audio routing before adjusting Sens.
- Decoded text colour gives a quick quality check without reading the raw characters. A stream of green text indicates the decoder is tracking the signal well.

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
