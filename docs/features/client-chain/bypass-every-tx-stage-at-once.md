# Bypass every TX stage at once

The BYPASS button disables every active stage in the TX DSP chain in one click and restores them just as quickly. Use it when you need a clean, unprocessed signal path without touching individual stage settings.

## Before you start

- The PooDoo Audio (TXDSP) container must be visible. If it is not, click the tray button labelled **PUDU** in the right sidebar to show it.
- The **TX** mode button must be selected (it is selected by default). BYPASS has no effect in RX mode.

## Steps

1. Locate the header row of the PooDoo Audio Chain applet. It contains the **TX**, **RX**, and **BYPASS** buttons.
2. Click **BYPASS**.
   - The button highlights with an amber border and fill, confirming it is active.
   - AetherSDR snapshots which stages were enabled at that moment and disables all of them.
3. To restore the chain, click **BYPASS** again.
   - Every stage that was enabled before you activated BYPASS is re-enabled.
   - Stages you toggled manually while BYPASS was active are not affected by the restore.

## What each control does

| Control | Kind | Default | Behavior | Setting key |
|---|---|---|---|---|
| **TX** | Toggle button | Checked | Shows the TX DSP chain; required for BYPASS to have any effect. | — |
| **RX** | Toggle button | Unchecked | Switches to the RX chain placeholder. BYPASS is a no-op in this mode. | — |
| **BYPASS** | Toggle button | Unchecked | Checked: snapshots currently-enabled stages and disables all of them. Unchecked: re-enables exactly the stages that were on before the snapshot. | `ClientCompTxChainStages` |

The `Applet_TXDSP` key persists whether the PooDoo Audio container is visible.

## Tips

- If you manually toggle a stage while BYPASS is active, that change is preserved when you release BYPASS. Only the original snapshot is restored, not your manual adjustments.
- The BYPASS button tooltip reads: "Disable every stage in the selected chain. Click again to restore the stages that were on before."

## Troubleshooting

- **BYPASS appears to do nothing** — Confirm the **TX** button is selected. BYPASS is a no-op when **RX** is active.
- **Some stages did not re-enable after releasing BYPASS** — Those stages were likely toggled manually while BYPASS was active. Their new state is preserved by design. Re-enable them individually by clicking each stage in the chain.

## Related

- [Re-enable a specific stage after a global bypass](re-enable-a-specific-stage-after-a-global-bypass.md)
- [PooDoo Audio Chain overview](overview.md)
- [Switch between TX chain view and RX placeholder](switch-between-tx-chain-view-and-rx-placeholder.md)
