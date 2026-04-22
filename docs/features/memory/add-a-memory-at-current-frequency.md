# Add a memory at current frequency

Save the active VFO frequency, mode, and filter settings as a named memory channel so you can return to it later without retuning manually.

## Before you start

- AetherSDR must be connected to the radio. The Memory Channels dialog requires an active radio connection.
- Tune the active slice to the frequency you want to store before opening the dialog.

## Steps

1. Click `Settings > Memory...` to open the Memory Channels dialog.
2. Click `Add`.

The radio creates a new memory row at the current VFO frequency. The new entry appears in the memory table with columns populated from the active slice, including Frequency, Mode, and filter settings.

3. To name the memory immediately, select the new row and click `Edit`, then type a name in the Name column.
4. Press Enter or click away from the cell to confirm the edit.

## What each control does

| Control | Behavior |
|---|---|
| `Add` | Creates a new memory at the current VFO frequency. |
| `Edit` | Enters inline-edit mode on the selected memory row. Use this after adding to set the Name, Group, or other fields. |
| Memory table | Displays all stored memories. Columns: Group, Owner, Frequency, Name, Mode, Step, FM TX Offset Dir, Repeater Offset, Tone Mode, Tone Value, Squelch, Squelch Level, RX Filter Low, RX Filter High, RTTY Mark, RTTY Shift, DIGL Offset, DIGU Offset. |

## Tips

- Double-clicking a memory row tunes the active slice to that memory. If you add a memory and want to verify it, double-click the row rather than clicking `Tune`.
- On Linux and Windows, Ctrl-click adds or removes individual rows from the selection without losing other selected rows.
- You can use Ctrl+N as a keyboard shortcut to add a memory without clicking the `Add` button.

## Related

- [Edit a memory's name, mode or offset inline](edit-a-memory-s-name-mode-or-offset-inline.md)
- [Tune the radio to a stored memory](tune-the-radio-to-a-stored-memory.md)
- [Search memories by name](search-memories-by-name.md)
- [Filter memories by profile](filter-memories-by-profile.md)
- [Memory Channels overview](overview.md)
