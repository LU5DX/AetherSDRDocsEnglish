# Memory Channels

The Memory Channels dialog (`Settings > Memory...`) manages the radio's stored frequencies — add, edit, search, filter by profile, tune, import, export, and delete memories.

## Controls

| Control | Kind | Behavior |
|---------|------|----------|
| **Search:** | text_field | Filters the table by memory name. Has a clear button; press Enter to submit. Press Ctrl+F to focus the search field. |
| **Profile:** | combo_box | Filters memories by active global or transmit profile. Default is "All Memories". Collects profile names from the radio's global profiles and transmit profiles. |
| **Memory table** | list | Displays and edits memory rows. Sortable by clicking column headers (Frequency, Name, Mode, and others). Columns include: Group, Owner, Frequency, Name, Mode, Step, FM TX Offset Dir, Repeater Offset, Tone Mode, Tone Value, Squelch, Squelch Level, RX Filter Low, RX Filter High, RTTY Mark, RTTY Shift, DIGL Offset, DIGU Offset. Supports ExtendedSelection; inline edit via Edit button or F2/Ctrl+E. Delete/Backspace removes selected rows. Double-click tunes to a memory. Ctrl+Shift+A selects all. |
| **Import...** | push_button | Imports memories from a CSV file. Shows a progress dialog and a summary with any skipped rows. |
| **Export...** | push_button | Exports selected (or filtered) memories to CSV. Validates the generated CSV before saving. |
| **Add** | push_button | Creates a new memory from the current (active) slice. Shortcut: Ctrl+N. |
| **Edit** | push_button | Enters inline edit mode on the selected memory's Name field. Only enabled when exactly one memory is selected. Shortcut: F2 or Ctrl+E. |
| **Tune** | push_button | Tunes the active slice to the selected memory. Only enabled when exactly one memory is selected. |
| **Select All** | push_button | Selects every visible row (respecting search and filter). Shortcut: Ctrl+Shift+A. |
| **Remove** | push_button | Deletes selected memories (with confirmation). Shows progress for batch removal. Button label changes to "Remove Selected" when more than one row is selected. Shortcut: Delete or Backspace. |
| **Title bar — Memory Channels** | indicator | Frameless 18 px gradient title bar with a grip glyph on the left and the dialog title. Added in v26.5.1 (#2509). |
| **— (Minimize)** | push_button | Minimizes the dialog. |
| **□ (Maximize)** | push_button | Maximizes or restores the dialog. |
| **× (Close)** | push_button | Closes the dialog. Press Escape to clear the search field first, then close. |
| **Drag-to-move** | drag_handle | Click and drag the title bar to move the dialog. Double-click the title bar to toggle maximize/restore. |
| **8-axis resize** | drag_handle | Click and drag any edge or corner of the dialog to resize. The cursor changes to indicate the resize direction. The resize hit zone is 12 px wide. |
| **Selection count** | indicator | Shows "<N> of <M> selected". |

### Adding a Memory from a Slice

1. Ensure the desired slice is active (click its slice bar).
2. Click **Add** (or press Ctrl+N).
3. A new row appears in the memory table with the active slice's frequency, mode, and other settings.

**Note:** The per-letter slice selection variant is removed. Adding always targets the active slice.

### Editing a Memory Inline

The memory table supports inline editing for constrained fields (such as Mode, Step, Tone Mode, Offset Direction) through combo-box delegates. When you double-click or press F2 on a constrained cell, a drop-down list appears with valid values. For editable fields, you can type a custom value that is validated by the radio on commit.

1. Select the memory row to edit.
2. Click **Edit** (or press F2 or Ctrl+E) to enter edit mode on the Name field.
3. To edit other fields, double-click the cell or press F2 while the cell is selected.
4. For combo-box fields (Mode, Step, Offset Dir, Tone Mode, Tone Value, Group), the list opens immediately. Select a value or type an editable value.
5. Press Enter to commit the change, or Escape to cancel.

### Tuning to a Memory

1. Select exactly one memory in the table.
2. Click **Tune**. The active slice tunes to the memory's frequency.

**Tip:** Double-click any memory to tune directly without using the Tune button.

### Deleting Memories

1. Select one or more memories (use Ctrl+click for non-contiguous selection, Shift+click for range, or Ctrl+Shift+A to select all visible rows).
2. Click **Remove** (or press Delete or Backspace).
3. Confirm the deletion when prompted. A progress bar appears for batch removals.

### Importing Memories from CSV

1. Click **Import...**.
2. Select a CSV file. A progress dialog shows the import process.
3. Review the summary for any skipped rows.

### Exporting Memories to CSV

1. Select the memories to export, or apply search/filter to limit the set.
2. Click **Export...**.
3. Choose a save location and filename. The exported CSV is validated before saving.

## Sorting the Memory Table

Click any sortable column header to sort the table by that column. Click the same header again to reverse the sort direction.

- The **Frequency** column uses numeric sorting (14.225 sorts between 14.200 and 14.300).
- Sort indicators appear on the header.
- Sorting does not affect the stored index on the radio.
- Search and profile filters remain active while sorting.

## Related

- [Sort Memory Table by Column Header](sort-memory-table-by-column-header.md)
- [Search memories by name](search-memories-by-name.md)
- [Filter memories by profile](filter-memories-by-profile.md)
- [Tune the radio to a stored memory](tune-the-radio-to-a-stored-memory.md)