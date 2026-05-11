# Tune the Radio to a Stored Memory

Open the Memory Channels dialog to find a stored frequency and send it directly to the active slice receiver.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The Memory Channels dialog requires an active radio connection.
- At least one memory must already be stored. See [Add a memory at current frequency](add-a-memory-at-current-frequency.md) if you have none.

## Steps

1. Click `Settings > Memory...` to open the Memory Channels dialog.
2. Locate the memory you want. Use the `Search:` field to filter by name, or use the `Profile:` combo box to narrow the list by profile.
3. Click the row in the memory table to select it.
4. Click `Tune`.

The active slice tunes to the frequency, mode, and filter settings stored in that memory.

**Shortcut:** Double-click any row in the memory table to tune immediately without clicking `Tune`.

## What each control does

| Control                     | Behavior                                                                                                                                                                                                                                                                                                           | Notes                                                                                                                                                   |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Search:`                   | Filters the memory table to rows whose name matches the text you type. Press Enter or clear the field to reset. Ctrl+F focuses the search field.                                                                                                                                                                      | Has clear button.                                                                                                                                       |
| `Profile:`                  | Filters the table to memories belonging to the selected global or transmit profile.                                                                                                                                                                                                                                | Collects profile names from RadioModel global profiles and transmit profiles.                                                                           |
| Memory table                | Displays and edits memory rows. Sortable by clicking column headers (Frequency, Name, Mode). Columns: Group, Owner, Frequency, Name, Mode, Step, FM TX Offset Dir, Repeater Offset, Tone Mode, Tone Value, Squelch, Squelch Level, RX Filter Low, RX Filter High, RTTY Mark, RTTY Shift, DIGL Offset, DIGU Offset. | ExtendedSelection; inline-edit mode via Edit button or F2/Ctrl+E. Delete/Backspace removes selected rows. Double-click tunes. Ctrl+Shift+A selects all. |
| `Import...`                 | Imports memories from a CSV file with progress dialog.                                                                                                                                                                                                                                                            | Shows import progress and a summary with any skipped rows.                                                                                              |
| `Export...`                 | Exports selected (or filtered) memories to CSV.                                                                                                                                                                                                                                                                    | Validates generated CSV before saving.                                                                                                                  |
| `Add`                       | Creates a new memory from the current (active) slice. Ctrl+N shortcut.                                                                                                                                                                                                                                               | No per-letter selection; always targets the active slice.                                                                                                |
| `Edit`                      | Enters inline-edit mode on the selected memory's Name field. F2 or Ctrl+E also triggers edit.                                                                                                                                                                                                                       | Only enabled when exactly one memory is selected.                                                                                                       |
| `Tune`                      | Tunes the active slice to the selected memory. Requires exactly one row to be selected.                                                                                                                                                                                                                            |                                                                                                                                                         |
| `Select All`                | Selects every visible row (respecting search/filter). Ctrl+Shift+A shortcut.                                                                                                                                                                                                                                         |                                                                                                                                                         |
| `Remove`                    | Deletes selected memories (with confirmation). Shows progress for batch removal. Delete/Backspace key also triggers. Button label changes to 'Remove Selected' when >1 row selected.                                                                                                                                    |                                                                                                                                                         |
| Title bar — Memory Channels | Frameless 18 px gradient title bar with grip glyph on the left and the dialog title.                                                                                                                                                                                                                               | Added in v26.5.1 (#2509). Uses FramelessWindowTitleBar; 8-axis resize via FramelessResizer.                                                             |
| — (Minimize)                | Minimizes the dialog.                                                                                                                                                                                                                                                                                              |                                                                                                                                                         |
| □ (Maximize)                | Maximizes or restores the dialog.                                                                                                                                                                                                                                                                                  |                                                                                                                                                         |
| × (Close)                   | Closes the dialog. Escape clears search first, then closes.                                                                                                                                                                                                                                                        |                                                                                                                                                         |
| Drag-to-move                | Click and drag the title bar to move the dialog.                                                                                                                                                                                                                                                                   | Double-click the title bar to toggle maximize/restore.                                                                                                  |
| 8-axis resize               | Click and drag any edge or corner of the dialog to resize. Cursor changes to indicate the resize direction.                                                                                                                                                                                                        | 12 px resize hit zone via FramelessResizer.                                                                                                             |
| Selection count             | Shows '<N> of <M> selected'.                                                                                                                                                                                                                                                                                       |                                                                                                                                                         |

## Tips

- If you cannot see the memory you want, check whether `Profile:` is set to a filter that excludes it. Set `Profile:` to show all entries.
- On Linux and Windows, hold Ctrl and click to select individual rows without deselecting others. On macOS, use Command-click. Only the first selected memory is used when you click `Tune`.
- Use the `Add` button or Ctrl+N to quickly store the current slice frequency as a new memory.
- Use the `Import...` and `Export...` buttons to transfer memories between radios or share with other operators.

## Troubleshooting

- **`Tune` has no effect or is disabled** — Confirm that a single row is selected in the memory table and that AetherSDR is connected to the radio.
- **The memory you want does not appear in the table** — The `Search:` or `Profile:` filter may be hiding it. Clear the `Search:` field and set `Profile:` to show all entries.
- **Cannot add a memory** — Ensure the radio is connected and an active slice is available.

## Related

- [Add a memory at current frequency](add-a-memory-at-current-frequency.md)
- [Recall an FM repeater memory and restore offset and CTCSS tone](recall-an-fm-repeater-memory-and-restore-offset-and-ctcss-tone.md)
- [Search memories by name](search-memories-by-name.md)
- [Filter memories by profile](filter-memories-by-profile.md)
- [Memory Channels overview](overview.md)