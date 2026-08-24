# Mini-Pan overview

The Mini-Pan is a compact, detachable narrow-band scope (span of ±5 or ±10 kHz) centered on the active VFO's receive passband. It works independently of the main panadapter, giving you a close-up view of your received signal that you can keep on top of other applications, and it remains reachable from the applet panel even when the main panadapter is hidden in Minimal Mode.

## Before you start

- You need a connected FLEX-8600 radio.
- The applet panel must be visible (or you must be in Minimal Mode).

## How it works

The Mini-Pan is an applet, not a radio object — it creates no panadapter or slice. Instead, it re-slices the FFT frames the active slice's pan is already streaming, so opening it costs the radio nothing extra.

The view is centered on the passband center, not the carrier, so on SSB the received signal sits in the middle of the scope instead of hard against one edge. The trace mirrors the source pan's own FFT Line/Fill settings and dBm range, and the scope's vertical scale is fixed from -130 dBm to -40 dBm.

A frequency readout and a hairline marker for the carrier are drawn inside the trace, on the same row as the span labels. The scope's useful detail is set by the main panadapter's bin width, not by the applet's own pixel width.

The applet reports two intents back to the main window: whether it wants a spectrum feed (shown or hidden) and when its span changes. When hidden — whether by the tray toggle, the container's close button, a float, or a dock — the feed stops, so a hidden applet costs nothing per frame.

## What each control does

| Control | What it does | Default | Valid range | Setting key |
| --- | --- | --- | --- | --- |
| **Span** (right-click the scope) | Opens a menu to choose the mini-pan frequency span; selecting re-slices the next frame to the new window. | ±5 kHz | ±5 kHz (10 kHz span), ±10 kHz (20 kHz span) | `MiniPan` |
| **VFO readout** | Shows the followed VFO frequency and a hairline marker, drawn inside the scope on the same row as the span labels. | — | — | — |

The span choice persists in the `MiniPan` AppSettings object (the `spanKHz` field). If the value is hand-edited outside the two menu options, it falls back to the ±5 kHz default.

Float, dock, always-on-top, and close are handled by the standard ContainerTitleBar wrapping the applet — they aren't in the right-click menu.

To open the Mini-Pan: Applet panel > **Mini-Pan** tile.

## Tips

- The scope's vertical dBm range is fixed and matches the source pan's own range — it won't auto-scale independently, so a signal's height agrees with the main panadapter.
- In Minimal Mode, the applet panel is the primary UI, so the **Mini-Pan** tray button is the only entry point to this feature.

## Related

- [Open the mini-pan narrow scope](open-the-mini-pan-narrow-scope.md)
- [Change the mini-pan span with a right-click (5 or 10 kHz)](change-the-mini-pan-span-with-a-right-click-5-or-10-khz.md)
