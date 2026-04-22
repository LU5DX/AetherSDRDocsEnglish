# Activate a memory with a single double-click

The Memory Browser lets you tune the radio directly to a stored memory by double-clicking its row in the memory table. This saves you from manually entering a frequency.

## Before you start

- AetherSDR must be connected to the radio. The Memory Browser requires an active radio connection.
- The Memory Browser panel must be visible. It appears as a side panel in the main window when memory browsing is enabled.
- At least one memory with a valid frequency must be stored on the radio. If none are loaded, the panel shows "No memories are available yet." instead of the table.

## Steps

1. Locate the Memory Browser side panel next to the panadapter.
2. Find the memory you want in the memory table. Columns show Frequency and Name.
3. Double-click the row for that memory.

The radio tunes to that memory's frequency immediately.

## What each control does

| Control | Behavior |
|---|---|
| Memory table | Lists all stored memories with valid frequencies, sorted by frequency. Double-click or press Enter to activate a row. |
| Highlighted row | Indicates the memory closest to the current tuned frequency. The panel scrolls automatically to keep this row visible. |
| "No memories are available yet." | Shown in place of the table when the radio has no memories loaded. |

## Tips

- You can also press Enter to activate the currently selected row if you prefer keyboard navigation.
- The highlighted row tracks your VFO as you tune, so the closest memory is always easy to spot.
- If a memory has no name, the table falls back to its group name, or displays a placeholder such as "Memory 1".

## Related

- [Memory Browser overview](overview.md)
- [Browse the radio's stored memories](browse-the-radio-s-stored-memories.md)
- [Jump to the memory closest to the current frequency](jump-to-the-memory-closest-to-the-current-frequency.md)
