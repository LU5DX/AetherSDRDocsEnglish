# Reorder the TX DSP chain

Drag TX DSP stages into a different order to change the sequence in which your audio is processed before transmission. The new order is saved automatically and persists across restarts.

## Before you start

- The Aetherial Audio Chain container must be visible. If it is not, click the tray button labelled **PUDU** in the right sidebar to show it.
- The TX chain must be the active side. If the **RX** button is currently selected, click **TX** first.

## Steps

1. Open the Aetherial Audio Chain container by clicking the **PUDU** tray button if it is not already visible.
2. Click **TX** in the header row to ensure the TX chain is shown.
3. Locate the stage you want to move. The TX chain contains these stages: **EQ**, **COMP**, **GATE**, **DESS**, **TUBE**, **PUDU**, **VERB**.
4. Click and hold on the stage tile you want to move, then drag it left or right along the chain strip.
5. A vertical cyan bar appears between tiles as you drag, showing where the stage will land.
6. Release the mouse button to drop the stage into the new position.
7. Repeat for any other stages you want to reorder.

The new chain order is saved automatically to `ClientCompTxChainStages`.

## What each control does

| Control                                                           | Kind          | Behavior                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------------------------------------------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **TX**                                                            | Toggle button | Shows and enables editing of the TX DSP chain. Must be selected to drag TX stages. Amber "PooDoo" colour when selected. Last-active tab persists via `PooDooAudioActiveTab`.                                                                                                                                                                                                                                                                                                                                                                                        |
| **RX**                                                            | Toggle button | Switches the strip to the RX chain. Drag operations on the RX strip do not affect TX order. Each side keeps independent stage state, chain order, and BYPASS snapshot.                                                                                                                                                                                                                                                                                                                                                                                              |
| TX chain stage (**EQ / COMP / GATE / DESS / TUBE / PUDU / VERB**) | Drag handle   | Single-click toggles bypass for that stage. Double-click opens its frameless floating editor (or the Aetherial Audio Channel Strip). Drag left or right to reorder. Hint text below chain reads "Click to bypass · Double click to edit · Drag to reorder".                                                                                                                                                                                                                                                                                                         |
| **BYPASS**                                                        | Toggle button | Disables every stage on the currently shown chain side at once, including RN2. When checked, snapshots the currently-enabled stages on the active side (TX or RX) and disables all of them. Unchecked: re-enables just the stages that were on before. TX and RX maintain separate snapshots. The scope is global (per audio engine), not per-profile — the button stays pressed across Channel Strip profile switches.                                                                                                                                             |
| RX chain stage (**EQ / AGC-G / AGC-C / DESS / TUBE / EVO**)       | Drag handle   | Single-click toggles bypass for the RX stage. Double-click opens its frameless floating editor in RX mode. Drag left or right to reorder the RX chain. Order is independent of the TX chain. Distinct mime type 'application/x-aethersdr-rx-chain-stage' prevents stray drops between the two strips.                                                                                                                                                                                                                                                               |
| **RADIO** status tile                                             | Indicator     | Non-interactive RX-side bookend. Greens when PC Audio (the standard SSB stream) is enabled. Only visible in RX mode.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **ADSP** status / bypass tile                                     | Toggle button | Interactive RX-side tile that mirrors which client-side noise reducer is currently active. Label rotates to the active module's short name (e.g. 'NR2', 'NR4', 'BNR'); falls back to 'ADSP' when none is on. Single-click bypasses the entire NR cluster with an in-memory snapshot; single-click again restores the prior NR state. Double-click opens the AetherDSP Settings dialog. Only visible in RX mode. Adopts the same blue-ring + green-LED-dot styling as implemented stage tiles. Snapshot restoration falls back to NR2 if no modules were active at bypass-time. |
| **SPEAK** status tile                                             | Indicator     | Non-interactive RX-side bookend. Greens when AetherSDR's audio output is unmuted. Only visible in RX mode.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Record** (circle glyph)                                         | Toggle button | Captures up to 30 s of post-PUDU TX audio; click again to stop (playback starts automatically). Tooltip: "Record up to 30 s of post-PooDoo™ TX audio (MIC must be set to PC and DAX off)." Hidden in RX mode (TX-only feature). Only enabled when the mic input is ready and playback is not running. Pulses red while recording.                                                                                                                                                                                                                                   |
| **Play** (triangle glyph)                                         | Toggle button | Plays back the captured PUDU audio; click again to cancel. Hidden in RX mode. Only enabled once a recording exists and recording is not active. Pulses green while playing.                                                                                                                                                                                                                                                                                                                                                                                         |

