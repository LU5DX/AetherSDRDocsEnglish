# Record up to 30 seconds of post-PUDU TX audio

Use the monitor recorder in the PooDoo Audio Chain to capture up to 30 seconds of your processed TX audio after it has passed through every stage, including PUDU. This lets you audition exactly what your signal sounds like before transmitting on air.

## Before you start

- The PooDoo Audio (TXDSP) container must be visible. If it is not, click the "PUDU" tray button in the right sidebar to show it.
- Your microphone input source must be set to PC and DAX must be off. The record button is disabled until both conditions are met.
- You must be in TX chain view. Click "TX" if "RX" is currently selected.

## Steps

1. Confirm the "TX" toggle is selected in the PooDoo Audio Chain header. The button is amber when active.
2. Locate the record button (⏺) in the header row, to the right of the "TX" and "RX" toggles. It is enabled only when the mic input is ready.
3. Click ⏺ to start recording. The button pulses red and its background brightens to confirm capture is active. Recording stops automatically after 30 seconds.
4. To stop before 30 seconds, click ⏺ again.
5. Playback starts automatically when recording stops. The play button (▶) pulses green during playback.
6. To replay the captured audio manually, click ▶. To cancel playback in progress, click ▶ again.

## What each control does

| Control | Behavior | Default | Notes |
|---|---|---|---|
| ⏺ (record) | Captures up to 30 s of post-PUDU TX audio. Click again to stop early; playback starts automatically. | Unchecked | Enabled only when mic source is PC, DAX is off, and playback is not running. Disabled when no recording exists and conditions are not met. Pulses red while recording. |
| ▶ (play) | Plays back the captured audio. Click again to cancel. | Unchecked | Enabled only once a recording exists and recording is not active. Pulses green while playing. |

Persisted settings involved: `ClientCompTxChainStages`, `Applet_TXDSP`.

## Tips

- If you want to hear the effect of a specific stage, bypass other stages using single-click on each chain stage before recording, then compare results.
- The record button remains enabled while recording so you can click it to stop at any time.
- The play button remains enabled during playback so you can cancel at any time.

## Troubleshooting

- **⏺ is greyed out and cannot be clicked** — The mic input source is not set to PC, DAX is on, or playback is currently running. Check your audio source settings and ensure DAX is disabled.
- **Playback does not start after recording stops** — No audio was captured, or the recording was too short. Verify that audio is reaching the chain and that MOX was active during recording.

## Related

- [PooDoo Audio Chain overview](overview.md)
- [Play back the captured PUDU audio](play-back-the-captured-pudu-audio.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Open a stage's floating editor from the chain](open-a-stage-s-floating-editor-from-the-chain.md)
