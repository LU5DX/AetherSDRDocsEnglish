# Reconnect automatically after a SmartLink WAN radio drop

AetherSDR's main window monitors your SmartLink WAN connection and can reconnect to the radio automatically after a drop, without requiring you to restart the application.

## Before you start

- You must have a SmartLink account configured and a WAN radio already added in AetherSDR.
- The radio must be reachable via SmartLink at the time reconnection is attempted.

## Steps

1. Launch AetherSDR. The main window opens automatically and begins managing your connection.
2. If the WAN radio drops, AetherSDR detects the disconnection and initiates automatic reconnection in the background. No manual action is required — the window will restore the radio connection and resume normal operation once the link is re-established.

## Tips

- If automatic reconnection does not succeed, check that your SmartLink credentials are still valid and that the radio is powered on and reachable from the WAN.
- Automatic reconnection runs silently; watch the connection status indicator in the main window to confirm the link has been restored.

## Related

- [Connect to a FlexRadio over SmartLink WAN](smartlink-connect.md)
- [Configure SmartLink credentials](smartlink-credentials.md)
<!-- docmesh:llm version=v0.9.5.1 date=2026-05-04 -->
