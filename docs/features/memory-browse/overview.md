# Memory Browser overview

The Memory Browser is a read-only side panel that lists your radio's stored memories alongside the panadapter. As you tune, it automatically highlights the memory closest to your current frequency so you can orient yourself quickly and jump to a stored channel without leaving the main display.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The radio must have at least one memory configured. Use `Settings > Memory...` to manage memories.

## How it works

The Memory Browser appears as a side panel in the main window. When memories are present, the panel displays a two-column table listing every stored memory that has a valid frequency. The table is sorted by frequency, lowest to highest.

As you tune the radio, the panel continuously recalculates which memory is closest to the active frequency and highlights that row. The panel scrolls automatically to keep the highlighted row visible.

When no memories are loaded, the panel shows the message "No memories are available yet." in place of the table.

**Activating a memory:** Double-click any row, or select a row and press Enter, to activate that memory on the radio.

## What each control does

| Control | Description |
|---|---|
| Memory table | Lists all memories with a valid frequency. Columns: Frequency (MHz, 6 decimal places) and Name. Single-selection; read-only. Double-click or press Enter on a row to activate that memory. |
| Highlighted row | Indicates the memory whose frequency is closest to the current tuned frequency. The panel scrolls to keep this row centered. |
| "No memories are available yet." | Shown in place of the table when the radio has no memories with a valid frequency. Disappears automatically once memories are available. |

**Name display:** The Name column shows the memory's name if set, the group name if no memory name is set, or "Memory N" (where N is the memory index) if neither is set.

## Tips

- The highlighted row updates as you tune — you do not need to take any action to refresh it.
- If two memories are equidistant from the current frequency, the one with the lower memory index is highlighted.
- Memories with a frequency of 0 or no frequency set are excluded from the table entirely.

## Related

- [Browse the radio's stored memories](browse-the-radio-s-stored-memories.md)
- [Jump to the memory closest to the current frequency](jump-to-the-memory-closest-to-the-current-frequency.md)
- [Activate a memory with a single double-click](activate-a-memory-with-a-single-double-click.md)
