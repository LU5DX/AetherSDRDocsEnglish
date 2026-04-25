# Record up to 30 seconds of post-PUDU TX audio

The PooDoo Audio Chain includes a monitor recorder that captures up to 30 seconds of audio taken from after the PUDU stage. Use it to check how your DSP chain sounds on the air without needing a second receiver.

## Before you start

- The PooDoo Audio (TXDSP) container must be visible. If it is not, click the PUDU tray button in the right sidebar to show it.
- Your microphone input must be set to PC and DAX must be off. The record button is disabled when these conditions are not met.
- Do not start a recording while playback of a previous recording is running. The record button is disabled during playback.

## Steps

1. Confirm the TX button at the top of the PooDoo Audio Chain is selected. The recorder is only accessible in TX mode.
2. Click the Record button (⏺) in the header row, to the right of the TX and RX buttons. The button pulses red while recording is active.
3. Speak into your microphone normally. The recorder captures up to 30 seconds of post-PUDU audio.
4. Click the Record button (⏺) again to stop before 30 seconds, or wait for the recorder to stop automatically at the 30-second limit. Playback starts automatically when recording stops.

## What each control does

| Control | Behavior | Enabled when | Visual state |
|---|---|---|---|
| Record (⏺) | Starts capture of post-PUDU TX audio; click again to stop early. | Mic input is ready (PC, DAX off) and playback is not running. Also enabled while recording (so you can stop it). | Pulses red at 500 ms intervals while recording. |
| Play (▶) | Plays back the captured audio; click again to cancel. | A recording exists and recording is not active. Also enabled while playing (so you can cancel). | Pulses green at 500 ms intervals while playing. |

## Tips

- The 30-second limit is fixed. If you need to check only a short phrase, click Record (⏺) again as soon as you finish speaking rather than waiting for the automatic stop.
- The recorder captures audio after the PUDU stage, so it reflects the full effect of every enabled stage in the chain, in the current order.
- If you want to compare the chain enabled versus bypassed, record a clip, then click BYPASS and record again.

## Troubleshooting

- **Record (⏺) is greyed out** — Either DAX is active, the microphone input is not set to PC, or playback is currently running. Disable DAX, set mic input to PC, and wait for any active playback to finish.
- **Playback does not start automatically after recording stops** — Recording may have been stopped before any audio was captured. Ensure you are speaking into the microphone while the button is pulsing red.
- **Record (⏺) is greyed out even though MIC is set to PC and DAX is off** — Confirm the TX button is selected at the top of the chain. The recorder is not active in RX mode.

## Related

- [Play back the captured PUDU audio](play-back-the-captured-pudu-audio.md)
- [PooDoo Audio Chain overview](overview.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Open a stage's floating editor from the chain](open-a-stage-s-floating-editor-from-the-chain.md)
