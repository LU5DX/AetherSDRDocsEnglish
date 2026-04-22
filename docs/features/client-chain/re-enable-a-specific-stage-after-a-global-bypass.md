# Re-enable a specific stage after a global bypass

After using BYPASS to silence every TX DSP stage at once, you may want to bring back one stage — for example, the compressor — without restoring all the others. Clicking that stage directly overrides the snapshot that BYPASS holds, so the stage turns on independently of the global state.

## Before you start

- The PooDoo Audio (TXDSP) container must be visible. If it is not, click the PUDU tray button in the right sidebar to show it.
- TX must be selected (not RX). Click TX in the header row if needed.
- BYPASS must already be checked (active). If it is not, see [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md).

## Steps

1. Locate the chain strip showing the stage tiles: Eq, Comp, Gate, DeEss, Tube, Enh / PUDU, Reverb.
2. Click the tile for the stage you want to re-enable — for example, click the Comp tile once.
3. The stage toggles on independently. It is now active even though BYPASS remains checked.
4. Repeat step 2 for any other individual stages you want to restore.

## What each control does

| Control | Kind | Default | Behavior | Setting key |
|---|---|---|---|---|
| BYPASS | Toggle button | Unchecked | Checked: snapshots currently-enabled stages and disables all of them. Unchecked: restores exactly the stages that were on before. | — |
| Chain stage (Eq) | Drag handle / toggle | — | Single click toggles bypass for the EQ stage. | `ClientCompTxChainStages` |
| Chain stage (Comp) | Drag handle / toggle | — | Single click toggles bypass for the compressor. | `ClientCompTxChainStages` |
| Chain stage (Gate) | Drag handle / toggle | — | Single click toggles bypass for the gate. | `ClientCompTxChainStages` |
| Chain stage (DeEss) | Drag handle / toggle | — | Single click toggles bypass for the de-esser. | `ClientCompTxChainStages` |
| Chain stage (Tube) | Drag handle / toggle | — | Single click toggles bypass for the tube saturator. | `ClientCompTxChainStages` |
| Chain stage (Enh / PUDU) | Drag handle / toggle | — | Single click toggles bypass for the PUDU exciter. | `ClientCompTxChainStages` |
| Chain stage (Reverb) | Drag handle / toggle | — | Single click toggles bypass for the reverb. | `ClientCompTxChainStages` |

## Tips

- Stages toggled manually while BYPASS is active are preserved outside the snapshot. When you later uncheck BYPASS, the snapshot restores only the stages that were enabled before you activated BYPASS — it does not undo the individual clicks you made during bypass.
- To restore all stages at once, uncheck BYPASS instead of clicking stages one by one.

## Related

- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [PooDoo Audio Chain overview](overview.md)
- [Open a stage's floating editor from the chain](open-a-stage-s-floating-editor-from-the-chain.md)
