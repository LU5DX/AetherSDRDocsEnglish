# Understand the slice capacity warning when adding panadapters

When you request a layout that needs more panadapters than your radio can support, AetherSDR blocks the change and explains why. This page describes what the warning means and how to work within your radio's slice limit.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The Panadapter Layout dialog requires an active radio connection.
- Know how many slices your radio supports. The warning message includes both the model name and the slice count.

## Steps

1. Right-click on the panadapter area to open the **Panadapter Layout** dialog.
2. Inspect the layout grid. Any layout whose panadapter count exceeds the radio's slice limit is rendered with a forbidden cursor and cannot be clicked.
3. If you click a layout button that is within the limit but the radio's slices are already all in use, AetherSDR cancels the change and displays a status-bar message:

   ```
   Slice capacity is full; cannot add another panadapter (<model> supports <N> slices)
   ```

   where `<model>` is your radio model and `<N>` is its slice limit.
4. To proceed, first reduce the number of active slices on the radio, then return to the **Panadapter Layout** dialog and select the desired layout.
5. To close the dialog without making any change, click **Cancel**.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| Layout buttons | Click a preview tile to select an arrangement. The dialog closes and the layout is applied. | Tiles requiring more panadapters than the radio's slice limit show a forbidden cursor and are disabled. If slices are already at capacity when a valid-looking layout is applied, the change is cancelled and the status-bar warning appears instead. Persisted as `PanLayout`. |
| **Cancel** | Closes the dialog without changing the current layout. | No settings are modified. |

## Tips

- Disabled layout tiles tell you at a glance which arrangements are out of reach for your radio. You do not need to attempt them to find out.
- The status-bar warning can appear even for layouts whose tile was not visually disabled, if other software or another client has consumed slices since the dialog opened.
- The currently active layout is highlighted with a distinct border in the grid, so you can always see which arrangement is in effect.

## Troubleshooting

- **A layout tile appears disabled even though the radio should support enough slices** — The dialog calculates the maximum panadapter count from the radio's reported slice limit at the time the dialog opens. If the connection was interrupted or the limit was not yet reported, some tiles may appear disabled incorrectly. Close the dialog, verify the radio connection is active, and reopen it.
- **The status-bar warning appeared but I expected that layout to be allowed** — Another client or an existing slice on the radio may be consuming the remaining capacity. Check for active slices in other SDR clients connected to the same radio, close any that are not needed, then try again.

## Related

- [Panadapter Layout overview](overview.md)
- [Preview and pick among the 10 layout variants](preview-and-pick-among-the-10-layout-variants.md)
- [Switch to a single full-width panadapter](switch-to-a-single-full-width-panadapter.md)
