# Fix stale slice tabs after switching to a radio with fewer slices

When you disconnect from one radio and connect to another that has fewer slices, the RX applet's slice tab row (buttons A through H) may still show tabs from the previous session. This page explains how to clear those stale tabs and restore a clean state.

## Before you start

- You have already disconnected from the first radio and are connected to, or are about to connect to, a second radio with fewer available slices.
- The RX applet is visible in the Applet Panel. If it is not, click the **RX** tray button on the right sidebar.

## Steps

1. Disconnect from the current radio if you have not already done so. Use `Settings > Connect to Radio...` to open the connection dialog, then close or cancel the existing connection.
2. Observe the slice tab row at the top of the RX applet. If tabs (for example A, B, C, D) from the previous radio are still shown, they are stale.
3. Connect to the new radio using `Settings > Connect to Radio...` and select the target radio.
4. Once the new connection is established, AetherSDR calls `clearSliceButtons()` internally on disconnect, which tears down all generated slice tab buttons and restores the static slice badge. The slice tab row will then be repopulated to match the new radio's maximum slice count.
5. Confirm that the slice tab row now shows only the correct number of tabs (capped at the new radio's hardware maximum). If the new radio supports only one slice, the tab row is hidden entirely and only the slice badge is shown.

## What each control does

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| Slice tabs (A..H) | Selects which slice the RX applet is bound to. The row is hidden when the radio's maximum slice count is 1 or fewer. On disconnect, all generated tab buttons are removed and the static slice badge is restored. | — | — |
| Slice badge | Displays the letter of the currently bound slice. Shown at all times; the only slice indicator visible when the tab row is hidden. | A | — |

## Tips

- Slice tab buttons are capped by the connected radio's hardware maximum. A radio that supports two slices will never show more than two tabs, regardless of what the previous radio had.
- Duplicate signal handler connections are guarded across reconnects, so reconnecting to the same radio multiple times will not multiply the tab click responses.

## Troubleshooting

- **Stale tabs remain after reconnecting** — This can occur if the disconnect event did not fire cleanly. Disconnect again using `Settings > Connect to Radio...`, wait for the slice badge to reappear in place of the tabs, then reconnect.
- **Tab row is missing entirely after connecting** — If the new radio reports a maximum slice count of 1 or fewer, the tab row is intentionally hidden. Only the slice badge is shown. This is expected behavior.

## Related

- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [RX Controls overview](overview.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)
