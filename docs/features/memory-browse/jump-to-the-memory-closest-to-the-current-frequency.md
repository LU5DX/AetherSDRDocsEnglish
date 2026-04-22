# Jump to the memory closest to the current frequency

The Memory Browser automatically highlights the memory whose stored frequency is nearest to your current tuning. This page explains how to read that highlight and use it to orient yourself within your saved memories.

## Before you start

- The radio must be connected. The Memory Browser requires an active radio connection.
- At least one memory with a valid frequency must be loaded on the radio. If no memories are available, the panel shows "No memories are available yet." and there is nothing to highlight.
- The Memory Browser side panel must be visible. See [Memory Browser overview](overview.md) for how to enable it.

## Steps

1. Tune your radio's VFO to any frequency using your normal method.
2. Look at the Memory Browser panel alongside the panadapter. The panel updates automatically — no button press is required.
3. Find the highlighted row in the memory table. That row is the memory whose stored frequency is closest to your current tuned frequency.
4. The panel scrolls automatically to keep the highlighted row centered in view.

## What each control does

| Control | Behavior |
|---|---|
| Memory table | Lists all memories with valid frequencies, sorted by frequency. Columns: Frequency (MHz, six decimal places), Name. |
| Highlighted row | Marks the single memory closest to the current tuned frequency. Updated each time the tuning changes. |
| "No memories are available yet." | Shown in place of the table when the radio has no memories with valid frequencies loaded. |

## Tips

- The table is sorted by frequency, not by memory index, so the highlighted row will always appear near other entries at similar frequencies.
- If two memories are equidistant from the current frequency, the one with the lower memory index is highlighted.
- The highlight updates as you tune, so you can sweep the VFO and watch the highlight move through the list to find a cluster of memories in a band segment.

## Related

- [Memory Browser overview](overview.md)
- [Browse the radio's stored memories](browse-the-radio-s-stored-memories.md)
- [Activate a memory with a single double-click](activate-a-memory-with-a-single-double-click.md)
