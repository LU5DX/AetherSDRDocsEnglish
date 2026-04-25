# Activate a memory with a single double-click

The Memory Browser lets you tune your radio directly to a stored memory by double-clicking its row in the memory table. This is faster than manually entering a frequency.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The Memory Browser panel must be open and visible in the main window.
- At least one memory with a valid frequency must be stored on the radio. If none are loaded, the panel shows "No memories are available yet." instead of the table.

## Steps

1. Locate the Memory Browser side panel alongside the panadapter.
2. Find the memory you want in the memory table. Columns are **Frequency** and **Name**. The row highlighted in a distinct background color is the memory closest to your current tuned frequency.
3. Double-click any row in the memory table to activate that memory. Your radio tunes to the memory's frequency immediately.

Alternatively, click a row to select it, then press **Enter** to activate it.

## What each control does

| Control | Behavior |
|---|---|
| Memory table | Lists all stored memories that have a valid frequency, sorted by frequency. Double-click or press Enter on a row to activate it. |
| Highlighted row | Indicates the memory whose frequency is closest to the current tuned frequency. The panel scrolls automatically to keep this row in view. |
| "No memories are available yet." | Shown in place of the table when the radio has no memories loaded. |

## Tips

- The highlighted row updates automatically as you tune. If you are browsing near a particular band segment, the closest memory is already marked before you double-click.
- If a memory has no name, the panel displays its group name instead. If neither is set, it falls back to a label based on the memory's index.

## Related

- [Memory Browser overview](overview.md)
- [Browse the radio's stored memories](browse-the-radio-s-stored-memories.md)
- [Jump to the memory closest to the current frequency](jump-to-the-memory-closest-to-the-current-frequency.md)
