# Browse the Radio's Stored Memories

The Memory Browser is a read-only side panel that lists all memories stored on the connected FLEX-8600, sorted by frequency. Use it to see what memories are available and to jump to or activate a specific one without leaving the panadapter view.

## Before you start

- AetherSDR must be connected to the radio. The Memory Browser requires an active radio connection.
- Memories must already be configured on the radio. If none exist, the panel shows "No memories are available yet."
- Memory browsing must be enabled so the panel appears in the main window. See `Settings > Memory...` to configure memory settings.

## Steps

1. Open `Settings > Memory...` to confirm memory browsing is enabled and that the radio has memories loaded.
2. The Memory Browser panel appears as a side panel next to the panadapter in the main window.
3. Scroll the memory table to review the list. Columns are **Frequency** (in MHz, six decimal places) and **Name**.
4. Observe the highlighted row. The row with a distinct background indicates the memory closest to the current tuned frequency.
5. To activate a memory, double-click its row, or select it and press Enter.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| Memory table | Lists all stored memories with valid frequencies, sorted by frequency ascending. | Columns: Frequency, Name. Single selection only. |
| Highlighted row | Marks the memory whose frequency is closest to the current VFO frequency. | Updates automatically as you tune. The panel scrolls to keep the highlighted row visible. |
| "No memories are available yet." | Shown in place of the table when the radio has no memories loaded or all memories have no valid frequency set. | Disappears once memories become available. |

## Tips

- The Name column displays the memory's name if set, the group name if no individual name is set, or a fallback label in the form `Memory N` if neither is configured.
- Memories with no frequency (zero or unset) are excluded from the list entirely.
- If two memories share the same frequency, the one with the lower index is highlighted as closest.
- The panel is fixed in size and does not resize with the main window.

## Related

- [Memory Browser overview](overview.md)
- [Activate a memory with a single double-click](activate-a-memory-with-a-single-double-click.md)
- [Jump to the memory closest to the current frequency](jump-to-the-memory-closest-to-the-current-frequency.md)
