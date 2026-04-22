# Record a new DVK slot

Use the Digital Voice Keyer panel to record your voice into one of up to 12 slots, which you can then play back on-air with a single click or F-key press.

## Before you start

- AetherSDR must be connected to the radio. The DVK panel is only available when a radio connection is active.
- The DVK panel must be visible in the main window. If it is not shown, switch to a voice mode or enable DVK on the radio.
- Your microphone must be configured and working through the radio's audio path.

## Steps

1. In the DVK panel, click the slot row you want to record into (F1 through F12). The selected row highlights with a blue border.
2. Click **● REC**. The button turns red and the status indicator changes to **Recording**. The slot's progress bar appears and advances as audio is captured.
3. Speak your message into the microphone.
4. Click **■ STOP** when you are done. The status indicator returns to **Idle**, the progress bar disappears, and the slot duration label updates from **Empty** to show the recorded length.

## What each control does

| Control | Behavior | Default |
|---|---|---|
| F1 … F12 slot buttons | Selects and plays that slot; right-click to rename or upload a WAV. | — |
| Slot name labels | Shows the name of each slot. | `Recording <n>` |
| Slot duration labels | Displays recording length or **Empty** if the slot has no audio. | Empty |
| Slot progress bars | Shows live record or playback progress. Hidden when idle. | — |
| **● REC** | Starts recording into the selected slot. Turns red while active. | — |
| **■ STOP** | Stops recording or playback. | — |
| **▶ PLAY** | Plays the selected slot on-air. | — |
| **◀ PREV** | Previews the selected slot through the local speaker without transmitting. | — |

## Tips

- Slot 1 is selected by default when the DVK panel first opens. If you click **● REC** without selecting a different slot, the recording goes into slot 1.
- Pressing Escape cancels recording with the same effect as **■ STOP**.
- You can rename a slot after recording by right-clicking its row and choosing rename from the context menu. The slot name label is editable inline.
- F-key buttons only trigger playback if the slot already contains a recording. A slot that still shows **Empty** in the duration label will not play when its F-key is pressed.

## Troubleshooting

- **Duration label stays Empty after recording** — The radio may not have received audio. Check that the correct microphone input is selected in `Settings > Radio Setup...` and that the radio is not in a mode that disables the microphone.
- **● REC does nothing when clicked** — No slot is selected. Click a slot row first, then click **● REC**.
- **Status shows Recording but no audio is captured** — Verify the microphone is not muted at the operating system level and that the audio input device is routed correctly through the radio.

## Related

- [Digital Voice Keyer overview](overview.md)
- [Play a stored voice-keyer slot](play-a-stored-voice-keyer-slot.md)
- [Preview a slot without transmitting](preview-a-slot-without-transmitting.md)
- [Rename a slot](rename-a-slot.md)
- [Upload a WAV file into a slot](upload-a-wav-file-into-a-slot.md)
- [Stop a playback in progress](stop-a-playback-in-progress.md)
