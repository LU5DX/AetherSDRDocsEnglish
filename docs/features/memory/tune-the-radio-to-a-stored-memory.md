# Tune the Radio to a Stored Memory

Open the Memory Channels dialog to find a stored frequency and send it directly to the active slice receiver.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The Memory Channels dialog requires an active radio connection.
- At least one memory must already be stored. See [Add a memory at current frequency](add-a-memory-at-current-frequency.md) if you have none.

## Steps

1. Click `Settings > Memory...` to open the Memory Channels dialog.
2. Locate the memory you want. Use the `Search:` field to filter by name, or use the `Profile:` combo box to narrow the list by profile.
3. Click the row in the memory table to select it.
4. Click `Tune`.

The active slice tunes to the frequency, mode, and filter settings stored in that memory.

**Shortcut:** Double-click any row in the memory table to tune immediately without clicking `Tune`.

## What each control does

| Control | Behavior |
|---|---|
| `Search:` | Filters the memory table to rows whose name matches the text you type. Press Enter or clear the field to reset. |
| `Profile:` | Filters the table to memories belonging to the selected global profile. |
| Memory table | Displays all stored memories. Columns include Group, Owner, Frequency, Name, Mode, Step, FM TX Offset Dir, Repeater Offset, Tone Mode, Tone Value, Squelch, Squelch Level, RX Filter Low, RX Filter High, RTTY Mark, RTTY Shift, DIGL Offset, and DIGU Offset. Click a column header to sort by that column. |
| `Tune` | Tunes the active slice to the selected memory. Requires exactly one row to be selected. |

## Tips

- If you cannot see the memory you want, check whether `Profile:` is set to a filter that excludes it. Set `Profile:` to show all entries.
- On Linux and Windows, hold Ctrl and click to select individual rows without deselecting others. On macOS, use Command-click. Only the first selected memory is used when you click `Tune`.

## Troubleshooting

- **`Tune` has no effect or is disabled** — Confirm that a single row is selected in the memory table and that AetherSDR is connected to the radio.
- **The memory you want does not appear in the table** — The `Search:` or `Profile:` filter may be hiding it. Clear the `Search:` field and set `Profile:` to show all entries.

## Related

- [Add a memory at current frequency](add-a-memory-at-current-frequency.md)
- [Recall an FM repeater memory and restore offset and CTCSS tone](recall-an-fm-repeater-memory-and-restore-offset-and-ctcss-tone.md)
- [Search memories by name](search-memories-by-name.md)
- [Filter memories by profile](filter-memories-by-profile.md)
- [Memory Channels overview](overview.md)
