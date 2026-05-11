# Memory Browser overview

The Memory Browser is a read-only side panel that lists the stored memories from your connected FLEX-8600 radio alongside the panadapter. It automatically highlights the memory closest to your current tuned frequency and lets you jump to any memory with a double-click or Enter key.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The Memory Browser requires an active radio connection.
- Memories must already be configured on the radio. Open `Settings > Memory...` to manage them.

## How it works

The Memory Browser sits as a side panel inside the main window splitter when memory browsing is enabled. It receives the radio's memory list and keeps itself synchronized with your current VFO frequency.

The table lists all memories that have a valid frequency, sorted by frequency in ascending order. Each time your tuned frequency changes, the panel evaluates all memories and highlights the row whose frequency is closest to where you are tuned. The panel then scrolls automatically to keep that highlighted row visible.

When no memories are loaded on the radio, the panel replaces the table with the message "No memories are available yet."

Activating a memory — by double-clicking a row or pressing Enter on a selected row — tunes the radio to that memory's frequency.

## What each control does

| Control                          | Description                                                                                                                                            | Notes                                                                                                                          |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Memory table                     | Shows each memory sorted by frequency; single-click or Enter to activate the tuned slice to that memory.                                               | Columns: Frequency, Name. Closest memory to current tuning is highlighted with a distinct background. Double-click also tunes. |
| Highlighted row                  | The row whose frequency is closest to the currently tuned frequency. The panel scrolls to keep this row centered whenever the tuned frequency changes. |                                                                                                                                |
| "No memories are available yet." | Shown in place of the table when the radio has no memories loaded.                                                                                     |                                                                                                                                |
| Add Memory                       | Saves the current slice as a new memory entry. Anchored at the bottom of the panel, always visible.                                                    | Added in v26.5.1 (#2533). Replaces earlier slice-letter badge variant.                                                         |

## Tips

- The Name column displays the memory's name if one is set, then the group name if no individual name exists, then a generated label of the form `Memory N` as a fallback.
- Long names are truncated with an ellipsis. Hover over any row to see the full frequency or name in a tooltip.
- Memories with a frequency of 0 MHz or below are excluded from the table entirely.
- Click **Add Memory** to save the active slice on the current panadapter as a new memory entry. The button remains visible at the bottom of the panel regardless of scroll position.

## Related

- [Browse the radio's stored memories](browse-the-radio-s-stored-memories.md)
- [Jump to the memory closest to the current frequency](jump-to-the-memory-closest-to-the-current-frequency.md)
- [Activate a memory with a single double-click](activate-a-memory-with-a-single-double-click.md)