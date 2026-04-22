# Delete one or more memories

Use this page to permanently remove one or more stored memory channels from your radio. Deletion requires a connected radio and cannot be undone.

## Before you start

- AetherSDR must be connected to your FLEX-8600. Memory Channels requires an active radio connection.
- Know which memories you want to remove. Use Search: or Profile: to narrow the list if needed.

## Steps

1. Open `Settings > Memory...`.
2. In the memory table, select the row or rows you want to delete.
   - Click a single row to select it.
   - Shift-click to select a contiguous range.
   - Ctrl-click (Command-click on macOS) to add or remove individual rows from the selection.
   - To remove every memory shown, click `Select All`.
3. Confirm your selection. The indicator at the bottom right of the dialog shows how many rows are currently selected (for example, `3 selected`).
4. Click `Remove`.
5. Confirm the deletion when the confirmation dialog appears.

The selected memories are deleted from the radio.

## What each control does

| Control | Behavior |
|---|---|
| `Search:` | Filters the table by memory name. Use this to locate specific entries before selecting them. |
| `Profile:` | Filters the table to show only memories belonging to the selected global profile. |
| Memory table | Displays all memory channels. Supports extended selection: click, Shift-click, and Ctrl-click (Command-click on macOS). |
| `Select All` | Selects every row currently visible in the table. |
| Selection count | Shows `<N> selected` in the bottom-right area of the dialog, reflecting the current selection. |
| `Remove` | Deletes all selected rows after confirmation. |

## Tips

- If you only want to delete memories belonging to one group, set `Profile:` to that group first, then click `Select All` before clicking `Remove`. This limits the selection to the filtered rows.
- If you are unsure which memories to remove, export a backup first before deleting anything.

## Troubleshooting

- **`Remove` has no effect or is not available** — Ensure at least one row is selected in the table. The button requires an active selection.
- **Memories reappear after deletion** — The radio connection may have dropped and re-synced stale data. Check your connection status and try again.

## Related

- [Memory Channels overview](overview.md)
- [Search memories by name](search-memories-by-name.md)
- [Filter memories by profile](filter-memories-by-profile.md)
- [Export memories for backup or sharing](export-memories-for-backup-or-sharing.md)
