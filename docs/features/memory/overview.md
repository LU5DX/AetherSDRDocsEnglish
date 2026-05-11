# Memory Channels overview

The Memory Channels dialog lets you store, organize, and recall radio frequencies along with their associated operating parameters. Use it to build a library of repeaters, net frequencies, DX spots, or any frequency you tune to regularly.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The dialog requires an active radio connection.

## How it works

Open the dialog with `Settings > Memory...`. The dialog displays all memories stored on the radio in a scrollable table. From here you can add new memories, edit existing ones, tune to a stored frequency, or manage your memory list in bulk.

**Filtering and searching**

The top of the dialog provides two filters that work together. The Search: field narrows the table to rows whose name matches the text you type; press Enter or use the clear button to reset it. The Profile: combo box filters by the currently active global or transmit profile. Both filters apply simultaneously.

**The memory table**

Each row represents one stored memory. The columns are:

| Column                      | What it stores                                                                                              | Notes                                                                                                |
|-----------------------------|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Group                       | Organizational group name                                                                                   |                                                                                                      |
| Owner                       | Owner tag                                                                                                   |                                                                                                      |
| Frequency                   | Stored frequency in MHz                                                                                     |                                                                                                      |
| Name                        | Memory label                                                                                                |                                                                                                      |
| Mode                        | Operating mode (e.g. USB, FM, CW)                                                                           |                                                                                                      |
| Step                        | Tuning step                                                                                                 |                                                                                                      |
| FM TX Offset Dir            | FM repeater offset direction                                                                                |                                                                                                      |
| Repeater Offset             | Repeater offset in MHz                                                                                      |                                                                                                      |
| Tone Mode                   | CTCSS/DCS tone mode                                                                                         |                                                                                                      |
| Tone Value                  | Tone frequency or code                                                                                      |                                                                                                      |
| Squelch                     | Squelch enabled/disabled                                                                                    |                                                                                                      |
| Squelch Level               | Squelch threshold level                                                                                     |                                                                                                      |
| RX Filter Low               | Low edge of receive filter in Hz                                                                            |                                                                                                      |
| RX Filter High              | High edge of receive filter in Hz                                                                           |                                                                                                      |
| RTTY Mark                   | RTTY mark frequency                                                                                         |                                                                                                      |
| RTTY Shift                  | RTTY shift                                                                                                  |                                                                                                      |
| DIGL Offset                 | Digital lower sideband offset                                                                               |                                                                                                      |
| DIGU Offset                 | Digital upper sideband offset                                                                               |                                                                                                      |
| Button                      | What it does                                                                                                |                                                                                                      |
| ---                         | ---                                                                                                         |                                                                                                      |
| Add                         | Creates a new memory from the current (active) slice -- no per-letter selection.                            | The slice-letter badge variant was dropped; adding always targets the active slice. Ctrl+N shortcut. |
| Edit                        | Enters inline-edit mode on the selected memory's Name field.                                                | F2 or Ctrl+E also triggers edit. Only enabled when exactly one memory is selected.                   |
| Tune                        | Tunes the active slice to the selected memory.                                                              | Only enabled when exactly one memory is selected.                                                    |
| Select All                  | Selects every visible row (respecting search/filter).                                                       | Ctrl+Shift+A shortcut.                                                                               |
| Import...                   | Imports memories from a CSV file with progress dialog.                                                      | Shows import progress and a summary with any skipped rows.                                           |
| Export...                   | Exports selected (or filtered) memories to CSV.                                                             | Validates generated CSV before saving.                                                               |
| Remove                      | Deletes selected memories (with confirmation). Shows progress for batch removal.                            | Delete/Backspace key also triggers. Button label changes to 'Remove Selected' when >1 row selected.  |

**Frameless window title bar**

The dialog uses a custom frameless title bar introduced in v26.5.1. The title bar displays the dialog name "Memory Channels" with a grip glyph on the left. Click and drag the title bar to move the dialog. Double-click the title bar to toggle between maximized and restored states.

**Window controls**

| Control       | What it does                                                                             | Notes                                                         |
|---------------|------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| — (Minimize)  | Minimizes the dialog.                                                                    |                                                               |
| □ (Maximize)  | Maximizes or restores the dialog.                                                        |                                                               |
| × (Close)     | Closes the dialog. Escape clears the search field first, then closes the dialog.         |                                                               |

**8-axis resize**

Click and drag any edge or corner of the dialog to resize it. The cursor changes to indicate the resize direction. The resize hit zone is 12 pixels wide via FramelessResizer.

**Selection count**

The indicator at the bottom right of the button row shows how many rows are currently selected, formatted as `<N> of <M> selected`.

## Tips

- The Search: field has a clear button on the right side; click it to remove the filter without clearing the Profile: selection.
- Press Ctrl+F to focus the Search: field directly.
- Sorting and filtering do not delete or reorder the memories on the radio; they only change what is visible in the table.
- The frameless window behavior mirrors SpotHub and RadioSetup dialogs. The global View > Frameless Window setting controls whether this dialog uses frameless chrome.

## Related

- [Add a memory at current frequency](add-a-memory-at-current-frequency.md)
- [Edit a memory's name, mode or offset inline](edit-a-memory-s-name-mode-or-offset-inline.md)
- [Tune the radio to a stored memory](tune-the-radio-to-a-stored-memory.md)
- [Delete one or more memories](delete-one-or-more-memories.md)
- [Search memories by name](search-memories-by-name.md)
- [Filter memories by profile](filter-memories-by-profile.md)
- [Import memories from a CSV/JSON file](import-memories-from-a-csv-json-file.md)
- [Export memories for backup or sharing](export-memories-for-backup-or-sharing.md)
- [Sort memory table by column header](sort-memory-table-by-column-header.md)
- [Recall an FM repeater memory and restore offset and CTCSS tone](recall-an-fm-repeater-memory-and-restore-offset-and-ctcss-tone.md)