# Re-enable a specific stage after a global bypass

After using BYPASS to silence every TX DSP stage at once, you may want to turn a single stage back on without releasing the global bypass. This page shows how to do that without disturbing the snapshot that BYPASS is holding.

## Before you start

- The PooDoo Audio (TXDSP) container must be visible. If it is not, click the PUDU tray button in the right sidebar to show it.
- TX must be the active mode in the applet. Confirm the TX toggle button is checked (amber). BYPASS has no effect in RX mode.
- BYPASS must already be checked. If it is not, this procedure does not apply — click a stage directly to toggle it instead.

## Steps

1. Locate the chain strip in the PooDoo Audio container. Stages are shown left to right: Eq, Comp, Gate, DeEss, Tube, Enh / PUDU, Reverb.
2. Find the stage you want to re-enable. Bypassed stages appear visually inactive.
3. Click that stage once. A single click toggles the bypass state for that stage alone, turning it back on while all other bypassed stages remain off.
4. Repeat for any other individual stages you want to restore.

## What each control does

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| BYPASS | Checked: snapshots currently-enabled stages and disables all of them. Unchecked: restores exactly the stages that were on before. | Unchecked | — |
| Chain stage (Eq) | Single click toggles bypass for the EQ stage. | — | `ClientCompTxChainStages` |
| Chain stage (Comp) | Single click toggles bypass for the compressor. | — | `ClientCompTxChainStages` |
| Chain stage (Gate) | Single click toggles bypass for the gate. | — | `ClientCompTxChainStages` |
| Chain stage (DeEss) | Single click toggles bypass for the de-esser. | — | `ClientCompTxChainStages` |
| Chain stage (Tube) | Single click toggles bypass for the tube saturator. | — | `ClientCompTxChainStages` |
| Chain stage (Enh / PUDU) | Single click toggles bypass for the PUDU exciter. | — | `ClientCompTxChainStages` |
| Chain stage (Reverb) | Single click toggles bypass for the reverb. | — | `ClientCompTxChainStages` |

## Tips

- Stages toggled manually while BYPASS is checked are tracked outside the snapshot. If you later uncheck BYPASS, only the stages that were on before you first checked BYPASS are restored — any stages you individually re-enabled during the bypass are not part of that snapshot.
- To restore all previously-enabled stages at once, simply uncheck BYPASS. This is faster than clicking each stage individually.
- The hint below the chain strip reads "Click to bypass · Double click to edit · Drag to reorder" and is visible whenever TX mode is active. Double-clicking a stage opens its editor rather than toggling it.

## Troubleshooting

- **Clicking a stage has no visible effect** — Confirm TX is the active mode. The RX chain view is a placeholder and BYPASS is a no-op there. Click TX to switch back.
- **Unchecking BYPASS does not restore the stage you manually re-enabled** — This is expected. Stages you toggle individually while BYPASS is checked are excluded from the snapshot that BYPASS tracks. Set the stage after you uncheck BYPASS.

## Related

- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Open a stage's floating editor from the chain](open-a-stage-s-floating-editor-from-the-chain.md)
- [Switch between TX chain view and RX placeholder](switch-between-tx-chain-view-and-rx-placeholder.md)
