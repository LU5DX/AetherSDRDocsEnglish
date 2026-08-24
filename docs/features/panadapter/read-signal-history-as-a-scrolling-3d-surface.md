# Read signal history as a scrolling 3D surface

Enable the 3D FFT spectrum view to see signal history rendered as a forward-scrolling 3D surface instead of the traditional 2D waterfall. The surface shows elevation shadows from slice flags and resynchronizes its floor after bandwidth zoom.

## Before you start

- Your AetherSDR must be connected to a FLEX-8600 radio (see [Radio Setup...] in the Settings menu).
- A panadapter must be visible in the main window showing spectrum and waterfall data.

## Steps

1. Locate the **3D FFT view** toggle button on the panadapter — it is labeled with the 3D FFT icon and sits with the other spectrum controls in the SpectrumWidget area.
2. Click the **3D FFT view** toggle button once to enable the 3D surface view. The spectrum display switches from the flat 2D waterfall to a scrolling 3D surface.
3. To return to the standard 2D view, click the same **3D FFT view** toggle button again to disable it.

## What each control does

| Control | Default | Behavior | Setting key |
|---------|---------|----------|-------------|
| 3D FFT view toggle | Disabled | Enables/disables the 3D FFT spectrum view showing signal history as a forward-scrolling surface with elevation shadows and smooth-scroll boundaries. | None |
| Slice title | Slice A | Shows which slice is bound to this panadapter (Slice A..Slice H). | None |
| ⬈ / ↩ (pop-out/dock) | — | Pops the panadapter out into a floating window or docks it back. Hidden in single-pan mode; always available when the panadapter is hosted on the workspace canvas. | None |
| □ (maximize) | — | Maximizes this panadapter in a multi-pan layout. Hidden in single-pan mode. | None |
| × (close) | — | Closes this panadapter. Hidden in single-pan mode. | None |
| Spectrum / waterfall | — | Click activates the panadapter; drag to tune, scroll to zoom. | None |
| CW stats label | — | Shows detected CW pitch and speed as `<hz> Hz  <wpm> WPM`. | None |
| Sens | 30 | Filters low-confidence decodes; higher = stricter. Maps 0-100 to cost threshold 1.0-0.1. | `CwDecoderSensitivity` |
| 🔒P (Lock Pitch) | — | Locks the CW decoder pitch to the current tuned frequency. | None |
| 🔒S (Lock Speed) | — | Locks the CW decoder speed to the current WPM. | None |
| Lo (pitch min) | 500 | Minimum pitch the CW decoder searches; clamped ≤ Hi. Range 300-1200 Hz. | None |
| Hi (pitch max) | 700 | Maximum pitch the CW decoder searches; clamped ≥ Lo. Range 300-1200 Hz. | None |
| CPY ALL | — | Copies the full decoded text to the clipboard. | None |
| CPY VIS | — | Copies only the text currently visible in the scroll area. | None |
| CLR | — | Clears the CW decode buffer. | None |
| ✕ (close CW) | — | Hides the CW decode panel. | None |
| CW decode text | — | Read-only rolling display of decoded CW coloured by confidence (green <0.15, yellow <0.35, orange <0.60, red ≥0.60). | None |

## Waterfall freeze and reconnect behavior

- The waterfall freezes whenever any client (including a second FlexRadio client) transmits, and resumes when transmission ends. This is driven by the radio's interlock TRANSMITTING state, eliminating the 10-23 s TX-trail artifact after unkeying.
- On radio reconnect, the desired panadapter FPS and waterfall line duration are reasserted automatically, preventing silently dropping to the radio's 10 Hz default.
- Secondary panadapters (Slices B-H) have their dBm range primed on reconnect so the noise-floor auto-adjust starts from the correct baseline rather than the default [-50, +50] range that caused flat spectrum on reconnect.

## Tips

- Slice flags cast cached elevation shadows on the 3D surface, making active slice positions easier to identify at a glance.
- The 3D surface floor resynchronizes automatically after you change the bandwidth zoom level, preventing a flat or misaligned baseline.
- The 3D FFT view shares the same panadapter freeze behavior as the 2D waterfall — during transmit (from any client), the display freezes and resumes when transmission ends.

## Canvas hosting

When the panadapter is hosted as an item on the workspace canvas (rather than in the standard stack layout):

- The title strip streams a live-move gesture you can drag to reposition the panadapter on the canvas.
- A 6 px drag threshold separates a click (which activates the panadapter) from a drag.
- The pop-out button remains available even in single-pan mode while on the canvas, so you can always float a canvas-hosted panadapter.

## Related

- [Toggle the 3D FFT spectrum view](toggle-the-3d-fft-spectrum-view.md)
- [Panadapter overview](overview.md)