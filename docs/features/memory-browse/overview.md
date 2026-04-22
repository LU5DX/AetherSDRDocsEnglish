# Memory Browser overview

The Memory Browser is a read-only side panel that lists the stored memories from your connected FLEX-8600 radio alongside the panadapter. It automatically highlights the memory closest to your current tuned frequency and lets you jump to any memory with a double-click or Enter key.

## Before you start

- AetherSDR must be connected to a radio. The Memory Browser requires an active radio connection.
- Your radio must have memories configured. Use `Settings > Memory...` to open the memory configuration dialog if no memories appear.

## How it works

The Memory Browser sits as a side panel in the main window when memory browsing is enabled. It has no tray button or separate window mode.

When memories are loaded, the panel displays them in a two-column table sorted by frequency in ascending order. As you tune, the panel continuously compares your current frequency against all stored memories and highlights the row belonging to the closest match. The panel scrolls automatically to keep that highlighted row visible.

If the radio has no memories loaded, the table is hidden and the panel shows the message "No memories are available yet." in its place.

Entries with no frequency value are excluded from the list entirely.

When a memory name is not set, the panel falls back to showing the memory's group name. If neither is set, it displays the memory's index number in the form `Memory N`.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| Memory table | List | Displays all memories with a valid frequency. Columns are **Frequency** (MHz, 6 decimal places) and **Name**. Double-click a row, or select it and press Enter, to activate that memory. The table is sorted by frequency, ascending. |
| Highlighted row | Indicator | The row whose frequency is closest to the current tuned frequency is highlighted. The panel scrolls to keep this row centered. |
| "No memories are available yet." | Indicator | Shown in place of the table when the radio has no memories with a valid frequency. |

The Memory Browser has no persisted settings of its own.

## Tips

- Hovering over a truncated **Frequency** or **Name** cell shows the full value in a tooltip.
- If two memories are equidistant from the current frequency, the one with the lower index number is highlighted.

## Related

- [Browse the radio's stored memories](browse-the-radio-s-stored-memories.md)
- [Jump to the memory closest to the current frequency](jump-to-the-memory-closest-to-the-current-frequency.md)
- [Activate a memory with a single double-click](activate-a-memory-with-a-single-double-click.md)
