# Add a memory at current frequency

Save the active VFO frequency, mode, and filter settings as a named memory channel so you can return to it quickly later.

## Before you start

- AetherSDR must be connected to the radio. The Memory Channels dialog requires an active radio connection.
- Tune the active slice to the frequency you want to store.

## Steps

1. Open `Settings > Memory...`.
2. Click `Add`.

The radio creates a new memory row populated with the current VFO frequency, mode, and filter settings. The row appears in the memory table.

3. To name or edit the new entry immediately, select the row and click `Edit`, then modify the fields inline.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| `Add` | Button | Creates a new memory at the current VFO. |
| `Edit` | Button | Enters inline-edit mode on the selected memory row. |
| Memory table | List | Displays all stored memories. Columns: Group, Owner, Frequency, Name, Mode, Step, FM TX Offset Dir, Repeater Offset, Tone Mode, Tone Value, Squelch, Squelch Level, RX Filter Low, RX Filter High, RTTY Mark, RTTY Shift, DIGL Offset, DIGU Offset. |

## Tips

- Double-clicking a row in the memory table tunes the active slice to that memory directly.
- On Linux and Windows, Ctrl+N opens the Add action from within the Memory Channels dialog.

## Troubleshooting

- **`Add` has no effect** — The dialog requires an active radio connection. If the radio is not connected, connect first via `Settings > Connect to Radio...`, then reopen `Settings > Memory...`.

## Related

- [Edit a memory's name, mode or offset inline](edit-a-memory-s-name-mode-or-offset-inline.md)
- [Tune the radio to a stored memory](tune-the-radio-to-a-stored-memory.md)
- [Delete one or more memories](delete-one-or-more-memories.md)
- [Memory Channels overview](overview.md)
