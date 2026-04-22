# Sort Memory Table by Column Header

Click a column header in the Memory Channels dialog to sort all visible memory rows by that column. Use sorting to quickly locate entries by frequency, name, group, or other fields.

## Before you start

- AetherSDR must be connected to the radio. The Memory Channels dialog requires an active radio connection.
- Open the dialog via `Settings > Memory...`.

## Steps

1. Open `Settings > Memory...` to display the Memory Channels dialog.
2. Click any sortable column header in the memory table — for example, **Frequency** or **Name**.
3. The table sorts in ascending order on the first click. A sort indicator arrow appears in the header.
4. Click the same column header again to reverse the sort order to descending.
5. Click a different column header to sort by that column instead, resetting to ascending order.

## What each control does

| Column header | What it sorts by |
|---|---|
| Group | Memory group name |
| Owner | Owner field |
| Frequency | Stored frequency (numeric) |
| Name | Memory name |
| Mode | Operating mode (e.g. USB, CW) |
| Step | Tuning step value |
| FM TX Offset Dir | FM repeater offset direction |
| Repeater Offset | Repeater offset frequency |
| Tone Mode | CTCSS/DCS tone mode |
| Tone Value | Tone frequency or code |
| Squelch | Squelch enabled state |
| Squelch Level | Squelch threshold level |
| RX Filter Low | Low edge of receive filter |
| RX Filter High | High edge of receive filter |
| RTTY Mark | RTTY mark frequency |
| RTTY Shift | RTTY shift value |
| DIGL Offset | Digital lower sideband offset |
| DIGU Offset | Digital upper sideband offset |

The sort indicator arrow in the column header shows the active sort column and direction. Frequency values sort numerically rather than alphabetically.

## Tips

- Sorting applies on top of any active search or profile filter. Narrow the list with **Search:** or **Profile:** first, then sort to arrange the filtered results.
- Sorting does not change the stored order of memories on the radio. It is a display-only operation.

## Related

- [Memory Channels overview](overview.md)
- [Search memories by name](search-memories-by-name.md)
- [Filter memories by profile](filter-memories-by-profile.md)
- [Tune the radio to a stored memory](tune-the-radio-to-a-stored-memory.md)
