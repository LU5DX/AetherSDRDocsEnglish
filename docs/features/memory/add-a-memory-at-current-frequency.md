# Add a memory at current frequency

Save the active VFO frequency, mode, and filter settings as a named memory channel so you can return to that frequency quickly later.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The Memory Channels dialog requires an active radio connection.
- Tune the active slice to the frequency you want to store.

## Steps

1. Open `Settings > Memory...`.
2. Click `Add`.

The new memory appears in the memory table with the current VFO frequency pre-filled in the Frequency column.

3. To give the memory a name immediately, select the new row, click `Edit`, type a name in the Name column, then press Enter to confirm.

## What each control does

| Control | Description |
|---|---|
| `Add` | Creates a new memory row at the current VFO frequency. |
| `Edit` | Enters inline-edit mode on the selected row so you can update any field. |
| Memory table | Displays all stored memories. Columns: Group, Owner, Frequency, Name, Mode, Step, FM TX Offset Dir, Repeater Offset, Tone Mode, Tone Value, Squelch, Squelch Level, RX Filter Low, RX Filter High, RTTY Mark, RTTY Shift, DIGL Offset, DIGU Offset. |

## Tips

- Double-clicking a row tunes the active slice to that memory without closing the dialog.
- On Linux and Windows, Ctrl-click adds or removes individual rows from the selection. On macOS, use Command-click.

## Related

- [Edit a memory's name, mode or offset inline](edit-a-memory-s-name-mode-or-offset-inline.md)
- [Tune the radio to a stored memory](tune-the-radio-to-a-stored-memory.md)
- [Delete one or more memories](delete-one-or-more-memories.md)
- [Memory Channels overview](overview.md)
