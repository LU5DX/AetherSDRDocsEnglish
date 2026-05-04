# Dock a floating panadapter back into the main window

A floating panadapter is one that has been detached from the main window into its own independent window. Use these steps to move it back into the main window's split layout.

## Before you start

- At least one panadapter must currently be floating (detached from the main window).

## Steps

1. In the floating panadapter window, click the **Dock** button (or double-click the window title bar) to return the panadapter to the main window.
2. The main window rebuilds its split layout automatically to include the newly docked panadapter. If the current layout setting does not match the number of docked panadapters, the layout adjusts to fit.

> **macOS note:** After docking, the GPU surface is reset automatically to clear any static spectrum image that may appear. A brief flicker is normal.

## What each control does

| Control | Behavior |
|---|---|
| Dock action (floating window) | Removes the panadapter from its standalone window, inserts it back into the main window splitter, and rebuilds the docked layout. |
| Main window splitter | Arranges all docked panadapters in the configured split layout (vertical stack, side-by-side, or grid). Resizes automatically when a pan is added or removed. |
| Pan-layout dialog | Sets the split arrangement used when panadapters are docked. Open it to change the layout after docking. |

## Tips

- If the spectrum display appears frozen or shows a static image after docking on macOS, the GPU surface resets automatically within about 50 ms. If the issue persists, open the pan-layout dialog and reapply your layout to force a full rebuild.
- The splitter hides empty placeholder slots — only docked panadapters occupy space, so the layout stays compact regardless of how many pans are floating.
- Floating and docked state is saved between sessions via the `FloatingPanIds` and `PanadapterLayout` settings.

## Related

- [Change the panadapter split layout](pan-layout.md)
- [Float a panadapter into its own window](float-panadapter.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
