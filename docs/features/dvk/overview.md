# Digital Voice Keyer overview

The Digital Voice Keyer (DVK) lets you record, store, and play back up to 12 voice-keyer slots on a connected Flex radio. Use it to send pre-recorded or live-recorded audio on-air without manually keying the microphone, or to preview recordings locally before transmitting.

## Before you start

- AetherSDR must be connected to a Flex radio. The DVK panel is not available without an active radio connection.
- A voice mode must be active, or DVK must be enabled, for the panel to appear in the main window.

## How it works

The DVK panel appears in the AetherSDR main window when a voice mode is active. It shows 12 slots arranged in a scrollable grid. Each slot displays an F-key button (F1 through F12), a name label, a duration label, and a progress bar that activates during recording or playback.

Clicking an F-key button selects that slot and starts playback if the slot contains a recording. Clicking it again while it is playing stops playback. The same behavior is available from the keyboard using F1 through F12. Pressing Escape stops whichever operation is currently active.

The four transport buttons at the bottom of the panel — ● REC, ■ STOP, ▶ PLAY, and ◀ PREV — act on whichever slot is currently selected. A status indicator at the bottom of the panel shows the current DVK state: Idle, Recording, or Playing.

Slots can be populated by recording directly through the radio or by uploading an existing WAV file. Right-clicking any slot row opens a context menu for renaming the slot or uploading a WAV. Double-clicking the slot's name label also opens inline rename.

## What each control does

| Control | Behavior | Default |
|---|---|---|
| F1 … F12 slot buttons | Selects the slot and toggles playback on-air. Right-click the row to rename or upload a WAV. | — |
| Slot name labels | Shows the name assigned to each slot. | Recording 1 … Recording 12 |
| Slot duration labels | Shows the recorded length of the slot, or "Empty" if the slot has no content. | Empty |
| Slot progress bars | Shows live playback or recording progress. Hidden when the slot is idle. | — |
| ● REC | Starts recording into the selected slot. Button stays highlighted while recording is in progress. | — |
| ■ STOP | Stops any active recording, playback, or preview. | — |
| ▶ PLAY | Plays the selected slot on-air. Button stays highlighted during playback. Has no effect if the slot is empty. | — |
| ◀ PREV | Previews the selected slot through the local speaker without transmitting. Has no effect if the slot is empty. | — |
| Rename edit | Inline text field for renaming a slot, triggered via the context menu or by double-clicking the name label. | — |
| Status indicator | Displays the current DVK state: Idle, Recording, or Playing. | Idle |

## Tips

- Pressing an F-key while that slot is already playing stops playback, so the same key both starts and stops a slot.
- Pressing Escape cancels an active rename without saving, or stops the current recording, playback, or preview if no rename is in progress.
- Progress bar color indicates the operation in progress: red for recording, green for playback, and blue for preview.

## Related

- [Record a new DVK slot](record-a-new-dvk-slot.md)
- [Play a stored voice-keyer slot](play-a-stored-voice-keyer-slot.md)
- [Preview a slot without transmitting](preview-a-slot-without-transmitting.md)
- [Stop a playback in progress](stop-a-playback-in-progress.md)
- [Rename a slot](rename-a-slot.md)
- [Upload a WAV file into a slot](upload-a-wav-file-into-a-slot.md)
