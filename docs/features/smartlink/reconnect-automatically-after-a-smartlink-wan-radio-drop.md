# Reconnect automatically after a SmartLink WAN radio drop

AetherSDR can detect when a SmartLink WAN connection to a FlexRadio drops and reconnect without requiring you to restart the application.

## Before you start

- You must already have a SmartLink account configured and have successfully connected to a remote radio at least once.
- Ensure your internet connection is active before enabling automatic reconnection.

## Steps

1. Launch AetherSDR — the Main Window opens automatically.
2. Connect to your remote radio via SmartLink WAN using your usual connection credentials.
3. If the WAN connection drops, AetherSDR detects the drop and attempts to reconnect automatically — no additional action is required. Watch the connection status indicator in the Main Window for progress.

## What each control does

| Control | Behavior |
|---|---|
| Connection status indicator | Shows the current state of the SmartLink WAN link (connected, dropped, reconnecting). Updates automatically as the reconnection process progresses. |
| Automatic reconnection | Triggers without user input when a WAN radio drop is detected. AetherSDR retries the SmartLink connection and restores the previous slice and panadapter layout on success. |

## Tips

- If reconnection does not succeed after several attempts, check your SmartLink credentials and verify the remote radio is powered on and reachable.
- All applets and slice/panadapter assignments are restored automatically after a successful reconnect — you do not need to reconfigure your layout.

## Related

- [Connect to a FlexRadio over SmartLink WAN](connect-smartlink-wan.md)
- [Configure SmartLink credentials](smartlink-credentials.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
