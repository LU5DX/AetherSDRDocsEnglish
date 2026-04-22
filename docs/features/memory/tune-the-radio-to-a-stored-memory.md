# Tune the Radio to a Stored Memory

Open the Memory Channels dialog to find a stored frequency and send it to the active slice receiver with a single click or double-click.

## Before you start

- AetherSDR must be connected to the radio. The Memory Channels dialog requires an active radio connection.
- At least one memory must already be stored. See [Add a memory at current frequency](add-a-memory-at-current-frequency.md) if your list is empty.

## Steps

1. Click `Settings > Memory...` to open the Memory Channels dialog.
2. Optional: Type a name in the **Search:** field to filter the table, or choose a group from the **Profile:** drop-down to narrow the list.
3. Click the row for the memory you want to tune to. The row highlights and the selection count at the bottom right updates.
4. Click **Tune**. The active slice tunes to the frequency, mode, and filter settings stored in that memory.

Alternatively, double-click any row in the memory table to tune immediately without using the **Tune** button.

## What each control does

| Control | Description |
|---|---|
| **Search:** | Filters the table to rows whose name matches the typed text. Has a clear button; press Enter to confirm. |
| **Profile:** | Filters the table to memories belonging to the selected global profile. |
| Memory table | Shows all stored memories. Columns include Group, Owner, Frequency, Name, Mode, Step, FM TX Offset Dir, Repeater Offset, Tone Mode, Tone Value, Squelch, Squelch Level, RX Filter Low, RX Filter High, RTTY Mark, RTTY Shift, DIGL Offset, and DIGU Offset. Click a column header to sort by that column. |
| **Tune** | Tunes the active slice to the selected memory. |
| Selection count | Displays the number of currently selected rows (shown as `N selected`). |

## Tips

- Double-clicking a row tunes the radio without needing to click **Tune**, which is faster when browsing through memories.
- Use **Search:** to jump to a named memory quickly. The table filters as you type; press Enter to tune the highlighted row.
- Shift-click selects a range of rows. On Linux and Windows, Ctrl-click adds or removes individual rows from the selection. On macOS, use Command-click instead.

## Troubleshooting

- **Tune does nothing** — Verify the radio is connected. The **Tune** button requires an active radio connection. Check the connection status and reconnect via `Settings > Connect to Radio...` if needed.
- **The memory you want is not visible** — A search term or Profile filter may be hiding it. Clear the **Search:** field and set **Profile:** back to its default to show all memories.

## Related

- [Memory Channels overview](overview.md)
- [Add a memory at current frequency](add-a-memory-at-current-frequency.md)
- [Search memories by name](search-memories-by-name.md)
- [Filter memories by profile](filter-memories-by-profile.md)
- [Sort memory table by column header](sort-memory-table-by-column-header.md)
