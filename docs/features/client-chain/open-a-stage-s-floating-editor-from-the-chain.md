# Open a Stage's Floating Editor from the Chain

Double-clicking a stage in the PooDoo Audio Chain opens that stage's floating editor, where you can adjust its parameters in detail without leaving the chain view.

## Before you start

- The PooDoo Audio (TXDSP) container must be visible. If it is not, click the PUDU tray button in the right sidebar to enable it.
- The chain must be in TX mode. The TX toggle button must be active (amber). In RX mode the chain is a placeholder and stages cannot be edited.

## Steps

1. Locate the PooDoo Audio Chain strip at the top of the TXDSP container.
2. Find the stage you want to edit: Eq, Comp, Gate, DeEss, Tube, Enh / PUDU, or Reverb.
3. Double-click that stage tile.

The stage's floating editor opens immediately. Single-clicking the same tile would toggle bypass instead, so use a deliberate double-click.

## What each control does

The hint text below the chain strip reads: "Click to bypass · Double click to edit · Drag to reorder". This describes the three interactions available on every stage tile.

| Stage tile label | Double-click result |
|---|---|
| Chain stage (Eq) | Opens the EQ editor |
| Chain stage (Comp) | Opens the compressor editor |
| Chain stage (Gate) | Opens the gate editor |
| Chain stage (DeEss) | Opens the de-ess editor |
| Chain stage (Tube) | Opens the tube editor |
| Chain stage (Enh / PUDU) | Opens the PUDU editor |
| Chain stage (Reverb) | Opens the reverb editor |

Stage order and enabled state are persisted in `ClientCompTxChainStages`. The container's visibility is persisted in `Applet_TXDSP`.

## Tips

- A single click on a stage toggles its bypass state. If you accidentally bypass a stage with a single click, click it once more to re-enable it before double-clicking to edit.
- You can open an editor for a bypassed stage. Bypassing a stage does not prevent editing it.

## Troubleshooting

- **Double-clicking a stage does nothing** — Confirm the TX button is active (amber). In RX mode, stage tiles are not displayed and no editor can be opened.
- **The chain strip is not visible** — The TXDSP container may be hidden. Click the PUDU tray button in the right sidebar to show it.

## Related

- [PooDoo Audio Chain overview](overview.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Re-enable a specific stage after a global bypass](re-enable-a-specific-stage-after-a-global-bypass.md)
- [Reorder the TX DSP chain](reorder-the-tx-dsp-chain.md)
- [Switch between TX chain view and RX placeholder](switch-between-tx-chain-view-and-rx-placeholder.md)
