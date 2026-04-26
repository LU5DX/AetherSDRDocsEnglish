# Import memories from a CSV/JSON file

Use this page to load stored frequencies and channel settings from a CSV or JSON file into AetherSDR's memory channel list. This is useful for restoring a backup or loading a frequency file shared by another operator.

## Before you start

- AetherSDR must be connected to the radio. The Memory Channels dialog requires an active radio connection.
- Have the CSV or JSON file you want to import ready on your local filesystem.

## Steps

1. Open `Settings > Memory...` to open the Memory Channels dialog.
2. Click `Import...`.
3. In the file browser that opens, navigate to your CSV or JSON file and select it.
4. Confirm the selection to begin the import. AetherSDR will process the file and add the memories to the table.

## Tips

- After importing, use the **Search:** field or the **Profile:** combo box to verify that the expected memories appear in the table.
- If you imported memories into a specific group, select that group in **Profile:** to filter the table and confirm the entries loaded correctly.

## Troubleshooting

- **Imported memories do not appear in the table** — The file may not match the expected CSV or JSON format. Try exporting an existing memory first to see the expected structure, then compare it with your import file. See [Export memories for backup or sharing](export-memories-for-backup-or-sharing.md).
- **Import... is greyed out or unavailable** — AetherSDR is not connected to the radio. Connect first via `Settings > Connect to Radio...`, then retry.

## Related

- [Export memories for backup or sharing](export-memories-for-backup-or-sharing.md)
- [Add a memory at current frequency](add-a-memory-at-current-frequency.md)
- [Search memories by name](search-memories-by-name.md)
- [Filter memories by profile](filter-memories-by-profile.md)
