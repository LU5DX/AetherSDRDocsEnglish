# Open a Stage's Frameless Floating Editor from the Chain

Double-clicking a stage tile in the Aetherial Audio Chain opens that stage's frameless floating editor, giving you direct access to its parameters without leaving the main window layout.

**Note for v0.9.7:** Double-clicking a TX chain tile no longer opens that stage's editor directly. Instead, it opens the Aetherial Audio Channel Strip — the unified TX DSP window. From there you can access individual stage controls. Double-clicking an RX chain tile still opens that stage's frameless floating editor directly.

## Before you start

- The Aetherial Audio (TXDSP) container must be visible. If it is not, click the **PUDU** tray button in the right sidebar to show it.
- Decide whether you want to edit a TX stage or an RX stage, and make sure the correct chain is active.

## Steps

1. If the chain is not already showing the side you want, click **TX** or **RX** in the header row of the Aetherial Audio Chain to switch to that chain.
2. Locate the stage tile you want to edit. TX chain tiles are labelled **EQ**, **COMP**, **GATE**, **DESS**, **TUBE**, **PUDU**, and **VERB**. RX chain tiles are labelled **EQ**, **AGC-T**, **AGC-C**, **TUBE**, and **PUDU**.
3. Double-click the stage tile:
   - On the **TX** chain, double-clicking any stage tile opens the Aetherial Audio Channel Strip. Use the Channel Strip's own controls to reach the individual stage you want to edit.
   - On the **RX** chain, double-clicking a stage tile opens that stage's frameless floating editor directly.

A single click bypasses the stage instead of opening the editor. Make sure to double-click.

## What each control does

| Control                                                                                    | Kind          | Behavior                                                                                                                        |
|--------------------------------------------------------------------------------------------|---------------|---------------------------------------------------------------------------------------------------------------------------------|
| **TX**                                                                                     | Toggle button | Shows the TX DSP chain. Amber when selected.                                                                                    |
| **RX**                                                                                     | Toggle button | Shows the RX DSP chain. Amber when selected.                                                                                    |
| **BYPASS**                                                                                 | Toggle button | Checked: snapshots enabled stages on the active side and disables all of them. Unchecked: re-enables only the stages that were on before. TX and RX maintain separate snapshots. On the TX side, the checked state also mirrors the TX bypass state set from the Aetherial Audio Channel Strip. |
| TX chain stage (**EQ** / **COMP** / **GATE** / **DESS** / **TUBE** / **PUDU** / **VERB**) | Stage tile    | Single-click toggles bypass. Double-click opens the Aetherial Audio Channel Strip (the unified TX DSP window). Drag reorders the chain. |
| RX chain stage (**EQ** / **AGC-T** / **AGC-C** / **TUBE** / **PUDU**)                     | Stage tile    | Single-click toggles bypass. Double-click opens the stage's frameless floating editor in RX mode. Drag reorders the RX chain independently of the TX chain. |

## Tips

- The hint line below the chain reads "Click to bypass · Double click to edit · Drag to reorder" and serves as a quick reminder of these interactions.
- The TX and RX chains are independent. Opening an editor on the TX side does not affect the RX chain, and vice versa.
- The last-active tab (**TX** or **RX**) is restored when you reopen the applet, so you will land on the same chain you were editing previously.
- The **BYPASS** button on the TX side stays in sync with the BYPASS control in the Aetherial Audio Channel Strip. Toggling bypass from either location updates both.

## Troubleshooting

- **Single-click opened the wrong action (bypass toggled instead of editor opening)** — You clicked once instead of twice. Click the stage tile a second time, or single-click again to restore the bypass state, then double-click to open the editor.
- **Double-clicking a TX stage tile opened the Channel Strip instead of that stage's editor** — This is expected behaviour from v0.9.7 onwards. Double-click on the TX chain is now the canonical "edit my TX audio" gesture and always opens the Channel Strip. Use the Channel Strip's own controls to navigate to the specific stage.
- **The TXDSP container is not visible so the chain cannot be reached** — Click the **PUDU** tray button in the right sidebar to toggle the Aetherial Audio container on.

## Related

- [Aetherial Audio Chain overview](overview.md)
- [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Bypass every RX stage at once](bypass-every-rx-stage-at-once.md)
- [Reorder the TX DSP chain](reorder-the-tx-dsp-chain.md)
- [Reorder the RX DSP chain (independent of TX order)](reorder-the-rx-dsp-chain-independent-of-tx-order.md)