# Panadapter overview

The panadapter is the primary display in AetherSDR. It shows a live FFT spectrum and waterfall for a single slice, and optionally an off-air CW decoder panel beneath it. This page describes every control in the panadapter and links to task-specific pages.

## How it works

Each panadapter is bound to one slice (shown in the title bar as "Slice A" through "Slice H"). The upper portion is the spectrum and waterfall display; clicking or dragging it tunes the bound slice. Scrolling zooms the frequency span.

In single-panadapter mode the title bar shows only the slice label and drag grip. In multi-slice mode, pop-out (⬈), maximize (□), and close (×) buttons appear in the title bar so you can rearrange the layout.

The CW decode panel is hidden by default. When active, it sits below the waterfall and runs an off-air Morse decoder against PC audio routed to AetherSDR. The panel displays decoded text, pitch, and speed, and provides controls to tune and lock the decoder.

## What each control does

### Title bar

| Control | Kind | Behavior | Notes |
|---|---|---|---|
| Slice title | Indicator | Shows which slice is bound (e.g. "Slice A"). Range: Slice A–Slice H. | — |
| ⬈ / ↩ (pop-out/dock) | Push button | Pops the panadapter into a floating window; click again to dock it back. | Hidden in single-pan mode. |
| □ (maximize) | Push button | Maximizes this panadapter to fill the main area. | Hidden in single-pan mode. |
| × (close) | Push button | Closes this panadapter. | Hidden in single-pan mode. |

### Spectrum / waterfall

| Control | Kind | Behavior |
|---|---|---|
| Spectrum / waterfall | Drag handle | Click to activate the panadapter (multi-slice mode); drag to pan frequency; scroll to zoom. |

### CW decode panel

| Control | Kind | Default | Range | Persisted key | Behavior |
|---|---|---|---|---|---|
| CW stats label | Indicator | — | `<hz> Hz  <wpm> WPM` | — | Shows detected pitch and speed from the decoder. |
| Sens | Slider | 30 | 0–100 | `CwDecoderSensitivity` | Filters low-confidence decodes. Higher values are stricter. Maps 0–100 to an internal cost threshold of 1.0–0.1. |
| 🔒P (Lock Pitch) | Toggle button | Off | On/Off | — | Locks the decoder pitch to the current tuned frequency. |
| 🔒S (Lock Speed) | Toggle button | Off | On/Off | — | Locks the decoder speed to the current WPM. |
| Lo (pitch min) | Slider | 500 Hz | 300–1200 Hz | — | Minimum pitch the decoder searches. Clamped to ≤ Hi. |
| Hi (pitch max) | Slider | 700 Hz | 300–1200 Hz | — | Maximum pitch the decoder searches. Clamped to ≥ Lo. |
| CPY ALL | Push button | — | — | — | Copies the full decoded text buffer to the clipboard. |
| CPY VIS | Push button | — | — | — | Copies only the text currently visible in the scroll area to the clipboard. |
| CLR | Push button | — | — | — | Clears the CW decode buffer. |
| ✕ (close CW) | Push button | — | — | — | Hides the CW decode panel. |
| CW decode text | Text field (read-only) | — | — | — | Rolling display of decoded CW. Text is coloured by decode confidence: green (highest confidence) through yellow, orange, to red (lowest confidence). |

## Tips

- The CW decoder requires PC audio to be routed to AetherSDR. If the panel shows "(requires PC Audio)", audio routing is not yet configured.
- Lo and Hi are clamped against each other: dragging Lo above Hi snaps Lo down to Hi's value, and vice versa. Set Lo first, then Hi.
- Decoded text colour reflects confidence. Green text is the most reliable; red text should be treated with caution.

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
