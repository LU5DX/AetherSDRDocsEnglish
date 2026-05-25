# Open a Stage's Frameless Floating Editor from the Chain

Double-clicking a stage tile in the Aetherial Audio Chain opens that stage's frameless floating editor, giving you direct access to its parameters without leaving the main window layout.

**Note:** Double-clicking a TX chain tile opens the Aetherial Audio Channel Strip — the unified TX DSP window — rather than that stage's individual editor. From the Channel Strip you can access individual stage controls. Double-clicking an RX chain tile opens that stage's frameless floating editor directly.

## Before you start

- The Aetherial Audio (TXDSP) container must be visible. If it is not, click the **PUDU** tray button in the right sidebar to show it.
- Decide whether you want to edit a TX stage or an RX stage, and make sure the correct chain is active.

## Steps

1. If the chain is not already showing the side you want, click **TX** or **RX** in the header row of the Aetherial Audio Chain to switch to that chain.
2. Locate the stage tile you want to edit. TX chain tiles are labelled **EQ**, **COMP**, **GATE**, **DESS**, **TUBE**, **PUDU**, and **VERB**. RX chain tiles are labelled **EQ**, **AGC-G**, **AGC-C**, **DESS**, **TUBE**, and **EVO**.
3. Double-click the stage tile:
   - On the **TX** chain, double-clicking any stage tile opens the Aetherial Audio Channel Strip. Use the Channel Strip's own controls to reach the individual stage you want to edit.
   - On the **RX** chain, double-clicking a stage tile opens that stage's frameless floating editor directly.

A single click bypasses the stage instead of opening the editor. Make sure to double-click.

## What each control does

| Control                                                                                   | Kind          | Behavior                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------------------------------------------------------------------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **TX**                                                                                    | Toggle button | Shows the TX DSP chain. Amber 'VUDU' colour when selected. Last-active tab persists via `PooDooAudioActiveTab='TX'` / `'RX'`.                                                                                                                                                                                                                                                          |
| **RX**                                                                                    | Toggle button | Shows the RX DSP chain. Amber 'VUDU' colour when selected. Last-active tab persists via `PooDooAudioActiveTab='TX'` / `'RX'`.                                                                                                                                                                                                                                                          |
| **BYPASS**                                                                                | Toggle button | Checked: snapshots the currently-enabled stages on the active side (TX or RX) and disables all of them. Unchecked: re-enables just the stages that were on before. TX and RX maintain separate snapshots — the visual checked state tracks the side currently shown.                                                                                                                   |
| **Record** (circle glyph)                                                                 | Toggle button | Captures up to 30 s of post-PUDU TX audio; click again to stop (playback starts automatically). Tooltip: 'Record up to 30 s of post-PooDoo™ TX audio (MIC must be set to PC and DAX off).' Hidden in RX mode. Only enabled when the mic input is ready and playback is not running. Pulses red while recording.                                                                        |
| **Play** (triangle glyph)                                                                 | Toggle button | Plays back the captured PUDU audio; click again to cancel. Hidden in RX mode. Only enabled once a recording exists and recording is not active. Pulses green while playing.                                                                                                                                                                                                            |
| TX chain stage (**EQ** / **COMP** / **GATE** / **DESS** / **TUBE** / **PUDU** / **VERB**) | Stage tile    | Single-click toggles bypass. Double-click opens the Aetherial Audio Channel Strip (the unified TX DSP window). Drag reorders the chain.                                                                                                                                                                                                                                                |
| RX chain stage (**EQ** / **AGC-G** / **AGC-C** / **DESS** / **TUBE** / **EVO**)           | Stage tile    | Single-click toggles bypass. Double-click opens the stage's frameless floating editor in RX mode. Drag reorders the RX chain independently of the TX chain. All six stages fully implemented. Distinct mime type `application/x-aethersdr-rx-chain-stage` prevents stray drops between the two strips.                                                                                |
| **RADIO** status tile                                                                     | Indicator     | Non-interactive RX-side bookend. Greens when PC Audio (standard SSB stream) is enabled. Only visible in RX mode.                                                                                                                                                                                                                                                                       |
| **ADSP** status / bypass tile                                                             | Toggle button | Interactive RX-side tile that mirrors which client-side noise reducer is currently active. Label rotates to the active module's short name (e.g. 'NR2', 'NR4', 'BNR'); falls back to 'ADSP' when none is on. Single-click bypasses the entire NR cluster with an in-memory snapshot; single-click again restores the prior NR state. Double-click opens the AetherDSP Settings dialog. |
| **SPEAK** status tile                                                                     | Indicator     | Non-interactive RX-side bookend. Greens when AetherSDR's audio output is unmuted. Only visible in RX mode.                                                                                                                                                                                                                                                                             |
## Tips

- The hint line below the chain reads "Click to bypass · Double click to edit · Drag to reorder" and serves as a quick reminder of these interactions.
- The TX and RX chains are independent. Opening an editor on the TX side does not affect the RX chain, and vice versa.
- The last-active tab (**TX** or **RX**) is restored when you reopen the applet, so you will land on the same chain you were editing previously.
- The **BYPASS** button stays in sync with the bypass state set from either the Aetherial Audio Channel Strip (TX) or directly via the RX engine. Toggling bypass from any location updates both the engine and the visual.
- The click discrimination interval used to distinguish single-clicks from double-clicks is drawn from the Interaction Settings rather than the system double-click interval, so you can tune the sensitivity independently.

## Troubleshooting

- **Single-click opened the wrong action (bypass toggled instead of editor opening)** — You clicked once instead of twice. Click the stage tile a second time, or single-click again to restore the bypass state, then double-click to open the editor.
- **Double-clicking a TX stage tile opened the Channel Strip instead of that stage's editor** — This is expected behaviour. Double-click on the TX chain is the canonical "edit my TX audio" gesture and always opens the Channel Strip. Use the Channel Strip's own controls to navigate to the specific stage.
- **The TXDSP container is not visible so the chain cannot be reached** — Click the **PUDU** tray button in the right sidebar to toggle the Aetherial Audio container on.

## Related

- [Aetherial Audio Chain overview](overview.md)
- [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Bypass every RX stage at once](bypass-every-rx-stage-at-once.md)
- [Reorder the TX DSP chain](reorder-the-tx-dsp-chain.md)
- [Reorder the RX DSP chain (independent of TX order)](reorder-the-rx-dsp-chain-independent-of-tx-order.md)