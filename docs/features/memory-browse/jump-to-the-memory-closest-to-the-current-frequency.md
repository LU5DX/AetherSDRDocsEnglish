# Jump to the memory closest to the current frequency

The Memory Browser automatically highlights the memory whose frequency is nearest to your current tuning. This page explains how to read that highlight and scroll to it.

## Before you start

- AetherSDR must be connected to the radio. The Memory Browser requires an active radio connection.
- At least one memory with a valid frequency must be stored on the radio. If none are present, the panel shows "No memories are available yet." instead of the table.
- The Memory Browser side panel must be visible in the main window.

## Steps

1. Tune your radio VFO to any frequency using your normal method.
2. Look at the Memory Browser panel to the side of the panadapter. The memory table updates automatically.
3. Locate the highlighted row. The highlighted row is the memory whose stored frequency is closest to your current tuned frequency. If two memories are equidistant, the one with the lower memory index is highlighted.
4. The panel scrolls automatically to center the highlighted row in view. No additional action is required.

## What each control does

| Control | Behavior |
|---|---|
| Memory table | Lists all memories with valid frequencies, sorted by frequency. Columns: Frequency (MHz, six decimal places), Name. |
| Highlighted row | Indicates the memory closest to the current tuned frequency. Updated each time the tuning changes. |
| "No memories are available yet." | Shown in place of the table when the radio has no memories with valid frequencies loaded. |

## Tips

- The highlight updates whenever your tuned frequency changes, so you can use it as a live nearest-memory indicator while spinning the VFO.
- Memory names are drawn from the memory's name field first, then the group field, then a fallback label of the form `Memory N`. Long names are truncated with an ellipsis; hover over a row to see the full name in a tooltip.
- To act on the highlighted memory, double-click its row or press Enter to activate it.

## Related

- [Memory Browser overview](overview.md)
- [Activate a memory with a single double-click](activate-a-memory-with-a-single-double-click.md)
- [Browse the radio's stored memories](browse-the-radio-s-stored-memories.md)
