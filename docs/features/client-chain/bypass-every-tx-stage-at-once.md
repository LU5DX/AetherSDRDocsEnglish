# Bypass every TX stage at once

Use the BYPASS button to silence the entire TX DSP chain in one click — for example, to compare your processed and unprocessed transmit audio, or to rule out a processing stage when troubleshooting.

## Before you start

- The Aetherial Audio Chain applet must be visible. If it is not, click the PUDU tray button in the right sidebar to show it.
- Click TX in the applet header to make sure the TX chain is the active side. BYPASS acts only on the currently-shown chain.

## Steps

1. Open the Aetherial Audio Chain applet by clicking the PUDU tray button in the right sidebar.
2. Click TX in the applet header to select the TX chain. The button turns amber when active.
3. Click BYPASS. The button highlights to show it is checked, and every enabled TX stage is disabled at once.
4. To restore the stages, click BYPASS again. Only the stages that were enabled before you engaged BYPASS are re-enabled.

## What each control does

| Control | Kind | Default | Persisted setting | Behavior |
|---|---|---|---|---|
| TX | Toggle button | Checked | `PooDooAudioActiveTab` | Selects the TX chain for display and editing. BYPASS acts on this chain when TX is active. |
| RX | Toggle button | Unchecked | `PooDooAudioActiveTab` | Selects the RX chain. TX and RX maintain independent BYPASS snapshots; switching sides reflects the BYPASS state of that side. |
| BYPASS | Toggle button | Unchecked | — | Checked: snapshots all currently-enabled stages on the active side and disables them all. Unchecked: re-enables only the stages that were on before. |

Stage order and individual stage state are persisted via `ClientCompTxChainStages`. The applet container visibility is persisted via `Applet_TXDSP`.

## Tips

- TX and RX keep completely separate BYPASS snapshots. Engaging BYPASS on the TX chain has no effect on the RX chain, and vice versa.
- If you manually toggle a stage while BYPASS is active, that manual change is preserved outside the snapshot and will not be reversed when you lift BYPASS.
- The BYPASS checked state shown in the header tracks whichever chain is currently visible. If you switch to RX and back to TX, the TX BYPASS state is restored exactly as you left it.

## Troubleshooting

- **BYPASS appears unchecked after switching from RX to TX** — This is expected. TX and RX track separate checked states. Check whether you engaged BYPASS while the RX chain was selected rather than the TX chain.
- **Clicking BYPASS re-enables fewer stages than expected** — Any stage you toggled off manually before clicking BYPASS was already disabled and was not part of the snapshot, so it will not be restored.

## Related

- [Bypass every RX stage at once](bypass-every-rx-stage-at-once.md)
- [Re-enable a specific stage after a global bypass](re-enable-a-specific-stage-after-a-global-bypass.md)
- [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)
- [Aetherial Audio Chain overview](overview.md)
