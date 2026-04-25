# Import memories from a CSV/JSON file

Import previously exported or third-party memory files into AetherSDR's memory channel list. Use this when migrating memories from another radio, restoring a backup, or loading a shared frequency list.

## Before you start

- AetherSDR must be connected to the radio. The Memory Channels dialog requires an active radio connection.
- Have your CSV or JSON memory file ready on disk.

## Steps

1. Open `Settings > Memory...` to open the Memory Channels dialog.
2. Click `Import...`.
3. In the file browser that opens, navigate to your CSV or JSON file and select it.
4. Confirm the selection. AetherSDR reads the file and adds the memories to the radio.

## Tips

- After importing, use the `Search:` field to filter by name or the `Profile:` combo box to filter by group, which can help you confirm the imported entries appeared correctly.
- If you imported memories into a specific group, set `Profile:` to that group name to see only those entries.

## Troubleshooting

- **Memories do not appear after import** — Verify the file is a valid CSV or JSON export produced by AetherSDR or a compatible source. Files with missing required fields (such as Frequency or Mode) may be skipped or produce unnamed entries.
- **Import... is greyed out or unavailable** — The dialog requires an active radio connection. Connect to the FLEX-8600 first via `Settings > Connect to Radio...`, then reopen `Settings > Memory...`.

## Related

- [Export memories for backup or sharing](export-memories-for-backup-or-sharing.md)
- [Memory Channels overview](overview.md)
- [Search memories by name](search-memories-by-name.md)
- [Filter memories by profile](filter-memories-by-profile.md)
