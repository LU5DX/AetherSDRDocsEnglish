# Reconnect automatically after a SmartLink WAN drop

`PanadapterStream::startWan` binds a local UDP port and registers with the remote radio's UDP endpoint to receive data over a SmartLink (WAN) connection. Use the steps below to re-establish that connection after a WAN drop.

## Before you start

- Confirm the SmartLink session is still authenticated and your internet connection is active.
- Ensure no other application is holding the UDP port open from the previous session.

## Steps

1. In the AetherSDR main window, open **Radio > Disconnect** to close the dropped session and release the bound UDP socket.
2. Select **Radio > Connect via SmartLink** and choose your radio from the list to trigger a fresh `startWan` call, which binds a new ephemeral local UDP port and re-registers with the remote radio's UDP endpoint.

## What each control does

| Control | Behavior |
|---|---|
| **Radio > Disconnect** | Closes the current WAN session, stops the routed prime timer, and releases the UDP socket so a new bind can succeed. |
| **Radio > Connect via SmartLink** | Calls `startWan`, binds an OS-assigned local UDP port using `DontShareAddress` mode, and registers the port with the remote radio to resume the panadapter data stream. |

## Tips

- If reconnection fails immediately, wait 10–15 seconds before retrying. The remote radio may still hold the previous UDP registration open until it times out.
- Check the application log for `PanadapterStream: LAN VITA UDP bind` to confirm the new port was assigned successfully.
- On networks with strict firewall rules, ensure outbound UDP traffic is not blocked for the OS-assigned ephemeral port range.

## Related

- [smartlink-setup.md](smartlink-setup.md)
- [panadapter-stream.md](panadapter-stream.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
