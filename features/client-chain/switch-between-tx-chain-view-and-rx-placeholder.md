# Switch between TX chain view and RX placeholder

The PooDoo Audio Chain applet shows either the interactive TX DSP chain or an RX placeholder panel. Use the TX and RX toggle buttons to switch between them.

## Before you start

- The PooDoo Audio (TXDSP) container must be visible. If it is not, click the PUDU tray button in the right sidebar to enable it.

## Steps

1. Locate the header row at the top of the PooDoo Audio Chain applet. It contains two mode buttons: TX and RX.
2. Click TX to show the TX DSP chain — the full interactive strip of stages (EQ, Compressor, Gate, De-Ess, Tube, PUDU, Reverb) with the hint text "Click to bypass · Double click to edit · Drag to reorder" below it. TX is selected by default.
3. Click RX to switch to the RX placeholder. The chain strip and hint text are hidden and replaced by the message "Client RX chain — coming in a future phase".
4. Click TX again at any time to return to the interactive chain view.

## What each control does

| Control | Kind | Default | Behavior |
|---|---|---|---|
| TX | Toggle button | Checked | Shows the interactive TX DSP chain. Displays amber when selected. |
| RX | Toggle button | Unchecked | Shows the RX placeholder message. BYPASS is a no-op in this mode. |
| BYPASS | Toggle button | Unchecked | Checked: snapshots currently-enabled stages and disables all of them. Unchecked: re-enables only the stages that were on before. Has no effect while RX is selected. |

TX and RX are mutually exclusive; selecting one deselects the other.

The chain stage order and enabled state are persisted under `ClientCompTxChainStages`. The container visibility is persisted under `Applet_TXDSP`.

## Tips

- The BYPASS button remains visible in RX mode but is a no-op. Any click in RX mode has no effect on the DSP engine.
- The interaction hint "Click to bypass · Double click to edit · Drag to reorder" is hidden automatically when RX is selected, because the RX chain is not yet interactive.

## Related

- [PooDoo Audio Chain overview](overview.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Reorder the TX DSP chain](reorder-the-tx-dsp-chain.md)
- [Open a stage's floating editor from the chain](open-a-stage-s-floating-editor-from-the-chain.md)
