# Memory Channels overview

The Memory Channels dialog lets you store, organize, and recall frequencies on your FLEX-8600. Use it to save a frequency and its associated mode, filter, tone, and offset settings so you can tune back to it instantly without re-entering values.

## Before you start

- AetherSDR must be connected to a radio. The dialog requires an active radio connection.

## How it works

Open the dialog with `Settings > Memory...`. The dialog shows a table of all stored memory channels. You can filter what is shown, add new memories, edit existing ones, tune the active slice to any stored memory, and import or export the list for backup or sharing.

**Filtering the table**

The Search field and Profile combo box work together to narrow the table. Typing in Search filters rows by memory name as you type; pressing Enter activates the currently highlighted row. The Profile combo box filters rows by the active global profile. Either filter can be used independently or together.

**The memory table**

Each row is one stored memory. The table supports multi-row selection (Shift-click for a range; Ctrl-click or Command-click on macOS to add or remove individual rows). Double-clicking a row tunes the active slice to that memory. Clicking a column header sorts the table by that column; clicking again reverses the order.

The table contains the following columns:

| Column | What it stores |
|---|---|
| Group | Group or category name |
| Owner | Owner label |
| Frequency | Stored frequency (MHz) |
| Name | Memory name |
| Mode | Operating mode (e.g. USB, CW, FM) |
| Step | Tuning step |
| FM TX Offset Dir | FM repeater offset direction |
| Repeater Offset | Repeater offset value |
| Tone Mode | CTCSS/DCS tone mode |
| Tone Value | Tone frequency or code |
| Squelch | Squelch enabled flag |
| Squelch Level | Squelch threshold level |
| RX Filter Low | Lower edge of the receive filter |
| RX Filter High | Upper edge of the receive filter |
| RTTY Mark | RTTY mark frequency |
| RTTY Shift | RTTY shift |
| DIGL Offset | Digital Lower offset |
| DIGU Offset | Digital Upper offset |

## What each control does

| Control | Behavior |
|---|---|
| Search | Filters table rows by memory name. Has a clear button. Press Enter to activate the highlighted row. |
| Profile | Filters table rows by active global profile. |
| Memory table | Displays and edits all stored memories. Supports multi-row selection and inline editing via keyboard. |
| Add | Creates a new memory at the current VFO frequency. |
| Edit | Enters inline-edit mode on the selected memory row. |
| Tune | Tunes the active slice to the selected memory. |
| Select All | Selects every row in the table. |
| Import... | Imports memories from a file. |
| Export... | Exports selected memories to a file. |
| Remove | Deletes selected memories after confirmation. |
| Selection count | Displays the number of currently selected rows as `<N> selected`. |

None of these controls persist settings to AppSettings keys; all memory data is stored on the radio.

## Tips

- Double-clicking a row is a shortcut for Tune — it tunes the active slice to that memory without using the Tune button.
- Use the Profile combo box together with Export... to export only the memories belonging to a specific group.
- The export filename is generated automatically using the current date and AetherSDR version, and defaults to your Documents folder.

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
