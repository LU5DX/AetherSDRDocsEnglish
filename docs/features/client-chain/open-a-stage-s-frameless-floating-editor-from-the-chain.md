# Open a stage's frameless floating editor from the chain

Double-clicking a stage tile in the Aetherial Audio Chain opens that stage's frameless floating editor, giving you direct access to its parameters without leaving the chain view.

## Before you start

- The Aetherial Audio (TXDSP) container must be visible. If it is not, click the `PUDU` tray button in the right sidebar to toggle it on.
- Decide whether you want to edit a TX stage or an RX stage, and make sure the correct chain is shown.

## Steps

1. If the chain is showing the wrong side, click `TX` or `RX` at the top of the Aetherial Audio Chain to switch to the chain that contains the stage you want to edit.
2. Locate the stage tile you want to edit. TX chain tiles are labeled `EQ`, `COMP`, `GATE`, `DESS`, `TUBE`, `PUDU`, and `VERB`. RX chain tiles are labeled `EQ`, `GATE`, `COMP`, `TUBE`, and `PUDU`.
3. Double-click the stage tile. The frameless floating editor for that stage opens.

The hint text below the chain reads "Click to bypass · Double click to edit · Drag to reorder" as a quick reminder of the available interactions.

## What each control does

| Control | Kind | Behavior | Persisted setting |
|---|---|---|---|
| `TX` | Toggle button | Shows the TX DSP chain. Amber when selected. | `PooDooAudioActiveTab` |
| `RX` | Toggle button | Shows the RX DSP chain. Amber when selected. | `PooDooAudioActiveTab` |
| TX chain stage (`EQ` / `COMP` / `GATE` / `DESS` / `TUBE` / `PUDU` / `VERB`) | Drag handle | Single-click toggles bypass; double-click opens the frameless editor; drag reorders. | `ClientCompTxChainStages` |
| RX chain stage (`EQ` / `GATE` / `COMP` / `TUBE` / `PUDU`) | Drag handle | Single-click toggles bypass; double-click opens the frameless editor in RX mode; drag reorders. | `ClientCompRxChainStages` |

## Tips

- A single click on a stage tile toggles its bypass state, not its editor. Make sure to double-click to open the editor.
- The TX and RX chains are independent. Editing a stage on one side does not affect the corresponding stage on the other side.
- The last-active tab (`TX` or `RX`) is restored automatically when you reopen the container, persisted via `PooDooAudioActiveTab`.

## Related

- [Aetherial Audio Chain overview](overview.md)
- [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)
- [Reorder the TX DSP chain](reorder-the-tx-dsp-chain.md)
- [Reorder the RX DSP chain (independent of TX order)](reorder-the-rx-dsp-chain-independent-of-tx-order.md)
