# Memory Channels overview

The Memory Channels dialog lets you store, organize, and recall frequencies on your FLEX-8600. Use it to save commonly used frequencies with their mode, filter, and repeater settings, then tune any slice to a stored memory in one click.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. Memory Channels requires an active radio connection.

## How it works

Open the dialog at `Settings > Memory...`. The dialog shows a table of all memories stored on the radio. You can filter the table, edit entries inline, tune a slice to any memory, and import or export memories as files.

**Filtering and searching**

The Search: field and the Profile: combo box sit above the table. Typing in Search: instantly filters the table to rows whose name matches. Selecting a profile in Profile: narrows the table to memories belonging to that global profile. Both filters can be active at the same time.

**The memory table**

Each row represents one stored memory. The table has 18 columns:

| Column | What it stores |
|---|---|
| Group | Logical group name for the memory |
| Owner | Owner tag |
| Frequency | Stored frequency in MHz |
| Name | Human-readable label |
| Mode | Operating mode (e.g. USB, CW, FM) |
| Step | Tuning step |
| FM TX Offset Dir | Repeater offset direction |
| Repeater Offset | Repeater offset value |
| Tone Mode | CTCSS/DCS tone mode |
| Tone Value | Tone frequency or code |
| Squelch | Squelch on/off |
| Squelch Level | Squelch threshold |
| RX Filter Low | Lower edge of the receive filter |
| RX Filter High | Upper edge of the receive filter |
| RTTY Mark | RTTY mark frequency |
| RTTY Shift | RTTY shift |
| DIGL Offset | Digital lower sideband offset |
| DIGU Offset | Digital upper sideband offset |

Click a column header to sort by that column. Click again to reverse the sort order.

The table supports extended selection: Shift-click selects a range; Ctrl-click (Command-click on macOS) adds or removes individual rows. Double-clicking a row tunes the active slice to that memory immediately.

**Buttons**

| Button | What it does |
|---|---|
| Add | Creates a new memory using the current VFO frequency and settings. |
| Edit | Enters inline-edit mode on the selected memory row. |
| Tune | Tunes the active slice to the selected memory. |
| Select All | Selects every row in the table. |
| Import... | Imports memories from a file into the radio. |
| Export... | Exports the selected memories to a file. |
| Remove | Deletes the selected memories after a confirmation prompt. |

**Selection count**

The indicator to the left of Remove shows how many rows are currently selected, displayed as `<N> selected`.

## Related

- [Add a memory at current frequency](add-a-memory-at-current-frequency.md)
- [Edit a memory's name, mode or offset inline](edit-a-memory-s-name-mode-or-offset-inline.md)
- [Tune the radio to a stored memory](tune-the-radio-to-a-stored-memory.md)
- [Search memories by name](search-memories-by-name.md)
- [Filter memories by profile](filter-memories-by-profile.md)
- [Sort memory table by column header](sort-memory-table-by-column-header.md)
- [Import memories from a CSV/JSON file](import-memories-from-a-csv-json-file.md)
- [Export memories for backup or sharing](export-memories-for-backup-or-sharing.md)
- [Delete one or more memories](delete-one-or-more-memories.md)
