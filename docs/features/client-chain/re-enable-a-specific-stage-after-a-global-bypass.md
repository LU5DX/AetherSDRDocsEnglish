# Re-enable a specific stage after a global bypass

When BYPASS is active, every TX DSP stage is disabled at once. This page shows how to bring a single stage back on while leaving the rest bypassed.

## Before you start

- The PooDoo Audio (TXDSP) container must be visible. If it is not, click the PUDU tray button in the right sidebar to show it.
- TX must be selected (not RX). The TX toggle is checked by default; if RX is selected, click TX.
- BYPASS must already be checked (amber border, saturated colour). If it is not, see [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md).

## Steps

1. Locate the chain strip. The stage tiles — Eq, Comp, Gate, DeEss, Tube, Enh / PUDU, Reverb — are visible in the horizontal strip below the TX / RX / BYPASS header row.
2. Identify the stage you want to re-enable.
3. Click that stage tile once. A single click toggles the bypass state for that stage alone, turning it back on without affecting any other stage.

## What each control does

| Control | Kind | Default | Behavior | Setting key |
|---|---|---|---|---|
| BYPASS | Toggle button | Unchecked | Checked: snapshots all currently-enabled stages and disables them all. Unchecked: restores exactly the stages that were on before. | — |
| Chain stage (Eq) | Drag handle | — | Single click toggles bypass for the EQ stage. Double-click opens its editor. Drag reorders. | `ClientCompTxChainStages` |
| Chain stage (Comp) | Drag handle | — | Single click toggles bypass for the compressor. Double-click opens its editor. Drag reorders. | `ClientCompTxChainStages` |
| Chain stage (Gate) | Drag handle | — | Single click toggles bypass for the gate. Double-click opens its editor. Drag reorders. | `ClientCompTxChainStages` |
| Chain stage (DeEss) | Drag handle | — | Single click toggles bypass for the de-esser. Double-click opens its editor. Drag reorders. | `ClientCompTxChainStages` |
| Chain stage (Tube) | Drag handle | — | Single click toggles bypass for the tube saturator. Double-click opens its editor. Drag reorders. | `ClientCompTxChainStages` |
| Chain stage (Enh / PUDU) | Drag handle | — | Single click toggles bypass for the PUDU exciter. Double-click opens its editor. Drag reorders. | `ClientCompTxChainStages` |
| Chain stage (Reverb) | Drag handle | — | Single click toggles bypass for the reverb. Double-click opens its editor. Drag reorders. | `ClientCompTxChainStages` |

## Tips

- Clicking a stage tile while BYPASS is checked re-enables that stage independently. The BYPASS snapshot does not absorb this change: if you later uncheck BYPASS, only the stages that were enabled before BYPASS was first activated are restored. Stages you toggled manually while BYPASS was active are preserved outside that snapshot.
- The hint below the chain strip reads "Click to bypass · Double click to edit · Drag to reorder" and is visible only in TX mode.

## Related

- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Open a stage's floating editor from the chain](open-a-stage-s-floating-editor-from-the-chain.md)
- [Reorder the TX DSP chain](reorder-the-tx-dsp-chain.md)
- [PooDoo Audio Chain overview](overview.md)
