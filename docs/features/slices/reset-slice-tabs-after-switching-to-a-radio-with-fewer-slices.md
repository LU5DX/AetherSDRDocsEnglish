# Reset slice tabs after switching to a radio with fewer slices

When you connect to a radio that supports fewer slices than your previous session, the Main Window may show stale slice tabs that no longer correspond to active slices. This page explains how to clear those tabs so the layout reflects the new radio's actual slice count.

## Before you start

- AetherSDR must be connected to a FlexRadio device (LAN or SmartLink WAN) before performing these steps.
- Note how many slices the new radio supports so you can confirm the tab count is correct after the reset.

## Steps

1. Connect to the new radio. AetherSDR opens the Main Window automatically on launch; if you are switching radios mid-session, use the radio-selection control in the Main Window to connect to the replacement radio.
2. If extra slice tabs remain visible after the connection completes, disconnect from the radio and reconnect. The Main Window resets the slice tab layout to match the slice count reported by the newly connected radio on each fresh connection.

## What each control does

| Control | Behavior |
|---|---|
| Radio connection / disconnect | Triggers a full slice-tab reset. On reconnect, the Main Window rebuilds the tab strip to match the number of slices the connected radio exposes, removing any tabs that exceed that count. |
| Slice tabs | Each tab represents one active slice on the connected radio. Tabs beyond the radio's maximum slice count are removed automatically after a reconnect. |

## Tips

- If stale tabs persist after reconnecting, check that the previous radio session closed cleanly. An unclean disconnect can leave residual state; a second disconnect-and-reconnect cycle clears it.
- When using SmartLink WAN, the automatic reconnection logic in the Main Window also triggers a tab reset, so you do not need to intervene manually after a WAN drop and recovery.

## Related

- [main-window.md](main-window.md)
- [connecting-to-a-radio.md](connecting-to-a-radio.md)
<!-- docmesh:llm version=v0.9.5.1 date=2026-05-04 -->
