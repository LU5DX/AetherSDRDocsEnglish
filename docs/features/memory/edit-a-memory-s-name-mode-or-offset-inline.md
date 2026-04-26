# Edit a memory's name, mode or offset inline

The Memory Channels dialog lets you change any field of a stored memory — including its name, mode, repeater offset, and more — without leaving the table. Use this when you need to correct or update a memory after it was added.

## Before you start

- AetherSDR must be connected to the radio. The Memory Channels dialog requires an active radio connection.
- The memory you want to edit must already exist in the table. To create a new memory, see [Add a memory at current frequency](add-a-memory-at-current-frequency.md).

## Steps

1. Open `Settings > Memory...`.
2. In the memory table, click the row you want to edit to select it.
3. Click `Edit`. The row enters inline-edit mode and its cells become editable.
4. Click the cell you want to change — for example, the **Name**, **Mode**, or **Repeater Offset** column — and type the new value.
5. Press Enter or click another cell to confirm each change.
6. To finish editing, click any other row or press Escape.

## What each control does

| Control | Description |
|---|---|
| Memory table | Displays all memory rows. Columns: Group, Owner, Frequency, Name, Mode, Step, FM TX Offset Dir, Repeater Offset, Tone Mode, Tone Value, Squelch, Squelch Level, RX Filter Low, RX Filter High, RTTY Mark, RTTY Shift, DIGL Offset, DIGU Offset. Inline editing is enabled after clicking `Edit`. |
| `Edit` | Enters inline-edit mode for the selected row. |
| `Search:` | Filters the table by memory name. Use this to locate a memory before editing. Has a clear button; press Enter to apply. |
| `Profile:` | Filters the table by active global profile. |

## Tips

- You can also enter inline-edit mode using the keyboard after selecting a row, consistent with the table's keyboard-driven edit mode.
- Double-clicking a row tunes the radio to that memory rather than opening it for editing. To edit, use the `Edit` button.
- Use `Search:` to narrow down the table before selecting a row to edit, especially if you have many memories stored.

## Troubleshooting

- **`Edit` has no effect** — Make sure exactly one row is selected before clicking `Edit`. If no row is selected, the button will not enter edit mode.
- **Changes do not appear to save** — The dialog requires an active radio connection. If the connection dropped, reconnect and re-enter the value.

## Related

- [Add a memory at current frequency](add-a-memory-at-current-frequency.md)
- [Search memories by name](search-memories-by-name.md)
- [Filter memories by profile](filter-memories-by-profile.md)
- [Sort memory table by column header](sort-memory-table-by-column-header.md)
- [Delete one or more memories](delete-one-or-more-memories.md)
