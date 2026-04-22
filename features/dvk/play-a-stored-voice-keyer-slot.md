# Play a stored voice-keyer slot

Use the Digital Voice Keyer panel to transmit a stored recording on-air. Triggering a slot keys the radio and plays the audio through the selected transmit slice.

## Before you start

- AetherSDR must be connected to the radio. The DVK panel requires an active radio connection.
- The target slot must contain a recording. Slots showing "Empty" in the duration label cannot be played.
- The radio must be in a voice mode (SSB, AM, FM) for the DVK panel to appear in the main window.

## Steps

1. Locate the Digital Voice Keyer panel in the main window central area.
2. Identify the slot you want to play. Check that its duration label shows a time value, not "Empty".
3. Click the slot's row to select it. The selected row highlights with a blue border.
4. Play the slot using one of these methods:
   - Click the **▶ PLAY** button to play the currently selected slot.
   - Click the slot's **F1** through **F8** button directly to select and play that slot in one action.
   - Press the corresponding F-key on your keyboard (F1–F8) to select and play that slot.
5. The slot's progress bar appears and advances during playback. The status indicator changes from "Idle" to "Playing". The active slot's F-key button highlights.
6. Playback stops automatically when the recording ends. To stop early, click **■ STOP** or press Escape.

## What each control does

| Control | Behavior | Default |
|---|---|---|
| **F1 … F8** slot buttons | Selects and plays that slot; if the slot is already playing, clicking again stops it. | — |
| Slot name labels | Shows the name of each slot. | `Recording <n>` |
| Slot duration labels | Displays the recording length or "Empty" if the slot has no content. | `Empty` |
| Slot progress bars | Shows live playback progress. Visible only during active playback. | Hidden |
| **▶ PLAY** | Plays the selected slot. Has no effect if the slot is empty. | — |
| **■ STOP** | Stops playback in progress. | — |

## Tips

- Clicking an **F1–F8** button while that slot is already playing stops playback rather than restarting it.
- Pressing the matching F-key on your keyboard is equivalent to clicking the on-screen **F1–F8** button. F1 through F8 are supported.
- To hear a slot through your local speaker without transmitting, use **◀ PREV** instead of **▶ PLAY**.

## Troubleshooting

- **▶ PLAY does nothing** — The selected slot is empty. The duration label will read "Empty". Record audio or upload a WAV file into the slot first.
- **F-key press has no effect** — The DVK panel must have keyboard focus, or the slot at that position is empty.

## Related

- [Digital Voice Keyer overview](overview.md)
- [Preview a slot without transmitting](preview-a-slot-without-transmitting.md)
- [Record a new DVK slot](record-a-new-dvk-slot.md)
- [Stop a playback in progress](stop-a-playback-in-progress.md)
- [Upload a WAV file into a slot](upload-a-wav-file-into-a-slot.md)
