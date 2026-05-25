# Recall an FM Repeater Memory and Restore Offset and CTCSS Tone

Open a saved FM repeater memory and tune the active slice to it, restoring the stored receive frequency, transmit offset direction, repeater offset, and CTCSS tone value in a single operation.

## Before you start

- AetherSDR must be connected to the radio. Memory Channels requires an active radio connection.
- The repeater memory must already exist in the memory table with its FM TX Offset Dir, Repeater Offset, Tone Mode, and Tone Value columns filled in. If it does not, see [Add a memory at current frequency](add-a-memory-at-current-frequency.md) and [Edit a memory's name, mode or offset inline](edit-a-memory-s-name-mode-or-offset-inline.md).
- At least one slice must be active on the radio.

## Steps

1. Open `Settings > Memory...`.
2. Locate the repeater memory. If the list is long, type part of the memory name in the **Search:** field and press Enter to filter the table.
3. Click the row for the repeater memory to select it.
4. Click **Tune**.

The active slice tunes to the stored frequency. The radio restores the mode, FM TX Offset Dir, Repeater Offset, Tone Mode, and Tone Value from the memory row.

Alternatively, double-click the row to tune without using the **Tune** button.

## What each control does

| Control                             | Purpose                                                                                                     | Notes                                                                                       |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| **Search:**                         | Filters the table by memory name.                                                                           | Has a clear button; press Enter to jump to the first match. Ctrl+F focuses the search field.|
| **Profile:**                        | Narrows the table to memories belonging to the selected global or transmit profile.                         | Collects profile names from RadioModel global profiles and transmit profiles.               |
| **Memory table — FM TX Offset Dir** | Stores the transmit offset direction (e.g. minus, plus, simplex).                                           | Column 7 in the table. Restored when you tune.                                              |
| **Memory table — Repeater Offset**  | Stores the offset frequency in MHz.                                                                         | Column 8 in the table. Restored when you tune.                                              |
| **Memory table — Tone Mode**        | Stores the CTCSS/DCS mode (e.g. CTCSS tone encode).                                                         | Column 9 in the table. Restored when you tune.                                              |
| **Memory table — Tone Value**       | Stores the CTCSS tone frequency or DCS code.                                                                | Column 10 in the table. Restored when you tune.                                             |
| **Import...**                       | Imports memories from a CSV file with progress dialog.                                                      | Shows import progress and a summary with any skipped rows.                                  |
| **Export...**                       | Exports selected (or filtered) memories to CSV.                                                             | Validates generated CSV before saving.                                                      |
| **Add**                             | Creates a new memory from the current (active) slice.                                                       | Ctrl+N shortcut. The slice-letter badge variant was dropped; adding always targets the active slice. |
| **Edit**                            | Enters inline-edit mode on the selected memory's Name field.                                                | F2 or Ctrl+E also triggers edit. Only enabled when exactly one memory is selected.          |
| **Tune**                            | Tunes the active slice to the selected memory, restoring all stored fields.                                 | One row must be selected. Double-clicking a row has the same effect.                        |
| **Select All**                      | Selects every visible row (respecting search/filter).                                                       | Ctrl+Shift+A shortcut.                                                                      |
| **Remove**                          | Deletes selected memories (with confirmation). Shows progress for batch removal.                            | Delete/Backspace key also triggers. Button label changes to 'Remove Selected' when >1 row selected. |
| Title bar — Memory Channels         | Frameless 18 px gradient title bar with grip glyph on the left and the dialog title.                        | Drag-to-move; double-click to toggle maximize/restore.                                      |
| — (Minimize)                        | Minimizes the dialog.                                                                                       |                                                                                             |
| □ (Maximize)                        | Maximizes or restores the dialog.                                                                           |                                                                                             |
| × (Close)                           | Closes the dialog. Escape clears search first, then closes.                                                 |                                                                                             |
| Drag-to-move                        | Click and drag the title bar to move the dialog.                                                            | Double-click the title bar to toggle maximize/restore.                                      |
| 8-axis resize                       | Click and drag any edge or corner of the dialog to resize. Cursor changes to indicate the resize direction. | 12 px resize hit zone.                                                                      |
| Selection count                     | Shows '<N> of <M> selected'.                                                                                |                                                                                             |

## Tips

- If your repeater memories are mixed with other entries, use **Profile:** to filter by a group dedicated to repeaters so the target row is easier to spot.
- You can sort the table by any sortable column — for example, Frequency — by clicking the column header. This can help you find a repeater by its output frequency. See [Sort memory table by column header](sort-memory-table-by-column-header.md).
- Press Ctrl+Shift+A to quickly select all visible memories matching your search or profile filter.
- Press Ctrl+N to add a new memory from the active slice without using the mouse.

## Troubleshooting

- **Tune is greyed out** — No row is selected. Click a row in the memory table first, then click **Tune**.
- **The repeater offset or tone is not applied after tuning** — The FM TX Offset Dir, Repeater Offset, Tone Mode, or Tone Value columns may be empty for that memory. Select the row, click **Edit**, fill in the missing columns, and tune again. See [Edit a memory's name, mode or offset inline](edit-a-memory-s-name-mode-or-offset-inline.md).
- **The expected memory does not appear in the table** — Check the **Profile:** filter. If a profile other than the one containing the repeater memory is selected, the row will be hidden. Set **Profile:** to the correct profile or clear the filter.
- **Add button does not create the expected memory** — The **Add** button now always targets the active slice. Ensure the correct slice is active before clicking Add.

## Related

- [Add a memory at current frequency](add-a-memory-at-current-frequency.md)
- [Edit a memory's name, mode or offset inline](edit-a-memory-s-name-mode-or-offset-inline.md)
- [Tune the radio to a stored memory](tune-the-radio-to-a-stored-memory.md)
- [Search memories by name](search-memories-by-name.md)
- [Filter memories by profile](filter-memories-by-profile.md)
- [Sort memory table by column header](sort-memory-table-by-column-header.md)
- Import memories from CSV
- Export memories to CSV
- Remove memories