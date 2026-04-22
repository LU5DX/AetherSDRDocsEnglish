# Panadapter Layout Overview

The Panadapter Layout feature controls how many panadapters are displayed and how they are arranged on screen. Use it to match your operating style — from a single full-width view to an eight-panadapter grid.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. Layout buttons for arrangements requiring more panadapters than the radio supports are disabled.

## How it works

Right-click on the panadapter area to open the **Panadapter Layout** dialog. The dialog presents a grid of thumbnail previews, each showing a labelled arrangement of lettered cells (A, B, C, and so on). The currently active layout is highlighted with a teal border.

Click any enabled thumbnail to apply that layout immediately. The dialog closes and AetherSDR rearranges the panadapter area. Click **Cancel** to close the dialog without making a change.

The chosen layout is persisted as `PanLayout`.

Thumbnails for arrangements that exceed the number of panadapters your radio supports are shown with a dimmed appearance and cannot be selected.

## What each control does

| Control | Description | Layouts available | Persisted setting |
|---|---|---|---|
| Layout buttons | Preview tiles — click one to apply that arrangement. | `1`, `2v`, `2h`, `2h1`, `12h`, `3v`, `2x2`, `4v`, `3h2`, `2x3`, `4h3`, `2x4` | `PanLayout` |
| **Cancel** | Closes the dialog without changing the current layout. | — | — |

The available arrangements are:

| Layout ID | Label | Panadapter count |
|---|---|---|
| `1` | Single | 1 |
| `2v` | A / B | 2 |
| `2h` | A \| B | 2 |
| `2h1` | A\|B / C | 3 |
| `12h` | A / B\|C | 3 |
| `3v` | A / B / C | 3 |
| `2x2` | A\|B / C\|D | 4 |
| `4v` | A/B/C/D | 4 |
| `3h2` | A\|B\|C / D\|E | 5 |
| `2x3` | A\|B / C\|D / E\|F | 6 |
| `4h3` | A\|B\|C\|D / E\|F\|G | 7 |
| `2x4` | A\|B / C\|D / E\|F / G\|H | 8 |

## Tips

- Each thumbnail label shows the pan count, for example "A\|B / C (3 pans)", so you can confirm the count before clicking.
- Layouts requiring more panadapters than the radio provides are disabled and show a forbidden cursor on hover. Connect to a radio that supports the desired number of panadapters to enable them.

## Related

- [Switch to a single full-width panadapter](switch-to-a-single-full-width-panadapter.md)
- [Split panadapter area side-by-side](split-panadapter-area-side-by-side.md)
- [Arrange a 2x2 grid of panadapters](arrange-a-2x2-grid-of-panadapters.md)
- [Preview and pick among the 10 layout variants](preview-and-pick-among-the-10-layout-variants.md)
