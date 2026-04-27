# Bypass every RX stage at once

Use the BYPASS button to disable all RX chain stages in a single click, without losing track of which stages were active. Clicking BYPASS again restores only the stages that were enabled before.

## Before you start

- The Aetherial Audio Chain applet must be visible. If it is not, click the PUDU tray button in the right sidebar to show the container.
- You must be viewing the RX chain. The BYPASS button acts on whichever chain side is currently shown.

## Steps

1. In the Aetherial Audio Chain applet header, click **RX**. The RX chain stages appear below.
2. Click **BYPASS**. The button changes to its checked appearance (amber border and fill). Every stage in the RX chain is disabled immediately. AetherSDR snapshots which stages were enabled at the moment you clicked.
3. To restore the previous stage states, click **BYPASS** again. Only the stages that were enabled before the bypass are re-enabled.

## What each control does

| Control | Kind | Default | Persisted key | Behavior |
|---|---|---|---|---|
| **RX** | Toggle button | Unchecked | `PooDooAudioActiveTab` | Switches the applet to show the RX chain. Required before BYPASS acts on RX stages. The last-active tab is saved as `TX` or `RX`. |
| **BYPASS** | Toggle button | Unchecked | — | Checked: snapshots currently-enabled RX stages and disables all of them. Unchecked: re-enables only the stages that were on before. TX and RX maintain separate snapshots. |
| RX chain stage (EQ / GATE / COMP / TUBE / PUDU) | Drag handle | — | `ClientCompRxChainStages` | Single-click toggles bypass on an individual stage. Stages toggled manually while BYPASS is active are preserved independently of the snapshot. |

## Tips

- TX and RX keep separate BYPASS snapshots. Activating BYPASS on the RX chain does not affect the TX chain, and vice versa.
- If you manually toggle an individual stage while BYPASS is checked, that change is preserved outside the snapshot and will not be reversed when you uncheck BYPASS.
- The BYPASS checked state shown in the header tracks whichever chain side is currently visible. Switch to TX and back to RX to confirm the RX BYPASS state at a glance.

## Troubleshooting

- **BYPASS appears checked but some stages are still active** — You may have toggled individual stages manually after engaging BYPASS. Those manual changes are independent of the snapshot. Uncheck and re-check BYPASS to take a fresh snapshot of the current stage states.
- **Clicking BYPASS re-enables stages you did not expect** — The snapshot was taken when BYPASS was first checked. Only the stages that were enabled at that moment are restored. Any stages you disabled before engaging BYPASS will remain off.

## Related

- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Re-enable a specific stage after a global bypass](re-enable-a-specific-stage-after-a-global-bypass.md)
- [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)
- [Aetherial Audio Chain overview](overview.md)
