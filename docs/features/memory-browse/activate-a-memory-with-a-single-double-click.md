# Activate a memory with a single double-click

The Memory Browser lets you tune the radio directly to a stored memory by double-clicking its row in the memory table. This is faster than navigating menus or retyping a frequency.

## Before you start

- AetherSDR must be connected to the radio. The Memory Browser requires an active radio connection.
- The memory table must contain at least one entry. If the radio has no memories loaded, the panel shows "No memories are available yet." and there is nothing to activate.

## Steps

1. Open the Memory Browser side panel. It appears alongside the panadapter in the main window when memory browsing is enabled.
2. Locate the memory you want in the memory table. The table lists two columns: **Frequency** and **Name**. The row highlighted in a darker shade is the memory closest to your current tuned frequency.
3. Double-click any row in the memory table to activate that memory.

Alternatively, click once to select a row, then press **Enter** to activate it.

## What each control does

| Control | Behavior |
|---|---|
| Memory table | Lists all stored memories sorted by frequency. Double-click or press Enter on a row to activate that memory. |
| Highlighted row | Indicates the memory closest to the current tuned frequency. Updated automatically as you tune. |
| "No memories are available yet." | Shown in place of the table when the radio has no memories loaded. |

## Tips

- The table sorts entries by frequency, so if you know roughly where a memory sits in the band you can scroll to that area rather than searching by name.
- Long names and frequencies are truncated with an ellipsis if they do not fit. Hover over a cell to see the full value in a tooltip.

## Related

- [Memory Browser overview](overview.md)
- [Browse the radio's stored memories](browse-the-radio-s-stored-memories.md)
- [Jump to the memory closest to the current frequency](jump-to-the-memory-closest-to-the-current-frequency.md)
