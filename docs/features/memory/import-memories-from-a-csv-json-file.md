# Import memories from a CSV/JSON file

Use this page to load stored memories from a CSV or JSON file into the radio's memory channel list. This lets you restore a backup, move memories between rigs, or load a frequency list prepared outside AetherSDR.

## Before you start

- AetherSDR must be connected to a radio. The Memory Channels dialog requires an active radio connection.
- Have your CSV or JSON file ready and note its location on disk.

## Steps

1. Open `Settings > Memory...` to open the Memory Channels dialog.
2. Click `Import...`.
3. In the file dialog that opens, navigate to your CSV or JSON file and select it.
4. Confirm the selection. AetherSDR reads the file and adds the memories to the radio.

## Tips

- After importing, use the `Search:` field or the `Profile:` combo box to verify that the imported memories appear correctly.
- If you imported memories into a specific group, set `Profile:` to that group name to view only those entries.

## Troubleshooting

- **Memories do not appear after import** — Confirm the radio is connected. The dialog requires an active radio connection to commit memory entries. Disconnect and reconnect if necessary, then try the import again.
- **Import dialog opens but no file is selectable** — Ensure your file has a `.csv` or `.json` extension. Files without a recognised extension may be filtered out by the dialog.

## Related

- [Memory Channels overview](overview.md)
- [Export memories for backup or sharing](export-memories-for-backup-or-sharing.md)
- [Add a memory at current frequency](add-a-memory-at-current-frequency.md)
- [Search memories by name](search-memories-by-name.md)
- [Filter memories by profile](filter-memories-by-profile.md)
