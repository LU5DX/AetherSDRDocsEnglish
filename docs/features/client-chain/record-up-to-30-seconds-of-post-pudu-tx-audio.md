# Aetherial Audio Chain

The Aetherial Audio Chain applet shows the client-side DSP signal flow as a horizontal strip of stages, with independent TX and RX chains. The TX chain runs Parametric EQ, Compressor (with built-in pre-comp Drive + Phase-rotator PAPR reduction), Gate, De-Ess (split-band, user-selectable 12–48 dB/oct slope), Tube (with RN2 noise-reduction toggle on TX), PUDU exciter, Reverb. The RX chain runs EQ, AGC-G (gate), AGC-C (compressor), DESS (de-esser), TUBE, EVO (pudu) — all six RX stages are fully implemented — bracketed by RADIO / ADSP / SPEAK status tiles. The ADSP tile is a clickable toggle that bypasses the entire client-side NR cluster (NR2 / NR4 / MNR / DFNR / RN2 / NVAFX); an in-memory snapshot restores the prior NR state on un-bypass.

## Record up to 30 seconds of post-PUDU TX audio

Use the built-in monitor recorder to capture and immediately play back how your transmitted audio sounds after it has passed through the full TX DSP chain, including PUDU. This helps you tune your chain settings without needing a second station to report back.

### Before you start

- The Aetherial Audio Chain applet must be open. If it is not visible, click the tray button labelled **PUDU** in the right sidebar.
- Your microphone input must be set to **PC** (not a radio front-panel mic source).
- DAX must be off. The tooltip on the record button reads: "MIC must be set to PC and DAX off."
- The **TX** tab must be active in the applet. The record controls are hidden when **RX** is selected.

### Steps

1. Click the **TX** tab button at the top of the Aetherial Audio Chain applet to ensure the TX chain is shown. The button turns amber when selected.
2. Confirm the record button (⏺) is enabled. It is enabled only when the mic input is ready and playback is not currently running. If it appears dimmed and unclickable, check that your mic source is set to PC and DAX is off.
3. Click **⏺** to start recording. The button pulses red to indicate capture is active. Recording stops automatically after 30 seconds, or you can stop it early.
4. To stop recording before 30 seconds have elapsed, click **⏺** again. Playback starts automatically once recording stops.
5. To cancel playback before it finishes, click **▶** while it is pulsing green.

## What each control does

| Control | Default | Behavior |
|---|---|---|
| **TX** / **RX** toggle buttons | TX is checked | Exclusive pair; shows and edits the corresponding DSP chain. Last-active tab persists via `PooDooAudioActiveTab='TX'` / `'RX'`. |
| **BYPASS** | Unchecked | Snapshots the currently-enabled stages on the active side (TX or RX) and disables all of them (including RN2). Uncheck to re-enable just the stages that were on before. TX and RX maintain separate snapshots. The visual checked state tracks the side currently shown. Scope is global (per audio engine), not per-profile — the button stays pressed across Channel Strip profile switches. |
| **⏺** (record) | Unchecked | Captures up to 30 s of post-PUDU TX audio. Click again to stop; playback starts automatically. Hidden in RX mode. Only enabled when the mic input is ready and playback is not running. Pulses red while recording. |
| **▶** (play) | Unchecked | Plays back the captured PUDU audio. Click again to cancel. Hidden in RX mode. Only enabled once a recording exists and recording is not active. Pulses green while playing. |
| TX chain stage (EQ / COMP / GATE / DESS / TUBE / PUDU / VERB) | N/A | Single-click toggles bypass for the stage; double-click opens its frameless floating editor (or the Channel Strip on TX); drag reorders the TX chain. Hint text: "Click to bypass · Double click to edit · Drag to reorder". |
| RX chain stage (EQ / AGC-G / AGC-C / DESS / TUBE / EVO) | N/A | Single-click toggles bypass for the RX stage; double-click opens its frameless floating editor in RX mode; drag reorders the RX chain. All six RX stages are fully implemented. Order is independent of the TX chain. Distinct mime type `application/x-aethersdr-rx-chain-stage` prevents stray drops between the two strips. |
| **RADIO** status tile | Always visible in RX mode | Greens when PC Audio (standard SSB stream) is enabled. Non-interactive. |
| **ADSP** status / bypass tile | Unchecked | Interactive RX-side tile that mirrors which client-side noise reducer is currently active. Label rotates to the active module's short name (e.g. 'NR2', 'NR4', 'BNR'); falls back to 'ADSP' when none is on. Single-click bypasses the entire NR cluster with an in-memory snapshot; single-click again restores the prior NR state. Double-click opens the AetherDSP Settings dialog. The bypass now correctly handles NVAFX in place of the legacy BNR module. |
| **SPEAK** status tile | Always visible in RX mode | Greens when AetherSDR's audio output is unmuted. Non-interactive. |

## Interaction settings

The click-discrimination interval used to distinguish a single click from a double-click is configurable via the **Interaction Settings** dialog. By default, AetherSDR uses the system double-click interval, but you can adjust it to suit your preference. This setting affects both the TX chain and RX chain widgets.

To adjust the interval:

1. Open **File > Settings**.
2. Select **Interaction** from the sidebar.
3. Adjust the **Click discrimination interval** slider.
4. Click **Apply**.

## Opening the TX DSP editor from the chain

Double-clicking any TX chain stage tile opens the Aetherial Audio Channel Strip — the unified TX DSP window. The channel strip provides access to all individual stage editors through its own controls. This double-click gesture is the standard way to open your TX audio settings from the chain applet.

## TX and RX BYPASS synchronisation

The **BYPASS** button in the Aetherial Audio Chain applet and the **BYPASS** button in the Aetherial Audio Channel Strip share a single engine-owned bypass state for each side. Pressing either button updates both. When you switch between the **TX** and **RX** tabs, the **BYPASS** button reflects the current engine state for the active side immediately.

## Tips

- The recorder captures audio at the point after the PUDU stage in the TX chain. To hear the effect of a specific stage, bypass or unbypass that stage, make a recording, and compare playback.
- You do not need to transmit to a receiver — the monitor records audio from the client-side DSP output directly.
- If you want to compare settings, stop the current recording, adjust a stage, record again, and play back to compare.
- To adjust individual TX stage settings, double-click any stage tile in the TX chain. The Aetherial Audio Channel Strip opens; use its controls to edit each stage.

## Troubleshooting

- **The ⏺ button is dimmed and cannot be clicked** — The mic input is not set to PC, DAX is on, or playback is currently running. Disable DAX, set the mic source to PC, and wait for any active playback to finish.
- **The ⏺ and ▶ buttons are not visible** — The **RX** tab is active. Click **TX** to switch to the TX chain; both buttons are hidden in RX mode.
- **Playback does not start after recording stops** — No audio was captured. Confirm your mic input is delivering audio to the PC during the recording window.
- **Double-clicking a TX stage tile does not open a floating editor** — This is expected behaviour. Double-clicking opens the Aetherial Audio Channel Strip instead. Access individual stage editors from within the channel strip.
- **The BYPASS button state does not match what I set in the channel strip** — If you have just connected the audio engine, reload the applet or switch away from and back to the active tab so the button can re-read the current engine state.
- **Double-click actions feel too fast or too slow** — Adjust the click discrimination interval in **File > Settings > Interaction**.

## Related

- [Aetherial Audio Chain overview](overview.md)
- [Play back the captured PUDU audio](play-back-the-captured-pudu-audio.md)
- [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)
- [Open a stage's frameless floating editor from the chain](open-a-stage-s-frameless-floating-editor-from-the-chain.md)