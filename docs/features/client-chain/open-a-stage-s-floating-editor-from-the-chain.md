# Open a Stage's Floating Editor from the Chain

Each stage in the TX DSP chain has a dedicated floating editor where you can adjust its parameters in detail. Double-clicking a stage tile opens that editor without affecting the stage's bypass state.

## Before you start

- The PooDoo Audio (TXDSP) container must be visible. If it is not, click the PUDU tray button in the right sidebar to show it.
- The chain must be in TX mode. Confirm that TX is selected (not RX) at the top of the chain strip.

## Steps

1. Locate the chain strip at the top of the PooDoo Audio container. The hint line below the strip reads "Click to bypass · Double click to edit · Drag to reorder".
2. Identify the stage you want to edit: Eq, Comp, Gate, DeEss, Tube, Enh / PUDU, or Reverb.
3. Double-click the stage tile. The editor for that stage opens as a floating window.
4. Adjust parameters in the editor as needed. Close the editor when finished.

## What each control does

| Stage tile | Opens editor for | Single-click action |
|---|---|---|
| Chain stage (Eq) | EQ | Toggles bypass for the EQ stage |
| Chain stage (Comp) | Compressor | Toggles bypass for the compressor |
| Chain stage (Gate) | Gate | Toggles bypass for the gate |
| Chain stage (DeEss) | De-esser | Toggles bypass for the de-esser |
| Chain stage (Tube) | Tube saturator | Toggles bypass for the tube saturator |
| Chain stage (Enh / PUDU) | PUDU exciter | Toggles bypass for the PUDU exciter |
| Chain stage (Reverb) | Reverb | Toggles bypass for the reverb |

The chain strip order and per-stage bypass states are persisted under `ClientCompTxChainStages`. The TXDSP container visibility is persisted under `Applet_TXDSP`.

## Tips

- A single click on a stage tile toggles its bypass rather than opening the editor. Be sure to double-click to reach the editor.
- Opening an editor does not bypass or otherwise change the stage's active state.

## Related

- [Reorder the TX DSP chain](reorder-the-tx-dsp-chain.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Re-enable a specific stage after a global bypass](re-enable-a-specific-stage-after-a-global-bypass.md)
- [Switch between TX chain view and RX placeholder](switch-between-tx-chain-view-and-rx-placeholder.md)
