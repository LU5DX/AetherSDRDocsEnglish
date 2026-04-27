# Sort Memory Table by Column Header

Click a column header in the Memory Channels dialog to sort the table by that column. This lets you quickly find memories by frequency, name, group, or other fields.

## Before you start

- AetherSDR must be connected to the radio. The Memory Channels dialog requires an active radio connection.
- Open the Memory Channels dialog via `Settings > Memory...`.

## Steps

1. Open `Settings > Memory...`.
2. In the memory table, click any sortable column header — for example, **Frequency** or **Name**.
3. The table sorts in ascending order. A sort indicator arrow appears on the header.
4. Click the same header again to reverse the sort to descending order.
5. Click a different header to sort by that column instead, starting in ascending order.

## Tips

- Not all columns are sortable. If clicking a header has no effect, that column does not support sorting.
- The **Frequency** column uses numeric sorting, so 14.225 sorts correctly between 14.200 and 14.300 rather than as plain text.
- Sorting affects only the display order. It does not change the stored index of any memory on the radio.
- Active search and profile filters remain in effect while sorting. To see all memories in sorted order, clear the **Search:** field and set **Profile:** to its default.

## Related

- [Memory Channels overview](overview.md)
- [Search memories by name](search-memories-by-name.md)
- [Filter memories by profile](filter-memories-by-profile.md)
- [Tune the radio to a stored memory](tune-the-radio-to-a-stored-memory.md)
