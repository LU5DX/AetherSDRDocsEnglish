# Fix a static spectrum in a floating panadapter window

When a panadapter is popped out into a floating window, the spectrum and waterfall can freeze. On macOS, popping out and docking resets the GPU surface so the display resumes updating live.

## Steps

1. In the panadapter title bar, click **⬈ / ↩ (pop-out/dock)** to pop the panadapter out into a floating window.
2. Click **⬈ / ↩ (pop-out/dock)** again to dock it back into the main window.

The GPU surface (QRhi/Metal) is reset on each pop-out/dock cycle, which clears the static spectrum.

## What each control does

| Control | Behavior |
|---|---|
| Slice title | Indicator showing which slice (Slice A–Slice H) is bound to this panadapter. |
| ⬈ / ↩ (pop-out/dock) | Pops the panadapter out into a floating frameless window or docks it back. On macOS, each toggle resets the QRhi/Metal GPU surface so the spectrum updates live in the detached window. Hidden in single-pan mode. |
| □ (maximize) | Maximizes this panadapter in a multi-pan layout. Hidden in single-pan mode. |
| × (close) | Closes this panadapter. Hidden in single-pan mode. |
| Spectrum / waterfall | Click to activate the panadapter; drag to tune; scroll to zoom. |
| CW stats label | Shows detected CW pitch and speed in the format `<hz> Hz  <wpm> WPM`. |
| Sens | Filters low-confidence CW decodes. Higher values are stricter. Default: 30 (range 0–100). |
| 🔒P (Lock Pitch) | Locks the CW decoder pitch to the current tuned frequency. |
| 🔒S (Lock Speed) | Locks the CW decoder speed to the current WPM. |
| Lo (pitch min) | Sets the minimum pitch the CW decoder searches. Clamped to ≤ Hi. Default: 500 Hz (range 300–1200 Hz). |
| Hi (pitch max) | Sets the maximum pitch the CW decoder searches. Clamped to ≥ Lo. Default: 700 Hz (range 300–1200 Hz). |
| CPY ALL | Copies the full decoded CW text to the clipboard. |
| CPY VIS | Copies only the text currently visible in the scroll area. |
| CLR | Clears the CW decode buffer. |
| ✕ (close CW) | Hides the CW decode panel. |
| CW decode text | Read-only rolling display of decoded CW coloured by confidence. Green: <0.15, yellow: <0.35, orange: <0.60, red: ≥0.60. |

## Tips

- The floating window is frameless — drag it by the in-app title strip and resize using the bottom-right size grip.
- Previously saved floating-window state is not restored after new panadapters are added, which prevents blank phantom windows from appearing on startup.
- The CW decoder requires PC audio routing to function; look for the `(requires PC Audio)` hint label if no decoding occurs.

## Related

- [Panadapter overview](panadapter-applet.md)
- [Navigation and window chrome](00-navigation.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
