# Delete a binding

Remove a single MIDI binding from the bindings table, or clear every binding at once. Use this when a controller assignment is wrong, redundant, or no longer needed.

## Before you start

- The MIDI Mapping dialog must be open. Go to `Settings > MIDI Mapping...`.
- You need at least one existing binding visible in the bindings table.

## Steps

### Delete one binding

1. Open `Settings > MIDI Mapping...`.
2. Locate the binding you want to remove in the bindings table.
3. Click `×` in the rightmost column of that row.

The row is removed immediately. The change is saved automatically.

### Delete all bindings at once

1. Open `Settings > MIDI Mapping...`.
2. Click `Clear All`.

Every row in the bindings table is removed. The change is saved automatically.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| Bindings table | List | Shows all current bindings. Columns: Parameter, MIDI Source, Channel, Invert, Relative, and a delete column. |
| `×` (delete row) | Button | Removes the binding on that row. |
| `Clear All` | Button | Removes every binding in the table. |

## Tips

- There is no confirmation prompt for either `×` or `Clear All`. If you delete bindings by mistake, you can restore them by loading a previously saved profile.
- Before making large changes, save the current state using `Save` so you can recover it with `Load`.

## Related

- [Record a new binding with Learn mode](record-a-new-binding-with-learn-mode.md)
- [Save the current mapping as a named profile](save-the-current-mapping-as-a-named-profile.md)
- [Load a previously saved MIDI profile](load-a-previously-saved-midi-profile.md)
- [MIDI Controller Mapping overview](overview.md)
