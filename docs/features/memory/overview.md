# Memory Channels overview

The Memory Channels dialog lets you store, organize, and recall radio frequencies along with their associated operating parameters. Use it to build a library of repeaters, net frequencies, DX spots, or any frequency you tune to regularly.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The dialog requires an active radio connection.

## How it works

Open the dialog with `Settings > Memory...`. The dialog displays all memories stored on the radio in a scrollable table. From here you can add new memories, edit existing ones, tune to a stored frequency, or manage your memory list in bulk.

**Filtering and searching**

The top of the dialog provides two filters that work together. The Search: field narrows the table to rows whose name matches the text you type; press Enter or use the clear button to reset it. The Profile: combo box filters by the currently active global profile. Both filters apply simultaneously.

**The memory table**

Each row represents one stored memory. The columns are:

| Column | What it stores |
|---|---|
| Group | Organizational group name |
| Owner | Owner tag |
| Frequency | Stored frequency in MHz |
| Name | Memory label |
| Mode | Operating mode (e.g. USB, FM, CW) |
| Step | Tuning step |
| FM TX Offset Dir | FM repeater offset direction |
| Repeater Offset | Repeater offset in MHz |
| Tone Mode | CTCSS/DCS tone mode |
| Tone Value | Tone frequency or code |
| Squelch | Squelch enabled/disabled |
| Squelch Level | Squelch threshold level |
| RX Filter Low | Low edge of receive filter in Hz |
| RX Filter High | High edge of receive filter in Hz |
| RTTY Mark | RTTY mark frequency |
| RTTY Shift | RTTY shift |
| DIGL Offset | Digital lower sideband offset |
| DIGU Offset | Digital upper sideband offset |

Click a column header to sort by that column. Click again to reverse the sort order. Multiple rows can be selected using Shift-click for a range or Ctrl-click (Command-click on macOS) to add or remove individual rows. Double-clicking a row tunes the active slice to that memory immediately.

**Buttons**

| Button | What it does |
|---|---|
| Add | Creates a new memory at the current VFO frequency. |
| Edit | Enters inline-edit mode on the selected memory row. |
| Tune | Tunes the active slice to the selected memory. |
| Select All | Selects every row in the table. |
| Import... | Imports memories from a file. |
| Export... | Exports the selected memories to a file. |
| Remove | Deletes the selected memories after asking for confirmation. |

The selection count indicator at the bottom right of the button row shows how many rows are currently selected.

## Tips

- The Search: field has a clear button on the right side; click it to remove the filter without clearing the Profile: selection.
- Sorting and filtering do not delete or reorder the memories on the radio; they only change what is visible in the table.

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
