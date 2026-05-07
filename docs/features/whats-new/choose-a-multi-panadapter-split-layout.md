# Choose a multi-panadapter split layout

The Panadapter Stack occupies the centre area of the main window and arranges all open panadapter displays in a configurable split layout — vertical stack, side-by-side, or grids up to 2×4. Individual panadapters can also be floated into their own windows and docked back at any time.

## Steps

1. Open the pan-layout dialog from the main window (the exact menu path is labelled **Pan Layout** in the toolbar or application menu).
2. Select the layout you want — vertical stack, side-by-side, or a grid arrangement up to 2×4.
3. Close the dialog. The Panadapter Stack immediately rearranges the displays to match.

> **macOS note:** When you float or dock a panadapter, the GPU surface is automatically reset. If a detached window shows a static spectrum image, dock it and float it again to trigger the reset.

## What each layout option does

| Layout | Behavior |
|---|---|
| Vertical stack | Panadapters are stacked top-to-bottom in a single column. |
| Side-by-side | Panadapters are arranged left-to-right in a single row. |
| Grid (up to 2×4) | Panadapters fill a grid of up to 2 columns and 4 rows. |

The selected layout is saved automatically as `PanadapterLayout` and restored on next launch.

## Tips

- Floated panadapters are remembered across sessions via `FloatingPanIds`. Close and reopen the application to verify that your floating windows restore correctly.
- When all panadapters are floated, the docked splitter collapses so no empty placeholder slots appear in the main window.
- Dock all floated panadapters before closing the application on macOS to avoid GPU teardown issues.

## Related

- [Panadapter overview](panadapter-overview.md)
- [Float a panadapter into its own window](float-panadapter.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
