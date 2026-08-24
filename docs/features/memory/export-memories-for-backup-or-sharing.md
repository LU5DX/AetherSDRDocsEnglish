# Export memories for backup or sharing

Export your stored memory channels to a CSV file for safekeeping or to share with other operators. You can export all memories at once or a specific selection.

## Before you start

- AetherSDR must be connected to the radio. The Memory Channels dialog requires an active radio connection.
- You must have at least one memory channel stored on the radio.

## Steps

1. Open `Settings > Memory...` to open the Memory Channels dialog.
2. Select the memories you want to export from the memory table. Click a row to select it. Shift-click to select a range. Ctrl-click (or Command-click on macOS) to add or remove individual rows.
3. To export every memory, click `Select All` to select all rows before proceeding.
4. Click `Export...`.
5. In the file dialog that opens, confirm or change the destination path and filename. The default filename is in the form `AetherSDR_Memories_<date-time>_v<version>.csv` and is placed in your home `Documents` folder.
6. Confirm the save. AetherSDR writes the selected memories to the CSV file.

## Notes on the dialog window

The Memory Channels dialog uses a custom title bar with an 18 px gradient background. The title bar displays "Memory Channels" with a grip glyph on the left side. You can:

- Click and drag the title bar to move the dialog.
- Double-click the title bar to toggle between maximized and restored state.
- Click any edge or corner and drag to resize the dialog. The cursor changes to indicate the resize direction. The resize hit zone is 12 pixels wide via FramelessResizer.
- Click the minimize button (—) to minimize the dialog.
- Click the maximize button (□) to maximize or restore the dialog.
- Click the close button (×) to close the dialog. Press Escape to clear the search field first, then close the dialog on a second press.

The dialog remembers its geometry across sessions. When reopened, it restores to its previous size and position.

The memory table uses themed background colors determined by the current application theme. The alternate row color and selected item highlight are set to match the active theme's color scheme.

## Editing memories

The memory table shows the following columns: Group, Owner, Frequency, Name, Mode, Step, FM TX Offset Dir, Repeater Offset, Tone Mode, Tone Value, Squelch, Squelch Level, RX Filter Low, RX Filter High, RTTY Mark, RTTY Shift, DIGL Offset, DIGU Offset. The table is sortable by clicking column headers for Frequency, Name, or Mode.

To edit a memory:

1. Select exactly one memory row in the table.
2. Click `Edit`, or press F2 or Ctrl+E. The Name field enters inline-edit mode.
3. Edit the field values directly in the table. Press Enter to confirm or Escape to cancel.

### Inline editing with combo-box delegates

Starting in v26.7.4, many memory fields use dedicated combo-box editors when you enter inline edit mode. This accelerates data entry by presenting a pick list of valid values while still allowing typed input where appropriate.

- **Mode, Offset Direction, Tone Mode, Tone Value, Step, Group**: A combo box pops open immediately when you start editing the cell. Select a value from the list or type a custom value.
- **Frequency and Repeater Offset**: Float-validated editors accept only numeric input with standard decimal notation.
- **Rx Filter Low, Rx Filter High, RTTY Mark, RTTY Shift, DIGL Offset, DIGU Offset**: Integer-validated editors accept only whole numbers.
- **Name**: Plain text editor with no validation.

The combo box drops open on a zero-delay timer so picking a value is effectively one click once the cell is being edited.

### Removing memories

To delete memories:

1. Select one or more rows in the table. Use Ctrl+Shift+A to select all visible rows, or press Delete/Backspace to remove the selected rows.
2. Click `Remove` (the button label changes to "Remove Selected" when more than one row is selected).
3. Confirm the deletion when prompted. A progress dialog shows the batch removal progress.

## Searching and filtering

Use the `Search:` field at the top of the dialog to filter the table by memory name. The field has a clear button; press Enter to submit. Press Ctrl+F to focus the search field.

Use the `Profile:` combo box to filter by an active global or transmit profile. The list collects profile names from the radio's global profiles and transmit profiles.

## Adding memories from the active slice

To create a new memory from the currently active slice:

1. Ensure the slice you want to use is active.
2. Click `Add` or press Ctrl+N. A new memory row is created from the active slice's settings.

The slice-letter badge variant was dropped in v26.8.4; adding always targets the active slice.

## Tuning to a memory

To tune the active slice to a stored memory:

1. Select exactly one memory row in the table.
2. Click `Tune`. The active slice tunes to the stored frequency.

You can also double-click a memory row to tune to it directly.

## Notes on the dialog window

The Memory Channels dialog uses a custom title bar with an 18 px gradient background. The title bar displays "Memory Channels" with a grip glyph on the left side. You can:

- Click and drag the title bar to move the dialog.
- Double-click the title bar to toggle between maximized and restored state.
- Click any edge or corner and drag to resize the dialog. The cursor changes to indicate the resize direction. The resize hit zone is 12 pixels wide via FramelessResizer.
- Click the minimize button (—) to minimize the dialog.
- Click the maximize button (□) to maximize or restore the dialog.
- Click the close button (×) to close the dialog. Press Escape to clear the search field first, then close the dialog on a second press.

The dialog remembers its geometry across sessions. When reopened, it restores to its previous size and position.

The dialog shows a selection count indicator in the format "<N> of <M> selected" so you can track how many rows are selected.

## Tips

- If you want to export only the memories belonging to a particular profile, use the `Profile:` combo box to filter the table to that profile first, then click `Select All` before clicking `Export...`.
- The exported file is sorted by frequency, then by internal memory index, regardless of the current table sort order.
- The exported CSV file can be imported back into AetherSDR using `Import...`.

## Related

- [Import memories from a CSV/JSON file](import-memories-from-a-csv-json-file.md)
- [Add a memory at current frequency](add-a-memory-at-current-frequency.md)
- [Filter memories by profile](filter-memories-by-profile.md)
- [Memory Channels overview](overview.md)