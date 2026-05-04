# Avoid blank floating windows after adding a second panadapter

The Panadapter Stack hosts all panadapter displays in the main window. When you add a second panadapter and float it into its own window, the GPU surface can become stale, leaving the detached window blank or showing a frozen spectrum.

## Before you start

- You must have at least two panadapters created before floating one.
- On macOS with GPU spectrum rendering enabled, AetherSDR applies an automatic surface reset when a panadapter is reparented — no manual GPU restart is required.

## Steps

1. Open the pan-layout dialog and select a layout that accommodates two or more panadapters (for example, **2v** for a vertical stack or **2h** for side-by-side).
2. Float the second panadapter by detaching it from the main window using the float control on that panadapter's title bar.
3. If the floating window appears blank, bring the window to focus and wait up to one second — AetherSDR automatically hides the widget, resets the GPU surface, destroys and recreates the native window handle, and repaints. The spectrum image should appear within 50 ms of the reset completing.
4. If the docked area shows an empty placeholder slot after floating a panadapter, open the pan-layout dialog and reselect the layout that matches the number of remaining docked panadapters. AetherSDR will rebuild the splitter to remove the empty slot.

## What each control does

| Control | Behavior |
|---|---|
| Pan-layout dialog | Sets the split arrangement for all docked panadapters (vertical stack, side-by-side, and grids up to 2×4). AetherSDR automatically adjusts the layout ID when the number of docked panadapters changes due to floating or docking. |
| Float control (panadapter title bar) | Detaches the selected panadapter into a standalone window. On macOS with GPU rendering, AetherSDR resets the Metal surface and recreates the native window handle to prevent a blank spectrum image. |
| Dock control (floating window) | Returns the floating panadapter to the main window splitter. AetherSDR rebuilds the docked splitter and removes any empty placeholder slots. |

## Tips

- After floating a panadapter, avoid resizing the floating window immediately — wait for the automatic GPU surface reset to complete (around 50 ms) before interacting with it.
- If you repeatedly see blank floating windows on macOS, confirm that GPU spectrum rendering (`AETHER_GPU_SPECTRUM`) is active; the multi-step surface reset only runs on that code path.
- The splitter between docked panadapters uses a 3 px handle and does not allow panes to collapse, so resizing will not produce zero-height panels.

## Related

- [panadapter-layout.md](panadapter-layout.md)
- [floating-panadapters.md](floating-panadapters.md)
- [gpu-spectrum-macos.md](gpu-spectrum-macos.md)
<!-- docmesh:llm version=v0.9.5.1 date=2026-05-04 -->
