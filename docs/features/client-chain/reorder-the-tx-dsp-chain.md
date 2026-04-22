# Reorder the TX DSP chain

Drag the stage tiles in the PooDoo Audio Chain applet to change the order in which EQ, Compressor, Gate, De-Esser, Tube, PUDU, and Reverb process your transmit audio. The new order is saved in `ClientCompTxChainStages` and takes effect immediately.

## Before you start

- The PooDoo Audio (TXDSP) container must be visible. If it is not, click the tray button labelled **PUDU** in the right sidebar to show it.
- The TX chain must be selected. Confirm that the **TX** button at the top of the applet is active (amber highlight). If **RX** is selected instead, click **TX**.

## Steps

1. Locate the horizontal strip of stage tiles inside the PooDoo Audio Chain applet. The tiles are labelled **Eq**, **Comp**, **Gate**, **DeEss**, **Tube**, **Enh**, and **Reverb**.
2. Click and hold the tile you want to move.
3. Drag it left or right to the position you want in the chain.
4. Release the mouse button. The tile drops into the new position and the chain order updates immediately.
5. Repeat for any other stages you want to reorder.

## What each control does

| Control | Kind | Behavior | Persisted key |
|---|---|---|---|
| **TX** | Toggle button | Switches to TX chain view (the interactive, reorderable chain). Default: checked. | — |
| **RX** | Toggle button | Switches to the RX placeholder view. Reordering is not available in this mode. Default: unchecked. | — |
| **BYPASS** | Toggle button | Checked: disables every stage at once. Unchecked: restores the stages that were active before. Default: unchecked. | — |
| **Eq** stage tile | Drag handle | Single-click toggles bypass for EQ; double-click opens the EQ editor; drag reorders. | `ClientCompTxChainStages` |
| **Comp** stage tile | Drag handle | Single-click toggles bypass for the compressor; double-click opens the compressor editor; drag reorders. | `ClientCompTxChainStages` |
| **Gate** stage tile | Drag handle | Single-click toggles bypass for the gate; double-click opens the gate editor; drag reorders. | `ClientCompTxChainStages` |
| **DeEss** stage tile | Drag handle | Single-click toggles bypass for the de-esser; double-click opens the de-ess editor; drag reorders. | `ClientCompTxChainStages` |
| **Tube** stage tile | Drag handle | Single-click toggles bypass for the tube saturator; double-click opens the tube editor; drag reorders. | `ClientCompTxChainStages` |
| **Enh** stage tile | Drag handle | Single-click toggles bypass for the PUDU exciter; double-click opens the PUDU editor; drag reorders. | `ClientCompTxChainStages` |
| **Reverb** stage tile | Drag handle | Single-click toggles bypass for the reverb; double-click opens the reverb editor; drag reorders. | `ClientCompTxChainStages` |

## Tips

- A hint below the chain strip reads "Click to bypass · Double click to edit · Drag to reorder" — this is only shown when TX mode is active.
- A single click on a tile toggles that stage's bypass state. Take care not to single-click when you intend to drag; the bypass state changes on release of a plain click.
- To audition the chain without any processing, click **BYPASS** rather than bypassing stages one by one. **BYPASS** snapshots the active stages and restores them when you uncheck it.

## Troubleshooting

- **The stage tiles do not respond to dragging** — confirm the **TX** button is selected (amber). The **RX** view is a placeholder and does not support reordering.
- **PUDU tray button is not visible** — open `View > Applet Panel` to ensure the right sidebar is shown, then look for the **PUDU** tray button.

## Related

- [PooDoo Audio Chain overview](overview.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Open a stage's floating editor from the chain](open-a-stage-s-floating-editor-from-the-chain.md)
- [Re-enable a specific stage after a global bypass](re-enable-a-specific-stage-after-a-global-bypass.md)
