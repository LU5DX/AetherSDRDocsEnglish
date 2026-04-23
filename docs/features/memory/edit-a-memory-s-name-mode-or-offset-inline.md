# Edit a memory's name, mode or offset inline

The Memory Channels dialog lets you edit any field of a stored memory — including its name, mode, repeater offset, and more — directly in the table without opening a separate form.

## Before you start

- AetherSDR must be connected to the radio. The Memory Channels dialog requires an active radio connection.
- The memory you want to edit must already exist in the table. To create one first, see [Add a memory at current frequency](add-a-memory-at-current-frequency.md).

## Steps

1. Open `Settings > Memory...`.
2. In the memory table, click the row you want to edit to select it.
3. Click **Edit**. The selected row enters inline-edit mode and its cells become editable.
4. Click the cell you want to change — for example, the **Name**, **Mode**, or **Repeater Offset** column — and type the new value.
5. Press Enter or click another cell to confirm each change.
6. Repeat for any other cells in the same row.
7. Click outside the row or select a different row to finish editing.

## What each control does

| Control | Description |
|---|---|
| **Edit** | Enters inline-edit mode on the currently selected memory row. |
| **Search:** text field | Filters the table by memory name. Use this to locate the row you want before editing. Has a clear button; press Enter to apply. |
| **Profile:** combo box | Filters the table to show only memories belonging to the selected global profile. Narrow the list here if the table is long. |
| Memory table | Displays all memory rows. Editable columns include: Group, Owner, Frequency, Name, Mode, Step, FM TX Offset Dir, Repeater Offset, Tone Mode, Tone Value, Squelch, Squelch Level, RX Filter Low, RX Filter High, RTTY Mark, RTTY Shift, DIGL Offset, DIGU Offset. |

## Tips

- You can also use the keyboard to navigate between cells while in inline-edit mode.
- To locate a memory quickly before editing, type part of its name into the **Search:** field. The table filters as you type.

## Troubleshooting

- **Edit does nothing when clicked** — No row is selected. Click a row in the table to select it, then click **Edit**.
- **Changes do not appear to save** — Confirm each cell change by pressing Enter before moving to a different row. Clicking away without confirming may discard the in-progress edit.

## Related

- [Add a memory at current frequency](add-a-memory-at-current-frequency.md)
- [Search memories by name](search-memories-by-name.md)
- [Filter memories by profile](filter-memories-by-profile.md)
- [Sort memory table by column header](sort-memory-table-by-column-header.md)
- [Tune the radio to a stored memory](tune-the-radio-to-a-stored-memory.md)
- [Delete one or more memories](delete-one-or-more-memories.md)
