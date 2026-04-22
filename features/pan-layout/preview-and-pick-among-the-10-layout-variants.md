# Preview and pick among the 10 layout variants

The Panadapter Layout dialog shows thumbnail previews of all available panadapter arrangements so you can compare them at a glance and switch with a single click. Use it whenever you want to change how many panadapters are visible and how they are arranged.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The dialog requires an active radio connection.
- The number of selectable layouts depends on how many panadapters your radio license supports. Layouts requiring more panadapters than your maximum are shown but cannot be selected.

## Steps

1. Right-click anywhere on the panadapter area to open the context menu.
2. Select the panadapter layout option from the context menu. The "Panadapter Layout" dialog opens.
3. Examine the thumbnail tiles. Each tile shows a miniature preview of the arrangement with lettered cells (A, B, C, …) and a label such as `A|B / C (3 pans)`. The currently active layout is highlighted with a blue border.
4. Click the thumbnail tile for the layout you want. The dialog closes immediately and the new layout is applied. The selection is saved to `PanLayout`.
5. To leave the layout unchanged, click "Cancel".

## What each control does

| Control | Description | Valid values | Persisted key |
|---|---|---|---|
| Layout buttons | Thumbnail tiles, one per arrangement. Click a tile to apply that layout and close the dialog. Tiles for layouts exceeding your radio's panadapter count are disabled. | `1`, `2v`, `2h`, `2h1`, `12h`, `2x2`, `3h2`, `2x3`, `4h3`, `2x4` | `PanLayout` |
| Cancel | Closes the dialog without changing the current layout. | — | — |

The 10 layouts and their pan counts are:

| Layout ID | Label | Pans |
|---|---|---|
| `1` | Single | 1 |
| `2v` | A / B | 2 |
| `2h` | A \| B | 2 |
| `2h1` | A\|B / C | 3 |
| `12h` | A / B\|C | 3 |
| `2x2` | A\|B / C\|D | 4 |
| `3h2` | A\|B\|C / D\|E | 5 |
| `2x3` | A\|B / C\|D / E\|F | 6 |
| `4h3` | A\|B\|C\|D / E\|F\|G | 7 |
| `2x4` | A\|B / C\|D / E\|F / G\|H | 8 |

## Tips

- The currently active layout tile has a distinct highlight so you can confirm your starting point before making a change.
- Disabled tiles display a dimmed thumbnail and a forbidden cursor. To unlock them, you need a radio license that supports a higher panadapter count.

## Related

- [Panadapter Layout overview](overview.md)
- [Switch to a single full-width panadapter](switch-to-a-single-full-width-panadapter.md)
- [Split panadapter area side-by-side](split-panadapter-area-side-by-side.md)
- [Arrange a 2x2 grid of panadapters](arrange-a-2x2-grid-of-panadapters.md)
