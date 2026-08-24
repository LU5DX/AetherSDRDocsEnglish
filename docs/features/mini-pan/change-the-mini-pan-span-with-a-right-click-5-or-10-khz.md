# Change the mini-pan span with a right-click (5 or 10 kHz)

This page shows you how to switch the mini-pan narrow scope between its two available spans — ±5 kHz (10 kHz total) and ±10 kHz (20 kHz total) — using a right-click menu.

## Before you start

- Your FLEX-8600 must be connected to AetherSDR.
- The Mini-Pan applet must be open (see [Open the mini-pan narrow scope](open-the-mini-pan-narrow-scope.md)).

## Steps

1. Right-click anywhere on the mini-pan scope.
2. In the context menu, choose **±5 kHz** or **±10 kHz**.
3. The scope immediately re-slices to the new span on the next frame.

## What each control does

| Control | Default | Valid range | Persisted setting |
|---------|---------|-------------|-------------------|
| **±5 kHz** (right-click menu action) | Selected | ±5 kHz (10 kHz span) | `MiniPan` |
| **±10 kHz** (right-click menu action) | — | ±10 kHz (20 kHz span) | `MiniPan` |

- The chosen span persists across sessions. Values in the `MiniPan` AppSettings object outside the two menu options fall back to the ±5 kHz default.
- The VFO readout and hairline marker are drawn inside the scope on the same row as the span labels; the readout is centred on the passband centre rather than the carrier.

## Tips

- The span menu only offers the two frequency options. Float, dock, always-on-top, and close controls are on the container title bar that wraps the applet.
- The scope's dBm range is fixed at −130 to −40; it does not auto-scale.

## Related

- [Open the mini-pan narrow scope](open-the-mini-pan-narrow-scope.md)
- [Mini-Pan overview](overview.md)
