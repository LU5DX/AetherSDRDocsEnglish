# Dock a floating panadapter back into the main window

The Panadapter Stack hosts all panadapter displays in the main window and supports floating individual panadapters into their own detached windows. Use the steps below to move a floating panadapter back into the main window.

## Before you start

- At least one panadapter must currently be floating in its own window.

## Steps

1. In the floating panadapter window, right-click the title bar (or anywhere on the panadapter) to open its context menu.
2. Select **Dock to main window**. The panadapter moves back into the Panadapter Stack and the splitter layout adjusts automatically to remove any empty placeholder slots.

## What each control does

| Control | Behavior |
|---|---|
| **Dock to main window** (context menu item) | Returns the floating panadapter to the main window's Panadapter Stack and updates the saved `FloatingPanIds` setting so the panadapter is no longer listed as floating on next launch. |
| Panadapter Stack splitter | Automatically resizes the remaining docked panadapters to fill the available space after docking. No empty slots are left behind. |

## Tips

- On macOS, the GPU surface resets automatically after docking to fix any static (frozen) spectrum image that appeared while the panadapter was detached.
- To rearrange docked panadapters after docking, use the pan-layout dialog accessible from the main window.
- The docked layout (including which panadapters are floating) is persisted in `PanadapterLayout` and `FloatingPanIds`, so your arrangement is restored on the next launch.

## Related

- [Float a panadapter into its own window](float-panadapter.md)
- [Configure the panadapter split layout](panadapter-layout.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
