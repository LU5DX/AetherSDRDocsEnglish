# Avoid blank floating windows after adding a second panadapter

When you float a panadapter into its own window and then add a second panadapter, the detached window can display a blank (static) spectrum image. The Panadapter Stack automatically resets the GPU surface after reparenting to fix this, but you need to follow the correct sequence to trigger that reset.

## Before you start

- You must have at least one panadapter visible in the main window.
- Open the pan-layout dialog before floating any panadapter.

## Steps

1. Open the pan-layout dialog and configure your desired split layout (vertical stack, side-by-side, or grid up to 2×4) **before** floating any panadapter.
2. Float the panadapter you want in a separate window by using the float control on that panadapter panel. The Panadapter Stack will reset the GPU surface automatically after reparenting.
3. Add the second panadapter through the pan-layout dialog. The docked splitter will compact itself so no empty placeholder slots appear in the main window.
4. If the floating window still shows a blank spectrum, dock the floating panadapter back into the main window and then re-float it. This forces a second GPU surface reset.

## What each control does

| Control | Behavior |
|---|---|
| Pan-layout dialog | Sets the arrangement of all panadapters (vertical stack, side-by-side, or grids up to 2×4). Open this before adding or floating panadapters to avoid blank windows. |
| Float control (per panadapter) | Detaches the panadapter into its own window. The Panadapter Stack resets the GPU surface on macOS after reparenting to prevent a static spectrum image. |
| Dock control (per floating panadapter) | Returns a floating panadapter to the main window. Use this to force a fresh GPU surface reset if the floating window remains blank. |
| Docked splitter | Keeps the in-window layout compact. Automatically removes empty placeholder slots when panadapters are floated or docked. |

## Tips

- On macOS, blank floating windows are most likely to occur when you add a second panadapter while an existing panadapter is already floating. Configure the layout first, then float.
- Releasing GPU resources happens automatically before main-window teardown, so you do not need to dock all panadapters before closing the application.

## Related

- [Pan-layout dialog](pan-layout-dialog.md)
- [Panadapter Stack](panadapter-stack.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
