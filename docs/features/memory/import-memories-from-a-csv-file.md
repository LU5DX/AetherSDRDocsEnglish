# Memory Channels Dialog

Manage the radio's memory channels — add from the active slice, edit, search, filter by profile, tune, import/export and delete stored frequencies.

## Opening the Dialog

1. Open the Memory Channels dialog: **Settings > Memory...**
2. The dialog opens as a frameless window with its own title bar. Drag the title bar to move the dialog, or drag any edge or corner to resize it.

## Search and Filter

### Search by name

1. Click the **Search:** field.
2. Type text to filter the table by memory name. The table updates as you type.
3. Click the **×** button in the field to clear the search, or press Escape to clear the search before closing the dialog.
4. Press Enter to submit the search, or Ctrl+F to focus the search field.

### Filter by profile

1. Click the **Profile:** combo box.
2. Select a global or transmit profile to filter the table. Select **All Memories** to show every memory.

## Memory Table

The memory table displays all columns of each memory: Group, Owner, Frequency, Name, Mode, Step, FM TX Offset Dir, Repeater Offset, Tone Mode, Tone Value, Squelch, Squelch Level, RX Filter Low, RX Filter High, RTTY Mark, RTTY Shift, DIGL Offset, DIGU Offset.

- Click a column header to sort by that column.
- Double-click a row to tune the active slice to that memory.
- Ctrl+Shift+A selects every visible row (respecting search and filter).
- Delete or Backspace removes selected rows (with confirmation).

### Edit a memory inline

1. Select a single memory row.
2. Click **Edit**, or press F2 or Ctrl+E. The **Name** field enters edit mode.
3. Edit the name and press Enter to commit.
4. To change other fields, click the cell and edit it directly. Fields with constrained values (Mode, Offset Direction, Tone Mode, Tone Value, Step, Group) use combo-box editors that open immediately when you enter edit mode.

## Adding and Tuning

### Add a memory from the active slice

1. Make sure the slice you want to store is the active slice.
2. Click **Add**, or press Ctrl+N. A new memory is created from the active slice's settings. No per-letter selection is needed — the active slice is always used.

### Tune to a memory

1. Select a single memory row.
2. Click **Tune**. The active slice tunes to that memory's frequency.

## Importing and Exporting

### Import memories from a CSV file

Import memory channels you prepared offline or received from another operator into the radio. AetherSDR reads a CSV file and adds every valid row as a new memory entry, showing a progress dialog and a summary of skipped rows.

**Before you start**

- A radio must be connected.
- The CSV file should use the same column layout as an AetherSDR export (Group, Owner, Frequency, Name, Mode, Step, FM TX Offset Dir, Repeater Offset, Tone Mode, Tone Value, Squelch, Squelch Level, RX Filter Low, RX Filter High, RTTY Mark, RTTY Shift, DIGL Offset, DIGU Offset).  
  See [Export memories for backup or sharing](export-memories-for-backup-or-sharing.md) for the exact column header format.

**Steps**

1. Open the Memory Channels dialog: **Settings > Memory...**
2. Click **Import...**
3. In the file picker, locate and select your CSV file, then click Open.
4. Wait for the progress dialog to complete. A summary will show how many memories were imported and list any rows that were skipped (for example, due to an invalid frequency or missing value).

### Export memories to a CSV file

1. Select the memories you want to export. If nothing is selected, all filtered memories are exported.
2. Click **Export...**
3. In the file picker, choose a location and file name, then click Save.
4. AetherSDR validates the generated CSV before saving. If validation fails, fix the issue and try again.

## Deleting Memories

1. Select one or more memory rows.
2. Click **Remove** (the button label changes to **Remove Selected** when more than one row is selected), or press Delete or Backspace.
3. Confirm the deletion. For batch removal, a progress dialog shows the deletion progress.

## Title Bar Controls

- **— (Minimize)**: Minimizes the dialog.
- **□ (Maximize)**: Maximizes or restores the dialog.
- **× (Close)**: Closes the dialog. Escape clears the search first, then closes.
- **Drag-to-move**: Click and drag the title bar to move the dialog. Double-click the title bar to toggle maximize/restore.
- **8-axis resize**: Click and drag any edge or corner of the dialog to resize. The cursor changes to indicate the resize direction.

## Tips

- Sort or filter the memory table after import to verify the new entries. See [Sort memory table by column header](sort-memory-table-by-column-header.md) and [Filter memories by profile](filter-memories-by-profile.md).
- The memory table uses the active theme's background color for alternating rows. The dialog container is styled with the `dialog/memory` theme key.
- The selection count at the bottom shows how many of the total rows are selected.

## Related

- [Export memories for backup or sharing](export-memories-for-backup-or-sharing.md)
- [Add a memory from the active slice](add-a-memory-from-the-active-slice.md)
- [Delete one or more memories](delete-one-or-more-memories.md)