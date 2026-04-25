# Edit a memory's name, mode or offset inline

Use this page to change a stored memory's name, mode, repeater offset, or any other editable field without leaving the Memory Channels dialog.

## Before you start

- AetherSDR must be connected to the radio. The Memory Channels dialog requires an active radio connection.
- The memory you want to edit must already exist. To create a new memory, see [Add a memory at current frequency](add-a-memory-at-current-frequency.md).

## Steps

1. Open `Settings > Memory...`.
2. Locate the memory you want to edit. Use the **Search:** field or the **Profile:** combo box to narrow the list if needed.
3. Click the row to select it.
4. Click **Edit**. The selected row enters inline-edit mode.
5. Click the cell you want to change — for example, the **Name**, **Mode**, or **Repeater Offset** column — and type the new value.
6. Press Enter or click another cell to confirm each change.
7. Repeat for any other columns in the same row.
8. Click outside the row or select a different row to finish editing.

## What each control does

| Column | What it stores |
|---|---|
| Group | Group or profile label for the memory. |
| Owner | Owner tag for the memory. |
| Frequency | Stored frequency in MHz. |
| Name | Human-readable label. |
| Mode | Operating mode (e.g. USB, LSB, CW, FM). |
| Step | Tuning step size. |
| FM TX Offset Dir | Repeater offset direction. |
| Repeater Offset | Repeater offset value. |
| Tone Mode | CTCSS/DCS tone mode. |
| Tone Value | Tone frequency or code. |
| Squelch | Squelch on/off (checkbox). |
| Squelch Level | Squelch threshold level. |
| RX Filter Low | Lower edge of the receive filter. |
| RX Filter High | Upper edge of the receive filter. |
| RTTY Mark | RTTY mark frequency offset. |
| RTTY Shift | RTTY shift value. |
| DIGL Offset | DIGL mode offset. |
| DIGU Offset | DIGU mode offset. |

The **Edit** button enters inline-edit mode on the selected memory. All columns listed above are editable inline.

## Tips

- You can also double-click a row to tune the radio to that memory rather than edit it. To edit, use the **Edit** button rather than double-clicking.
- To find a specific memory quickly before editing, type part of its name into the **Search:** field. The table filters as you type.

## Troubleshooting

- **Edit button does nothing** — No row is selected. Click a row in the memory table first, then click **Edit**.
- **Changes do not appear to save** — Confirm each cell edit by pressing Enter or moving focus to another cell before clicking away from the row.

## Related

- [Add a memory at current frequency](add-a-memory-at-current-frequency.md)
- [Search memories by name](search-memories-by-name.md)
- [Filter memories by profile](filter-memories-by-profile.md)
- [Tune the radio to a stored memory](tune-the-radio-to-a-stored-memory.md)
- [Delete one or more memories](delete-one-or-more-memories.md)
