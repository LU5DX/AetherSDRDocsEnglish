# Browse the Radio's Stored Memories

The Memory Browser is a side panel that lists all memories stored on the connected FLEX-8600. Use it to scan stored frequencies at a glance, quickly tune to any entry, or save the current slice as a new memory.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The Memory Browser requires an active radio connection.
- At least one memory must be stored on the radio. If none exist, the panel shows "No memories are available yet." and the table is not displayed.
- Memory browsing must be enabled so the panel appears in the main window. See `Settings > Memory...` to configure memory options.

## Steps

1. Open the Memory Browser side panel. It appears docked in the main window splitter when memory browsing is enabled.
2. Review the memory table. Columns are **Frequency** (in MHz, six decimal places) and **Name**.
3. Scroll through the list. Memories are sorted by frequency in ascending order. Entries with the same frequency are ordered by their internal index.
4. Note the highlighted row. The row highlighted in a distinct background color is the memory whose frequency is closest to the current tuned frequency.
5. To activate a memory, double-click its row, or select it and press Enter.
6. To save the current slice as a new memory, click **Add Memory** at the bottom of the panel.

## What each control does

| Control                          | Behavior                                                                                                     | Notes                                                                                                                          |
|----------------------------------|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Memory table                     | Shows each memory sorted by frequency; single-click or Enter to activate the tuned slice to that memory.     | Columns: Frequency, Name. Closest memory to current tuning is highlighted with a distinct background. Double-click also tunes. |
| Highlighted row                  | Marks the memory closest to the current tuned frequency. The panel scrolls automatically to keep it visible. | Updated whenever the tuned frequency changes.                                                                                  |
| "No memories are available yet." | Shown in place of the table when the radio has no memories loaded.                                           | Disappears once memories are available.                                                                                        |
| Add Memory                       | Saves the current slice as a new memory entry. Anchored at the bottom of the panel, always visible.          | Added in v26.5.1 (#2533). Replaces earlier slice-letter badge variant.                                                         |

## Tips

- The **Name** column shows the memory's name if set. If no name is set but a group is assigned, the group name is shown instead. If neither is set, the entry appears as "Memory" followed by its index number.
- Memories with a frequency of 0 or unset are excluded from the table entirely.
- Long names and frequencies that exceed column width are truncated with an ellipsis. Hover over any cell to see the full value in a tooltip.
- The **Add Memory** button stays visible regardless of how far you scroll in the memory table.
- The Memory Browser panel and its controls now use the active theme's color scheme. Panel, table, header, scrollbar, label, and button colors are defined by the theme rather than hardcoded values. Custom theme files can adjust the appearance via theme parameters such as `color.background.0`, `color.background.1`, `color.background.2`, `color.text.primary`, `color.text.label`, and `color.accent.dim`.

## Related

- [Memory Browser overview](overview.md)
- [Activate a memory with a single double-click](activate-a-memory-with-a-single-double-click.md)
- [Jump to the memory closest to the current frequency](jump-to-the-memory-closest-to-the-current-frequency.md)
- Save the current slice as a memory