# Upload a WAV file into a slot

Load a pre-recorded WAV file from your computer into one of the Digital Voice Keyer's slots so you can play it back on-air without recording live.

## Before you start

- AetherSDR must be connected to the radio. The DVK panel is only available when a radio connection is active.
- The DVK panel must be visible in the main window. It appears when DVK is enabled or a voice mode is active.
- Have the WAV file ready on your computer.

## Steps

1. Locate the slot row you want to load the file into (F1 through F8).
2. Right-click anywhere on that slot's row frame.
3. In the context menu that appears, select the upload option.
4. In the file dialog that opens, navigate to your WAV file and select it.
5. Confirm the selection. The slot duration label updates from "Empty" to the file length when the transfer completes.

## What each control does

| Control | Behavior | Default |
|---|---|---|
| F1 … F8 slot buttons | Selects and plays that slot; right-click to open the context menu for rename or WAV upload. | — |
| Slot name labels | Shows the name assigned to the slot. | `Recording <n>` |
| Slot duration labels | Displays the recording length, or "Empty" if the slot has no content. | Empty |
| Slot progress bars | Shows live playback or record progress. Hidden when the slot is idle. | — |
| ● REC | Starts recording into the selected slot. | — |
| ■ STOP | Stops recording or playback. | — |
| ▶ PLAY | Plays the selected slot. | — |
| ◀ PREV | Previews the slot through the local speaker. | — |
| Rename edit | Inline rename of a slot triggered via context menu. | — |
| Status indicator | Displays current DVK state: Idle, Recording, or Playing, or a failure message if the radio rejected a command. | Idle |

## Keyboard shortcuts

The DVK panel registers keyboard shortcuts F1–F12 and Escape. These shortcuts are enabled or disabled based on the active slice's mode, ensuring they are mutually exclusive with the CWX panel's F1–F12 shortcuts. When the active slice is in a voice mode, the DVK shortcuts are active regardless of whether the DVK panel is visible.

| Key | Action |
|---|---|
| F1 … F12 | Select and play the corresponding slot (F1 selects slot 1, F2 selects slot 2, etc.). The slot must contain a recording. |
| Escape | Cancel an active rename operation. If no rename is in progress, stops any DVK recording or playback. |

## Tips

- After the upload finishes, verify the slot duration label no longer shows "Empty" before transmitting.
- You can rename the slot immediately after uploading by right-clicking the row again and selecting the rename option. See [Rename a slot](rename-a-slot.md).
- Use the keyboard shortcuts (F1–F8) to quickly select and play stored messages on-air. The Escape key provides a convenient way to stop operation.
- If the REC button momentarily appears checked after recording fails, the button returns to its previous state and the status indicator displays a failure message.

## Troubleshooting

- **Slot duration still shows "Empty" after selecting a file** — The transfer to the radio may have failed. Check that the radio connection is still active, then try the upload again.
- **The context menu does not appear** — Click somewhere else first to deselect any active control, then right-click directly on the slot row frame.
- **Keyboard shortcuts (F1–F8, Escape) do not work** — Ensure the active slice is in a voice mode. The DVK shortcuts are only enabled when the slice mode supports voice keyer operation. If the slice is in CW mode, the CWX panel shortcuts take precedence.
- **Status shows "Transfer failed" instead of a success message** — The WAV file upload encountered an error. Verify the file format is a valid WAV and the radio connection is active, then try again.
- **Status shows a failure message like "Status: Recording (slot 2) failed — ..."** — The radio rejected the recording or playback command. The REC button automatically releases and the panel returns to its previous idle state. Check the radio's microphone connection and that the slot is not in use by another client.

## Related

- [Digital Voice Keyer overview](overview.md)
- [Record a new DVK slot](record-a-new-dvk-slot.md)
- [Play a stored voice-keyer slot](play-a-stored-voice-keyer-slot.md)
- [Rename a slot](rename-a-slot.md)