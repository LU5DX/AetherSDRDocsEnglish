# Reorder the TX DSP Chain

Drag the stage tiles in the PooDoo Audio Chain strip to change the order in which DSP processing is applied to your TX audio. The new order is saved automatically in `ClientCompTxChainStages`.

## Before you start

- The PooDoo Audio (TXDSP) container must be visible. If it is not, click the tray button labelled **PUDU** in the right sidebar to show it.
- The **TX** mode button must be selected (it is selected by default). The RX view does not support reordering.

## Steps

1. Locate the chain strip at the top of the PooDoo Audio container. It shows the stages in their current order: **Eq**, **Comp**, **Gate**, **DeEss**, **Tube**, **Enh / PUDU**, **Reverb**.
2. Click and hold the stage tile you want to move.
3. Drag it left or right to the target position. The other tiles shift to indicate the insertion point.
4. Release to drop the stage in the new position. The chain updates immediately and the new order is saved to `ClientCompTxChainStages`.

## What each control does

| Control | Kind | Default | Behavior |
|---|---|---|---|
| **TX** | Toggle button | Checked | Shows the interactive TX DSP chain. Amber when selected. |
| **RX** | Toggle button | Unchecked | Switches to the RX placeholder view. Reordering is not available in this mode. |
| **BYPASS** | Toggle button | Unchecked | When checked, disables every stage at once. When unchecked, restores the stages that were active before. |
| **Chain stage (Eq)** | Drag handle | — | Single-click bypasses the EQ stage; double-click opens its editor; drag reorders. |
| **Chain stage (Comp)** | Drag handle | — | Single-click bypasses the compressor; double-click opens its editor; drag reorders. |
| **Chain stage (Gate)** | Drag handle | — | Single-click bypasses the gate; double-click opens its editor; drag reorders. |
| **Chain stage (DeEss)** | Drag handle | — | Single-click bypasses the de-esser; double-click opens its editor; drag reorders. |
| **Chain stage (Tube)** | Drag handle | — | Single-click bypasses the tube saturator; double-click opens its editor; drag reorders. |
| **Chain stage (Enh / PUDU)** | Drag handle | — | Single-click bypasses the PUDU exciter; double-click opens its editor; drag reorders. |
| **Chain stage (Reverb)** | Drag handle | — | Single-click bypasses the reverb; double-click opens its editor; drag reorders. |

The persisted setting `Applet_TXDSP` controls whether the PooDoo Audio container is shown at all.

## Tips

- The hint line beneath the chain strip reads "Click to bypass · Double click to edit · Drag to reorder" and is visible only when **TX** is selected.
- A single-click on a stage tile bypasses that stage, not just picks it up. Start your drag before releasing to avoid an unintended bypass toggle.
- To silence all stages temporarily without losing the current order, use **BYPASS** rather than bypassing stages individually. See [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md).

## Troubleshooting

- **The chain strip is not visible** — The container may be hidden. Click the **PUDU** tray button in the right sidebar to show it, or check that **TX** is selected rather than **RX**.
- **Dragging has no effect** — Confirm that **TX** is selected. The RX placeholder does not support drag-to-reorder.
- **Stages snap back after a drag** — If **BYPASS** is checked, the bypass snapshot may conflict with the reorder. Uncheck **BYPASS** first, reorder, then re-enable **BYPASS** if needed.

## Related

- [PooDoo Audio Chain overview](overview.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Open a stage's floating editor from the chain](open-a-stage-s-floating-editor-from-the-chain.md)
- [Re-enable a specific stage after a global bypass](re-enable-a-specific-stage-after-a-global-bypass.md)
