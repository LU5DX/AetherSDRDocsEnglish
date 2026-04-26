# Reorder the TX DSP chain

Drag stages in the TX DSP chain to change the order in which your audio is processed before transmission. The new order is saved automatically and persists across sessions.

## Before you start

- The Aetherial Audio container must be visible. If it is not, click the tray button labelled **PUDU** in the applet panel to show it.
- The TX chain must be the active view. If the **RX** button is currently selected, click **TX** to switch.

## Steps

1. Open the Aetherial Audio container by clicking the **PUDU** tray button in the applet panel, if it is not already visible.
2. In the header row, click **TX** if it is not already selected. The TX chain strip becomes active.
3. Locate the stage you want to move. The TX chain contains up to seven stages: EQ, COMP, GATE, DESS, TUBE, PUDU, and VERB.
4. Click and hold on the stage tile you want to reorder.
5. Drag the tile left or right along the chain strip. A vertical cyan bar appears between tiles to show where the stage will land when you release.
6. Release the mouse button to drop the stage into the new position.
7. Repeat for any other stages you want to reorder.

The updated order is saved immediately to `ClientCompTxChainStages`.

## What each control does

| Control | Kind | Default | Behavior | Setting key |
|---|---|---|---|---|
| **TX** | Toggle button | Checked | Shows and enables editing of the TX DSP chain. Part of an exclusive pair with **RX**. | `PooDooAudioActiveTab` |
| **RX** | Toggle button | Unchecked | Switches the view to the RX chain. TX chain reordering is not available while RX is active. | `PooDooAudioActiveTab` |
| TX chain stage (EQ / COMP / GATE / DESS / TUBE / PUDU / VERB) | Drag handle | — | Single-click toggles bypass for the stage. Double-click opens its frameless floating editor. Drag reorders the TX chain. | — |
| **BYPASS** | Toggle button | Unchecked | Checked: snapshots the currently-enabled stages and disables all of them. Unchecked: re-enables only the stages that were on before. Does not affect stage order. | — |

## Tips

- A static hint below the chain strip reads "Click to bypass · Double click to edit · Drag to reorder" as a quick reminder of all three interactions.
- The cyan drop indicator shows the landing position before you release, so you can adjust your drop target without committing.
- The TX and RX chains have independent order. Reordering the TX chain does not affect the RX chain, and vice versa.
- If you want to compare your audio with and without the current chain order, use **BYPASS** to disable all stages temporarily without losing the order you have set.

## Related

- [Aetherial Audio Chain overview](overview.md)
- [Reorder the RX DSP chain (independent of TX order)](reorder-the-rx-dsp-chain-independent-of-tx-order.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Open a stage's frameless floating editor from the chain](open-a-stage-s-frameless-floating-editor-from-the-chain.md)
- [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)
