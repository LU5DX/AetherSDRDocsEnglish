# Memory Browser Overview

The Memory Browser is a read-only side panel that lists your radio's stored memories alongside the panadapter. It automatically highlights the memory closest to your current tuned frequency so you can orient yourself quickly and jump to a nearby channel.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The panel does not appear or populate without an active radio connection.
- At least one memory must be stored on the radio. If none are loaded, the panel displays "No memories are available yet." in place of the table.

## How it works

The Memory Browser panel sits inside the main window splitter, to the side of the panadapter. When memory browsing is enabled, the panel opens automatically within that layout — it is not a floating window.

The panel continuously tracks the current tuned frequency. As you tune, the panel finds the stored memory whose frequency is nearest to your VFO and highlights that row. The table also scrolls to keep the highlighted row visible, so you do not need to scroll manually.

Memories are listed in ascending frequency order. Each row shows two columns:

| Column | Contents |
|---|---|
| Frequency | Memory frequency in MHz, displayed to six decimal places. |
| Name | Memory name if set; falls back to the group name; falls back to "Memory _N_" where _N_ is the memory index. |

When the radio reports no memories, the table is hidden and the label "No memories are available yet." is shown instead.

## What each control does

| Control | Behavior |
|---|---|
| Memory table | Lists all stored memories with valid frequencies, sorted by frequency. Double-click a row, or select it and press Enter, to activate that memory. |
| Highlighted row | The row whose frequency is closest to the current tuned frequency. The panel scrolls automatically to keep this row centered. |
| "No memories are available yet." | Shown in place of the table when the radio has no memories loaded. Disappears as soon as memories become available. |

## Tips

- If two memories are equidistant from the current frequency, the one with the lower memory index is highlighted.
- Memories with a frequency of 0 are excluded from the table entirely and are never highlighted.
- Long names that exceed the column width are truncated with an ellipsis. Hover over a cell to see the full text in a tooltip.

## Related

- [Browse the radio's stored memories](browse-the-radio-s-stored-memories.md)
- [Jump to the memory closest to the current frequency](jump-to-the-memory-closest-to-the-current-frequency.md)
- [Activate a memory with a single double-click](activate-a-memory-with-a-single-double-click.md)
