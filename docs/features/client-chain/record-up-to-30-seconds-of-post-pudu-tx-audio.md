# Record up to 30 seconds of post-PUDU TX audio

Use the built-in monitor recorder to capture a short sample of your processed TX audio — after every stage in the chain, including PUDU — so you can hear exactly what your signal sounds like on air without needing a second receiver.

## Before you start

- The PooDoo Audio (TXDSP) container must be visible. If it is not, click the PUDU tray button in the right sidebar to show it.
- Your microphone input must be set to PC source and DAX must be off. The record button is disabled until both conditions are met.
- You must be in TX chain view. Click TX in the applet header if RX is currently selected.

## Steps

1. Confirm the ⏺ (record) button in the applet header is enabled. If it appears dimmed, check your mic source and DAX state as described above.
2. Click ⏺ to start recording. The button pulses red while capture is active. Recording stops automatically after 30 seconds.
3. To stop before 30 seconds have elapsed, click ⏺ again.
4. Playback starts automatically when recording stops. The ▶ (play) button pulses green during playback.
5. To stop playback early, click ▶.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| ⏺ (record) | Starts or stops capture of post-PUDU TX audio. Maximum recording length is 30 seconds. | Enabled when mic input is ready and playback is not active. Pulses red while recording. Disabled when dimmed. |
| ▶ (play) | Plays back the most recent recording. Click again to cancel. | Enabled only after a recording exists and recording is not currently active. Pulses green during playback. |

## Tips

- You do not need to transmit to use the recorder; the recorder captures the processed audio from the client-side chain, not over-the-air audio.
- If you want to hear the effect of a single stage, bypass all others using BYPASS before recording, then compare a second recording with BYPASS off. See [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md).
- The recorder captures audio after every stage in the chain, including the PUDU exciter. To hear the chain without PUDU, single-click the PUDU stage tile to bypass it before recording.

## Troubleshooting

- **⏺ is permanently dimmed** — The mic input is not set to PC source, DAX is active, or playback is currently running. Disable DAX, set mic source to PC, and wait for any playback to finish.
- **Playback does not start automatically after recording stops** — No audio was captured (for example, recording was stopped immediately). Click ⏺ to record again and speak into the microphone during the session.
- **▶ is dimmed after recording** — Recording is still in progress. Click ⏺ to stop it first.

## Related

- [Play back the captured PUDU audio](play-back-the-captured-pudu-audio.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Open a stage's floating editor from the chain](open-a-stage-s-floating-editor-from-the-chain.md)
- [PooDoo Audio Chain overview](overview.md)
