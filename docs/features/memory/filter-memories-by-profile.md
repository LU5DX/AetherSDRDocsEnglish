# Filter memories by profile

Use the Profile: filter in the Memory Channels dialog to narrow the memory table to entries belonging to a single global profile. This is useful when you have a large memory list and want to see only the channels relevant to a particular operating context.

## Before you start

- AetherSDR must be connected to the radio. The Memory Channels dialog requires an active radio connection.
- At least one global profile must exist on the radio. Profiles are managed under `Profiles > Profile Manager...`.

## Steps

1. Open `Settings > Memory...` to open the Memory Channels dialog.
2. Locate the `Profile:` drop-down at the top of the dialog, to the right of the `Search:` field.
3. Click the `Profile:` drop-down and select the profile you want to filter by.

The memory table immediately updates to show only memories whose Group matches the selected profile. Memories belonging to other profiles are hidden but not deleted.

4. To remove the filter and show all memories, open the `Profile:` drop-down and select the blank or all-profiles entry.

## What each control does

| Control | Behavior |
|---|---|
| `Profile:` (combo box) | Filters the memory table to show only memories associated with the selected global profile. Selecting no profile (blank entry) shows all memories. |
| `Search:` (text field) | Further filters the already-filtered table by memory name. Both filters apply simultaneously. |

## Tips

- The `Search:` and `Profile:` filters stack. You can select a profile first, then type in the `Search:` field to narrow results further within that profile.
- The `Export...` button respects the active profile filter. Exporting while a profile is selected will export only the memories currently visible in the table.

## Related

- [Memory Channels overview](overview.md)
- [Search memories by name](search-memories-by-name.md)
- [Export memories for backup or sharing](export-memories-for-backup-or-sharing.md)
- [Sort memory table by column header](sort-memory-table-by-column-header.md)
