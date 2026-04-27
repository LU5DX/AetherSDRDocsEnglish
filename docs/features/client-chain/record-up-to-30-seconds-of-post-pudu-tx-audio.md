# Record up to 30 seconds of post-PUDU TX audio

Use the built-in monitor recorder to capture and immediately play back how your transmitted audio sounds after it has passed through the full TX DSP chain, including PUDU. This helps you tune your chain settings without needing a second station to report back.

## Before you start

- The Aetherial Audio (TXDSP) container must be open. If it is not visible, click the tray button labelled **PUDU** in the right sidebar.
- Your microphone input must be set to **PC** (not a radio front-panel mic source).
- DAX must be off. The tooltip on the record button reads: "MIC must be set to PC and DAX off."
- The **TX** tab must be active in the applet. The record controls are hidden when **RX** is selected.

## Steps

1. Click the **TX** tab button at the top of the Aetherial Audio Chain applet to ensure the TX chain is shown. The button turns amber when selected.
2. Confirm the record button (⏺) is enabled. It is enabled only when the mic input is ready and playback is not currently running. If it appears dimmed and unclickable, check that your mic source is set to PC and DAX is off.
3. Click **⏺** to start recording. The button pulses red to indicate capture is active. Recording stops automatically after 30 seconds, or you can stop it early.
4. To stop recording before 30 seconds have elapsed, click **⏺** again. Playback starts automatically once recording stops.
5. To cancel playback before it finishes, click **▶** while it is pulsing green.

## What each control does

| Control | Default | Behavior | Notes |
|---|---|---|---|
| **⏺** (record) | Unchecked | Captures up to 30 s of post-PUDU TX audio. Click again to stop; playback starts automatically. | Pulses red while recording. Disabled when mic input is not ready or playback is running. Hidden in RX mode. |
| **▶** (play) | Unchecked | Plays back the captured audio. Click again to cancel. | Pulses green while playing. Enabled only after a recording exists and recording is not active. Hidden in RX mode. |

## Tips

- The recorder captures audio at the point after the PUDU stage in the TX chain. To hear the effect of a specific stage, bypass or unbypas that stage, make a recording, and compare playback.
- You do not need to transmit to a receiver — the monitor records audio from the client-side DSP output directly.
- If you want to compare settings, stop the current recording, adjust a stage, record again, and play back to compare.

## Troubleshooting

- **The ⏺ button is dimmed and cannot be clicked** — The mic input is not set to PC, DAX is on, or playback is currently running. Disable DAX, set the mic source to PC, and wait for any active playback to finish.
- **The ⏺ and ▶ buttons are not visible** — The **RX** tab is active. Click **TX** to switch to the TX chain; both buttons are hidden in RX mode.
- **Playback does not start after recording stops** — No audio was captured. Confirm your mic input is delivering audio to the PC during the recording window.

## Related

- [Aetherial Audio Chain overview](overview.md)
- [Play back the captured PUDU audio](play-back-the-captured-pudu-audio.md)
- [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)
- [Open a stage's frameless floating editor from the chain](open-a-stage-s-frameless-floating-editor-from-the-chain.md)
