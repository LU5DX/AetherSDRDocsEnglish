# Sort Memory Table by Column Header

Click a column header in the Memory Channels dialog to sort the memory table by that column. Use this to quickly bring related entries together — for example, sorting by Frequency to scan stored channels in band order, or by Group to cluster memories by category.

## Before you start

- AetherSDR must be connected to a radio. The Memory Channels dialog requires an active radio connection.
- Open the dialog via `Settings > Memory...`.

## Steps

1. Open `Settings > Memory...`.
2. Click any sortable column header in the memory table — for example, **Frequency**, **Name**, **Group**, or **Mode**.
3. The table sorts in ascending order. A sort indicator arrow appears on the header.
4. Click the same header again to reverse to descending order.
5. Click a different header to sort by that column instead, resetting to ascending order.

## What each control does

| Column header | What it sorts by |
|---|---|
| Group | Memory group name |
| Owner | Owner field |
| Frequency | Stored frequency (numeric) |
| Name | Memory name |
| Mode | Operating mode |
| Step | Tuning step |
| FM TX Offset Dir | Repeater offset direction |
| Repeater Offset | Repeater offset value |
| Tone Mode | Tone mode setting |
| Tone Value | Tone frequency value |
| Squelch | Squelch enabled state |
| Squelch Level | Squelch threshold |
| RX Filter Low | Lower filter edge |
| RX Filter High | Upper filter edge |
| RTTY Mark | RTTY mark frequency |
| RTTY Shift | RTTY shift value |
| DIGL Offset | Digital lower offset |
| DIGU Offset | Digital upper offset |

Not all columns may support sorting. If clicking a header produces no sort indicator, that column is not sortable.

## Tips

- Frequency values sort numerically, not as text, so 14.225 sorts correctly between 14.200 and 14.300.
- Sorting does not reorder memories on the radio itself — it only changes the display order in the table.
- Sorting persists while the dialog is open. Closing and reopening the dialog resets the sort order.
- Use the **Search:** field alongside sorting to narrow results before sorting. See [Search memories by name](search-memories-by-name.md).

## Related

- [Memory Channels overview](overview.md)
- [Search memories by name](search-memories-by-name.md)
- [Filter memories by profile](filter-memories-by-profile.md)
- [Tune the radio to a stored memory](tune-the-radio-to-a-stored-memory.md)
