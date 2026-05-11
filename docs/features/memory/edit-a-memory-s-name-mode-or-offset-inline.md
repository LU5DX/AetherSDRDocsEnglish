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

| Control                     | Column(s) affected                                                                                                                                                                                                                                                                                                 | Notes                                                                                                                                                   |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Search:**                 | —                                                                                                                                                                                                                                                                                                                  | Filters the table by memory name. Has clear button; Enter submits. Ctrl+F focuses the search field.                                                     |
| **Profile:**                | —                                                                                                                                                                                                                                                                                                                  | Filters by active global or transmit profile. Collects profile names from RadioModel global profiles and transmit profiles.                             |
| Memory table                | Group, Owner, Frequency, Name, Mode, Step, FM TX Offset Dir, Repeater Offset, Tone Mode, Tone Value, Squelch, Squelch Level, RX Filter Low, RX Filter High, RTTY Mark, RTTY Shift, DIGL Offset, DIGU Offset                                                                                                       | ExtendedSelection; inline-edit mode via Edit button or F2/Ctrl+E. Delete/Backspace removes selected rows. Double-click tunes. Ctrl+Shift+A selects all. Sortable by clicking column headers (Frequency, Name, Mode). |
| **Import...**               | —                                                                                                                                                                                                                                                                                                                  | Imports memories from a CSV file with progress dialog. Shows import progress and a summary with any skipped rows.                                       |
| **Export...**               | —                                                                                                                                                                                                                                                                                                                  | Exports selected (or filtered) memories to CSV. Validates generated CSV before saving.                                                                  |
| **Add**                     | —                                                                                                                                                                                                                                                                                                                  | Creates a new memory from the current (active) slice. Ctrl+N shortcut.                                                                                  |
| **Edit**                    | —                                                                                                                                                                                                                                                                                                                  | Enters inline-edit mode on the selected memory's Name field. F2 or Ctrl+E also triggers edit. Only enabled when exactly one memory is selected.         |
| **Tune**                    | —                                                                                                                                                                                                                                                                                                                  | Tunes the active slice to the selected memory. Only enabled when exactly one memory is selected.                                                        |
| **Select All**              | —                                                                                                                                                                                                                                                                                                                  | Selects every visible row (respecting search/filter). Ctrl+Shift+A shortcut.                                                                            |
| **Remove**                  | —                                                                                                                                                                                                                                                                                                                  | Deletes selected memories (with confirmation). Shows progress for batch removal. Delete/Backspace key also triggers. Button label changes to 'Remove Selected' when >1 row selected. |
| Title bar — Memory Channels | —                                                                                                                                                                                                                                                                                                                  | Frameless 18 px gradient title bar with grip glyph on the left and the dialog title. Added in v26.5.1 (#2509). Uses FramelessWindowTitleBar; 8-axis resize via FramelessResizer. |
| — (Minimize)                | —                                                                                                                                                                                                                                                                                                                  | Minimizes the dialog.                                                                                                                                   |
| □ (Maximize)                | —                                                                                                                                                                                                                                                                                                                  | Maximizes or restores the dialog.                                                                                                                        |
| × (Close)                   | —                                                                                                                                                                                                                                                                                                                  | Closes the dialog. Escape clears search first, then closes.                                                                                             |
| Drag-to-move                | —                                                                                                                                                                                                                                                                                                                  | Click and drag the title bar to move the dialog. Double-click the title bar to toggle maximize/restore.                                                 |
| 8-axis resize               | —                                                                                                                                                                                                                                                                                                                  | Click and drag any edge or corner of the dialog to resize. Cursor changes to indicate the resize direction. 12 px resize hit zone via FramelessResizer. |
| Selection count             | —                                                                                                                                                                                                                                                                                                                  | Shows '<N> of <M> selected'.                                                                                                                            |

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