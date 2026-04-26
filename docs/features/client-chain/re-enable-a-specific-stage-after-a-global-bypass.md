# Re-enable a specific stage after a global bypass

After using BYPASS to silence the entire TX or RX chain, you may want to bring back one or more individual stages without lifting the global bypass or restoring every stage at once. A single click on the stage tile is all it takes.

## Before you start

- The Aetherial Audio Chain must be visible. If it is not, click the PUDU tray button in the right sidebar to show it.
- BYPASS must currently be checked (amber, active) on the chain side — TX or RX — where you want to re-enable a stage.
- Make sure you are viewing the correct chain side. Click TX or RX in the applet header to confirm.

## Steps

1. Look at the header row of the Aetherial Audio Chain. Confirm BYPASS is checked (amber border and fill).
2. If you need to work on the TX chain, click TX. If you need to work on the RX chain, click RX.
3. Locate the stage tile you want to re-enable — for example, COMP on the TX chain or GATE on the RX chain.
4. Click the stage tile once. The stage toggles from bypassed to active.
5. Repeat step 4 for any other individual stages you want to restore.

The BYPASS button remains checked. Only the stages you clicked are now active; all others remain bypassed. Stages re-enabled this way are preserved outside the bypass snapshot, so clicking BYPASS off later restores only the stages that were on *before* BYPASS was first engaged.

## What each control does

| Control | Kind | Default | Behavior | Setting key |
|---|---|---|---|---|
| TX | Toggle button | Checked | Switches the applet to show and interact with the TX DSP chain (EQ, COMP, GATE, DESS, TUBE, PUDU, VERB). | `PooDooAudioActiveTab` |
| RX | Toggle button | Unchecked | Switches the applet to show and interact with the RX DSP chain (EQ, GATE, COMP, TUBE, PUDU). | `PooDooAudioActiveTab` |
| BYPASS | Toggle button | Unchecked | Checked: snapshots the currently-enabled stages and disables all of them. Unchecked: restores only the stages that were on before. TX and RX maintain separate snapshots. | — |
| TX chain stage (EQ / COMP / GATE / DESS / TUBE / PUDU / VERB) | Stage tile | — | Single-click toggles bypass for that stage. Double-click opens its frameless editor. Drag reorders the chain. | `ClientCompTxChainStages` |
| RX chain stage (EQ / GATE / COMP / TUBE / PUDU) | Stage tile | — | Single-click toggles bypass for that stage. Double-click opens its frameless editor. Drag reorders the chain. | `ClientCompRxChainStages` |

## Tips

- Stages toggled manually while BYPASS is active are not recorded in the bypass snapshot. If you re-enable a stage while BYPASS is checked and then uncheck BYPASS, that stage stays on — it will not be switched off by the snapshot restore.
- TX and RX keep independent bypass snapshots. Clicking BYPASS on one side does not affect the other.
- The hint line below the chain reads "Click to bypass · Double click to edit · Drag to reorder" as a reminder that a single click is always a toggle.

## Troubleshooting

- **Clicking a stage tile does nothing** — Confirm the Aetherial Audio Chain container is fully expanded and that you are clicking the stage tile itself, not the gap between tiles.
- **Unchecking BYPASS restores a stage you wanted to leave bypassed** — Any stage that was enabled before BYPASS was first checked will be restored when BYPASS is unchecked. To keep a stage bypassed after lifting BYPASS, click it once after unchecking BYPASS to toggle it back off.

## Related

- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Bypass every RX stage at once](bypass-every-rx-stage-at-once.md)
- [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)
- [Aetherial Audio Chain overview](overview.md)