## Indicators

| Indicator                    | States                                  | Meaning                                                                                                          |
|------------------------------|-----------------------------------------|------------------------------------------------------------------------------------------------------------------|
| TX endpoint indicator        | idle, red pulse                         | Red pulse while the user is transmitting on their own slice (driven by TransmitModel::moxChanged). TX chain only. |
| MIC ready indicator          | ready, not ready                        | Enables/disables the record button based on mic source (PC) and DAX state.                                       |
| Monitor record pulse         | idle, bright red, dim red               | 500 ms pulse while the post-PUDU recorder is capturing audio.                                                     |
| Monitor play pulse           | idle, bright green, dim green           | 500 ms pulse while captured audio is being played back.                                                           |
| Interaction hint             | Click to bypass · Double click to edit · Drag to reorder | Static usage hint, shown on both TX and RX modes.                                                  |
| Drop indicator               | idle, vertical cyan bar between two tiles | Live preview of where a dragged stage will land before release; rendered by both chain widgets during drag.       |

## Tips

- The hint text below the chain reads "Click to bypass · Double click to edit · Drag to reorder" as a quick reminder of all three interactions.
- TX and RX chain orders are fully independent. Reordering the TX chain has no effect on `ClientCompRxChainStages`.
- The RX chain stage labels are **AGC-G** (gate) and **AGC-C** (compressor). These correspond to the gate and compressor functions respectively. All six RX stages (EQ, AGC-G, AGC-C, DESS, TUBE, EVO) are fully implemented.
- A single-click on a stage tile toggles its bypass state, not a reorder. Make sure you are dragging, not clicking, when you intend to move a stage.
- If **BYPASS** is currently checked when you reorder, the stage positions still update. The bypass snapshot is based on which stages were enabled, not their position.
- Double-clicking any TX chain stage tile opens the Aetherial Audio Channel Strip, which provides the unified TX DSP editor. The **BYPASS** button in the channel strip and the **BYPASS** button on the chain applet control the same engine-level TX bypass state and stay in sync with each other automatically.
- The **BYPASS** button now synchronizes with the engine-level bypass for both TX and RX modes. When you toggle bypass in the Aetherial Audio Channel Strip (TX) or in the RX chain editor, the chain applet's BYPASS button updates automatically. The **BYPASS** bypass state is global (per audio engine), not per-profile, so it stays pressed across Channel Strip profile switches.
- The **BYPASS** button disables every stage in the selected chain, including RN2.
- The click discrimination interval used to distinguish single-clicks from double-clicks is configurable via the `clickDiscriminationIntervalMs()` function in `InteractionSettings`. This setting interacts equally with both the TX and RX chain widgets.

## Troubleshooting

- **Drag does nothing or the drop is rejected** — Confirm **TX** is the selected mode button (amber highlight). Dragging is only active on the currently shown chain strip; if **RX** is selected, drops to the TX strip are not accepted.
- **New order is lost after restart** — This should not happen if the drop completed successfully (cyan drop indicator appeared and you released over the strip). If it recurs, check that AetherSDR has write access to its settings storage.
- **BYPASS button state does not match what I set in the channel strip** — The chain applet mirrors the appropriate bypass state based on the current mode. When TX is active, it shows the TX bypass state; when RX is active, it shows the RX bypass state. Both are synchronized with the engine.
- **Single-click is not reliably toggling bypass** — If you are clicking and dragging too quickly, the click may be interpreted as the start of a drag operation. Ensure you release the mouse button promptly after clicking without any lateral movement.

## Related

- [Aetherial Audio Chain overview](overview.md)
- [Reorder the RX DSP chain (independent of TX order)](reorder-the-rx-dsp-chain-independent-of-tx-order.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Open a stage's frameless floating editor from the chain](open-a-stage-s-frameless-floating-editor-from-the-chain.md)
- [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)