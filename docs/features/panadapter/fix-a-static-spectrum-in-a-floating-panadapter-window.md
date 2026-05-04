# Fix a static spectrum in a floating panadapter window

When a panadapter is popped out into a floating window, the spectrum can appear frozen. On macOS, popping the window out and back in resets the GPU surface so live spectrum updates resume.

## Steps

1. Click **⬈ / ↩ (pop-out/dock)** in the panadapter title bar to pop the panadapter into a floating window.
2. Click **⬈ / ↩ (pop-out/dock)** again to dock it back into the main window. The QRhi/Metal GPU surface is reset and the spectrum resumes updating.

## What each control does

| Control | Behavior |
|---|---|
| Slice title | Indicator showing which slice (Slice A–Slice H) is bound to this panadapter. |
| ⬈ / ↩ (pop-out/dock) | Pops the panadapter out into a floating window or docks it back. On macOS, each pop-out/dock cycle resets the QRhi/Metal GPU surface, restoring live spectrum updates. The floating window is frameless — drag it using the in-app title strip and resize using the bottom-right size grip. |
| □ (maximize) | Maximizes this panadapter in a multi-pan layout. Hidden in single-pan mode. |
| × (close) | Closes this panadapter. Hidden in single-pan mode. |
| Spectrum / waterfall | Click to activate the panadapter; drag to tune; scroll to zoom. |

## Tips

- If the spectrum stays frozen after one dock/undock cycle, check that the slice shown in the **Slice title** indicator matches the slice you expect — a mismatched slice binding can also cause a blank display.
- Previously saved floating-window state is not restored after new panadapters are added, which prevents blank phantom windows on startup.

## Related

- [panadapter-applet.md](panadapter-applet.md)
- [navigation.md](navigation.md)
<!-- docmesh:llm version=v0.9.5.1 date=2026-05-04 -->
