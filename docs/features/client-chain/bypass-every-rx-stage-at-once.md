# Bypass every RX stage at once

Use the BYPASS control to mute the entire RX DSP chain in one click — useful for a quick A/B check of what the client-side processing is doing to incoming audio.

## Before you start

- The Aetherial Audio Chain applet must be visible. If it is not, click the PUDU tray button in the right sidebar to show the container.
- The RX chain must be the active view. If TX is currently shown, you need to switch to RX first.

## Steps

1. Click RX in the applet header row. The RX chain strip becomes visible, showing the EQ, GATE, COMP, TUBE, and PUDU stages between the RADIO and SPEAK status tiles.
2. Click BYPASS. The button highlights in amber and every currently-enabled RX stage is disabled at once. The snapshot of which stages were on is saved internally.
3. To restore the chain, click BYPASS again. Only the stages that were enabled before the bypass was applied are re-enabled.

## What each control does

| Control | Kind | Default | Behavior | Setting key |
|---|---|---|---|---|
| RX | Toggle button | Unchecked | Switches the applet to show and edit the RX DSP chain. Persists the active tab. | `PooDooAudioActiveTab` |
| TX | Toggle button | Checked | Switches the applet to show and edit the TX DSP chain. Persists the active tab. | `PooDooAudioActiveTab` |
| BYPASS | Toggle button | Unchecked | Checked: snapshots enabled RX stages and disables all of them. Unchecked: re-enables only the stages that were on before. TX and RX maintain separate snapshots. | None |
| RX chain stage (EQ / GATE / COMP / TUBE / PUDU) | Drag handle | — | Single-click toggles bypass for that individual stage; double-click opens its frameless editor; drag reorders the chain. | `ClientCompRxChainStages` |

## Tips

- TX and RX keep entirely separate bypass snapshots. Engaging BYPASS on RX has no effect on the TX chain, and vice versa.
- If you toggle an individual stage manually while BYPASS is active, that change is preserved outside the snapshot and will not be reversed when you lift the bypass.
- The visual checked state of BYPASS tracks whichever side (TX or RX) is currently shown. Switching to TX while RX bypass is active will reflect the TX bypass state, not the RX one.

## Troubleshooting

- **BYPASS appears checked after switching from RX to TX** — Each side has its own bypass state. What you see reflects the active chain. Switch back to RX to see or change the RX bypass state.
- **Stages remain disabled after clicking BYPASS a second time** — A stage toggled manually while BYPASS was active sits outside the snapshot and will not be automatically restored. Click each affected stage individually to re-enable it.

## Related

- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Re-enable a specific stage after a global bypass](re-enable-a-specific-stage-after-a-global-bypass.md)
- [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)
- [Aetherial Audio Chain overview](overview.md)
