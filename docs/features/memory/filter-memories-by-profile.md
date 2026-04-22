# Filter memories by profile

Use the Profile filter in Memory Channels to narrow the table to memories belonging to a specific global profile. This is useful when you have a large memory list and want to see only the entries associated with one operating setup.

## Before you start

- AetherSDR must be connected to the radio. Memory Channels requires an active radio connection.
- At least one global profile must exist on the radio. The Profile filter lists only profiles the radio has reported. To create profiles, use `Profiles > Profile Manager...`.

## Steps

1. Open `Settings > Memory...` to open the Memory Channels dialog.
2. Locate the `Profile:` combo box in the filter row at the top of the dialog.
3. Click the `Profile:` combo box and select the profile you want to filter by.

The memory table updates immediately to show only memories whose Group matches the selected profile. Memories belonging to other profiles are hidden but not deleted.

4. To remove the filter and show all memories, open the `Profile:` combo box and select the blank or "all" entry at the top of the list.

## What each control does

| Control | Behavior |
|---|---|
| `Profile:` combo box | Filters the memory table to show only memories associated with the selected global profile. The list is populated from the profiles reported by the connected radio. |
| Memory table | Displays the filtered result. Columns include Group, Owner, Frequency, Name, Mode, and others. The Group column reflects the profile association used for filtering. |

## Tips

- The `Profile:` filter and the `Search:` text field work together. You can select a profile and type a name in `Search:` to narrow the table further.
- When you use `Export...` while a profile filter is active, only the memories matching the current filter profile are included in the export file.

## Troubleshooting

- **The `Profile:` combo box is empty or shows no profiles** — The radio has not reported any global profiles. Verify the radio connection is active and that at least one profile exists. Use `Profiles > Profile Manager...` to create profiles.
- **Expected memories do not appear after selecting a profile** — The memory's Group field may not match the profile name exactly. Open the memory for editing with Edit and check the Group column value.

## Related

- [Memory Channels overview](overview.md)
- [Search memories by name](search-memories-by-name.md)
- [Add a memory at current frequency](add-a-memory-at-current-frequency.md)
- [Export memories for backup or sharing](export-memories-for-backup-or-sharing.md)
