# Reorder the TX DSP chain

Drag the stage tiles in the PooDoo Audio Chain strip to change the order in which DSP stages process your TX audio. The new order is persisted in `ClientCompTxChainStages`.

## Before you start

- The PooDoo Audio (TXDSP) container must be visible. If it is not, click the tray button labelled `PUDU` in the right sidebar to show it.
- TX must be selected in the applet. The TX button is checked by default; if RX is selected, click TX to switch back to the interactive chain view.

## Steps

1. Locate the chain strip at the top of the PooDoo Audio container. The strip shows the stages in their current processing order: Eq, Comp, Gate, DeEss, Tube, Enh, Reverb.
2. Click and hold any stage tile (for example, Chain stage (Comp)).
3. Drag the tile left or right to the position you want in the chain. A visual indicator shows where the stage will land.
4. Release the mouse button. The stage snaps into its new position and the order is saved to `ClientCompTxChainStages`.

## What each control does

| Control | Kind | Behavior | Default | Setting key |
|---|---|---|---|---|
| TX | Toggle button | Shows the interactive TX DSP chain. Amber colour when selected. | Checked | — |
| RX | Toggle button | Switches to the RX placeholder view. Dragging is not available in this mode. | Unchecked | — |
| BYPASS | Toggle button | Checked: disables all stages at once. Unchecked: restores only the stages that were enabled before. | Unchecked | — |
| Chain stage (Eq) | Drag handle | Single-click bypasses EQ; double-click opens editor; drag reorders. | — | — |
| Chain stage (Comp) | Drag handle | Single-click bypasses compressor; double-click opens editor; drag reorders. | — | — |
| Chain stage (Gate) | Drag handle | Single-click bypasses gate; double-click opens editor; drag reorders. | — | — |
| Chain stage (DeEss) | Drag handle | Single-click bypasses de-esser; double-click opens editor; drag reorders. | — | — |
| Chain stage (Tube) | Drag handle | Single-click bypasses tube saturator; double-click opens editor; drag reorders. | — | — |
| Chain stage (Enh / PUDU) | Drag handle | Single-click bypasses PUDU exciter; double-click opens editor; drag reorders. | — | — |
| Chain stage (Reverb) | Drag handle | Single-click bypasses reverb; double-click opens editor; drag reorders. | — | — |

## Tips

- The hint text below the chain strip reads "Click to bypass · Double click to edit · Drag to reorder" and is visible whenever TX mode is active. It is hidden in RX mode.
- A single click on a stage tile bypasses that stage, not the whole chain. Be careful not to click when you intend to drag.
- BYPASS does not reset the stage order. Reordering while BYPASS is active is preserved when you uncheck BYPASS.

## Troubleshooting

- **The chain strip is not visible** — The RX button may be selected. Click TX to switch to the interactive chain view.
- **Dragging has no effect** — Confirm the PooDoo Audio container is showing the TX chain. The drag-to-reorder interaction is not available in the RX placeholder view.

## Related

- [PooDoo Audio Chain overview](overview.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Open a stage's floating editor from the chain](open-a-stage-s-floating-editor-from-the-chain.md)
- [Re-enable a specific stage after a global bypass](re-enable-a-specific-stage-after-a-global-bypass.md)
- [Switch between TX chain view and RX placeholder](switch-between-tx-chain-view-and-rx-placeholder.md)
