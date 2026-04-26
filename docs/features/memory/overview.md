# Memory Channels overview

The Memory Channels dialog lets you store, organize, and recall radio frequencies along with their associated mode and filter settings. Use it to build a personal channel list, tune quickly to saved frequencies, and share or back up your memories via import and export.

## Before you start

- A radio connection is required. The dialog will not populate without an active connection to the FLEX-8600.
- Open the dialog via `Settings > Memory...`.

## How it works

AetherSDR stores memories on the radio. Each memory holds a frequency and a set of operating parameters. When you open `Settings > Memory...`, the dialog fetches the current memory list from the radio and displays it in a table. Changes you make — adding, editing, or removing memories — are sent to the radio immediately.

The table supports multiple simultaneous selections. Use Shift-click to select a range and Ctrl-click (Command-click on macOS) to add or remove individual rows. Double-clicking any row tunes the active slice to that memory directly, without pressing Tune.

You can narrow the list using the Search field, the Profile filter, or by clicking a column header to sort. These filters affect only what is displayed; they do not modify the stored memories.

## What each control does

| Control | What it does |
|---|---|
| **Search:** | Filters the table to show only memories whose name matches the text you type. Press Enter to confirm, or use the clear button to reset. |
| **Profile:** | Filters the table to show only memories belonging to the selected global profile. |
| **Memory table** | Displays all stored memories. Columns: Group, Owner, Frequency, Name, Mode, Step, FM TX Offset Dir, Repeater Offset, Tone Mode, Tone Value, Squelch, Squelch Level, RX Filter Low, RX Filter High, RTTY Mark, RTTY Shift, DIGL Offset, DIGU Offset. Supports extended (multi-row) selection and inline editing. |
| **Add** | Creates a new memory using the current VFO frequency and settings. |
| **Edit** | Enters inline-edit mode on the selected memory row, allowing you to change any field directly in the table. |
| **Tune** | Tunes the active slice to the selected memory's frequency and mode. |
| **Select All** | Selects every row in the table. |
| **Import...** | Imports memories from a file into the radio. |
| **Export...** | Exports the selected memories to a file for backup or sharing. |
| **Remove** | Deletes the selected memories after asking for confirmation. |
| **Selection count** | Shows the number of currently selected rows as `<N> selected`. |

## Tips

- Double-clicking a row in the memory table tunes the active slice immediately, without needing to press Tune.
- Sorting is available by clicking column headers. Click the same header again to reverse the sort order.
- The Search field updates the table as you type, so you do not need to press Enter to filter; Enter activates the currently highlighted row.

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
