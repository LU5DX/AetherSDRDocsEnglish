# Play back the captured PUDU audio

This page explains how to play back audio you recorded with the post-PUDU TX monitor. Use this to hear how your TX signal sounds after the full client-side DSP chain has processed it.

## Before you start

- You must have at least one recording already captured. The Play button is disabled until a recording exists.
- The Aetherial Audio Chain applet must be visible. If it is not, click the "PUDU" tray button in the right sidebar to show it.
- Make sure you are not currently recording. The Play button is disabled while recording is active.
- The TX chain must be shown. The Play button is hidden when the RX chain is active.

## Steps

1. If the RX chain is currently shown, click **TX** to switch to the TX chain.
2. Locate the **Play (triangle glyph)** button in the header row, to the right of the **Record (circle glyph)** button.
3. Click **Play (triangle glyph)** to start playback. The button pulses green while audio is playing.
4. To stop playback before it finishes, click **Play (triangle glyph)** again.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| **Play (triangle glyph)** | Starts playback of the captured PUDU audio. Click again to cancel. | Enabled only when a recording exists and recording is not active. Pulses green while playing. Hidden when the RX chain is shown. |
| **Record (circle glyph)** | Disabled during playback. | Re-enables automatically when playback ends. |

## Tips

- Playback begins immediately when you click **Play (triangle glyph)**; there is no confirmation step.
- If you want a new recording first, wait for playback to finish or cancel it, then use **Record (circle glyph)**.
- The green pulse on the **Play (triangle glyph)** button alternates between bright and dim every 500 ms while playback is running, giving a clear at-a-glance indication that audio is in progress.

## Troubleshooting

- **Play (triangle glyph) is greyed out** — No recording has been made yet, or recording is currently active. Complete or stop the recording first.
- **Play (triangle glyph) is not visible** — The RX chain is currently shown. Click **TX** to switch to the TX chain; the play and record buttons only appear in TX mode.

## Related

- [Record up to 30 seconds of post-PUDU TX audio](record-up-to-30-seconds-of-post-pudu-tx-audio.md)
- [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)
- [Aetherial Audio Chain overview](overview.md)
