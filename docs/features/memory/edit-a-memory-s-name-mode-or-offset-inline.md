# Edit a memory's name, mode or offset inline

Use this page to change a stored memory's name, mode, repeater offset, or any other field without leaving the Memory Channels dialog.

## Before you start

- AetherSDR must be connected to the radio. The Memory Channels dialog requires an active radio connection.
- At least one memory must already exist in the table. To create one, see [Add a memory at current frequency](add-a-memory-at-current-frequency.md).

## Steps

1. Open `Settings > Memory...`.
2. In the memory table, click the row you want to edit to select it.
3. Click **Edit**.  
   The selected row enters inline-edit mode. The cell that was highlighted becomes editable.
4. Type the new value into the cell.
5. Press **Tab** to move to the next cell, or click another cell in the same row to edit it.
6. When you have finished editing all fields you want to change, press **Enter** or click outside the row to commit the changes.

## What each control does

| Control | Column(s) affected | Notes |
|---|---|---|
| Memory table | All 18 columns | Columns: Group, Owner, Frequency, Name, Mode, Step, FM TX Offset Dir, Repeater Offset, Tone Mode, Tone Value, Squelch, Squelch Level, RX Filter Low, RX Filter High, RTTY Mark, RTTY Shift, DIGL Offset, DIGU Offset. Inline-edit mode is entered via the **Edit** button or keyboard. |
| **Edit** | — | Enters inline-edit mode on the currently selected row. |

## Tips

- You can also enter inline-edit mode using the keyboard after selecting a row, without clicking **Edit**.
- Double-clicking a row tunes the active slice to that memory rather than opening it for editing. Use the **Edit** button when you want to change values, not tune.
- Use the **Search:** field to filter the table by memory name before selecting a row, which is useful when the list is long. See [Search memories by name](search-memories-by-name.md).
- To narrow the table to a specific group before editing, use the **Profile:** combo box. See [Filter memories by profile](filter-memories-by-profile.md).

## Troubleshooting

- **Edit button has no effect** — No row is selected. Click a row in the table first, then click **Edit**.
- **Changes are not saved after typing** — Press **Enter** or click outside the edited cell to commit. Closing the dialog without confirming may discard in-progress edits.
- **Frequency column shows unexpected values after editing** — The Frequency field expects a value in MHz. Verify the format matches the existing entries in the table.

## Related

- [Add a memory at current frequency](add-a-memory-at-current-frequency.md)
- [Tune the radio to a stored memory](tune-the-radio-to-a-stored-memory.md)
- [Search memories by name](search-memories-by-name.md)
- [Filter memories by profile](filter-memories-by-profile.md)
- [Recall an FM repeater memory and restore offset and CTCSS tone](recall-an-fm-repeater-memory-and-restore-offset-and-ctcss-tone.md)
- [Sort memory table by column header](sort-memory-table-by-column-header.md)
- [Delete one or more memories](delete-one-or-more-memories.md)
