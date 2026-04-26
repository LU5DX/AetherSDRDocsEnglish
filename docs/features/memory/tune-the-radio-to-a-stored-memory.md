# Tune the Radio to a Stored Memory

Open the Memory Channels dialog to find a stored frequency and send it directly to the active slice receiver.

## Before you start

- AetherSDR must be connected to the radio. The Memory Channels dialog requires an active radio connection.
- At least one memory must already be stored. See [Add a memory at current frequency](add-a-memory-at-current-frequency.md) if you have none.

## Steps

1. Click `Settings > Memory...` to open the Memory Channels dialog.
2. Optional: Type a name in the **Search:** field to narrow the list, or select a group from the **Profile:** combo box to filter by profile.
3. Click the row in the memory table that contains the frequency you want to tune to. The row highlights and the selection count at the bottom right updates to show `1 selected`.
4. Click **Tune**.

The active slice tunes immediately to the stored frequency, mode, and filter settings from that memory.

## Tips

- Double-clicking any row in the memory table tunes the active slice to that memory without clicking **Tune**.
- If you need to tune to a memory that is buried in a long list, use the **Search:** field to filter by name first. The table updates as you type. Press Enter after typing to tune the currently highlighted row directly.
- On Linux and Windows, Ctrl-click selects or deselects individual rows without clearing the rest of the selection. Only the first selected row is used when you click **Tune** or double-click.

## Troubleshooting

- **Tune does nothing** — Confirm the radio is connected. The dialog requires an active radio connection. Check that exactly one row is selected in the table.
- **The memory you want is not visible** — A filter may be active. Clear the **Search:** field using its clear button and set **Profile:** back to its default (no filter) to show all memories.

## Related

- [Memory Channels overview](overview.md)
- [Add a memory at current frequency](add-a-memory-at-current-frequency.md)
- [Search memories by name](search-memories-by-name.md)
- [Filter memories by profile](filter-memories-by-profile.md)
- [Edit a memory's name, mode or offset inline](edit-a-memory-s-name-mode-or-offset-inline.md)
