# Switch to a single full-width panadapter

This page explains how to change the panadapter area to display one full-width panadapter. Use this when you want to focus on a single slice without split-screen clutter.

## Before you start

- AetherSDR must be connected to a Flex radio. The layout dialog requires an active radio connection.

## Steps

1. Right-click anywhere in the panadapter area to open the **Panadapter Layout** dialog.
2. Click the preview tile labeled **Single (1 pan)**.
3. The dialog closes immediately and the panadapter area switches to a single full-width view.

## What each control does

| Control | Description | Setting key |
|---|---|---|
| **Single (1 pan)** tile | Selects the single full-width layout (layout ID `1`). Clicking it confirms the selection and closes the dialog. | `PanLayout` |
| Layout tiles (other) | Preview tiles for all other arrangements: **2v** (2 vertical), **2h** (2 horizontal), **2h1** (2 horizontal, 1 small), **12h** (1 large, 2 horizontal), **2x2** (2x2 grid), **3h2** (3 horizontal, 2 below), **2x3** (2x3 grid), **4h3** (4 horizontal, 3 below), **2x4** (2x4 grid). Tiles requiring more panadapters than the radio's supported slice count are disabled (forbidden cursor). If the radio's slice limit is already at capacity when a layout requiring more panadapters is selected, a status-bar warning is shown and the layout change is cancelled. | `PanLayout` |
| **Cancel** | Closes the dialog without changing the current layout. | — |

## Tips

- The tile for the currently active layout is highlighted with a distinct border. If the **Single (1 pan)** tile is already highlighted, the layout is already set to single and no change is needed.
- Tiles for layouts that require more panadapters than your radio supports are disabled and show a forbidden cursor. The single layout is always available.
- If you attempt to apply a layout that requires more panadapters than the radio's available slice capacity, a status-bar message appears: "Slice capacity is full; cannot add another panadapter (<model> supports <N> slices)" and the layout change is cancelled.
- The dialog window now follows the active AetherSDR theme. Button colors and text styling adapt to the theme's background and accent colors for consistent visual appearance.

## Related

- [Panadapter Layout overview](overview.md)
- [Split panadapter area side-by-side](split-panadapter-area-side-by-side.md)
- [Preview and pick among the 10 layout variants](preview-and-pick-among-the-10-layout-variants.md)