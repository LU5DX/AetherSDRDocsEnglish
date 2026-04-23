# Split panadapter area side-by-side

Use this page to divide the panadapter area into two panels displayed left and right. The side-by-side layout (A | B) gives each panadapter equal horizontal space.

## Before you start

- AetherSDR must be connected to a Flex radio. The layout dialog requires an active radio connection.
- Your radio license must support at least 2 panadapters. Layout buttons for pan counts exceeding your radio's maximum are disabled automatically.

## Steps

1. Right-click anywhere in the panadapter area to open the **Panadapter Layout** dialog.
2. Click the preview tile labeled **A | B (2 pans)**. The tile shows two equal cells side by side.
3. The dialog closes immediately and the panadapter area splits into two side-by-side panels.

To cancel without changing the layout, click **Cancel**.

## What each control does

| Control | Description | Setting key |
|---|---|---|
| **A | B (2 pans)** layout button | Applies the two-panel side-by-side arrangement (`2h`). Clicking it confirms the selection and closes the dialog. | `PanLayout` |
| Other layout buttons | Apply a different arrangement. Buttons for layouts requiring more panadapters than the radio supports are disabled. | `PanLayout` |
| **Cancel** | Closes the dialog without changing the current layout. | — |

## Tips

- The currently active layout tile is highlighted with a distinct border so you can see which arrangement is in effect before making a change.
- If the **A | B (2 pans)** tile appears dimmed and cannot be clicked, your radio connection does not support 2 panadapters. Check your radio's slice and panadapter limits.

## Related

- [Panadapter Layout overview](overview.md)
- [Switch to a single full-width panadapter](switch-to-a-single-full-width-panadapter.md)
- [Arrange a 2x2 grid of panadapters](arrange-a-2x2-grid-of-panadapters.md)
- [Preview and pick among the 10 layout variants](preview-and-pick-among-the-10-layout-variants.md)
