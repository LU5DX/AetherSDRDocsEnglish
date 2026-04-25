# Bypass every TX stage at once

The BYPASS button disables all active TX DSP stages in a single click and restores them just as quickly. Use it when you want to compare processed and unprocessed audio without manually toggling each stage.

## Before you start

- The PooDoo Audio (TXDSP) container must be visible. If it is not, click the PUDU tray button in the right sidebar to show it.
- Make sure TX is the active mode. The TX toggle button should be checked (amber). BYPASS has no effect in RX mode.

## Steps

1. Locate the header row of the PooDoo Audio Chain applet. You will see TX, RX, and BYPASS buttons.
2. Click BYPASS.
   - BYPASS becomes checked (amber border and fill).
   - Every stage that was enabled is disabled. The chain stages display their bypassed state.
3. To restore all stages, click BYPASS again.
   - BYPASS returns to unchecked.
   - Only the stages that were enabled before you clicked BYPASS are re-enabled. Stages you had already bypassed individually before activating BYPASS remain bypassed.

## What each control does

| Control | Default | Behavior | Persisted setting |
|---|---|---|---|
| TX | Checked | Shows and edits the TX DSP chain. BYPASS is active in this mode. | — |
| RX | Unchecked | Switches to the RX chain placeholder. BYPASS is a no-op in this mode. | — |
| BYPASS | Unchecked | Checked: snapshots currently-enabled stages and disables all of them. Unchecked: re-enables only the stages that were on before. | — |
| Chain stage (Eq) | — | Single-click toggles bypass for the EQ stage individually. | `ClientCompTxChainStages` |
| Chain stage (Comp) | — | Single-click toggles bypass for the compressor individually. | `ClientCompTxChainStages` |
| Chain stage (Gate) | — | Single-click toggles bypass for the gate individually. | `ClientCompTxChainStages` |
| Chain stage (DeEss) | — | Single-click toggles bypass for the de-esser individually. | `ClientCompTxChainStages` |
| Chain stage (Tube) | — | Single-click toggles bypass for the tube saturator individually. | `ClientCompTxChainStages` |
| Chain stage (Enh / PUDU) | — | Single-click toggles bypass for the PUDU exciter individually. | `ClientCompTxChainStages` |
| Chain stage (Reverb) | — | Single-click toggles bypass for the reverb individually. | `ClientCompTxChainStages` |

The TXDSP container visibility is persisted under `Applet_TXDSP`.

## Tips

- If you manually toggle a stage while BYPASS is checked, that stage's new state is preserved outside the snapshot. Unchecking BYPASS will not override a stage you changed during the bypass.
- BYPASS only works in TX mode. If RX is selected, clicking BYPASS has no effect on any DSP stage.

## Troubleshooting

- **BYPASS is checked but stages do not appear bypassed** — Confirm TX is the active mode, not RX. Click TX if needed, then click BYPASS again.
- **Stages are not restored after unchecking BYPASS** — Any stage that was already individually bypassed before you activated BYPASS will not be restored; BYPASS only restores stages that were enabled at the moment you checked it.

## Related

- [Re-enable a specific stage after a global bypass](re-enable-a-specific-stage-after-a-global-bypass.md)
- [PooDoo Audio Chain overview](overview.md)
- [Switch between TX chain view and RX placeholder](switch-between-tx-chain-view-and-rx-placeholder.md)
- [Open a stage's floating editor from the chain](open-a-stage-s-floating-editor-from-the-chain.md)
