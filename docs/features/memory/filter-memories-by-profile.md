# Filter memories by profile

Use the Profile: filter in the Memory Channels dialog to narrow the memory table to entries belonging to a specific global profile. This is useful when you have a large memory list and want to see only the memories associated with one operating configuration.

## Before you start

- AetherSDR must be connected to the radio. The Memory Channels dialog requires an active radio connection.
- At least one global profile must exist on the radio. Profiles are populated dynamically from the radio.

## Steps

1. Open `Settings > Memory...` to open the Memory Channels dialog.
2. Locate the **Profile:** combo box in the filter row at the top of the dialog.
3. Click **Profile:** and select the profile you want to filter by. The memory table updates immediately to show only memories whose Group matches the selected profile.
4. To remove the filter and show all memories, open the **Profile:** combo box again and select the blank or "all" entry at the top of the list.

## What each control does

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| **Profile:** | Filters the memory table by the selected global profile. Only memories whose Group matches the profile are shown. | None (all memories shown) | None |
| **Search:** | Filters the table by memory name. Can be used at the same time as the profile filter. | Empty | None |

## Tips

- The **Profile:** filter and the **Search:** field work together. You can select a profile and then type in **Search:** to narrow results further within that profile.
- The **Export...** button respects the active profile filter. Exporting while a profile is selected will export only the memories visible in the current filtered view.

## Related

- [Memory Channels overview](overview.md)
- [Search memories by name](search-memories-by-name.md)
- [Export memories for backup or sharing](export-memories-for-backup-or-sharing.md)
- [Sort memory table by column header](sort-memory-table-by-column-header.md)
