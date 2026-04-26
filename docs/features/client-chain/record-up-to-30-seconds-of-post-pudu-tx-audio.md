# Record up to 30 seconds of post-PUDU TX audio

Use the built-in monitor recorder to capture your processed TX audio after it passes through the PUDU stage, then play it back immediately to evaluate your audio chain settings.

## Before you start

- The Aetherial Audio (TXDSP) container must be visible. If it is not, click the tray button labelled **PUDU** in the right sidebar to show it.
- The TX chain must be the active view. Click **TX** in the applet header if **RX** is currently selected.
- Your microphone source must be set to PC and DAX must be off. The record button is disabled when these conditions are not met.

## Steps

1. Confirm the **TX** button in the Aetherial Audio Chain header is checked. If not, click **TX**.
2. Click the **⏺** (Record) button in the header row, to the right of the **TX** / **RX** toggles. The button pulses red to indicate recording is active.
3. Speak into your microphone. Recording stops automatically after 30 seconds, or click **⏺** again to stop early.
4. When recording stops, playback starts automatically. The **▶** (Play) button pulses green during playback.

## What each control does

| Control | Behavior | Default | Notes |
|---|---|---|---|
| **⏺** (Record) | Starts capturing post-PUDU TX audio; click again to stop early. Playback starts automatically when recording ends. | Unchecked | Pulses red while recording. Disabled when MIC source is not PC, DAX is on, or playback is currently running. Hidden when **RX** is the active tab. |
| **▶** (Play) | Plays back the captured audio; click again to cancel playback. | Unchecked | Pulses green while playing. Only enabled once a recording exists and recording is not active. Hidden when **RX** is the active tab. |

## Tips

- The **⏺** button remains enabled while recording so you can click it to stop before the 30-second limit is reached.
- The **▶** button remains enabled during playback so you can click it to cancel at any time.
- Switching to **RX** mode hides both the **⏺** and **▶** buttons. Switch back to **TX** to access them again.

## Troubleshooting

- **The ⏺ button is greyed out** — The mic source is not set to PC, DAX is enabled, or playback is currently running. Disable DAX, set the mic input to PC, and wait for playback to finish before recording.
- **The ▶ button is greyed out** — No recording exists yet, or recording is currently active. Complete a recording first.
- **The ⏺ button is not visible** — The **RX** tab is active. Click **TX** to switch to the TX chain; the record and play buttons only appear in TX mode.

## Related

- [Play back the captured PUDU audio](play-back-the-captured-pudu-audio.md)
- [Aetherial Audio Chain overview](overview.md)
- [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)
