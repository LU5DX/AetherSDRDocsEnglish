# Delete one or more memories

Use this page to remove one memory or a batch of memories from the radio. Deleted memories are removed from the radio permanently after confirmation.

## Before you start

- AetherSDR must be connected to the radio. The Memory Channels dialog requires an active radio connection.
- Open the dialog via `Settings > Memory...`.

## Steps

1. Open `Settings > Memory...`.
2. Select the memory or memories you want to delete.
   - Click a single row to select it.
   - Shift-click to select a contiguous range.
   - On Linux and Windows, Ctrl-click to add or remove individual rows from the selection. On macOS, use Command-click.
   - To select every row, click **Select All**.
   - To narrow the list before selecting, use the **Search:** field or the **Profile:** combo box. See [Search memories by name](search-memories-by-name.md) and [Filter memories by profile](filter-memories-by-profile.md).
3. Confirm the count shown in the selection indicator (for example, "3 selected") matches your intent.
4. Click **Remove**.
5. When the confirmation dialog appears, confirm the deletion.

The selected memories are removed from the radio.

## What each control does

| Control | Description |
|---|---|
| **Select All** | Selects every row currently visible in the table. |
| **Remove** | Deletes all selected rows. Presents a confirmation prompt before removing. |
| **Search:** | Filters the table by memory name, reducing the rows available for selection. |
| **Profile:** | Filters the table to memories belonging to the chosen global profile. |
| Selection count | Displays the number of currently selected rows as "N selected". |

## Tips

- Use **Select All** after filtering with **Search:** or **Profile:** to quickly select a named subset before clicking **Remove**.
- The selection hint below the table is a reminder: "Tip: Double-click tunes. Shift-click selects a range. Ctrl-click adds or removes rows." (On macOS, Ctrl-click is shown as Command-click.) Use these to build your selection precisely before deleting.

## Troubleshooting

- **Remove is not available or has no effect** — At least one row must be selected. Click a row in the table, then click **Remove**.
- **The memory you want to delete is not visible** — A search term or profile filter may be hiding it. Clear the **Search:** field and set **Profile:** back to its unfiltered state, then locate the row.

## Related

- [Add a memory at current frequency](add-a-memory-at-current-frequency.md)
- [Search memories by name](search-memories-by-name.md)
- [Filter memories by profile](filter-memories-by-profile.md)
- [Export memories for backup or sharing](export-memories-for-backup-or-sharing.md)
