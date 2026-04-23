# Play back the captured PUDU audio

Use the play button in the PooDoo Audio Chain applet to listen to audio you have already recorded through the TX DSP chain. This lets you audition how your signal sounds post-processing without transmitting.

## Before you start

- The PooDoo Audio (TXDSP) container must be visible. If it is not, click the tray button labelled **PUDU** in the right sidebar.
- You must have already captured a recording using the Record button. The Play button is disabled until a recording exists.
- Recording must not be active when you start playback.

## Steps

1. Confirm the **TX** toggle is selected in the chain header (it is selected by default).
2. Locate the Play button (▶) in the header row, to the right of the Record button.
3. Click ▶ to start playback. The button pulses green while audio is playing.
4. To stop playback before it finishes, click ▶ again.

## What each control does

| Control | Behavior | Default | Notes |
|---|---|---|---|
| ▶ (Play) | Starts playback of the captured PUDU audio; click again to cancel. | Unchecked | Enabled only when a recording exists and recording is not active. Pulses green while playing. |
| ⏺ (Record) | Captures up to 30 s of post-PUDU TX audio; click again to stop. Playback starts automatically after recording stops. | Unchecked | Requires MIC set to PC and DAX off. Disabled while playback is running. |

## Tips

- Playback starts automatically when you stop a recording by clicking ⏺ a second time. You do not need to click ▶ manually after each recording.
- While playback is running, the Record button is disabled. Wait for playback to finish, or click ▶ to cancel it, before starting a new recording.

## Troubleshooting

- **▶ is greyed out** — No recording exists yet, or a recording is currently in progress. Complete or stop the recording first.
- **Playback does not produce audio** — Verify your system audio output is configured correctly. AetherSDR plays back through the default audio output device.

## Related

- [Record up to 30 seconds of post-PUDU TX audio](record-up-to-30-seconds-of-post-pudu-tx-audio.md)
- [PooDoo Audio Chain overview](overview.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
