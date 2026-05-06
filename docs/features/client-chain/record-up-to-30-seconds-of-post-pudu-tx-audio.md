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

| Control | Default | Behavior |
|---|---|---|
| **⏺** (record) | Unchecked | Captures up to 30 s of post-PUDU TX audio. Click again to stop; playback starts automatically. |
| **▶** (play) | Unchecked | Plays back the captured audio. Click again to cancel. |
| RX chain stage (EQ / AGC-T / AGC-C / TUBE / PUDU) | — | Single-click toggles bypass for the RX stage; double-click opens its frameless floating editor in RX mode; drag reorders the RX chain. All five RX stages (EQ, AGC-T/Gate, AGC-C/Comp, Tube, PUDU) are fully implemented. Order is independent of the TX chain. Distinct mime type `application/x-aethersdr-rx-chain-stage` prevents stray drops between the two strips. |

## Opening the TX DSP editor from the chain

In v0.9.7, double-clicking any TX chain stage tile no longer opens a per-stage floating editor directly. Instead, it opens the Aetherial Audio Channel Strip — the unified TX DSP window. The channel strip provides access to all individual stage editors through its own controls. This double-click gesture is now the standard way to open your TX audio settings from the chain applet.

## TX BYPASS synchronisation

The **BYPASS** button in the Aetherial Audio Chain applet and the **BYPASS** button in the Aetherial Audio Channel Strip now share a single engine-owned bypass state. Pressing either button updates both. When you switch to the TX side of the applet, the **BYPASS** button reflects the current engine state immediately.

## Tips

- The recorder captures audio at the point after the PUDU stage in the TX chain. To hear the effect of a specific stage, bypass or unbypass that stage, make a recording, and compare playback.
- You do not need to transmit to a receiver — the monitor records audio from the client-side DSP output directly.
- If you want to compare settings, stop the current recording, adjust a stage, record again, and play back to compare.
- To adjust individual TX stage settings, double-click any stage tile in the TX chain. The Aetherial Audio Channel Strip opens; use its controls to edit each stage.

## Troubleshooting

- **The ⏺ button is dimmed and cannot be clicked** — The mic input is not set to PC, DAX is on, or playback is currently running. Disable DAX, set the mic source to PC, and wait for any active playback to finish.
- **The ⏺ and ▶ buttons are not visible** — The **RX** tab is active. Click **TX** to switch to the TX chain; both buttons are hidden in RX mode.
- **Playback does not start after recording stops** — No audio was captured. Confirm your mic input is delivering audio to the PC during the recording window.
- **Double-clicking a TX stage tile does not open a floating editor** — This is expected behaviour from v0.9.7 onwards. Double-clicking now opens the Aetherial Audio Channel Strip instead. Access individual stage editors from within the channel strip.
- **The BYPASS button state does not match what I set in the channel strip** — If you have just connected the audio engine, reload the applet or switch away from and back to the TX tab so the button can re-read the current engine state.

## Related

- [Aetherial Audio Chain overview](overview.md)
- [Play back the captured PUDU audio](play-back-the-captured-pudu-audio.md)
- [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)
- [Open a stage's frameless floating editor from the chain](open-a-stage-s-frameless-floating-editor-from-the-chain.md)