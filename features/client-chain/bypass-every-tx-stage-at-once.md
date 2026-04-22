# Bypass every TX stage at once

The BYPASS button disables all active TX DSP chain stages in a single click and restores them with another click. Use it to compare your processed and unprocessed TX audio without manually toggling each stage.

## Before you start

- The PooDoo Audio (TXDSP) container must be visible. If it is not, click the PUDU tray button in the right sidebar to show it.
- TX must be selected in the chain applet. The TX toggle is checked by default; if RX is selected instead, BYPASS is a no-op.

## Steps

1. Confirm the TX toggle is checked in the header row of the PooDoo Audio Chain applet. The button lights amber when active.
2. Click BYPASS.
3. AetherSDR snapshots the currently-enabled stages and disables all of them. The BYPASS button lights amber to indicate the bypass is active.
4. Click BYPASS again to restore the stages that were enabled before you activated the bypass.

## What each control does

| Control | Default | Behavior | Setting key |
|---|---|---|---|
| TX | Checked | Shows and edits the TX DSP chain. BYPASS operates on this chain only. | — |
| RX | Unchecked | Switches to the RX placeholder view. BYPASS is a no-op in this mode. | — |
| BYPASS | Unchecked | Checked: snapshots enabled stages and disables all of them. Unchecked: re-enables only the stages that were on before. | `ClientCompTxChainStages` |

## Tips

- Stages you toggle individually while BYPASS is active are not part of the snapshot. When you uncheck BYPASS, only the stages that were on at the moment you activated the bypass are restored.
- The PUDU tray button controls visibility of the entire PooDoo Audio container, which is persisted in `Applet_TXDSP`.

## Troubleshooting

- **Clicking BYPASS has no effect** — Check that TX is selected, not RX. In RX mode BYPASS does nothing, as the RX chain is not yet implemented.
- **BYPASS restores fewer stages than expected** — Any stage you manually toggled off while BYPASS was active was removed from the snapshot and will not be restored automatically. Re-enable it by clicking that stage directly.

## Related

- [Re-enable a specific stage after a global bypass](re-enable-a-specific-stage-after-a-global-bypass.md)
- [PooDoo Audio Chain overview](overview.md)
- [Switch between TX chain view and RX placeholder](switch-between-tx-chain-view-and-rx-placeholder.md)
