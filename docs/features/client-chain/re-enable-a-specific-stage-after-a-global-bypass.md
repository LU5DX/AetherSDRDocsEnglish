# Re-enable a specific stage after a global bypass

After using BYPASS to silence every stage in the TX or RX chain, you can bring back individual stages one at a time without lifting the global bypass or restoring all stages at once.

## Before you start

- The Aetherial Audio Chain applet must be visible. If it is not, click the PUDU tray button in the right sidebar to show the container.
- BYPASS must currently be active (the BYPASS button will appear checked, with an amber border and fill) on the chain side you want to edit.
- Confirm you are viewing the correct chain side — click TX or RX to switch if needed.

## Steps

1. In the Aetherial Audio Chain header row, confirm BYPASS is checked. While BYPASS is active, all stages are visually disabled.
2. Click TX or RX to ensure the chain side you want to edit is shown.
3. Locate the stage tile you want to re-enable in the horizontal strip (for TX: EQ, COMP, GATE, DESS, TUBE, PUDU, VERB; for RX: EQ, AGC-T, AGC-C, TUBE, PUDU).
4. Single-click that stage tile. This toggles bypass off for that stage alone, re-enabling it while all other stages remain bypassed.
5. Repeat step 4 for any additional stages you want to bring back individually.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| TX | Toggle button | Switches the chain view to the TX DSP chain. TX and RX keep independent stage states and BYPASS snapshots. |
| RX | Toggle button | Switches the chain view to the RX DSP chain. |
| BYPASS | Toggle button | When checked, snapshots the currently-enabled stages and disables all of them. When unchecked, restores only the stages that were on before. Stages toggled manually while BYPASS is active are preserved outside the snapshot. On the TX side, bypass state is owned by the audio engine; the BYPASS button stays in sync with the engine automatically, including changes made from the Aetherial Audio Channel Strip. |
| TX chain stage (EQ / COMP / GATE / DESS / TUBE / PUDU / VERB) | Stage tile | Single-click toggles bypass for that stage only. Double-click opens the Aetherial Audio Channel Strip (the unified TX DSP window). Drag reorders the chain. |
| RX chain stage (EQ / AGC-T / AGC-C / TUBE / PUDU) | Stage tile | Single-click toggles bypass for that stage only. Double-click opens its frameless floating editor in RX mode. Drag reorders the RX chain. All five RX stages are fully implemented. Order is independent of the TX chain. |

## Tips

- Manually re-enabling a stage while BYPASS is checked places that stage outside the bypass snapshot. If you later uncheck BYPASS to do a full restore, that stage's pre-bypass state (not its current state) is what gets applied. Re-enable only the stages you deliberately want active during bypass.
- TX and RX maintain separate BYPASS snapshots. Enabling specific stages on the TX side does not affect the RX side's snapshot, and vice versa.
- On the TX side, the BYPASS button reflects engine-owned state. If you toggle TX bypass from the Aetherial Audio Channel Strip, the BYPASS button in the chain applet updates automatically to match.
- Double-clicking any TX stage tile now opens the Aetherial Audio Channel Strip rather than a per-stage floating editor. Individual stage editors are still accessible from within the Channel Strip itself.
- The hint below the chain strip reads "Click to bypass · Double click to edit · Drag to reorder" and applies to both chain sides.

## Related

- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Bypass every RX stage at once](bypass-every-rx-stage-at-once.md)
- [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)
- [Open a stage's frameless floating editor from the chain](open-a-stage-s-frameless-floating-editor-from-the-chain.md)