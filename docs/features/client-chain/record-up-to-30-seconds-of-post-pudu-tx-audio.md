# Record up to 30 seconds of post-PUDU TX audio

Use the post-PUDU monitor recorder to capture up to 30 seconds of your processed TX audio after it passes through the full PooDoo chain. This lets you hear exactly what the chain produces without needing a second receiver.

## Before you start

- The PooDoo Audio (TXDSP) container must be visible. If it is not, click the "PUDU" tray button in the right sidebar to show it.
- Your microphone input must be set to PC and DAX must be off. The record button is disabled if either condition is not met.
- No playback must be in progress. The record button is disabled while the Play button is active.

## Steps

1. In the PooDoo Audio container, confirm the TX button is selected (amber). The monitor recorder operates on the TX chain only.
2. Click the Record button (⏺) in the header row, to the right of the TX and RX buttons.
3. Transmit as normal. The Record button pulses red while capturing.
4. Click the Record button (⏺) again to stop, or allow the recording to stop automatically at 30 seconds. Playback starts automatically once recording stops.

## What each control does

| Control | Behavior | Default | Notes |
|---|---|---|---|
| Record (⏺) | Starts or stops capture of up to 30 s of post-PUDU TX audio. Playback starts automatically on stop. | Unchecked | Enabled only when mic input is ready and playback is not running. Pulses red while recording. |
| Play (▶) | Plays back the captured audio. Click again to cancel. | Unchecked | Enabled only once a recording exists and recording is not active. Pulses green while playing. |

## Tips

- The tooltip on the Record button reads: "Record up to 30 s of post-PooDoo™ TX audio (MIC must be set to PC and DAX off). Click again to stop; playback starts automatically." If the button appears dimmed, check both the mic source setting and DAX state first.
- The Record button remains enabled while recording is active so you can click it to stop the capture at any time before the 30-second limit.
- The chain processes audio regardless of which stages are bypassed. To evaluate specific stages, bypass others before recording. See [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md).

## Troubleshooting

- **Record button (⏺) is dimmed and cannot be clicked** — Either the mic input is not set to PC, DAX is on, or playback is currently running. Correct the mic and DAX settings, or wait for playback to finish.
- **Recording stops before you finish** — The recorder captures a maximum of 30 seconds. Start the capture closer to the part of your transmission you want to evaluate.
- **Playback does not start after recording stops** — Playback requires a completed recording. If you stopped recording immediately after starting it, try again and allow at least a brief capture before stopping.

## Related

- [Play back the captured PUDU audio](play-back-the-captured-pudu-audio.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Open a stage's floating editor from the chain](open-a-stage-s-floating-editor-from-the-chain.md)
- [PooDoo Audio Chain overview](overview.md)
