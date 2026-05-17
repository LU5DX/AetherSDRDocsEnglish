# Digital Voice Keyer (DVK) Panel

The Digital Voice Keyer panel records and plays back up to 8 voice-keyer slots on the radio. You can rename slots, upload WAV files, record new audio, and trigger playback via F-keys or on-screen buttons.

## Before you start

- The radio must be connected. The DVK panel requires an active radio connection.
- F1-F12 keyboard shortcuts are active based on the currently selected slice mode, regardless of DVK panel visibility. This ensures DVK shortcuts are mutually exclusive with CWX panel shortcuts and avoids shortcut conflicts.

## Understanding the DVK Panel

The DVK panel displays eight slots (F1 through F8). Each slot shows:

- **Slot name** – Default name is "Recording <n>". You can rename any slot.
- **Slot duration** – Displays the recording length in seconds, or "Empty" if no recording exists.
- **Progress bar** – Shows live playback or recording progress.

At the bottom of the panel, a status indicator displays the current DVK state: "Idle", "Recording", or "Playing".

## Controls

| Control | Description |
|---|---|
| **F1 … F8 slot buttons** | Select and play the corresponding slot. Right-click to rename or upload a WAV file. Click an already-playing slot button to stop playback. |
| **● REC** | Starts recording into the currently selected slot. |
| **■ STOP** | Stops the current operation (recording, playback, or preview). |
| **▶ PLAY** | Plays the currently selected slot. |
| **◀ PREV** | Previews the selected slot through the local speaker (no transmission). |
| **Rename edit** | Inline text field that appears when you right-click a slot and choose rename. |

## Record a New DVK Slot

1. Select the desired slot by clicking the **F1** through **F8** button.
2. Click **● REC** to start recording.
3. Click **■ STOP** when finished.

The slot now contains your recording and shows its duration.

## Play a Stored Voice-Keyer Slot

1. Click the slot's **F-key button** (for example, **F1**).
2. Alternatively, select the slot by clicking its button, then click **▶ PLAY**.

The transmission begins and the progress bar advances. Click **■ STOP** or press Escape to stop playback.

## Preview a Slot Without Transmitting

1. Select the slot by clicking its **F-key button**.
2. Click **◀ PREV**.

The recording plays through your local speaker only — no RF transmission occurs.

## Stop a Playback in Progress

Stopping playback drops the transmission immediately and returns the DVK to the Idle state.

1. Click **■ STOP**.

Playback stops immediately. The status indicator returns to "Status: Idle" and the slot's progress bar is hidden.

**Alternative — keyboard:** Press Escape. If no inline rename is active, Escape stops the current playback.

**Alternative — F-key button:** Click the slot's active F-key button (for example, **F1**). Clicking an F-key button while that slot is playing acts as a toggle and stops playback.

## Rename a Slot

1. Right-click the slot's **F-key button**.
2. Select **Rename** from the context menu.
3. Type the new name in the text field that appears.
4. Press Enter to confirm, or press Escape to cancel.

## Upload a WAV File

1. Right-click the slot's **F-key button**.
2. Select **Upload WAV** from the context menu.
3. Navigate to and select a WAV file on your computer.
4. The file is uploaded to the radio and replaces any existing recording in that slot.

## Keyboard Shortcuts

| Key | Function | Notes |
|---|---|---|
| **F1** through **F8** | Select and play the corresponding slot | Shortcuts are active based on the active slice mode, regardless of panel visibility. This prevents conflicts with the CWX panel's F1-F12 shortcuts. |
| **Escape** | Stop the current operation, or cancel an inline rename | If a rename text field is active, Escape cancels the rename instead of stopping playback. |

## Status Indicator

The status indicator at the bottom of the panel shows:

- **Idle** – No operation in progress.
- **Recording** – A slot is currently being recorded.
- **Playing** – A slot is currently playing on-air.

## Tips

- **■ STOP** works for recording and preview as well as playback. One button covers all three active states.
- Pressing Escape only stops the active operation if no slot rename is currently open. If a rename text field is visible, Escape cancels the rename instead.
- The DVK and CWX panels share F1-F12 shortcuts. Shortcuts are enabled or disabled based on the active slice mode so they fire regardless of panel visibility, while staying mutually exclusive to avoid Qt shortcut ambiguity.

## Related

- [Play a stored voice-keyer slot](play-a-stored-voice-keyer-slot.md)
- [Preview a slot without transmitting](preview-a-slot-without-transmitting.md)
- [Record a new DVK slot](record-a-new-dvk-slot.md)