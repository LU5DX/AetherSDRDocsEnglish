# Sort Memory Table by Column Header

Click a column header in the Memory Channels dialog to sort all visible memory rows by that column. Use this to quickly find entries by frequency, name, group, or other fields.

## Before you start

- A radio connection is required to open the Memory Channels dialog.
- Open the dialog via `Settings > Memory...`.

## Steps

1. Go to `Settings > Memory...`.
2. In the memory table, click the header of the column you want to sort by (for example, "Frequency" or "Name").
3. The table sorts in ascending order on the first click. A sort indicator arrow appears in the header.
4. Click the same header again to reverse the sort to descending order.
5. Click a different column header to sort by that column instead; the order resets to ascending.

## What each control does

| Column header | What it sorts by |
|---|---|
| Group | Memory group name |
| Owner | Owner name |
| Frequency | Stored frequency (numeric) |
| Name | Memory name |
| Mode | Operating mode (e.g. USB, CW) |
| Step | Tuning step |
| FM TX Offset Dir | Repeater offset direction |
| Repeater Offset | Repeater offset value |
| Tone Mode | CTCSS/DCS tone mode |
| Tone Value | Tone frequency or code |
| Squelch | Squelch enabled state |
| Squelch Level | Squelch threshold level |
| RX Filter Low | Lower RX filter edge |
| RX Filter High | Upper RX filter edge |
| RTTY Mark | RTTY mark frequency |
| RTTY Shift | RTTY shift value |
| DIGL Offset | Digital lower sideband offset |
| DIGU Offset | Digital upper sideband offset |

Sorting applies to the currently visible rows. If a name filter or profile filter is active, only filtered rows are sorted.

## Tips

- Numeric columns such as Frequency use numeric comparison, so 14.225 sorts correctly above 7.200.
- Sorting does not change the stored order of memories on the radio; it only affects the display in this dialog.
- To return to an unsorted view, close and reopen the dialog via `Settings > Memory...`.

## Related

- [Memory Channels overview](overview.md)
- [Search memories by name](search-memories-by-name.md)
- [Filter memories by profile](filter-memories-by-profile.md)
