# Open a Stage's Frameless Floating Editor from the Chain

Double-clicking a stage tile in the Aetherial Audio Chain opens that stage's frameless floating editor, giving you direct access to its parameters without leaving the main window layout.

## Before you start

- The Aetherial Audio (TXDSP) container must be visible. If it is not, click the **PUDU** tray button in the right sidebar to show it.
- Decide whether you want to edit a TX stage or an RX stage, and make sure the correct chain is active.

## Steps

1. If the chain is not already showing the side you want, click **TX** or **RX** in the header row of the Aetherial Audio Chain to switch to that chain.
2. Locate the stage tile you want to edit. TX chain tiles are labelled **EQ**, **COMP**, **GATE**, **DESS**, **TUBE**, **PUDU**, and **VERB**. RX chain tiles are labelled **EQ**, **GATE**, **COMP**, **TUBE**, and **PUDU**.
3. Double-click the stage tile. The frameless floating editor for that stage opens.

A single click bypasses the stage instead of opening the editor. Make sure to double-click.

## What each control does

| Control | Kind | Behavior | Persisted setting |
|---|---|---|---|
| **TX** | Toggle button | Shows the TX DSP chain. Amber when selected. | `PooDooAudioActiveTab` (`TX`) |
| **RX** | Toggle button | Shows the RX DSP chain. Amber when selected. | `PooDooAudioActiveTab` (`RX`) |
| TX chain stage (**EQ** / **COMP** / **GATE** / **DESS** / **TUBE** / **PUDU** / **VERB**) | Stage tile | Single-click toggles bypass. Double-click opens the frameless floating editor. Drag reorders the chain. | `ClientCompTxChainStages` |
| RX chain stage (**EQ** / **GATE** / **COMP** / **TUBE** / **PUDU**) | Stage tile | Single-click toggles bypass. Double-click opens the frameless floating editor in RX mode. Drag reorders the chain. | `ClientCompRxChainStages` |

## Tips

- The hint line below the chain reads "Click to bypass · Double click to edit · Drag to reorder" and serves as a quick reminder of these interactions.
- The TX and RX chains are independent. Opening an editor on the TX side does not affect the RX chain, and vice versa.
- The last-active tab (**TX** or **RX**) is restored when you reopen the applet, so you will land on the same chain you were editing previously.

## Troubleshooting

- **Single-click opened the wrong action (bypass toggled instead of editor opening)** — You clicked once instead of twice. Click the stage tile a second time, or single-click again to restore the bypass state, then double-click to open the editor.
- **The TXDSP container is not visible so the chain cannot be reached** — Click the **PUDU** tray button in the right sidebar to toggle the Aetherial Audio container on.

## Related

- [Aetherial Audio Chain overview](overview.md)
- [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Bypass every RX stage at once](bypass-every-rx-stage-at-once.md)
- [Reorder the TX DSP chain](reorder-the-tx-dsp-chain.md)
- [Reorder the RX DSP chain (independent of TX order)](reorder-the-rx-dsp-chain-independent-of-tx-order.md)
