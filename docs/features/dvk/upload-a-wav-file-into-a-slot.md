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

## Tips

- After the upload finishes, verify the slot duration label no longer shows "Empty" before transmitting.
- You can rename the slot immediately after uploading by right-clicking the row again and selecting the rename option. See [Rename a slot](rename-a-slot.md).

## Troubleshooting

- **Slot duration still shows "Empty" after selecting a file** — The transfer to the radio may have failed. Check that the radio connection is still active, then try the upload again.
- **The context menu does not appear** — Click somewhere else first to deselect any active control, then right-click directly on the slot row frame.

## Related

- [Digital Voice Keyer overview](overview.md)
- [Record a new DVK slot](record-a-new-dvk-slot.md)
- [Play a stored voice-keyer slot](play-a-stored-voice-keyer-slot.md)
- [Rename a slot](rename-a-slot.md)
