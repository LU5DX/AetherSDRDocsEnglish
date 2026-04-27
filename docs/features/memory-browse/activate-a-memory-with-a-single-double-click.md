# Activate a memory with a single double-click

The Memory Browser lets you tune the radio directly to a stored memory by double-clicking its row in the memory table. This is faster than manually entering a frequency.

## Before you start

- AetherSDR must be connected to the radio. The Memory Browser requires an active radio connection.
- At least one memory with a valid frequency must be stored on the radio. If none exist, the panel shows "No memories are available yet." and the table is not displayed.
- The Memory Browser side panel must be visible in the main window.

## Steps

1. Locate the Memory Browser side panel to the left or right of the panadapter.
2. Find the memory you want in the memory table. Columns are **Frequency** and **Name**.
3. Double-click the row for that memory.

The radio tunes to the memory's stored frequency immediately.

## What each control does

| Control | Behavior |
|---|---|
| Memory table | Lists all stored memories that have a valid frequency, sorted by frequency. Double-click or press Enter to activate a row. |
| Highlighted row | Indicates the memory closest to the currently tuned frequency. The panel scrolls automatically to keep this row visible. |
| "No memories are available yet." | Shown in place of the table when the radio has no memories with a valid frequency loaded. |

## Tips

- You can also press Enter to activate the currently selected row without reaching for the mouse.
- The highlighted row tracks your current tuning automatically. If you tune across the band, the highlight moves to whichever stored memory is nearest your current frequency.
- If a memory has no name, the table shows its group name instead. If neither exists, it shows a generated label such as "Memory 3".

## Troubleshooting

- **The memory table is not visible** — The radio has no memories with a valid frequency. The label "No memories are available yet." appears instead. Add memories through `Settings > Memory...` or on the radio itself, then reconnect or refresh.
- **Double-clicking does nothing** — Confirm the radio is still connected. The Memory Browser requires an active radio connection to activate memories.

## Related

- [Memory Browser overview](overview.md)
- [Browse the radio's stored memories](browse-the-radio-s-stored-memories.md)
- [Jump to the memory closest to the current frequency](jump-to-the-memory-closest-to-the-current-frequency.md)
