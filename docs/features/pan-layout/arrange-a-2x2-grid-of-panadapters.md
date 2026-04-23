# Arrange a 2x2 grid of panadapters

Use the Panadapter Layout dialog to display four panadapters arranged in two rows and two columns. This layout is useful when you want to monitor four separate slices or bands simultaneously.

## Before you start

- AetherSDR must be connected to a Flex radio. The layout dialog requires an active radio connection.
- Your radio configuration must support at least four panadapters. Layout options requiring more panadapters than your radio allows are disabled in the dialog.

## Steps

1. Right-click anywhere in the panadapter area to open the **Panadapter Layout** dialog.
2. Locate the preview tile labeled **A|B / C|D (4 pans)**.
3. Click that tile. The dialog closes immediately and the panadapter area switches to the 2×2 grid arrangement.

## What each control does

| Control | Description | Setting key |
|---|---|---|
| Layout buttons | Preview tiles representing each available arrangement. Click a tile to apply it and close the dialog. Tiles requiring more panadapters than the radio supports are shown disabled. | `PanLayout` |
| Cancel | Closes the dialog without changing the current layout. | — |

The 2×2 layout is stored as value `2x2` in `PanLayout`.

## Tips

- The currently active layout tile is highlighted with a distinct border in the dialog, so you can see your starting point before making a change.
- If the **A|B / C|D (4 pans)** tile appears dimmed and cannot be clicked, your radio does not support four simultaneous panadapters. Check your radio's slice and panadapter limits.

## Troubleshooting

- **The 2×2 tile is greyed out and cannot be clicked** — The radio connection does not support four panadapters at once. The dialog limits available layouts to those within the radio's panadapter count. Verify your Flex radio's current configuration.
- **Right-clicking the panadapter area does nothing** — AetherSDR is not connected to a radio. Establish a connection via `Settings > Connect to Radio...` first.

## Related

- [Panadapter Layout overview](overview.md)
- [Preview and pick among the 10 layout variants](preview-and-pick-among-the-10-layout-variants.md)
- [Split panadapter area side-by-side](split-panadapter-area-side-by-side.md)
- [Switch to a single full-width panadapter](switch-to-a-single-full-width-panadapter.md)
