# Memory Channels

The Memory Channels dialog lets you manage the radio's memory channels — add frequencies from the active slice, edit existing memories, search and filter, tune, import/export, and delete stored frequencies.

## Opening the dialog

1. Open **Settings > Memory...**

   The Memory Channels dialog appears with a frameless title bar and 8-axis resize capability.

## Search and filter

| Control | Behavior |
|---------|----------|
| **Search:** text field | Filters the table by memory name. Has a clear button; press Enter to submit. **Ctrl+F** focuses the search field. |
| **Profile:** combo box | Filters by active global or transmit profile. Default is "All Memories". Collects profile names from RadioModel global profiles and transmit profiles. |

## Memory table

The memory table displays and edits memory rows. Columns include Group, Owner, Frequency, Name, Mode, Step, FM TX Offset Dir, Repeater Offset, Tone Mode, Tone Value, Squelch, Squelch Level, RX Filter Low, RX Filter High, RTTY Mark, RTTY Shift, DIGL Offset, DIGU Offset.

- Sort by clicking column headers (Frequency, Name, Mode).
- ExtendedSelection mode; inline-edit via **Edit** button or **F2**/**Ctrl+E**.
- **Delete**/**Backspace** removes selected rows.
- Double-click tunes the active slice to that memory.
- **Ctrl+Shift+A** selects all.

### Inline editing with drop-down fields

When editing a memory cell, constrained fields (Mode, Offset Dir, Tone Mode, Tone Value, Step, Group) open a combo-box editor. The list pops open immediately so you can pick a value in one click.

- **Strict fields** (not editable): Only known values from the radio are offered.
- **Editable fields**: Common values are seeded, but you can type custom text; the radio validates the input on commit. Int and Double validators apply where appropriate.
- If a cell contains a value not in the list (e.g., from a legacy memory), the value is preserved and shown as the first item so it isn't silently changed.

## Managing memories

| Control | Behavior |
|---------|----------|
| **Import...** | Imports memories from a CSV file with progress dialog. Shows import progress and a summary with any skipped rows. |
| **Export...** | Exports selected (or filtered) memories to CSV. Validates generated CSV before saving. |
| **Add** | Creates a new memory from the current (active) slice. **Ctrl+N** shortcut. The slice-letter badge variant was dropped; adding always targets the active slice. |
| **Edit** | Enters inline-edit mode on the selected memory's Name field. **F2** or **Ctrl+E** also triggers edit. Only enabled when exactly one memory is selected. |
| **Tune** | Tunes the active slice to the selected memory. Only enabled when exactly one memory is selected. |
| **Select All** | Selects every visible row (respecting search/filter). **Ctrl+Shift+A** shortcut. |
| **Remove** | Deletes selected memories (with confirmation). Shows progress for batch removal. **Delete**/**Backspace** key also triggers. Button label changes to "Remove Selected" when more than one row is selected. |

## Title bar and window controls

The Memory Channels dialog has a modern frameless interface:

| Control | Behavior |
|---------|----------|
| **Title bar — Memory Channels** | Frameless 18 px gradient title bar with grip glyph on the left and the dialog title. |
| **— (Minimize)** | Minimizes the dialog. |
| **□ (Maximize)** | Maximizes or restores the dialog. |
| **× (Close)** | Closes the dialog. Escape clears search first, then closes. |
| **Drag-to-move** | Click and drag the title bar to move the dialog. Double-click the title bar to toggle maximize/restore. |
| **8-axis resize** | Click and drag any edge or corner of the dialog to resize. Cursor changes to indicate the resize direction. 12 px resize hit zone via FramelessResizer. The top edge reserves an area (the title bar height) for drag-to-move instead of resize. |
| **Selection count** | Shows "<N> of <M> selected". |

## Keyboard shortcuts

| Shortcut | Action |
|----------|--------|
| **Ctrl+N** | Add a new memory from the active slice (works even when dialog is closed) |
| **Ctrl+F** | Focus the search field |
| **F2** or **Ctrl+E** | Edit the selected memory's name |
| **Delete** or **Backspace** | Remove selected memories |
| **Ctrl+Shift+A** | Select all visible rows |
| **Esc** | Clear search first, then close dialog |
| **Double-click** on a memory row | Tune the active slice to that memory |

## Adding a memory quickly (Ctrl+N)

Add a memory channel from the active slice without opening any menus — just press a keyboard shortcut.

### Before you start

- The radio must be connected and have an active slice.
- The Memory Channels dialog doesn't need to be open.

### Steps

1. Press **Ctrl+N** anywhere in the main application window.

   A new memory is created from the current active slice's frequency, mode, and filter settings.

2. (Optional) Open **Settings > Memory...** to view the new memory in the table and edit its name or other fields.

### Tips

- Ctrl+N works even when other dialogs have focus, as long as the main window is active.
- Use **Settings > Memory...** to add, edit, or delete memories in bulk. Ctrl+N is the fastest single-memory shortcut.

## Theme integration

The Memory Channels dialog supports theme styling. The table uses the theme-defined background color for alternate rows. To apply a custom theme, configure the `dialog/memory` container in your theme definition.