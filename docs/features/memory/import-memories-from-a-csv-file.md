# Import memories from a CSV file

Import memory channels you prepared offline or received from another operator into the radio. AetherSDR reads a CSV file and adds every valid row as a new memory entry, showing a progress dialog and a summary of skipped rows.

## Before you start

- A radio must be connected.
- The CSV file should use the same column layout as an AetherSDR export (Group, Owner, Frequency, Name, Mode, Step, FM TX Offset Dir, Repeater Offset, Tone Mode, Tone Value, Squelch, Squelch Level, RX Filter Low, RX Filter High, RTTY Mark, RTTY Shift, DIGL Offset, DIGU Offset).  
  See [Export memories for backup or sharing](export-memories-for-backup-or-sharing.md) for the exact column header format.

## Steps

1. Open the Memory Channels dialog: **Settings > Memory...**
2. Click **Import...**
3. In the file picker, locate and select your CSV file, then click Open.
4. Wait for the progress dialog to complete. A summary will show how many memories were imported and list any rows that were skipped (for example, due to an invalid frequency or missing value).

## Tips

- Sort or filter the memory table after import to verify the new entries. See [Sort memory table by column header](sort-memory-table-by-column-header.md) and [Filter memories by profile](filter-memories-by-profile.md).
- The memory table uses the active theme's background color for alternating rows. The dialog container is styled with the `dialog/memory` theme key.

## Related

- [Export memories for backup or sharing](export-memories-for-backup-or-sharing.md)
- [Add a memory from the active slice](add-a-memory-from-the-active-slice.md)
- [Delete one or more memories](delete-one-or-more-memories.md)