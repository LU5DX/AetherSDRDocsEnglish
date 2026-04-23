# Switch between TX chain view and RX placeholder

The PooDoo Audio Chain applet shows either the interactive TX DSP stage strip or an RX placeholder panel. Use the TX and RX toggle buttons to switch between them.

## Before you start

- The PooDoo Audio (TXDSP) container must be visible. If it is not, click the PUDU tray button in the right sidebar to enable it.

## Steps

1. Locate the header row at the top of the PooDoo Audio Chain applet. It contains the TX and RX buttons on the left side.
2. Click TX to show the interactive TX DSP chain strip. TX is selected by default and renders amber when active.
3. Click RX to switch to the RX placeholder panel. The panel displays the text "Client RX chain — coming in a future phase". The stage strip, the interaction hint, and BYPASS become inactive in this mode.
4. Click TX to return to the editable chain at any time.

## What each control does

| Control | Default | Behavior |
|---------|---------|----------|
| TX | Checked | Shows the TX DSP chain strip with all interactive stages. Highlighted amber when selected. |
| RX | Unchecked | Replaces the chain strip with a placeholder. BYPASS is a no-op in this mode. The interaction hint is hidden. |
| BYPASS | Unchecked | Disables every enabled TX stage at once; click again to restore them. Has no effect while RX is selected. |

TX and RX are mutually exclusive; only one can be selected at a time. The stage order and enabled state are persisted under `ClientCompTxChainStages`. The container visibility is persisted under `Applet_TXDSP`.

## Tips

- The interaction hint "Click to bypass · Double click to edit · Drag to reorder" appears only when TX is selected, because the RX chain is not yet interactive.
- Switching to RX does not affect the TX chain state. Stages remain in whatever enabled or bypassed state you left them.

## Troubleshooting

- **PUDU tray button is not visible** — Open `View > Applet Panel` to ensure the applet panel is shown, then locate the PUDU tray button in the right sidebar.
- **BYPASS appears to do nothing after clicking RX** — This is expected. BYPASS is a no-op in RX mode and will have no effect until the RX chain is implemented in a future release.

## Related

- [PooDoo Audio Chain overview](overview.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Re-enable a specific stage after a global bypass](re-enable-a-specific-stage-after-a-global-bypass.md)
- [Reorder the TX DSP chain](reorder-the-tx-dsp-chain.md)
