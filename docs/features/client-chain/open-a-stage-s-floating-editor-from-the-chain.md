# Open a stage's floating editor from the chain

Double-clicking a stage in the PooDoo Audio Chain opens that stage's floating editor, where you can adjust its parameters in detail.

## Before you start

- The PooDoo Audio (TXDSP) container must be visible. If it is not, click the PUDU tray button in the right sidebar to toggle it on.
- The chain must be in TX mode. The TX button must be selected (amber) in the chain header.

## Steps

1. Locate the PooDoo Audio Chain strip at the top of the TXDSP container.
2. Find the stage you want to edit: Eq, Comp, Gate, DeEss, Tube, Enh / PUDU, or Reverb.
3. Double-click the stage tile.

The stage's floating editor opens immediately.

## What each control does

| Stage tile | Single-click | Double-click | Drag |
|---|---|---|---|
| Chain stage (Eq) | Toggles bypass for the EQ stage | Opens the EQ editor | Reorders the chain |
| Chain stage (Comp) | Toggles bypass for the compressor | Opens the compressor editor | Reorders the chain |
| Chain stage (Gate) | Toggles bypass for the gate | Opens the gate editor | Reorders the chain |
| Chain stage (DeEss) | Toggles bypass for the de-esser | Opens the de-ess editor | Reorders the chain |
| Chain stage (Tube) | Toggles bypass for the tube saturator | Opens the tube editor | Reorders the chain |
| Chain stage (Enh / PUDU) | Toggles bypass for the PUDU exciter | Opens the PUDU editor | Reorders the chain |
| Chain stage (Reverb) | Toggles bypass for the reverb | Opens the reverb editor | Reorders the chain |

The chain's stage order and enabled states are persisted under `ClientCompTxChainStages`. The container's visibility state is persisted under `Applet_TXDSP`.

## Tips

- The hint text below the chain strip reads "Click to bypass · Double click to edit · Drag to reorder" and is visible whenever TX mode is active.
- A single click bypasses the stage rather than opening the editor. If the editor did not open, check whether you single-clicked instead of double-clicked.
- The stage tile responds to double-click regardless of whether the stage is currently bypassed.

## Troubleshooting

- **The chain strip is not visible** — The TXDSP container may be hidden. Click the PUDU tray button in the right sidebar to show it, or verify that TX is selected in the chain header rather than RX.
- **Double-clicking has no effect** — The chain must be in TX mode. Click TX in the chain header to switch to it. In RX mode the chain strip is replaced by a placeholder and stage interaction is not available.

## Related

- [PooDoo Audio Chain overview](overview.md)
- [Reorder the TX DSP chain](reorder-the-tx-dsp-chain.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Re-enable a specific stage after a global bypass](re-enable-a-specific-stage-after-a-global-bypass.md)
- [Switch between TX chain view and RX placeholder](switch-between-tx-chain-view-and-rx-placeholder.md)
