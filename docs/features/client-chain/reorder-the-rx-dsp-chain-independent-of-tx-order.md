# Reorder the RX DSP chain (independent of TX order)

This page explains how to drag RX DSP stages into a new order inside the Aetherial Audio Chain applet. The RX chain order is stored and applied independently from the TX chain.

## Before you start

- The Aetherial Audio (TXDSP) container must be visible. If it is not, click the tray button labelled "PUDU" in the applet panel to show it.
- The RX chain strip must be active. If the TX chain is currently shown, switch to RX first (see [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)).

## Steps

1. In the Aetherial Audio Chain header row, click "RX" to show the RX chain strip. The RX button turns amber when selected.
2. Locate the stage you want to move. The RX chain contains up to six stages: EQ, AGC-G, AGC-C, DESS, TUBE, and EVO, bookended by the non-interactive RADIO, ADSP, and SPEAK status tiles.
3. Click and hold the stage tile you want to reorder.
4. Drag it left or right along the chain strip. A vertical cyan bar appears between tiles to show where the stage will land.
5. Release to drop the stage in the new position. The chain reorders immediately and the new order is saved to `ClientCompRxChainStages`.

## What each control does

| Control                                                       | Kind                                                                                                                     | Behavior                                                                                                                                                                                                                                                                                                                                                                                                        |
|---------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TX                                                            | Shows and edits the TX DSP chain (ClientChainWidget) — fully interactive: click-bypass, double-click-edit, drag-reorder. | Part of an exclusive pair with RX; amber 'VUDU' colour when selected. Last-active tab persists via PooDooAudioActiveTab='TX' / 'RX'.                                                                                                                                                                                                                                                                            |
| RX                                                            | Toggle button                                                                                                            | Shows and edits the RX DSP chain (ClientRxChainWidget) — also fully interactive with click-bypass, double-click-edit, drag-reorder; bookended by RADIO / ADSP / SPEAK status tiles. Each side keeps independent stage state, chain order, and BYPASS snapshot. Default: unchecked.                                                                                                                              |
| BYPASS                                                        | Toggle button                                                                                                            | Checked: snapshots the currently-enabled stages on the active side (TX or RX) and disables all of them. Unchecked: re-enables just the stages that were on before. Stages toggled manually while BYPASS was active are preserved outside the snapshot. TX and RX maintain separate snapshots.                                                                                                                   |
| Record (circle glyph)                                         | Toggle button                                                                                                            | Captures up to 30 s of post-PUDU TX audio; click again to stop (playback starts automatically). Tooltip: 'Record up to 30 s of post-PooDoo™ TX audio (MIC must be set to PC and DAX off).' Hidden in RX mode (TX-only feature). Only enabled when the mic input is ready and playback is not running. Pulses red while recording.                                                                               |
| Play (triangle glyph)                                         | Toggle button                                                                                                            | Plays back the captured PUDU audio; click again to cancel. Hidden in RX mode. Only enabled once a recording exists and recording is not active. Pulses green while playing.                                                                                                                                                                                                                                     |
| TX chain stage (EQ / COMP / GATE / DESS / TUBE / PUDU / VERB) | Drag handle                                                                                                              | Single-click toggles bypass for the stage; double-click opens the Aetherial Audio Channel Strip (v0.9.7+); drag reorders the TX chain. Hint text below reads 'Click to bypass · Double click to edit · Drag to reorder'.                                                                                                                                                                                        |
| RX chain stage (EQ / AGC-G / AGC-C / DESS / TUBE / EVO)       | Drag handle                                                                                                              | Single-click toggles bypass for the RX stage; double-click opens its frameless floating editor in RX mode; drag reorders the RX chain. All six RX stages (EQ, AGC-G/Gate, AGC-C/Comp, DESS/DeEss, TUBE, EVO/Pudu) are fully implemented. Order is independent of the TX chain. Distinct mime type prevents stray drops.                                                                                         |
| RADIO status tile                                             | Indicator                                                                                                                | Non-interactive RX-side bookend. Greens when PC Audio (the standard SSB stream) is enabled. Only visible in RX mode.                                                                                                                                                                                                                                                                                            |
| ADSP status / bypass tile                                     | Toggle button                                                                                                            | Interactive RX-side tile that mirrors which client-side noise reducer is currently active. Label rotates to the active module's short name (e.g. 'NR2', 'NR4', 'BNR'); falls back to 'ADSP' when none is on. Single-click bypasses the entire NR cluster with an in-memory snapshot; single-click again restores the prior NR state. Double-click opens the AetherDSP Settings dialog. Only visible in RX mode. |
| SPEAK status tile                                             | Indicator                                                                                                                | Non-interactive RX-side bookend. Greens when AetherSDR's audio output is unmuted. Only visible in RX mode.                                                                                                                                                                                                                                                                                                      |
## TX chain double-click behaviour (v0.9.7)

In v0.9.7, double-clicking any TX chain stage tile no longer opens that stage's individual frameless floating editor directly. Instead, it opens the unified **Aetherial Audio Channel Strip** — the single TX DSP window. The per-stage floating editors remain accessible from within the channel strip. This change affects only the TX chain; double-clicking an RX stage still opens that stage's frameless floating editor as before.

## BYPASS synchronisation (v0.9.8)

The BYPASS button now mirrors the engine-owned bypass state for both TX and RX independently. This means:

- The BYPASS button state updates automatically when switching between TX and RX modes.
- Activating BYPASS from within the Aetherial Audio Channel Strip updates the chain applet's BYPASS button, and vice versa for both TX and RX.
- The visual checked state of the BYPASS button always reflects the engine state for the currently displayed side (TX or RX).

## Tips

- The hint text below the chain reads "Click to bypass · Double click to edit · Drag to reorder" and applies to both TX and RX modes.
- The RX chain uses a distinct drag-and-drop type internally, so stages cannot be accidentally dropped into the TX chain strip and vice versa.
- Switching to TX with "TX" and reordering there does not affect the saved RX order. The two chains maintain independent stage sequences.
- On the TX side, double-clicking any stage is the canonical gesture for opening the TX audio editor. Use the channel strip's own controls to navigate to individual stage settings.

## Troubleshooting

- **Dragging a stage has no effect** — Confirm the "RX" button is checked (amber). If the TX chain strip is visible, drops are ignored by the RX chain.
- **The RADIO, ADSP, or SPEAK tiles move unexpectedly** — These tiles are status indicators and are not draggable. Only the six named stage tiles (EQ, AGC-G, AGC-C, DESS, TUBE, EVO) can be reordered.
- **Reordered chain reverts after restart** — This should not happen if `ClientCompRxChainStages` is being written. Verify AetherSDR has write access to its settings storage location.
- **The BYPASS button state does not match between TX and RX** — Ensure the audio engine has initialised before opening the chain applet. Each side maintains its own engine-owned bypass state, and switching modes updates the button automatically.

## Related

- [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)
- [Reorder the TX DSP chain](reorder-the-tx-dsp-chain.md)
- [Bypass every RX stage at once](bypass-every-rx-stage-at-once.md)
- [Open a stage's frameless floating editor from the chain](open-a-stage-s-frameless-floating-editor-from-the-chain.md)
- [See at a glance whether PC Audio, the noise reducer, and audio output are live (RX status tiles)](see-at-a-glance-whether-pc-audio-the-noise-reducer-and-audio-output-are-live-rx-status-tiles.md)