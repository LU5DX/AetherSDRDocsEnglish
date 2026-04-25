# Re-enable a specific stage after a global bypass

After using BYPASS to silence every TX DSP stage at once, you can re-enable individual stages without turning off the global bypass first. This is useful when you want to audition a single stage in isolation while keeping the rest of the chain silent.

## Before you start

- The PooDoo Audio (TXDSP) container must be visible. If it is not, click the PUDU tray button in the right sidebar to show it.
- TX must be selected in the chain applet header (not RX).
- BYPASS must already be active (the BYPASS toggle is checked).

## Steps

1. Locate the BYPASS toggle in the header row of the PooDoo Audio Chain. Confirm it is checked (amber border and fill).
2. Find the stage you want to re-enable in the chain strip — for example, Chain stage (Comp) or Chain stage (Eq).
3. Single-click that stage tile. The stage toggles from bypassed to active. Its visual state updates immediately.
4. Repeat step 3 for any other individual stages you want to re-enable.

Stages you re-enable manually while BYPASS is checked are preserved outside the bypass snapshot. If you later uncheck BYPASS, only the stages that were on before BYPASS was first activated are restored; the stages you toggled manually during bypass retain their current state.

## What each control does

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| BYPASS | Checked: snapshots currently-enabled stages and disables all of them. Unchecked: re-enables only the stages that were on before BYPASS was activated. | Unchecked | — |
| Chain stage (Eq) | Single-click toggles bypass for the EQ stage. | — | `ClientCompTxChainStages` |
| Chain stage (Comp) | Single-click toggles bypass for the compressor. | — | `ClientCompTxChainStages` |
| Chain stage (Gate) | Single-click toggles bypass for the gate. | — | `ClientCompTxChainStages` |
| Chain stage (DeEss) | Single-click toggles bypass for the de-esser. | — | `ClientCompTxChainStages` |
| Chain stage (Tube) | Single-click toggles bypass for the tube saturator. | — | `ClientCompTxChainStages` |
| Chain stage (Enh / PUDU) | Single-click toggles bypass for the PUDU exciter. | — | `ClientCompTxChainStages` |
| Chain stage (Reverb) | Single-click toggles bypass for the reverb. | — | `ClientCompTxChainStages` |

## Tips

- To return the entire chain to its pre-bypass state in one action, uncheck BYPASS. Only stages that were enabled before the bypass snapshot are restored; any stages you toggled individually while BYPASS was active are not affected by this restore.
- The interaction hint below the chain strip reads "Click to bypass · Double click to edit · Drag to reorder" — single-click is always the bypass toggle regardless of BYPASS state.
- BYPASS is a no-op in RX mode. Switch to TX before attempting to re-enable stages.

## Related

- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [PooDoo Audio Chain overview](overview.md)
- [Open a stage's floating editor from the chain](open-a-stage-s-floating-editor-from-the-chain.md)
