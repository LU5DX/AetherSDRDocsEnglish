# Reorder the RX DSP chain (independent of TX order)

This page explains how to drag RX DSP stages into a different order in the Aetherial Audio Chain. The RX chain order is stored and applied completely separately from the TX chain order.

## Before you start

- The Aetherial Audio (TXDSP) container must be visible. If it is not, click the tray button labelled "PUDU" in the right sidebar to show it.
- You must be on the RX tab of the applet. The RX chain is not visible while TX is selected.

## Steps

1. In the Aetherial Audio Chain applet, click **RX**. The RX chain strip replaces the TX strip. The stages shown are: EQ, GATE, COMP, TUBE, and PUDU, bracketed by the RADIO, DSP, and SPEAK status tiles.
2. Locate the stage you want to move. The hint text below the strip reads "Click to bypass · Double click to edit · Drag to reorder" — this confirms drag-to-reorder is active.
3. Click and hold the stage tile, then drag it left or right. A vertical cyan bar appears between tiles to preview where the stage will land.
4. Release to drop the stage at the indicated position. The chain updates immediately and the new order is persisted to `ClientCompRxChainStages`.

## What each control does

| Control | Kind | Default | Behavior | Setting key |
|---|---|---|---|---|
| **RX** | Toggle button | Unchecked | Switches the chain strip to show the RX DSP stages. Last-active tab (TX or RX) is restored on next launch. | `PooDooAudioActiveTab` |
| **TX** | Toggle button | Checked | Switches the chain strip to show the TX DSP stages. The TX order is independent of the RX order. | `PooDooAudioActiveTab` |
| **RX chain stage (EQ / GATE / COMP / TUBE / PUDU)** | Drag handle | Factory default order | Single-click toggles bypass for that stage. Double-click opens its frameless floating editor. Drag left or right to reorder. | `ClientCompRxChainStages` |
| **BYPASS** | Toggle button | Unchecked | Checked: snapshots all currently-enabled RX stages and disables them. Unchecked: re-enables only the stages that were on before. TX and RX maintain separate snapshots. | — |

## Tips

- The RX chain uses a distinct internal drag type (`application/x-aethersdr-rx-chain-stage`), so stages cannot be accidentally dropped into the TX chain strip and vice versa.
- Switching to the TX tab and back does not disturb the RX order you set. Each chain stores its state independently.
- The RADIO, DSP, and SPEAK tiles at each end of the RX strip are status indicators only — they cannot be moved or bypassed.

## Troubleshooting

- **Dragging a stage has no effect** — confirm you are on the RX tab (the **RX** button should show amber text and border). Dragging on the TX strip affects only `ClientCompTxChainStages`, not the RX order.
- **The RX chain is not visible** — the TXDSP container may be hidden. Click the tray button labelled "PUDU" to toggle it on.
- **The chain order reverts after relaunch** — `ClientCompRxChainStages` is the persisted key. If the setting cannot be written (e.g. a read-only profile or permissions issue), the order will not survive a restart.

## Related

- [Reorder the TX DSP chain](reorder-the-tx-dsp-chain.md)
- [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)
- [Bypass every RX stage at once](bypass-every-rx-stage-at-once.md)
- [Open a stage's frameless floating editor from the chain](open-a-stage-s-frameless-floating-editor-from-the-chain.md)
- [See at a glance whether PC Audio, the noise reducer, and audio output are live (RX status tiles)](see-at-a-glance-whether-pc-audio-the-noise-reducer-and-audio-output-are-live-rx-status-tiles.md)
- [Aetherial Audio Chain overview](overview.md)
