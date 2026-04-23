# Bypass every TX stage at once

Use the BYPASS button to silence the entire TX DSP chain instantly — EQ, Compressor, Gate, De-Ess, Tube, PUDU, and Reverb — and restore them all in a single click when you are done.

## Before you start

- The PooDoo Audio (TXDSP) container must be visible. If it is not, click the tray button labelled **PUDU** in the right sidebar to show it.
- The TX mode must be active. BYPASS has no effect in RX mode.

## Steps

1. Confirm the **TX** button at the top-left of the PooDoo Audio chain strip is checked. If **RX** is checked instead, click **TX**.
2. Click **BYPASS**. The button changes to its checked state (saturated amber border and fill). Every currently-enabled stage is snapshotted and disabled.
3. To restore, click **BYPASS** again. The stages that were enabled before the bypass are re-enabled.

## What each control does

| Control | Kind | Default | Behavior | Setting key |
|---|---|---|---|---|
| TX | Toggle button | Checked | Shows the interactive TX DSP chain. Required for BYPASS to take effect. | — |
| RX | Toggle button | Unchecked | Switches to the RX chain placeholder. BYPASS is a no-op in this mode. | — |
| BYPASS | Toggle button | Unchecked | Checked: snapshots currently-enabled stages and disables all of them. Unchecked: re-enables only the stages that were on before. | `ClientCompTxChainStages` |

The chain strip and its container visibility are persisted under `Applet_TXDSP`.

## Tips

- If you manually toggle individual stages while BYPASS is checked, those changes are tracked separately from the snapshot. When you uncheck BYPASS, only the stages that were enabled at the moment you checked BYPASS are restored; your manual changes during the bypass are preserved.
- BYPASS applies only to the TX chain. Clicking it while **RX** is selected does nothing.

## Troubleshooting

- **BYPASS is checked but audio still passes through one stage** — A stage may have been turned on manually after BYPASS was activated. That stage is outside the snapshot. Click the stage once to bypass it individually, or uncheck and re-check BYPASS to take a fresh snapshot.
- **BYPASS button is present but clicking it has no effect** — The **RX** button is selected. Click **TX** first; BYPASS only operates on the TX chain.

## Related

- [PooDoo Audio Chain overview](overview.md)
- [Re-enable a specific stage after a global bypass](re-enable-a-specific-stage-after-a-global-bypass.md)
- [Open a stage's floating editor from the chain](open-a-stage-s-floating-editor-from-the-chain.md)
- [Switch between TX chain view and RX placeholder](switch-between-tx-chain-view-and-rx-placeholder.md)
