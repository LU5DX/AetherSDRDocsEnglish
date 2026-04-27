# Jump to the memory closest to the current frequency

The Memory Browser automatically highlights the stored memory whose frequency is nearest to your current tuning. This lets you quickly see and scroll to the most relevant memory without searching through the full list.

## Before you start

- AetherSDR must be connected to the radio. The Memory Browser requires an active radio connection.
- The radio must have at least one memory with a valid frequency stored. If no memories are loaded, the panel shows "No memories are available yet." and no highlighting occurs.
- The Memory Browser side panel must be open. See [Memory Browser overview](overview.md) for how to enable it.

## Steps

1. Open the Memory Browser side panel. It appears alongside the panadapter in the main window.
2. Tune the radio to any frequency using your normal method (VFO knob, panadapter click, or direct entry).
3. Look at the memory table. The row whose frequency is closest to the current tuning is highlighted with a distinct background.
4. The panel automatically scrolls the table so the highlighted row is centered in view. No additional action is required.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| Memory table | Lists all stored memories sorted by frequency, lowest to highest. | Columns: Frequency (MHz, six decimal places), Name. |
| Highlighted row | Marks the memory closest to the current tuned frequency. | Ties are broken by memory index — the lower index wins. |
| "No memories are available yet." | Shown in place of the table when the radio has no valid memories loaded. | Disappears as soon as at least one memory with a non-zero frequency is available. |

## Tips

- The highlight updates whenever the tuned frequency changes. If you retune, the highlighted row moves to whichever memory is now closest.
- Memories with a frequency of 0 MHz are excluded from the table entirely and cannot be selected as the closest match.
- If a memory has no name, the panel displays its group name instead. If neither is set, it shows "Memory" followed by its index number.

## Related

- [Memory Browser overview](overview.md)
- [Browse the radio's stored memories](browse-the-radio-s-stored-memories.md)
- [Activate a memory with a single double-click](activate-a-memory-with-a-single-double-click.md)
