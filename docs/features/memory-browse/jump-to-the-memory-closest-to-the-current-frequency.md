# Jump to the Memory Closest to the Current Frequency

The Memory Browser automatically highlights the memory whose stored frequency is nearest to your current tuning. Use this to quickly find and confirm the closest reference point without scrolling manually.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The Memory Browser side panel must be open. See [Memory Browser overview](overview.md).
- The radio must have at least one memory with a valid frequency stored. If none are loaded, the panel shows "No memories are available yet." and no highlighting occurs.

## Steps

1. Open the Memory Browser side panel. It sits alongside the panadapter in the main window.
2. Tune the radio to any frequency using the VFO or panadapter.
3. Look at the memory table. The row corresponding to the memory closest to your current frequency is highlighted automatically.
4. If the highlighted row is not visible, the panel scrolls it to the center of the table.

## What each control does

| Control | Behavior |
|---|---|
| Memory table | Lists all stored memories sorted by frequency. Columns: Frequency (MHz), Name. |
| Highlighted row | Marks the single memory whose frequency is nearest to the current tuned frequency. Updated each time you retune. |
| "No memories are available yet." | Shown in place of the table when the radio has no memories loaded. |

## Tips

- The table is sorted by frequency, so the highlighted row also shows you where your current frequency sits relative to all stored memories.
- If two memories are equally close to the current frequency, the one with the lower memory index is highlighted.
- Memories with a frequency of 0 are excluded from the table and from the closest-match calculation.
- A memory's displayed name comes from its name field if set, its group name if the name is blank, or "Memory N" as a fallback.

## Related

- [Memory Browser overview](overview.md)
- [Browse the radio's stored memories](browse-the-radio-s-stored-memories.md)
- [Activate a memory with a single double-click](activate-a-memory-with-a-single-double-click.md)
