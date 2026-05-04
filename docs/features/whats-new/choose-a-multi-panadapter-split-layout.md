# Choose a multi-panadapter split layout

The Panadapter Stack hosts all panadapter displays in the main window and arranges them in configurable split layouts, from a single panel up to a 2×4 grid. Use the pan-layout dialog to switch between arrangements at any time.

## Steps

1. Open the pan-layout dialog from the main window's centre area (the Panadapter Stack is always visible there).
2. Select the layout that matches the number of panadapters you want displayed. Available options are listed in the table below. Confirm your choice to apply it immediately.

## What each control does

| Layout ID | Arrangement | Panadapter slots |
|-----------|-------------|-----------------|
| `1` | Single panel | 1 |
| `2v` | Two panels, vertical stack | 2 |
| `2h` | Two panels, side by side | 2 |
| `2h1` | Two side-by-side over one full-width | 3 |
| `12h` | One full-width over two side-by-side | 3 |
| `3v` | Three panels, vertical stack | 3 |
| `2x2` | 2×2 grid | 4 |
| `4v` | Four panels, vertical stack | 4 |
| `3h2` | Three over two | 5 |
| `2x3` | 2×3 grid | 6 |
| `4h3` | Four over three | 7 |
| `2x4` | 2×4 grid | 8 |

## Tips

- If the number of open panadapters does not match the selected layout's slot count, the stack automatically falls back to a sensible default for that panel count.
- Floating a panadapter into its own window removes it from the docked splitter. The remaining docked panels reflow to fill the splitter without leaving empty placeholder slots.
- On macOS, GPU resources are automatically reset after a panadapter is floated or docked back to fix static spectrum images.
- The chosen layout is saved in `PanadapterLayout` and restored on next launch.

## Related

- [Manage panadapter windows](manage-panadapter-windows.md)
- [Float and dock a panadapter](float-dock-panadapter.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
