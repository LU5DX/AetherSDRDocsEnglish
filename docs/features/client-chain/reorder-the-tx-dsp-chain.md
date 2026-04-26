# Reorder the TX DSP Chain

Drag the stage tiles in the PooDoo Audio Chain to change the order in which DSP processing is applied to your transmitted audio. The new order is saved automatically in `ClientCompTxChainStages`.

## Before you start

- The PooDoo Audio (TXDSP) container must be visible. If it is not, click the `PUDU` tray button in the right sidebar to show it.
- The TX chain must be active. Confirm that TX is selected (amber highlight) in the header row. If RX is selected instead, click TX.

## Steps

1. Locate the chain strip showing the stage tiles: Eq, Comp, Gate, DeEss, Tube, Enh / PUDU, and Reverb.
2. Click and hold on the stage tile you want to move.
3. Drag the tile left or right to its new position in the chain.
4. Release to drop the tile. The chain updates immediately and the new order is persisted in `ClientCompTxChainStages`.
5. Repeat for any other stages you want to reorder.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| TX | Toggle button | Selects the TX chain view. Default: checked (amber). Reordering is only available in this mode. |
| RX | Toggle button | Selects the RX chain view. Default: unchecked. Drag-to-reorder is not available in this mode. |
| BYPASS | Toggle button | Default: unchecked. When checked, disables every stage at once. Uncheck to restore the stages that were active before. Does not affect stage order. |
| Chain stage (Eq) | Drag handle | Single-click toggles bypass for EQ. Double-click opens the EQ editor. Drag to reorder. |
| Chain stage (Comp) | Drag handle | Single-click toggles bypass for the compressor. Double-click opens the compressor editor. Drag to reorder. |
| Chain stage (Gate) | Drag handle | Single-click toggles bypass for the gate. Double-click opens the gate editor. Drag to reorder. |
| Chain stage (DeEss) | Drag handle | Single-click toggles bypass for the de-esser. Double-click opens the de-ess editor. Drag to reorder. |
| Chain stage (Tube) | Drag handle | Single-click toggles bypass for the tube saturator. Double-click opens the tube editor. Drag to reorder. |
| Chain stage (Enh / PUDU) | Drag handle | Single-click toggles bypass for the PUDU exciter. Double-click opens the PUDU editor. Drag to reorder. |
| Chain stage (Reverb) | Drag handle | Single-click toggles bypass for the reverb. Double-click opens the reverb editor. Drag to reorder. |

## Tips

- The hint text below the chain reads "Click to bypass · Double click to edit · Drag to reorder" and is only shown in TX mode.
- A single click on a stage tile bypasses that stage, not the whole chain. Use BYPASS to disable everything at once.

## Troubleshooting

- **Dragging a tile has no effect** — Confirm TX is selected. The RX view does not support reordering in the current release.
- **PUDU tray button is not visible** — Open the applet panel via `View > Applet Panel`, then locate the PUDU tray button in the right sidebar.

## Related

- [PooDoo Audio Chain overview](overview.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Open a stage's floating editor from the chain](open-a-stage-s-floating-editor-from-the-chain.md)
- [Re-enable a specific stage after a global bypass](re-enable-a-specific-stage-after-a-global-bypass.md)
