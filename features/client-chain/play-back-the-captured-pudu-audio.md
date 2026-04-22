# Play back the captured PUDU audio

Use the Play button in the PooDoo Audio Chain applet to listen to audio you have already recorded through the post-PUDU monitor. This lets you judge how your TX DSP chain sounds without transmitting.

## Before you start

- The PooDoo Audio (TXDSP) container must be visible. If it is not, click the PUDU tray button in the right sidebar to enable it.
- You must have already captured a recording using the Record button. The Play button is disabled until a recording exists.
- Recording must not be active when you start playback.

## Steps

1. Open the PooDoo Audio Chain applet by clicking the PUDU tray button in the right sidebar.
2. Confirm TX is selected (the TX toggle button is checked in amber). The monitor buttons are only active in TX mode.
3. Click the Play (▶) button in the header row of the applet.
4. The Play button pulses green while playback runs. To stop before the recording ends, click the Play (▶) button again.

## What each control does

| Control | Behavior | Default | Notes |
|---|---|---|---|
| Play (▶) | Starts playback of the captured PUDU audio; click again to cancel. | Unchecked | Enabled only when a recording exists and recording is not active. Pulses green during playback. |
| Record (⏺) | Disabled during playback. | Unchecked | Becomes available again once playback stops. |

## Tips

- If playback starts immediately after recording stops, it is because the Record button automatically triggers playback when you stop recording. You do not need to click Play (▶) separately in that case.
- The Play (▶) button remains enabled while playback is running so you can cancel at any time by clicking it again.

## Troubleshooting

- **Play (▶) is greyed out** — No recording has been captured yet, or recording is currently active. Complete a recording first, then click Play (▶).
- **Play (▶) is greyed out even after recording** — Confirm that recording has fully stopped (the Record (⏺) button is no longer pulsing red) before attempting playback.

## Related

- [Record up to 30 seconds of post-PUDU TX audio](record-up-to-30-seconds-of-post-pudu-tx-audio.md)
- [PooDoo Audio Chain overview](overview.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
