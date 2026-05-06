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

| Control                                           | Kind                                                                                                                                   | Default                                                                                                                                                                                                                                                             |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TX                                                | Toggle button                                                                                                                          | Checked                                                                                                                                                                                                                                                             |
| RX                                                | Toggle button                                                                                                                          | Unchecked                                                                                                                                                                                                                                                           |
| BYPASS                                            | Toggle button                                                                                                                          | Unchecked                                                                                                                                                                                                                                                           |
| RX chain stage (EQ / AGC-T / AGC-C / TUBE / PUDU) | Single-click toggles bypass for the RX stage; double-click opens its frameless floating editor in RX mode; drag reorders the RX chain. | Delegated to ClientRxChainWidget. All five RX stages (EQ, AGC-T/Gate, AGC-C/Comp, Tube, PUDU) are fully implemented. Order is independent of the TX chain. Distinct mime type `application/x-aethersdr-rx-chain-stage` prevents stray drops between the two strips. |

Stage order and individual stage state are persisted via `ClientCompTxChainStages`. The applet container visibility is persisted via `Applet_TXDSP`.

## Tips

- TX and RX keep completely separate BYPASS snapshots. Engaging BYPASS on the TX chain has no effect on the RX chain, and vice versa.
- If you manually toggle a stage while BYPASS is active, that manual change is preserved outside the snapshot and will not be reversed when you lift BYPASS.
- The BYPASS checked state shown in the header tracks whichever chain is currently visible. If you switch to RX and back to TX, the TX BYPASS state is restored exactly as you left it.
- In v0.9.7, TX bypass is owned by the audio engine rather than the applet snapshot. This means the BYPASS button in the Aetherial Audio Chain applet and the BYPASS button in the Aetherial Audio Channel Strip both reflect and control the same state. Clicking BYPASS in either location produces the same result.
- Double-clicking any TX chain stage tile now opens the Aetherial Audio Channel Strip — the unified TX DSP editor window — rather than a per-stage floating editor. Individual stage editors remain accessible from within the channel strip.

## Troubleshooting

- **BYPASS appears unchecked after switching from RX to TX** — This is expected. TX and RX track separate states. For the TX side, the displayed state now mirrors the engine's `isTxBypassed` value directly. Check whether you engaged BYPASS while the RX chain was selected rather than the TX chain.
- **Clicking BYPASS re-enables fewer stages than expected** — Any stage you toggled off manually before clicking BYPASS was already disabled and was not part of the snapshot, so it will not be restored.
- **BYPASS state in the applet does not match the channel strip** — Ensure you are running v0.9.7 or later. Earlier versions tracked TX bypass state only in the applet snapshot; v0.9.7 synchronises both controls through the audio engine.

## Related

- [Bypass every RX stage at once](bypass-every-rx-stage-at-once.md)
- [Re-enable a specific stage after a global bypass](re-enable-a-specific-stage-after-a-global-bypass.md)
- [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)
- [Aetherial Audio Chain overview](overview.md)