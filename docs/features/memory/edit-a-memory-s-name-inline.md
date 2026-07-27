# Edit a memory's name inline

Rename a stored memory channel directly in the Memory table without opening a separate dialog.

## Before you start

- Open **Settings > Memory...** to display the Memory Channels dialog.
- The radio must be connected.

## Steps

1. Click a row in the Memory table to select it. Only one memory can be edited at a time.

2. Do one of the following to enter inline-edit mode on the Name field:
   - Click **Edit**.
   - Press **F2** or **Ctrl+E**.

3. Type the new name.

4. Press **Enter** to confirm, or press **Esc** to cancel.

## What each control does

| Control | Behavior |
|---------|----------|
| **Edit** button | Enters inline-edit mode on the selected memory's Name column. Only enabled when exactly one memory is selected. |
| **F2** / **Ctrl+E** | Keyboard shortcut that triggers the same edit mode as the **Edit** button. |

## Tips

- The Name column supports up to the character limit set by the radio firmware. AetherSDR encodes the name as required by SmartSDR protocol.
- To cancel editing, press **Esc** before pressing Enter.
- The Memory Channels dialog uses a **PersistentDialog** framework that remembers its size and position across sessions. Geometry is stored in the setting `MemoryDialogGeometry` and is restored the next time the dialog opens.

## Related

- [Memory Channels overview](overview.md)
- [Add a memory from the active slice](add-a-memory-from-the-active-slice.md)
- [Delete one or more memories](delete-one-or-more-memories.md)
- [Tune the radio to a stored memory](tune-the-radio-to-a-stored-memory.md)
- [Search memories by name](search-memories-by-name.md)

# Memory Channels dialog

Manage the radio's memory channels — add, edit, search, filter, tune, import, export, and delete stored frequencies.

## Open the dialog

- Select **Settings > Memory...**

## Dialog features

| Control | Description |
|---------|-------------|
| Title bar — Memory Channels | Frameless 18 px gradient title bar with grip glyph on the left and the dialog title. Added in v26.5.1. |
| — (Minimize) | Minimizes the dialog. |
| □ (Maximize) | Maximizes or restores the dialog. |
| × (Close) | Closes the dialog. Pressing Escape clears the search field first, then closes the dialog. |
| Drag-to-move | Click and drag the title bar to move the dialog. Double-click the title bar to toggle maximize/restore. The title bar provides an edge-to-edge move handle; the top-edge resize zone is reserved for the title bar to prevent the resizer from stealing grab events. |
| 8-axis resize | Click and drag any edge or corner of the dialog to resize. The cursor changes to indicate the resize direction. The resize hit zone is 12 px. The top edge is not resizable — the title bar handles move operations instead. |
| **Search:** text field | Filters the table by memory name. Has a clear button. Press Enter to submit. Press **Ctrl+F** to focus the search field. |
| **Profile:** combo box | Filters the table by active global or transmit profile. Default: "All Memories". Collects profile names from RadioModel global profiles and transmit profiles. |
| Memory table | Displays and edits memory rows. Sortable by clicking column headers (Frequency, Name, Mode). Columns: Group, Owner, Frequency, Name, Mode, Step, FM TX Offset Dir, Repeater Offset, Tone Mode, Tone Value, Squelch, Squelch Level, RX Filter Low, RX Filter High, RTTY Mark, RTTY Shift, DIGL Offset, DIGU Offset. Supports ExtendedSelection. Inline-edit mode via **Edit** button or **F2**/**Ctrl+E**. Delete or Backspace removes selected rows. Double-click tunes. Ctrl+Shift+A selects all. Several constrained fields (Mode, Offset Dir, Tone Mode, Tone Value, Step, Group) use a combo-box editor that pops open immediately for one-click selection. Editable combo fields accept typed input validated by the radio on commit. |
| Selection count | Shows "<N> of <M> selected". |
| **Import...** button | Imports memories from a CSV file with a progress dialog. Shows import progress and a summary with any skipped rows. |
| **Export...** button | Exports selected (or filtered) memories to CSV. Validates the generated CSV before saving. |
| **Add** button | Creates a new memory from the current (active) slice. Keyboard shortcut: **Ctrl+N**. |
| **Edit** button | Enters inline-edit mode on the selected memory's Name field. Only enabled when exactly one memory is selected. Keyboard shortcuts: **F2** or **Ctrl+E**. |
| **Tune** button | Tunes the active slice to the selected memory. Only enabled when exactly one memory is selected. |
| **Select All** button | Selects every visible row (respecting search/filter). Keyboard shortcut: **Ctrl+Shift+A**. |
| **Remove** button | Deletes selected memories (with confirmation). Shows progress for batch removal. Button label changes to "Remove Selected" when more than one row is selected. Keyboard shortcuts: **Delete** or **Backspace**. |

## Visual style

The dialog uses themed styling. The table's alternate row background color is controlled by the `dialog/memory` theme container and the `{{color.background.0}}` theme token. The selected item background uses color `#2060a0`. These styles are applied via `AetherSDR::ThemeManager`.

## Tips

- The dialog remembers its size and position across sessions. Geometry is stored in the setting `MemoryDialogGeometry`.
- To add a memory from the active slice, press **Ctrl+N** or click **Add**.
- To delete memories, select one or more rows and press **Delete** or **Backspace**, or click **Remove**.
- To tune the radio to a stored memory, double-click the row or select it and click **Tune**.
- To select all visible memories, press **Ctrl+Shift+A** or click **Select All**.
- The search field supports filtering by memory name. Press **Ctrl+F** to focus it.
- Import and export use CSV format. The export validates the generated file before saving.
- In the Memory table, constrained fields (Mode, Offset Dir, Tone Mode, Tone Value, Step, Group) use a combo-box editor. The list pops open automatically when you start editing the cell. For strict fields, only known values are available. For editable fields, you can type a custom value, which will be validated by the radio when committed. If a legacy or corrupt value is present, it is preserved rather than silently replaced.