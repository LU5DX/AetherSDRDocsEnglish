# Preview a slot without transmitting

Use this page to audition a DVK slot through your local speaker before sending it on air. Preview lets you confirm the audio content and level without keying the transmitter.

## Before you start

- AetherSDR must be connected to the radio. The DVK panel requires an active radio connection.
- The slot you want to preview must contain a recording. Slots showing "Empty" cannot be previewed.

## Steps

1. Open the Digital Voice Keyer panel in the MainWindow central area.
2. Click the slot row (F1 through F8) you want to preview. The selected row highlights with a blue border.
3. Click ◀ PREV.
4. Listen to the audio through your local speaker. The slot's progress bar turns blue and advances during playback.
5. When the slot finishes, playback stops automatically and the status returns to "Status: Idle". To stop early, click ■ STOP or press Escape.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| F1 … F8 slot buttons | Selects the slot. If the slot is currently playing back on air, clicking again stops it. Right-click to rename or upload a WAV. | Does not trigger preview. |
| Slot name labels | Shows the name of each slot. | Default name is "Recording \<n\>". |
| Slot duration labels | Shows recording length or "Empty". | A slot showing "Empty" cannot be previewed. |
| Slot progress bars | Displays playback progress in blue during preview. | Hidden when idle. |
| ● REC | Starts recording into the selected slot. | |
| ■ STOP | Stops any active recording, playback, or preview. | Also activated by Escape. |
| ▶ PLAY | Plays the selected slot on air. | Does not preview. |
| ◀ PREV | Starts preview of the selected slot through the local speaker. Click again to stop. | Does not transmit. |
| Rename edit | Inline rename of a slot triggered via context menu. | |
| Status: Idle / Recording / Playing | Shows the current DVK state at the bottom of the panel. | |

## Keyboard shortcuts

The DVK panel registers F1–F12 and Escape keyboard shortcuts. Shortcut availability is controlled by the active slice's operating mode, not by panel visibility. This ensures the DVK shortcuts are enabled only when the active slice is in a compatible mode, and are mutually exclusive with the CWX panel's F1–F12 shortcuts to prevent key conflicts.

| Key | Action |
|---|---|
| F1–F12 | Select and play the corresponding slot (F1 = slot 1, F2 = slot 2, etc.). Slots beyond F8 (F9–F12) are non-functional in most configurations. |
| Escape | Stops recording, playback, or preview. If a rename edit is active, cancels the rename instead. |

## Tips

- If you click ◀ PREV on a slot that is already in preview, it stops the preview.
- Pressing Escape stops an active preview without using the mouse.
- The F-key buttons and F1–F12 keyboard shortcuts trigger on-air playback, not preview. Use ◀ PREV specifically when you do not want to transmit.
- Right-click a slot button to rename it or upload a WAV file.
- Keyboard shortcuts work regardless of whether the DVK panel is currently visible, provided the active slice mode supports them.

## Troubleshooting

- **◀ PREV has no effect** — The selected slot is empty. Check that the slot's duration label does not show "Empty". Record audio or upload a WAV file first, then retry.
- **No audio heard during preview** — Preview routes audio to the local speaker. Verify your system audio output is correctly configured and not muted.
- **F1–F12 keyboard shortcuts do not work** — The active slice's operating mode may not support DVK shortcuts. Switch to a mode that supports DVK operation. If the CWX panel's F1–F12 shortcuts are enabled, the DVK shortcuts are automatically disabled.

## Related

- [Digital Voice Keyer overview](overview.md)
- [Record a new DVK slot](record-a-new-dvk-slot.md)
- [Upload a WAV file into a slot](upload-a-wav-file-into-a-slot.md)
- [Play a stored voice-keyer slot](play-a-stored-voice-keyer-slot.md)
- [Stop a playback in progress](stop-a-playback-in-progress.md)