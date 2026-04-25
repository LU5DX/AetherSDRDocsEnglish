# Tune the Radio to a Stored Memory

Open the Memory Channels dialog to locate a stored frequency and send it directly to the active slice receiver.

## Before you start

- AetherSDR must be connected to the radio. The Memory Channels dialog requires an active radio connection.
- At least one memory must already be stored. See [Add a memory at current frequency](add-a-memory-at-current-frequency.md) if your list is empty.

## Steps

1. Click `Settings > Memory...` to open the Memory Channels dialog.
2. Optional: Type a name in the **Search:** field to narrow the list, or choose a group from the **Profile:** drop-down to filter by profile.
3. Click the row in the memory table that contains the frequency you want.
4. Click **Tune**.

The active slice tunes immediately to the stored frequency, mode, and filter settings of that memory.

**Shortcut:** Double-click any row in the memory table to tune without clicking **Tune**.

## What each control does

| Control | Description |
|---|---|
| **Search:** | Filters the table to rows whose name matches the text you type. Press Enter or clear the field with the built-in clear button. |
| **Profile:** | Limits the table to memories belonging to the selected global profile. |
| Memory table | Displays all stored memories. Columns: Group, Owner, Frequency, Name, Mode, Step, FM TX Offset Dir, Repeater Offset, Tone Mode, Tone Value, Squelch, Squelch Level, RX Filter Low, RX Filter High, RTTY Mark, RTTY Shift, DIGL Offset, DIGU Offset. |
| **Tune** | Tunes the active slice to the selected memory. Requires exactly one row to be selected. |
| Selection count | Shows how many rows are currently selected (for example, `1 selected`). |

## Tips

- On Linux and Windows, hold Ctrl and click to add or remove individual rows from the selection. On macOS, use Command-click. Only the first selected memory is tuned when you click **Tune**.
- Shift-click selects a contiguous range of rows.
- To find a memory quickly, click a column header to sort by that column, then scroll to the frequency or name you want.

## Troubleshooting

- **Tune is not available** — No row is selected. Click a row in the memory table first.
- **The radio does not change frequency** — Confirm AetherSDR is connected to the radio. A lost connection disables all radio commands.

## Related

- [Add a memory at current frequency](add-a-memory-at-current-frequency.md)
- [Search memories by name](search-memories-by-name.md)
- [Filter memories by profile](filter-memories-by-profile.md)
- [Sort memory table by column header](sort-memory-table-by-column-header.md)
- [Memory Channels overview](overview.md)
