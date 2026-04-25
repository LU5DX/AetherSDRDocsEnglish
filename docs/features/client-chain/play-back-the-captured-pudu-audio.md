# Play back the captured PUDU audio

Use the Play button in the PooDoo Audio Chain applet to listen to a previously recorded post-PUDU TX audio capture. This lets you hear exactly how your processed signal sounds without transmitting.

## Before you start

- The PooDoo Audio (TXDSP) container must be visible. If it is not, click the tray button labelled **PUDU** in the right sidebar to toggle it on.
- The TX mode must be selected (the **TX** toggle must be checked, not **RX**).
- A recording must already exist. The Play button is disabled until at least one capture has been made. See [Record up to 30 seconds of post-PUDU TX audio](record-up-to-30-seconds-of-post-pudu-tx-audio.md).
- Recording must not be in progress. The Play button is disabled while the Record button is active.

## Steps

1. Confirm the **TX** toggle is checked in the applet header row. The Play button is not functional in RX mode.
2. Locate the Play button (▶) to the right of the Record button (⏺) in the applet header row.
3. Click the Play button (▶) to start playback. The button pulses green while playback is active.
4. To stop playback before it finishes, click the Play button (▶) again.

## What each control does

| Control | Behavior | Enabled when | Indicator |
|---|---|---|---|
| Play (▶) | Plays back the captured PUDU audio; click again to cancel. | A recording exists and recording is not active. While playing, remains enabled so you can cancel. | Pulses green (500 ms alternating bright/dim) during playback. |
| Record (⏺) | Captures up to 30 s of post-PUDU TX audio; click again to stop. Recording stops and playback starts automatically. | MIC input is ready (source set to PC, DAX off) and playback is not running. | Pulses red during recording. |

## Tips

- If playback starts automatically after you stop a recording, that is expected behavior — stopping the Record button triggers playback immediately.
- The Play button becomes disabled as soon as you click the Record button to start a new recording. Cancel or finish recording first.

## Troubleshooting

- **Play button (▶) is greyed out** — No recording exists yet, or recording is currently in progress. Make a recording first, or wait for the current recording to finish.
- **Play button (▶) is greyed out even though a recording was made** — Recording may still be active (the Record button still pulses red). Click the Record button (⏺) to stop recording, then click Play.

## Related

- [Record up to 30 seconds of post-PUDU TX audio](record-up-to-30-seconds-of-post-pudu-tx-audio.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [PooDoo Audio Chain overview](overview.md)
