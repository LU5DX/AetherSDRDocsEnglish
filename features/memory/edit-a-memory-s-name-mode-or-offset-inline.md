# Edit a memory's name, mode or offset inline

Use inline editing to change a stored memory's fields — such as its name, mode, repeater offset, or any other column — without leaving the Memory Channels dialog.

## Before you start

- AetherSDR must be connected to the radio. Inline editing requires a live radio connection.
- The Memory Channels dialog must be open. If it is not, go to `Settings > Memory...`.

## Steps

1. Open `Settings > Memory...`.
2. In the memory table, click the row you want to change to select it.
3. Click **Edit**.
4. The selected row enters inline-edit mode. Click the cell you want to change.
5. Type the new value and press Enter to confirm, or press Escape to cancel.
6. Repeat for any other cells in the row you want to update.
7. Click anywhere outside the row, or select a different row, to finish editing.

## What each control does

| Control | Description |
|---|---|
| **Search:** text field | Filters the table to rows whose name matches the typed text. Has a clear button; press Enter to activate. |
| **Profile:** combo box | Filters the table to memories belonging to the selected global profile. |
| Memory table | Displays all memory rows. Columns available for inline editing: Group, Owner, Frequency, Name, Mode, Step, FM TX Offset Dir, Repeater Offset, Tone Mode, Tone Value, Squelch, Squelch Level, RX Filter Low, RX Filter High, RTTY Mark, RTTY Shift, DIGL Offset, DIGU Offset. |
| **Edit** | Enters inline-edit mode on the selected memory row. |

## Tips

- Double-clicking a row tunes the active slice to that memory rather than opening it for editing. To edit, use the **Edit** button instead.
- To locate a specific memory before editing, type its name in the **Search:** field. The table filters as you type.
- You can sort the table by clicking a column header to help find the memory you want before clicking **Edit**. See [Sort memory table by column header](sort-memory-table-by-column-header.md).

## Troubleshooting

- **Edit button has no effect** — Confirm that exactly one row is selected and that AetherSDR is connected to the radio. Inline editing is not available without a live radio connection.
- **Changes do not appear after editing** — Press Enter to confirm a cell value before clicking away. Pressing Escape discards the change.

## Related

- [Add a memory at current frequency](add-a-memory-at-current-frequency.md)
- [Search memories by name](search-memories-by-name.md)
- [Sort memory table by column header](sort-memory-table-by-column-header.md)
- [Tune the radio to a stored memory](tune-the-radio-to-a-stored-memory.md)
