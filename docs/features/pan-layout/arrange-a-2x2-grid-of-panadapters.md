# Panadapter Layout

Choose how many panadapters are shown and how they are arranged in the panadapter area.

## Before you start

- AetherSDR must be connected to a Flex radio. The layout dialog requires an active radio connection.
- Your radio configuration must support the requested number of panadapters. The dialog limits available layouts to those within the radio's panadapter count.

## Opening the dialog

Right-click anywhere in the panadapter area to open the **Panadapter Layout** dialog.

## Available layouts

The dialog presents preview tiles for the following arrangements:

| Layout value | Visual description |
|---|---|
| `1` | Single full-width panadapter |
| `2v` | Two panadapters stacked vertically |
| `2h` | Two panadapters side-by-side horizontally |
| `2h1` | Two panadapters side-by-side with a third, smaller panadapter below |
| `12h` | One large panadapter with two smaller ones side-by-side below |
| `2x2` | Four panadapters in a 2×2 grid |
| `3h2` | Three panadapters side-by-side with two below |
| `2x3` | Six panadapters in a 2×3 grid |
| `4h3` | Four panadapters side-by-side with three below |
| `2x4` | Eight panadapters in a 2×4 grid |

## What each control does

| Control | Description | Setting key |
|---|---|---|
| Layout buttons | Preview tiles representing each available arrangement. Click a tile to apply it and close the dialog. Tiles requiring more panadapters than the radio supports are shown disabled with a forbidden cursor. | `PanLayout` |
| Cancel | Closes the dialog without changing the current layout. | — |

## Tips

- The currently active layout tile is highlighted with a distinct border in the dialog, so you can see your starting point before making a change.
- If you select a layout requiring more panadapters than the radio's current slice limit allows, a warning appears in the status bar: *"Slice capacity is full; cannot add another panadapter (<model> supports <N> slices)"* and the layout change is cancelled.

## Troubleshooting

- **A tile appears greyed out and cannot be clicked** — The radio connection does not support that many panadapters at once. The dialog limits available layouts to those within the radio's panadapter count. Verify your Flex radio's current configuration.
- **A layout change is applied but the status bar shows a warning** — The radio has reached its slice capacity for the current connection. The layout change is cancelled; try a layout with fewer panadapters.
- **Right-clicking the panadapter area does nothing** — AetherSDR is not connected to a radio. Establish a connection via `Settings > Connect to Radio...` first.

## Related

- [Panadapter Layout overview](overview.md)
- [Split panadapter area side-by-side](split-panadapter-area-side-by-side.md)
- [Switch to a single full-width panadapter](switch-to-a-single-full-width-panadapter.md)