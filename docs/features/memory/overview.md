# Memory Channels overview

The Memory Channels dialog stores, organizes, and recalls frequencies with their associated operating parameters. Use it to build a personal channel list, tune the radio quickly to a saved frequency, or exchange memory data with other operators.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The dialog requires an active radio connection.

## How it works

Open the dialog with `Settings > Memory...`. The dialog shows a table of all memories stored on the radio. You can filter, sort, add, edit, tune, and remove memories, or move them in and out of files.

Each memory row holds a complete set of operating parameters. The table columns are:

| Column | What it stores |
|---|---|
| Group | Category or group name for the memory |
| Owner | Owner tag for the memory |
| Frequency | Receive frequency in MHz |
| Name | User-assigned label |
| Mode | Operating mode (e.g. USB, CW, FM) |
| Step | Tuning step size |
| FM TX Offset Dir | Direction of FM transmit offset |
| Repeater Offset | FM repeater offset value |
| Tone Mode | CTCSS/DCS tone mode |
| Tone Value | Tone frequency or code |
| Squelch | Squelch enabled or disabled |
| Squelch Level | Squelch threshold level |
| RX Filter Low | Low edge of the receive filter |
| RX Filter High | High edge of the receive filter |
| RTTY Mark | RTTY mark frequency |
| RTTY Shift | RTTY shift value |
| DIGL Offset | Digital lower sideband offset |
| DIGU Offset | Digital upper sideband offset |

Click any sortable column header to sort the table. Click the same header again to reverse the sort order.

Double-clicking a row tunes the active slice to that memory immediately.

## What each control does

| Control | What it does |
|---|---|
| Search: | Filters the table to rows whose name matches the typed text. Has a clear button; press Enter to confirm. |
| Profile: | Filters the table to memories belonging to the selected global profile. |
| Memory table | Displays all memories matching the current filter. Supports range selection with Shift-click and individual row toggling with Ctrl-click (Command-click on macOS). |
| Add | Creates a new memory using the current VFO frequency and settings. |
| Edit | Enters inline-edit mode on the selected memory row. |
| Tune | Tunes the active slice to the selected memory. |
| Select All | Selects every row in the current filtered view. |
| Import... | Imports memories from a file into the radio. |
| Export... | Exports the selected memories to a file. |
| Remove | Deletes the selected memories after asking for confirmation. |
| Selection count | Shows how many rows are currently selected (displayed as `N selected`). |

## Tips

- To find a memory quickly, press the standard Find shortcut for your platform — the cursor jumps to Search: and selects any existing text.
- To add a new memory from the keyboard, press the standard New shortcut for your platform while the dialog is open.
- Exported filenames include the date, time, and AetherSDR version number, and are placed in your Documents folder by default.

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
