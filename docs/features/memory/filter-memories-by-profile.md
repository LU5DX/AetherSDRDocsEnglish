# Filter memories by profile

Use the Profile filter in the Memory Channels dialog to narrow the memory table to entries belonging to a specific global profile. This is useful when you have a large memory list and want to see only the channels relevant to your current operating context.

## Before you start

- The radio must be connected. The Memory Channels dialog requires an active radio connection.
- At least one global profile must exist on the radio. The `Profile:` combo box is populated from the radio's active global profiles.

## Steps

1. Open `Settings > Memory...`.
2. Locate the `Profile:` combo box in the filter row at the top of the dialog.
3. Click the `Profile:` combo box and select the profile you want to filter by.
4. The memory table updates immediately to show only entries matching the selected profile.

To clear the filter and show all memories, select the blank or default entry at the top of the `Profile:` combo box.

## What each control does

| Control                     | Behavior                                                                                                                                                                     | Notes                                                                                                                                      |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| `Search:` text field        | Filters the table by memory name.                                                                                                                                            | Has clear button; Enter submits. Ctrl+F focuses the search field.                                                                          |
| `Profile:` combo box        | Filters the memory table by the selected global or transmit profile. Populated from the radio's active global profiles and transmit profiles.                                |                                                                                                                                            |
| Memory table                | Displays and edits memory rows. Sortable by clicking column headers (Frequency, Name, Mode). Columns: Group, Owner, Frequency, Name, Mode, Step, FM TX Offset Dir, Repeater Offset, Tone Mode, Tone Value, Squelch, Squelch Level, RX Filter Low, RX Filter High, RTTY Mark, RTTY Shift, DIGL Offset, DIGU Offset. | ExtendedSelection; inline-edit mode via Edit button or F2/Ctrl+E. Delete/Backspace removes selected rows. Double-click tunes. Ctrl+Shift+A selects all. The table uses theme-aware alternate row colors. |
| `Import...` button          | Imports memories from a CSV file with progress dialog.                                                                                                                       | Shows import progress and a summary with any skipped rows.                                                                                 |
| `Export...` button          | Exports selected (or filtered) memories to CSV.                                                                                                                              | Validates generated CSV before saving.                                                                                                     |
| `Add` button                | Creates a new memory from the current (active) slice.                                                                                                                        | Ctrl+N shortcut.                                                                                                                           |
| `Edit` button               | Enters inline-edit mode on the selected memory's Name field.                                                                                                                 | F2 or Ctrl+E also triggers edit. Only enabled when exactly one memory is selected.                                                         |
| `Tune` button               | Tunes the active slice to the selected memory.                                                                                                                               | Only enabled when exactly one memory is selected.                                                                                          |
| `Select All` button         | Selects every visible row (respecting search/filter).                                                                                                                        | Ctrl+Shift+A shortcut.                                                                                                                     |
| `Remove` button             | Deletes selected memories (with confirmation). Shows progress for batch removal.                                                                                             | Delete/Backspace key also triggers. Button label changes to 'Remove Selected' when >1 row selected.                                        |
| Title bar — Memory Channels | Frameless 18 px gradient title bar with grip glyph on the left and the dialog title.                                                                                         | Added in v26.5.1 (#2509). Uses FramelessWindowTitleBar; 8-axis resize via FramelessResizer.                                                |
| — (Minimize)                | Minimizes the dialog.                                                                                                                                                        |                                                                                                                                            |
| □ (Maximize)                | Maximizes or restores the dialog.                                                                                                                                            |                                                                                                                                            |
| × (Close)                   | Closes the dialog. Escape clears search first, then closes.                                                                                                                  |                                                                                                                                            |
| Drag-to-move                | Click and drag the title bar to move the dialog.                                                                                                                             | Double-click the title bar to toggle maximize/restore.                                                                                     |
| 8-axis resize               | Click and drag any edge or corner of the dialog to resize. Cursor changes to indicate the resize direction.                                                                  | 12 px resize hit zone via FramelessResizer.                                                                                                |
| Selection count             | Shows '<N> of <M> selected'.                                                                                                                                                 |                                                                                                                                            |

## Tips

- Profile filtering and name search (`Search:`) work together. You can select a profile in `Profile:` and type in `Search:` to narrow results further by memory name.
- The `Export...` button respects the current profile filter — only memories visible under the active filter are exported.
- The frameless title bar and 8-axis edge resize are now part of the persistent dialog infrastructure. The dialog remembers its geometry across sessions via the `MemoryDialogGeometry` setting key. Title bar behavior (drag-to-move, double-click to maximize/restore) and 8-axis edge resize remain as described in the controls table.
- The memory table uses theme-aware alternate row colors. The appearance adapts to the active theme's background color scheme for the dialog.

## Related

- [Memory Channels overview](overview.md)
- [Search memories by name](search-memories-by-name.md)
- [Export memories for backup or sharing](export-memories-for-backup-or-sharing.md)