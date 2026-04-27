# Import memories from a CSV/JSON file

Load a saved memory file into AetherSDR to populate your radio's memory channels with stored frequencies, modes, and offsets.

## Before you start

- Your radio must be connected. The Memory Channels dialog requires an active radio connection.
- Have your CSV or JSON memory file ready on disk.

## Steps

1. Click `Settings > Memory...` to open the Memory Channels dialog.
2. Click `Import...`.
3. In the file picker that opens, navigate to your CSV or JSON file and select it.
4. Confirm the selection. AetherSDR reads the file and adds the memories to the radio.

## Tips

- After importing, use the `Search:` field or the `Profile:` combo box to verify that the imported memories appear with the expected names and groups.
- If you want a backup before importing, click `Export...` first to save the current memories to a file.

## Troubleshooting

- **Imported memories do not appear in the table** — The file may contain formatting errors or unsupported fields. Check that the file is a valid CSV or JSON export from AetherSDR or a compatible source. Rows with missing required fields (such as frequency) may be silently skipped.
- **Import... is not clickable** — The dialog requires an active radio connection. Connect to the FLEX-8600 first via `Settings > Connect to Radio...`, then reopen the Memory Channels dialog.

## Related

- [Export memories for backup or sharing](export-memories-for-backup-or-sharing.md)
- [Add a memory at current frequency](add-a-memory-at-current-frequency.md)
- [Search memories by name](search-memories-by-name.md)
- [Filter memories by profile](filter-memories-by-profile.md)
- [Memory Channels overview](overview.md)
