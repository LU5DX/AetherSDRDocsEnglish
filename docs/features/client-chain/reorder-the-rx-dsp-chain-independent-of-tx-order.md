# Reorder the RX DSP chain (independent of TX order)

This page explains how to drag RX DSP stages into a new order inside the Aetherial Audio Chain applet. The RX chain order is stored and applied independently from the TX chain.

## Before you start

- The Aetherial Audio (TXDSP) container must be visible. If it is not, click the tray button labelled "PUDU" in the applet panel to show it.
- The RX chain strip must be active. If the TX chain is currently shown, switch to RX first (see [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)).

## Steps

1. In the Aetherial Audio Chain header row, click "RX" to show the RX chain strip. The RX button turns amber when selected.
2. Locate the stage you want to move. The RX chain contains up to five stages: EQ, GATE, COMP, TUBE, and PUDU, bookended by the non-interactive RADIO, DSP, and SPEAK status tiles.
3. Click and hold the stage tile you want to reorder.
4. Drag it left or right along the chain strip. A vertical cyan bar appears between tiles to show where the stage will land.
5. Release to drop the stage in the new position. The chain reorders immediately and the new order is saved to `ClientCompRxChainStages`.

## What each control does

| Control | Kind | Behavior | Persisted key |
|---|---|---|---|
| RX | Toggle button | Shows the RX chain strip; becomes the active side for drag-reorder, bypass, and editing. Default: unchecked. | `PooDooAudioActiveTab` |
| RX chain stage (EQ / GATE / COMP / TUBE / PUDU) | Drag handle | Single-click toggles bypass; double-click opens the frameless editor; drag reorders the chain. | `ClientCompRxChainStages` |
| RADIO status tile | Indicator | Non-interactive left bookend; greens when PC Audio is enabled. Not draggable. | — |
| DSP status tile | Indicator | Non-interactive tile showing the active noise reducer short name (e.g. NR2, NR4, BNR) or generic "DSP". Not draggable. | — |
| SPEAK status tile | Indicator | Non-interactive right bookend; greens when AetherSDR's audio output is unmuted. Not draggable. | — |

## Tips

- The hint text below the chain reads "Click to bypass · Double click to edit · Drag to reorder" and applies to both TX and RX modes.
- The RX chain uses a distinct drag-and-drop type internally, so stages cannot be accidentally dropped into the TX chain strip and vice versa.
- Switching to TX with "TX" and reordering there does not affect the saved RX order. The two chains maintain independent stage sequences.

## Troubleshooting

- **Dragging a stage has no effect** — Confirm the "RX" button is checked (amber). If the TX chain strip is visible, drops are ignored by the RX chain.
- **The RADIO, DSP, or SPEAK tiles move unexpectedly** — These tiles are status indicators and are not draggable. Only the five named stage tiles (EQ, GATE, COMP, TUBE, PUDU) can be reordered.
- **Reordered chain reverts after restart** — This should not happen if `ClientCompRxChainStages` is being written. Verify AetherSDR has write access to its settings storage location.

## Related

- [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)
- [Reorder the TX DSP chain](reorder-the-tx-dsp-chain.md)
- [Bypass every RX stage at once](bypass-every-rx-stage-at-once.md)
- [Open a stage's frameless floating editor from the chain](open-a-stage-s-frameless-floating-editor-from-the-chain.md)
- [See at a glance whether PC Audio, the noise reducer, and audio output are live (RX status tiles)](see-at-a-glance-whether-pc-audio-the-noise-reducer-and-audio-output-are-live-rx-status-tiles.md)
