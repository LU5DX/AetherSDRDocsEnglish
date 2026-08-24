# Toggle the 3D FFT spectrum view

Switch the spectrum display from the default 2D FFT waterfall to a 3D surface view that shows signal history scrolling forward in time, with elevation shadows for slice markers.

## Before you start

- Your radio must be connected and the panadapter visible in the main window.
- The panadapter must be in a normal (docked) state — the 3D toggle is part of the SpectrumWidget embedded in each Panadapter.

## Steps

1. Locate the panadapter's spectrum display area (the FFT / waterfall region).
2. Click the **3D FFT view** toggle button on the panadapter. This button is a toggle that switches between the default 2D spectrum and the 3D surface view.
   - The button label reads **3D FFT view** (a toggle button in the SpectrumWidget).
   - The default state is **Disabled**.
3. To return to the 2D view, click the **3D FFT view** toggle again.

## What each control does

| Control | Behavior |
|---|---|
| **3D FFT view** toggle button | Switches between 2D spectrum/waterfall and the 3D surface view. When enabled, signal history displays as a forward-scrolling 3D surface with elevation shadows cast by slice flags. The floor resynchronizes after bandwidth zoom. |
| **Slice title** | Shows which slice is bound to this panadapter (Slice A through Slice H). |
| **⬈ / ↩ (pop-out/dock)** | Pops the panadapter out into a floating window or docks it back. Hidden in single-pan mode. Floating window is frameless — drag via the in-app title strip, resize via the bottom-right size grip. On macOS, every float/dock cycle re-binds the GPU surface so the spectrum stays live. Saved floating-window state is not restored when subsequent panadapters are added. When docked back, empty splitter slots are reclaimed. |
| **□ (maximize)** | Maximizes this panadapter in a multi-pan layout. Hidden in single-pan mode. |
| **× (close)** | Closes this panadapter. Hidden in single-pan mode. |
| **Spectrum / waterfall** | Click activates the panadapter; drag to tune, scroll to zoom. |
| **CW stats label** | Shows detected CW pitch and speed in the format `<hz> Hz  <wpm> WPM`. |
| **Sens** | Slider (0–100, default 30) that filters low-confidence decodes; higher = stricter. Maps to a cost threshold of 1.0–0.1. |
| **🔒P (Lock Pitch)** | Locks the CW decoder pitch to the current tuned frequency. |
| **🔒S (Lock Speed)** | Locks the CW decoder speed to the current WPM. |
| **Lo (pitch min)** | Slider (300–1200 Hz, default 500) for the minimum pitch the CW decoder searches; clamped ≤ Hi. |
| **Hi (pitch max)** | Slider (300–1200 Hz, default 700) for the maximum pitch the CW decoder searches; clamped ≥ Lo. |
| **CPY ALL** | Copies the full decoded text to the clipboard. |
| **CPY VIS** | Copies only the text currently visible in the scroll area. |
| **CLR** | Clears the CW decode buffer. |
| **✕ (close CW)** | Hides the CW decode panel. |
| **CW decode text** | Read-only rolling display of decoded CW coloured by confidence. Colours: <0.15 green, <0.35 yellow, <0.60 orange, ≥0.60 red. |

## Panadapter behavior and canvas mode

The panadapter includes a number of automatic behaviors:

- The waterfaall freeze/unfreeze is driven by the radio's interlock TRANSMITTING state. When any client on the network (including remote clients) transmits, the waterfall freezes; it unfreezes when transmitting ends. This eliminates the 10–23 second TX-trail artifact after unkeying.
- On radio reconnect, the desired panadapter frame rate (FPS) and waterfall line duration are re-applied to prevent silently dropping to the radio's 10 Hz default.
- Secondary panadapters (Slices B–H) have their dBm range primed on reconnect so the noise-floor auto-adjust starts from the correct baseline (rather than the default range that caused a flat spectrum on reconnect).
- When the panadapter is hosted as an item on the workspace canvas (canvas mode), the title strip streams live-move gestures. A 6 px drag threshold separates a click (which activates the pan) from a drag. The pop-out button remains visible in canvas mode even if you are the only panadapter.
- The CW decoder additionally shows a hint that it requires PC audio routing to work ("(requires PC Audio)").

## Tips

- The 3D FFT view includes smooth-scroll history boundaries and cached elevation shadows for slice markers.
- Bandwidth zoom works normally — the floor resynchronizes automatically.
- This feature is new in v26.7.x and is part of the SpectrumWidget.

## Related

- [Read signal history as a scrolling 3D surface](read-signal-history-as-a-scrolling-3d-surface.md)