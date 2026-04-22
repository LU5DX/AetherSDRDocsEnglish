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
| F1 … F8 slot buttons | Selects the slot. If the slot is currently playing back on air, clicking again stops it. | Does not trigger preview. |
| Slot duration labels | Shows recording length or "Empty". | A slot showing "Empty" cannot be previewed. |
| Slot progress bars | Displays playback progress in blue during preview. | Hidden when idle. |
| ◀ PREV | Starts preview of the selected slot through the local speaker. Click again to stop. | Does not transmit. |
| ■ STOP | Stops any active recording, playback, or preview. | Also activated by Escape. |
| Status: Idle / Recording / Playing | Shows the current DVK state at the bottom of the panel. | |

## Tips

- If you click ◀ PREV on a slot that is already in preview, it stops the preview.
- Pressing Escape stops an active preview without using the mouse.
- The F-key buttons and F1–F8 keyboard shortcuts trigger on-air playback, not preview. Use ◀ PREV specifically when you do not want to transmit.

## Troubleshooting

- **◀ PREV has no effect** — The selected slot is empty. Check that the slot's duration label does not show "Empty". Record audio or upload a WAV file first, then retry.
- **No audio heard during preview** — Preview routes audio to the local speaker. Verify your system audio output is correctly configured and not muted.

## Related

- [Digital Voice Keyer overview](overview.md)
- [Record a new DVK slot](record-a-new-dvk-slot.md)
- [Upload a WAV file into a slot](upload-a-wav-file-into-a-slot.md)
- [Play a stored voice-keyer slot](play-a-stored-voice-keyer-slot.md)
- [Stop a playback in progress](stop-a-playback-in-progress.md)
