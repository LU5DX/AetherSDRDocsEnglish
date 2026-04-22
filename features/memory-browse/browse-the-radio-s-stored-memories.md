# Browse the Radio's Stored Memories

The Memory Browser is a read-only side panel that lists all memories stored on the radio. Use it to survey what is stored, see frequencies and names at a glance, and jump to or activate any entry.

## Before you start

- AetherSDR must be connected to the radio. The Memory Browser requires an active radio connection.
- Memories must already be configured on the radio. If none exist, the panel displays "No memories are available yet." instead of a list.
- Memory browsing must be enabled so the panel appears in the main window. See [Memory Browser overview](overview.md) for how to enable it.

## Steps

1. Open `Settings > Memory...` to verify that memories are configured on the radio.
2. Close the dialog. The Memory Browser panel appears as a side panel next to the panadapter when memory browsing is enabled.
3. Scroll the memory table to find the entry you want. Columns are **Frequency** and **Name**.
4. Tune your VFO. The row closest to your current tuned frequency is highlighted automatically, and the table scrolls to keep that row visible.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| Memory table | Lists all stored memories with a valid frequency. Rows are sorted by frequency, low to high. | Columns: Frequency (MHz, 6 decimal places), Name. Names long enough to overflow are truncated with an ellipsis. |
| Highlighted row | Marks the memory whose frequency is nearest to the current tuned frequency. Updates as you tune. | Only one row is highlighted at a time. |
| "No memories are available yet." | Shown in place of the table when the radio has no memories loaded. | The table is hidden while this indicator is visible. |

## Tips

- A memory's **Name** column shows the memory name if set, the group name if no memory name is set, or "Memory N" (where N is the index) if neither is set.
- Memories with a frequency of zero are excluded from the table entirely.
- The highlighted row scrolls into the center of the visible area automatically when tuning changes the closest match.

## Related

- [Memory Browser overview](overview.md)
- [Jump to the memory closest to the current frequency](jump-to-the-memory-closest-to-the-current-frequency.md)
- [Activate a memory with a single double-click](activate-a-memory-with-a-single-double-click.md)
