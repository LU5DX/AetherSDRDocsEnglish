# Rename a slot

Give a DVK slot a meaningful name so you can identify it at a glance instead of the default "Recording \<n\>" label.

## Before you start

- The Digital Voice Keyer panel must be visible in the main window. It appears when DVK is enabled or a voice mode is active.
- A radio connection must be established.

## Steps

1. In the Digital Voice Keyer panel, locate the slot you want to rename (F1 through F8).
2. Right-click the slot row.
3. From the context menu, select "Rename".
4. The slot name label is replaced by the "Rename edit" text field. Type the new name.
5. Press Enter to confirm, or press Escape to cancel without saving.

## What each control does

| Control | Behavior | Default |
|---|---|---|
| Slot name labels | Displays the current name of each slot. | `Recording <n>` |
| Rename edit | Inline text field that appears when a rename is triggered via the context menu. Type the new name and press Enter to apply. | — |
| F1 … F8 slot buttons | Selects and plays that slot; right-click to rename or upload a WAV. | — |
| Slot duration labels | Displays recording length or 'Empty'. | Empty |
| Slot progress bars | Live playback / record progress. | — |
| ● REC | Starts recording into the selected slot. | — |
| ■ STOP | Stops recording or playback. | — |
| ▶ PLAY | Plays the selected slot. | — |
| ◀ PREV | Previews the slot through the local speaker. | — |

## Status indicator

The panel shows a status indicator at the top:

| Label | Possible states | Meaning |
|---|---|---|
| Status: | Idle, Recording, Playing | Current DVK state. If a command fails, the status shows the failure message (e.g., "Status: Record (slot 2) failed — reason"). The panel buttons reset to reflect the current state after a failure. |

## Keyboard shortcuts

The following keyboard shortcuts are active based on the active slice's mode (mutually exclusive with CWX panel shortcuts):

- **F1 through F8** — Select and play the corresponding slot (F1 = slot 1, F2 = slot 2, etc.).
- **F9 through F12** — Select and play slots 9 through 12 (if your radio supports more than 8 slots).
- **Escape** — Cancel a rename operation if the rename edit field is open; otherwise stop any DVK recording or playback.

Shortcuts are automatically enabled when the active slice is in a voice mode and disabled when switching to a CW mode, preventing conflicts with the CWX panel while allowing the keys to fire regardless of panel visibility.

## Tips

- Double-clicking the slot name label also opens the "Rename edit" field directly.
- Pressing Escape while the "Rename edit" field is open cancels the rename and restores the previous name.
- If a record or playback command is rejected by the radio (e.g., another client holds the DVK resource), the status indicator displays a failure message and the panel buttons return to their previous state.

## Related

- [Digital Voice Keyer overview](overview.md)
- [Record a new DVK slot](record-a-new-dvk-slot.md)
- [Upload a WAV file into a slot](upload-a-wav-file-into-a-slot.md)