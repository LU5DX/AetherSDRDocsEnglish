# Add a memory from the active slice

Save the current active slice's frequency, mode, and other settings as a new memory channel for later recall.

## Before you start

- A radio must be connected and at least one slice must be active.
- Open the Memory Channels dialog: **Settings > Memory...**

## Steps

1. In the Memory Channels dialog, click **Add**.
   - Or press **Ctrl+N**.
2. A new row appears in the memory table populated with the active slice's current frequency, mode, and other parameters.
3. (Optional) Edit the memory's name or other fields:
   - Click **Edit** to enter inline editing on the Name field.
   - Click other cells directly to edit their values. For constrained fields (Mode, Step, Offset Direction, Tone Mode, Tone Value, Group), a combo box opens automatically with common values. For editable fields, you can type custom values.

## What each control does

| Control | Label | Behavior |
|---|---|---|
| Title bar | Memory Channels | Frameless 18 px gradient title bar with grip glyph on the left and the dialog title. Click and drag to move; double-click to toggle maximize/restore. |
| Minimize button | — (Minimize) | Minimizes the dialog. |
| Maximize button | □ (Maximize) | Maximizes or restores the dialog. |
| Close button | × (Close) | Closes the dialog. Escape clears the search field first, then closes the dialog. |
| Drag-to-move | — | Click and drag the title bar to move the dialog. The top 18 px (title bar height) is reserved for moving; the resize zone starts below it. Double-click to toggle maximize/restore. |
| 8-axis resize | — | Click and drag any edge or corner to resize. Cursor changes to indicate resize direction. 12 px resize hit zone. The top edge resize zone starts below the title bar. |
| Search field | Search: | Filters the table by memory name. Has a clear button; press Enter to submit. Ctrl+F focuses this field. |
| Profile filter | Profile: | Filters memories by active global or transmit profile. Default: "All Memories". |
| Memory table | — | Displays memory rows. Sortable by clicking column headers (Frequency, Name, Mode). Columns: Group, Owner, Frequency, Name, Mode, Step, FM TX Offset Dir, Repeater Offset, Tone Mode, Tone Value, Squelch, Squelch Level, RX Filter Low, RX Filter High, RTTY Mark, RTTY Shift, DIGL Offset, DIGU Offset. ExtendedSelection; inline-edit mode via Edit button or F2/Ctrl+E. Delete/Backspace removes selected rows. Double-click tunes. Ctrl+Shift+A selects all. Editable cells use combo-box editors for constrained fields (Mode, Step, Offset Direction, Tone Mode, Tone Value, Group) — the drop-down opens immediately when you start editing. The table background uses the theme color `dialog/memory`. |
| Selection count | — | Shows "<N> of <M> selected". |
| Add button | Add | Creates a new memory from the active slice's current settings (no per-letter selection — always targets the active slice). Shortcut: Ctrl+N. |
| Edit button | Edit | Enables inline editing on the selected memory's Name field. Only enabled when exactly one memory is selected. Shortcut: F2 or Ctrl+E. |
| Tune button | Tune | Tunes the active slice to the selected memory. Only enabled when exactly one memory is selected. |
| Select All button | Select All | Selects every visible row (respecting search/filter). Shortcut: Ctrl+Shift+A. |
| Remove button | Remove | Deletes selected memories (with confirmation). Shows progress for batch removal. Button label changes to "Remove Selected" when more than one row is selected. Shortcut: Delete or Backspace. |
| Import button | Import... | Imports memories from a CSV file with progress dialog. Shows import progress and a summary with any skipped rows. |
| Export button | Export... | Exports selected (or filtered) memories to CSV. Validates generated CSV before saving. |

## Tips

- The memory is automatically assigned a sequential index number. To rename it, select the row and click **Edit** or press **F2**.
- The memory captures the active slice's frequency, mode, step, filter settings, and any FM repeater parameters (offset direction, offset, tone mode, tone value, squelch settings).
- The dialog remembers its size and position between sessions.
- The Add button always targets the active slice; there is no per-slice-letter selection.
- The dialog uses the theme color set for `dialog/memory`. Alternate row colors in the memory table follow the theme's background color.
- When editing constrained fields (Mode, Step, Offset Direction, Tone Mode, Tone Value, Group), a combo box opens automatically with the known values. For editable fields, you can type custom values which are validated by the radio when committed.

## Related

- [Edit a memory's name inline](edit-a-memory-s-name-inline.md)
- [Tune the radio to a stored memory](tune-the-radio-to-a-stored-memory.md)
- [Use Ctrl+N to add a memory quickly](use-ctrl-n-to-add-a-memory-quickly.md)