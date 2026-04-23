# Search Memories by Name

Use the Search field in the Memory Channels dialog to filter the memory table down to entries whose names match what you type. This is useful when you have a large number of stored channels and want to find one quickly.

## Before you start

- AetherSDR must be connected to the radio. The Memory Channels dialog requires an active radio connection.
- Open the dialog via `Settings > Memory...`.

## Steps

1. Open `Settings > Memory...`.
2. Click the **Search:** field at the top of the dialog.
3. Type part or all of the memory name you are looking for. The table filters as you type.
4. To confirm the selection and tune to the first matching result, press **Enter**.
5. To clear the search and show all memories again, click the clear button inside the **Search:** field.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| **Search:** | Filters the memory table to rows whose name matches the typed text. | Has a clear button. Pressing Enter activates the currently highlighted row. |
| Memory table | Displays the filtered set of memories. | Columns include Group, Owner, Frequency, Name, Mode, and others. |

## Tips

- The table updates on every keystroke; you do not need to press Enter to see filtered results.
- Pressing Enter after typing tunes the active slice to the currently highlighted memory row, equivalent to clicking **Tune**.
- To narrow results further after searching by name, use the **Profile:** combo box to additionally filter by profile.

## Related

- [Memory Channels overview](overview.md)
- [Filter memories by profile](filter-memories-by-profile.md)
- [Tune the radio to a stored memory](tune-the-radio-to-a-stored-memory.md)
- [Sort memory table by column header](sort-memory-table-by-column-header.md)
