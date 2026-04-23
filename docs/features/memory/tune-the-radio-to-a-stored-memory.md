# Tune the Radio to a Stored Memory

Open a saved memory channel and retune the active slice to its stored frequency, mode, and filter settings.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The Memory Channels dialog requires an active radio connection.
- At least one memory must already be stored. See [Add a memory at current frequency](add-a-memory-at-current-frequency.md) if the list is empty.

## Steps

1. Click `Settings > Memory...` to open the Memory Channels dialog.
2. Optional: Type a name in the **Search:** field to narrow the list, or select a group from the **Profile:** drop-down to filter by profile.
3. Click the row for the memory you want to tune to. The row highlights and the selection count updates.
4. Click **Tune**.

The active slice retunes to the frequency, mode, and stored filter settings of the selected memory.

**Shortcut:** Double-click any row in the memory table to tune immediately without clicking **Tune**.

## What each control does

| Control | Behavior |
|---|---|
| **Search:** | Filters the table to rows whose name matches the typed text. Press Enter to confirm, or use the clear button to reset. |
| **Profile:** | Filters the table to memories belonging to the selected global profile. |
| Memory table | Displays all stored memories. Columns include Group, Owner, Frequency, Name, Mode, Step, FM TX Offset Dir, Repeater Offset, Tone Mode, Tone Value, Squelch, Squelch Level, RX Filter Low, RX Filter High, RTTY Mark, RTTY Shift, DIGL Offset, and DIGU Offset. Click a column header to sort. |
| **Tune** | Tunes the active slice to the selected memory. Enabled when exactly one row is selected. |

## Tips

- To select a contiguous range of memories, click the first row then Shift-click the last. To add or remove individual rows from a selection, use Ctrl-click (Command-click on macOS). Only the single memory you act on with **Tune** or a double-click is applied to the slice.
- If you know the memory name, type it in **Search:** and press Enter to tune directly from the keyboard without reaching for the mouse.

## Troubleshooting

- **Tune is not available** — No row is selected. Click a row in the table first.
- **The table is empty** — A profile filter may be active. Set **Profile:** back to its unfiltered state, or clear the **Search:** field to show all memories.

## Related

- [Memory Channels overview](overview.md)
- [Add a memory at current frequency](add-a-memory-at-current-frequency.md)
- [Search memories by name](search-memories-by-name.md)
- [Filter memories by profile](filter-memories-by-profile.md)
- [Sort memory table by column header](sort-memory-table-by-column-header.md)
