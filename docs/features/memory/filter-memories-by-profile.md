# Filter memories by profile

Use the Profile filter in the Memory Channels dialog to narrow the memory table to entries belonging to a specific global profile. This is useful when you have a large memory list and want to see only the channels relevant to your current operating context.

## Before you start

- The radio must be connected. The Memory Channels dialog requires an active radio connection.
- At least one global profile must exist on the radio. The `Profile:` combo box is populated from the radio's active global profiles.

## Steps

1. Open `Settings > Memory...`.
2. Locate the `Profile:` combo box in the filter row at the top of the dialog.
3. Click the `Profile:` combo box and select the profile you want to filter by.
4. The memory table updates immediately to show only entries matching the selected profile.

To clear the filter and show all memories, select the blank or default entry at the top of the `Profile:` combo box.

## What each control does

| Control | Behavior |
|---|---|
| `Profile:` combo box | Filters the memory table by the selected global profile. Populated from the radio's active global profiles. |
| Memory table | Displays only the rows whose Group matches the selected profile while the filter is active. |

## Tips

- Profile filtering and name search (`Search:`) work together. You can select a profile in `Profile:` and type in `Search:` to narrow results further by memory name.
- The `Export...` button respects the current profile filter — only memories visible under the active filter are exported.

## Related

- [Memory Channels overview](overview.md)
- [Search memories by name](search-memories-by-name.md)
- [Export memories for backup or sharing](export-memories-for-backup-or-sharing.md)
