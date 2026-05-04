# Fix SmartLink WAN disconnect leaving stale panadapters

AetherSDR's main window manages SmartLink WAN connections and automatically cleans up panadapters when a WAN session drops. Version 0.9.5.1 fixes a bug where disconnecting from a SmartLink WAN session could leave orphaned panadapters visible in the layout.

## Before you start

- Update to AetherSDR v0.9.5.1 or later. Earlier builds do not include the stale-panadapter cleanup fix.
- Confirm you are connecting via SmartLink WAN, not a direct LAN connection. LAN connections are not affected.

## Steps

1. Launch AetherSDR. The main window opens automatically.
2. Connect to your radio using SmartLink WAN as normal.
3. If a WAN disconnect occurs (deliberate or unexpected), AetherSDR now automatically removes any panadapters that were open during the dropped session before attempting reconnection. No manual cleanup is required.
4. Once the automatic reconnection completes, your panadapter layout rebuilds cleanly from the radio's current state.

## What each control does

| Control | Behavior |
|---|---|
| SmartLink WAN connection | Connects the main window to a remote FlexRadio over the internet via SmartLink. On disconnect, v0.9.5.1 ensures all panadapters from that session are torn down before reconnection is attempted. |
| Automatic WAN reconnection | After a WAN drop is detected, the main window cleans up stale panadapters, then initiates a reconnect sequence without requiring user interaction. |
| Panadapter layout | Rebuilt from the radio's live state after each successful reconnection. Orphaned panadapters from the previous session no longer persist. |

## Tips

- If you see leftover panadapters after a disconnect on a build older than v0.9.5.1, manually close them before reconnecting to avoid layout conflicts.
- LAN-connected sessions are unaffected by this fix. Panadapter cleanup on LAN disconnect was already handled correctly in earlier versions.

## Related

- [SmartLink WAN connection setup](smartlink-wan-setup.md)
- [Panadapter layout management](panadapter-layout.md)
- [Automatic WAN reconnection](wan-reconnection.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
