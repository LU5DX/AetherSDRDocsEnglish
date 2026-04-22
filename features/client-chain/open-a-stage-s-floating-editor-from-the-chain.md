# Open a Stage's Floating Editor from the Chain

Double-clicking a stage in the PooDoo Audio Chain opens that stage's floating editor, letting you adjust its parameters without leaving the chain view.

## Before you start

- The PooDoo Audio (TXDSP) container must be visible. If it is not, click the PUDU tray button in the right sidebar to show it.
- The chain must be in TX mode. Click TX in the header row if RX is currently selected.

## Steps

1. Locate the PooDoo Audio Chain strip at the top of the TXDSP container.
2. Find the stage you want to edit: Eq, Comp, Gate, DeEss, Tube, Enh / PUDU, or Reverb.
3. Double-click that stage tile.

The stage's floating editor opens immediately. Single-clicking the same tile would toggle its bypass state instead, so be sure to double-click.

## What each control does

| Stage tile | Single-click | Double-click | Drag |
|---|---|---|---|
| Chain stage (Eq) | Toggle EQ bypass | Open EQ editor | Reorder chain |
| Chain stage (Comp) | Toggle compressor bypass | Open compressor editor | Reorder chain |
| Chain stage (Gate) | Toggle gate bypass | Open gate editor | Reorder chain |
| Chain stage (DeEss) | Toggle de-esser bypass | Open de-ess editor | Reorder chain |
| Chain stage (Tube) | Toggle tube saturator bypass | Open tube editor | Reorder chain |
| Chain stage (Enh / PUDU) | Toggle PUDU exciter bypass | Open PUDU editor | Reorder chain |
| Chain stage (Reverb) | Toggle reverb bypass | Open reverb editor | Reorder chain |

The hint text below the chain strip reads "Click to bypass · Double click to edit · Drag to reorder" and is visible whenever TX mode is active.

The chain stage order and enabled states are persisted in `ClientCompTxChainStages`. The container's visibility is persisted in `Applet_TXDSP`.

## Tips

- If the stage is bypassed, its editor still opens on double-click. You can adjust parameters before re-enabling the stage.
- A single accidental click will bypass or un-bypass the stage. If this happens, single-click the same tile again to restore its previous state.

## Related

- [PooDoo Audio Chain overview](overview.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Re-enable a specific stage after a global bypass](re-enable-a-specific-stage-after-a-global-bypass.md)
- [Reorder the TX DSP chain](reorder-the-tx-dsp-chain.md)
- [Switch between TX chain view and RX placeholder](switch-between-tx-chain-view-and-rx-placeholder.md)
