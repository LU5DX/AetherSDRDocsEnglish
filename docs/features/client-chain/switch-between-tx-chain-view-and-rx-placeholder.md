# Switch between TX chain view and RX placeholder

The PooDoo Audio Chain applet shows either the active TX DSP chain or an RX placeholder view. Use the TX and RX toggle buttons to switch between them. The TX view is the fully interactive mode; the RX view currently shows a placeholder message.

## Before you start

- The PooDoo Audio (TXDSP) container must be visible. If it is not, click the PUDU tray button in the right sidebar to enable it.

## Steps

1. Locate the header row at the top of the PooDoo Audio Chain applet. It contains the TX, RX, and BYPASS buttons.
2. Click TX to show the TX DSP chain. The button turns amber and the chain strip with its stage controls becomes visible. The interaction hint "Click to bypass · Double click to edit · Drag to reorder" appears below the chain.
3. Click RX to switch to the RX view. The chain strip and hint are hidden and replaced by the placeholder text "Client RX chain — coming in a future phase".
4. Click TX to return to the interactive TX chain at any time.

## What each control does

| Control | Kind | Default | Behavior |
|---|---|---|---|
| TX | Toggle button | Checked | Shows the TX DSP chain. Turns amber when selected. Exclusive with RX. |
| RX | Toggle button | Unchecked | Shows the RX placeholder "Client RX chain — coming in a future phase". Exclusive with TX. BYPASS is a no-op in this mode. |
| BYPASS | Toggle button | Unchecked | In TX mode: snapshots and disables all active stages; click again to restore them. In RX mode: no effect. |

The order of stages in the TX chain is persisted under `ClientCompTxChainStages`. The visibility of the TXDSP container is persisted under `Applet_TXDSP`.

## Tips

- TX is selected by default each time the applet is shown. You do not need to set it manually after opening the container.
- The hint text "Click to bypass · Double click to edit · Drag to reorder" is only visible in TX mode. It disappears automatically when you switch to RX.
- BYPASS has no effect on the RX view. If BYPASS is checked when you switch to RX, it remains checked but does nothing until you return to TX mode.

## Related

- [PooDoo Audio Chain overview](overview.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Reorder the TX DSP chain](reorder-the-tx-dsp-chain.md)
- [Open a stage's floating editor from the chain](open-a-stage-s-floating-editor-from-the-chain.md)
