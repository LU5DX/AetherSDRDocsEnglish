# Filter memories by profile

Use the Profile filter in the Memory Channels dialog to narrow the memory table to entries belonging to a specific global profile. This is useful when you have a large memory list and want to see only the entries relevant to a particular operating context.

## Before you start

- AetherSDR must be connected to the radio. The Memory Channels dialog requires an active radio connection.
- At least one global profile must exist on the radio. Profiles are managed under `Profiles > Profile Manager...`.

## Steps

1. Open `Settings > Memory...` to open the Memory Channels dialog.
2. Locate the **Profile:** combo box in the filter row at the top of the dialog.
3. Click the **Profile:** combo box and select the profile you want to filter by.
4. The memory table updates immediately to show only memories whose Group matches the selected profile.
5. To remove the filter and show all memories, open the **Profile:** combo box and select the blank or all-entries option at the top of the list.

## What each control does

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| **Profile:** | Filters the memory table by the selected global profile. Only memories whose Group matches the profile are shown. | No filter (all memories shown) | None |
| **Search:** | Filters the table by memory name. Works together with the profile filter — both filters apply at the same time. | Empty | None |

## Tips

- The **Profile:** filter and the **Search:** field stack. You can select a profile in **Profile:** and then type in **Search:** to narrow results further within that profile.
- If the **Profile:** combo box is empty or contains only a blank entry, no global profiles have been loaded from the radio yet. Verify the radio connection and that at least one profile exists under `Profiles > Profile Manager...`.

## Troubleshooting

- **The Profile: combo box is empty** — The radio has not reported any global profiles, or AetherSDR is not connected. Check the connection status and ensure profiles exist under `Profiles > Profile Manager...`.
- **Filtering by profile shows no memories** — The memories on the radio may not have their Group field set to match the selected profile name. Edit the relevant memories and set the Group column to the correct profile name.

## Related

- [Memory Channels overview](overview.md)
- [Search memories by name](search-memories-by-name.md)
- [Edit a memory's name, mode or offset inline](edit-a-memory-s-name-mode-or-offset-inline.md)
- [Sort memory table by column header](sort-memory-table-by-column-header.md)
