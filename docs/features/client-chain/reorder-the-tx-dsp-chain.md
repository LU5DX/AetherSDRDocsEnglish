# Reorder the TX DSP chain

Drag TX DSP stages into a different order to change the sequence in which your audio is processed before transmission. The new order is saved automatically and persists across restarts.

## Before you start

- The Aetherial Audio (TXDSP) container must be visible. If it is not, click the tray button labelled **PUDU** in the right sidebar to show it.
- The TX chain must be the active side. If the **RX** button is currently selected, click **TX** first.

## Steps

1. Open the Aetherial Audio container by clicking the **PUDU** tray button if it is not already visible.
2. Click **TX** in the header row to ensure the TX chain is shown.
3. Locate the stage you want to move. The TX chain contains these stages: **EQ**, **COMP**, **GATE**, **DESS**, **TUBE**, **PUDU**, **VERB**.
4. Click and hold on the stage tile you want to move, then drag it left or right along the chain strip.
5. A vertical cyan bar appears between tiles as you drag, showing where the stage will land.
6. Release the mouse button to drop the stage into the new position.
7. Repeat for any other stages you want to reorder.

The new chain order is saved automatically to `ClientCompTxChainStages`.

## What each control does

| Control | Kind | Behavior | Default | Setting key |
|---|---|---|---|---|
| **TX** | Toggle button | Shows and enables editing of the TX DSP chain. Must be selected to drag TX stages. | Checked | `PooDooAudioActiveTab` |
| **RX** | Toggle button | Switches the strip to the RX chain. Drag operations on the RX strip do not affect TX order. | Unchecked | `PooDooAudioActiveTab` |
| TX chain stage (**EQ / COMP / GATE / DESS / TUBE / PUDU / VERB**) | Drag handle | Single-click toggles bypass for that stage. Double-click opens its frameless floating editor. Drag left or right to reorder. | — | — |
| **BYPASS** | Toggle button | Disables every stage on the currently shown chain side at once. Does not affect stage order. | Unchecked | — |

## Tips

- The hint text below the chain reads "Click to bypass · Double click to edit · Drag to reorder" as a quick reminder of all three interactions.
- TX and RX chain orders are fully independent. Reordering the TX chain has no effect on `ClientCompRxChainStages`.
- A single-click on a stage tile toggles its bypass state, not a reorder. Make sure you are dragging, not clicking, when you intend to move a stage.
- If **BYPASS** is currently checked when you reorder, the stage positions still update. The bypass snapshot is based on which stages were enabled, not their position.

## Troubleshooting

- **Drag does nothing or the drop is rejected** — Confirm **TX** is the selected mode button (amber highlight). Dragging is only active on the currently shown chain strip; if **RX** is selected, drops to the TX strip are not accepted.
- **New order is lost after restart** — This should not happen if the drop completed successfully (cyan drop indicator appeared and you released over the strip). If it recurs, check that AetherSDR has write access to its settings storage.

## Related

- [Aetherial Audio Chain overview](overview.md)
- [Reorder the RX DSP chain (independent of TX order)](reorder-the-rx-dsp-chain-independent-of-tx-order.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Open a stage's frameless floating editor from the chain](open-a-stage-s-frameless-floating-editor-from-the-chain.md)
- [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)
