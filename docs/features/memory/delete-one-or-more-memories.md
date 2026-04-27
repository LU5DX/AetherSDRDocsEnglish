# Delete one or more memories

Remove stored memory channels you no longer need. AetherSDR asks for confirmation before deleting, so no memory is lost accidentally.

## Before you start

- AetherSDR must be connected to the radio. Memory Channels requires an active radio connection.
- Know which memories you want to remove. Use Search: or Profile: to narrow the list first if needed.

## Steps

1. Open `Settings > Memory...` to open the Memory Channels dialog.
2. Select the memory or memories you want to delete:
   - Click a single row to select it.
   - Shift-click a second row to select a contiguous range.
   - On Linux and Windows, Ctrl-click individual rows to add or remove them from the selection. On macOS, use Command-click.
   - Click Select All to select every row currently shown in the table.
3. Confirm your selection by checking the selection count indicator in the lower-right area of the dialog (shown as `<N> selected`).
4. Click Remove.
5. Confirm the deletion in the confirmation dialog that appears.

The selected memories are permanently removed from the radio.

## Tips

- If you have a long memory list, use the Search: field or the Profile: combo box to filter the table before using Select All. This lets you quickly select and remove a subset of memories without manually picking each row.
- Deletion cannot be undone from within AetherSDR. Export your memories before a bulk delete if you may want them later.

## Related

- [Export memories for backup or sharing](export-memories-for-backup-or-sharing.md)
- [Search memories by name](search-memories-by-name.md)
- [Filter memories by profile](filter-memories-by-profile.md)
- [Import memories from a CSV/JSON file](import-memories-from-a-csv-json-file.md)
- [Memory Channels overview](overview.md)
