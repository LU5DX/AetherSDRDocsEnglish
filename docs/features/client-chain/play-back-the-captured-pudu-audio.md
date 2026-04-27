# Play back the captured PUDU audio

This page explains how to play back audio you have already recorded with the post-PUDU TX monitor. Use this to hear exactly what your transmitted signal sounds like after the full TX DSP chain has processed it.

## Before you start

- You must have an existing recording. The Play (▶) button is only enabled once a recording exists.
- Recording must not be currently active. The Play (▶) button is disabled while the Record (⏺) button is engaged.
- The Aetherial Audio (TXDSP) container must be visible. If it is not, click the tray button labelled `PUDU` in the right sidebar to show it.
- The TX chain must be the active view. The Play (▶) button is hidden in RX mode.

## Steps

1. In the ClientChainApplet header row, confirm the **TX** button is selected. If not, click **TX**.
2. Click the **Play (▶)** button.
   - The button pulses green while playback is running.
3. To stop playback before it finishes, click the **Play (▶)** button again.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| **Play (▶)** | Starts playback of the captured PUDU audio; click again to cancel. | Hidden in RX mode. Enabled only when a recording exists and recording is not active. Pulses green while playing. |
| **Record (⏺)** | Disabled during playback. | Re-enabled automatically when playback ends. |

## Tips

- The Play (▶) button remains enabled while playback is running so you can cancel at any time by clicking it again.
- If you want a new recording before listening, click **Record (⏺)** to capture up to 30 seconds of post-PUDU TX audio. Playback starts automatically when recording stops.
- The Play (▶) button is hidden whenever the **RX** tab is active. Switch back to **TX** to access it.

## Troubleshooting

- **Play (▶) is greyed out** — No recording exists yet, or recording is currently in progress. Make a recording first using **Record (⏺)**, or wait for the current recording to finish.
- **Play (▶) is not visible** — The **RX** tab is active. Click **TX** to switch to the TX chain view.

## Related

- [Record up to 30 seconds of post-PUDU TX audio](record-up-to-30-seconds-of-post-pudu-tx-audio.md)
- [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)
- [Aetherial Audio Chain overview](overview.md)
