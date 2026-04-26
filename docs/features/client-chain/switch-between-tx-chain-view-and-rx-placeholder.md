# Switch between TX chain view and RX placeholder

The PooDoo Audio Chain applet shows either the TX DSP processing stages or an RX chain view. Use TX to work with the live signal chain; switch to RX to see the placeholder for the upcoming RX processing feature.

## Before you start

- The PooDoo Audio (TXDSP) container must be visible. If it is not, click the PUDU tray button in the right sidebar to show it.

## Steps

1. Locate the header row at the top of the PooDoo Audio Chain applet. It contains two mode buttons: TX and RX.
2. Click TX to display the interactive TX DSP chain (EQ, Compressor, Gate, De-Ess, Tube, PUDU, Reverb stages). TX is selected by default and shown in amber when active.
3. Click RX to switch to the RX chain view. The TX stage strip is hidden and replaced with the text "Client RX chain — coming in a future phase". The BYPASS button has no effect in this mode.
4. Click TX again at any time to return to the editable TX chain.

AetherSDR saves your last-selected tab automatically. The next time you open the applet, it restores whichever mode was active when you closed it.

## What each control does

| Control | Kind | Default | Behavior | Setting key |
|---|---|---|---|---|
| TX | Toggle button | Checked | Shows and enables editing of the TX DSP chain. Displayed in amber when selected. | — |
| RX | Toggle button | Unchecked | Switches to the RX chain placeholder view. BYPASS is a no-op in this mode. | — |
| BYPASS | Toggle button | Unchecked | Checked: snapshots currently-enabled TX stages and disables all of them. Unchecked: restores only the stages that were enabled before. No effect when RX is active. | — |

The chain stage order and enabled state for the TX chain are persisted under `ClientCompTxChainStages`. The container visibility is persisted under `Applet_TXDSP`.

## Tips

- TX and RX are mutually exclusive. Clicking one automatically deselects the other; there is no way to have neither selected.
- The interaction hint "Click to bypass · Double click to edit · Drag to reorder" is shown only when TX is the active mode.

## Troubleshooting

- **The PUDU tray button is not visible** — open the applet panel via `View > Applet Panel`, then look for the PUDU tray button in the right sidebar.
- **Clicking BYPASS in RX mode has no effect** — this is expected. BYPASS only acts on TX chain stages and is a no-op when RX is selected.

## Related

- [PooDoo Audio Chain overview](overview.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Reorder the TX DSP chain](reorder-the-tx-dsp-chain.md)
- [Open a stage's floating editor from the chain](open-a-stage-s-floating-editor-from-the-chain.md)
