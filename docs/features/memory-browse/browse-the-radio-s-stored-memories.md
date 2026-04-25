# Browse the Radio's Stored Memories

The Memory Browser is a read-only side panel that lists all memories stored on the connected FLEX-8600. Use it to see your saved frequencies at a glance and to navigate to any memory directly from the panadapter view.

## Before you start

- AetherSDR must be connected to the radio. The Memory Browser requires an active radio connection.
- Memories must already be configured on the radio. If none have been saved, the panel shows "No memories are available yet." and the table does not appear.

## Steps

1. Open `Settings > Memory...` to verify that memory browsing is enabled and that memories are configured.
2. The Memory Browser panel appears as a side panel inside the main window, next to the panadapter. No additional action is needed to open it once memory browsing is enabled.
3. Scroll the memory table to find the entry you want. The table lists all memories with valid frequencies, sorted by frequency in ascending order. Each row shows two columns: **Frequency** (in MHz, six decimal places) and **Name**.
4. To see which memory is closest to your current tuned frequency, look for the highlighted row. The highlighted row indicates the memory whose frequency is nearest to the current VFO frequency. The panel scrolls automatically to keep that row visible.
5. To activate a memory, double-click its row, or select it and press Enter.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| Memory table | Lists all stored memories with valid frequencies. Double-click or press Enter to activate a row. | Columns: **Frequency**, **Name**. Sorted by frequency ascending. |
| Highlighted row | Marks the memory closest to the current tuned frequency. | Updates automatically as you tune. The panel scrolls to keep the highlighted row centered. |
| "No memories are available yet." | Shown in place of the table when the radio has no memories loaded. | The table is hidden until at least one memory with a valid frequency exists. |

## Tips

- If a memory has no name, the panel falls back to its group name. If neither is set, it displays as "Memory" followed by its index number.
- Memories with a frequency of zero or less are excluded from the table entirely.
- The **Frequency** column is fixed at 96 pixels wide. Long names in the **Name** column are truncated with an ellipsis. Hover over a row to see the full name or frequency in a tooltip.

## Related

- [Memory Browser overview](overview.md)
- [Activate a memory with a single double-click](activate-a-memory-with-a-single-double-click.md)
- [Jump to the memory closest to the current frequency](jump-to-the-memory-closest-to-the-current-frequency.md)
