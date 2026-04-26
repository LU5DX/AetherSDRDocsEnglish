# Bypass every TX stage at once

Use the BYPASS control to silence the entire TX DSP chain in one click — useful when you want a dry, unprocessed signal for a quick comparison or to troubleshoot a processing stage.

## Before you start

- The Aetherial Audio Chain applet must be visible. If it is not, click the PUDU tray button in the right sidebar to show the "Aetherial Audio" container.
- The TX chain must be the active side. If RX is currently shown, click TX in the applet header to switch.

## Steps

1. Open the Aetherial Audio Chain applet by clicking the PUDU tray button in the right sidebar if the applet is not already visible.
2. Click TX in the applet header to make the TX chain active. TX uses amber highlighting when selected.
3. Click BYPASS.

   All stages on the TX chain (EQ, COMP, GATE, DESS, TUBE, PUDU, VERB) are disabled at once. BYPASS remains checked with an amber border to indicate the chain is bypassed.

4. To restore processing, click BYPASS again.

   Only the stages that were enabled before you activated BYPASS are re-enabled. Any stage you toggled manually while BYPASS was active is not included in the restore.

## What each control does

| Control | Default | Behavior | Persisted setting |
|---------|---------|----------|-------------------|
| TX | Checked | Shows and edits the TX DSP chain. Amber highlight when active. | `PooDooAudioActiveTab` |
| RX | Unchecked | Shows and edits the RX DSP chain. TX and RX keep independent BYPASS snapshots. | `PooDooAudioActiveTab` |
| BYPASS | Unchecked | Checked: snapshots currently-enabled TX stages and disables all of them. Unchecked: re-enables only the stages that were on before. | — (not persisted) |

## Tips

- BYPASS acts only on the side currently shown. Activating BYPASS while TX is displayed has no effect on the RX chain, and vice versa.
- If you toggle individual stages while BYPASS is checked, those manual changes are preserved outside the snapshot and will not be reversed when you uncheck BYPASS.
- The TX chain stage order (and each stage's enabled state) persists via `ClientCompTxChainStages`.

## Troubleshooting

- **BYPASS is checked but you can still hear processing** — Confirm that TX is the active tab. If RX is selected, BYPASS applies to the RX chain, not TX. Click TX and check BYPASS state again.
- **After unchecking BYPASS, fewer stages are active than expected** — A stage that was already disabled before you engaged BYPASS will not be restored by BYPASS, because it was not part of the snapshot.

## Related

- [Bypass every RX stage at once](bypass-every-rx-stage-at-once.md)
- [Re-enable a specific stage after a global bypass](re-enable-a-specific-stage-after-a-global-bypass.md)
- [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)
- [Aetherial Audio Chain overview](overview.md)
