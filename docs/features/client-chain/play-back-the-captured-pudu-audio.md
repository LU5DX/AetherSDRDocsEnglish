# Play back the captured PUDU audio

Use the Play button in the PooDoo Audio Chain to listen to audio you have already recorded through the TX DSP chain. This lets you hear exactly what your signal sounded like after every processing stage, without transmitting.

## Before you start

- You must have at least one recording captured using the Record button. The Play button is disabled until a recording exists.
- Recording must not be active. You cannot play back while a capture is in progress.
- The PooDoo Audio (TXDSP) container must be visible. If it is not, click the tray button labelled **PUDU** in the right sidebar to show it.
- The **TX** mode button must be selected (default). The monitor buttons are part of the TX chain view.

## Steps

1. Confirm the **TX** button in the PooDoo Audio Chain header is checked. If not, click **TX**.
2. Confirm the Record button (circle glyph) is not lit or pulsing red. If it is, click it to stop the current recording before proceeding.
3. Click the Play button (triangle glyph ▶) in the header row of the PooDoo Audio Chain.
4. The Play button pulses green while playback is running.
5. To stop playback before it finishes, click the Play button (triangle glyph ▶) again.

## What each control does

| Control | Behavior | Enabled when | Visual state |
|---|---|---|---|
| Play (triangle glyph) | Starts playback of the captured PUDU audio. Click again to cancel. | A recording exists and recording is not active. While playing, remains enabled so you can cancel. | Pulses green (alternating bright and dim at 500 ms) during playback. Dimmed and inactive at idle. |
| Record (circle glyph) | Captures post-PUDU TX audio. Disabled during playback. | MIC input is ready (source set to PC, DAX off) and playback is not running. | Pulses red during recording. |

## Tips

- Playback starts automatically after a recording completes. You do not need to click Play manually if you just stopped the Record button.
- The Play button remains enabled during playback so you can cancel at any time by clicking it again.
- The green pulse on the Play button is the only on-screen indicator that playback is running. Watch for it if you are unsure whether audio is playing.

## Troubleshooting

- **Play button (triangle glyph) is disabled and grey** — No recording has been captured yet, or recording is currently active. If the Record button is pulsing red, click it to stop recording first. Then click Play.
- **Play button is enabled but no audio is heard** — Verify your system audio output is configured correctly. AetherSDR plays the captured audio through the host audio system; check your OS mixer and output device selection.

## Related

- [Record up to 30 seconds of post-PUDU TX audio](record-up-to-30-seconds-of-post-pudu-tx-audio.md)
- [PooDoo Audio Chain overview](overview.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
