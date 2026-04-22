# Switch to a single full-width panadapter

This page explains how to change the panadapter area to display one full-width panadapter. Use this when you want to focus on a single slice without split-screen clutter.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The layout dialog requires an active radio connection.

## Steps

1. Right-click anywhere in the panadapter area to open the **Panadapter Layout** dialog.
2. Click the preview tile labeled **Single (1 pan)**.
3. The dialog closes immediately and the panadapter area switches to a single full-width view.

## What each control does

| Control | Description | Setting key |
|---|---|---|
| **Single (1 pan)** tile | Selects the single full-width layout (layout ID `1`). Clicking it confirms the selection and closes the dialog. | `PanLayout` |
| Layout tiles (other) | Preview tiles for all other arrangements. Grayed out if the radio's licensed pan count is insufficient. | `PanLayout` |
| **Cancel** | Closes the dialog without changing the current layout. | — |

## Tips

- The tile for the currently active layout is highlighted with a distinct border. If the **Single (1 pan)** tile is already highlighted, the layout is already set to single and no change is needed.
- Tiles for layouts that require more panadapters than your radio supports are disabled and show a forbidden cursor. The single layout is always available.

## Related

- [Panadapter Layout overview](overview.md)
- [Split panadapter area side-by-side](split-panadapter-area-side-by-side.md)
- [Preview and pick among the 10 layout variants](preview-and-pick-among-the-10-layout-variants.md)
