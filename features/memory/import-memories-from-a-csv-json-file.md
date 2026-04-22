# Import memories from a CSV/JSON file

Use this page to load stored memory channels from a CSV or JSON file into AetherSDR. This lets you restore a previous backup or load memories prepared on another system.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The Memory Channels dialog requires an active radio connection.
- You need a CSV or JSON file of memories to import. To create one from your current memories, see [Export memories for backup or sharing](export-memories-for-backup-or-sharing.md).

## Steps

1. Open `Settings > Memory...` to open the Memory Channels dialog.
2. Click `Import...`.
3. In the file browser that opens, navigate to your CSV or JSON file and select it.
4. Confirm the selection. AetherSDR will read the file and add the memories to the radio.

## Tips

- If the import encounters rows with problems, AetherSDR reports the issue per row, including the memory name and frequency where available.
- Use the `Search:` field or the `Profile:` combo box after importing to verify that the expected memories appear in the table.

## Related

- [Export memories for backup or sharing](export-memories-for-backup-or-sharing.md)
- [Memory Channels overview](overview.md)
- [Search memories by name](search-memories-by-name.md)
- [Filter memories by profile](filter-memories-by-profile.md)
