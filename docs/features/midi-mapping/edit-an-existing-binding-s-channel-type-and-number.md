# Edit an existing binding's channel, type and number

Correct a MIDI binding's channel, message type, or number after it was recorded with Learn mode or added manually.

## Before you start

- Open the MIDI Controller Mapping dialog: `Settings > MIDI Mapping...`
- The binding you want to edit must be visible in the Bindings table.

## Steps

1. In the Bindings table, locate the row for the binding you want to change.
2. Click the **✎ (edit binding)** button in that row.
3. In the manual editor dialog, change the **Channel**, **Message Type**, and **Number** fields as needed.
4. Click OK to save your changes.
5. The Bindings table updates immediately with the corrected values.

## What each control does

The manual editor dialog lets you set three values for the binding:

| Field | Description |
|---|---|
| Channel | MIDI channel (typically 1–16). |
| Message Type | The MIDI message type, such as Note On, Control Change, or Program Change. |
| Number | The MIDI message number (for example, the CC number or note number). |

The **✎ (edit binding)** button appears in each row of the Bindings table, between the Relative checkbox and the delete button. It opens the same manual editor used by the **Manual…** button in the "Add binding" row.

## Tips

- Use Learn mode to record a new binding if you're unsure of the exact channel, type, and number values — the manual editor is best for fixing a known mistake.
- Changes you make here apply instantly; there is no separate save action for the edit.

## Related

- [Add a MIDI binding manually by typing channel, type and number](add-a-midi-binding-manually-by-typing-channel-type-and-number.md)
- [Record a new binding with Learn mode](record-a-new-binding-with-learn-mode.md)
- [Delete a binding](delete-a-binding.md)
- [MIDI Controller Mapping overview](overview.md)
