# Keep a SmartLink WAN session alive through NAT

When connecting to a radio over WAN through SmartLink, `PanadapterStream` automatically registers your client's UDP port with the radio and then sends periodic keepalive pings to prevent the NAT mapping from expiring.

## Before you start

- Your radio must be reachable over WAN via a SmartLink account.
- The SmartLink session must already be authenticated and a `RadioConnection` established before the keepalive sequence begins.

## Steps

1. Connect to your radio using SmartLink (WAN mode). AetherSDR calls `startWanUdpRegister` automatically once the connection is established — no manual action is required.
2. Confirm the session is active by watching the panadapter populate. The SDK sends an immediate `client udp_register` datagram to the radio, retries every 50 ms until the radio acknowledges, then switches to a 5-second ping to hold the NAT mapping open.

## What each control does

| Phase | Datagram sent | Interval | Stops when |
|---|---|---|---|
| Registration | `client udp_register handle=0x<handle>` | Every 50 ms | Radio confirms receipt |
| Keepalive ping | `client ping handle=0x<handle>` | Every 5 000 ms | Session is closed |

## Tips

- If the panadapter never populates, a firewall or router may be dropping the UDP registration datagrams before the radio can acknowledge them. Check that outbound UDP to the radio's WAN port is not blocked.
- The 5-second ping interval is fixed in the SDK. If your NAT device has an unusually short UDP mapping timeout (less than 5 seconds), you may need to configure the router to extend it.
- Byte counters (`totalTxBytes`, `totalRxBytes`) are updated atomically and are safe to read from any thread for diagnostics.

## Related

- [SmartLink WAN connection overview](smartlink-wan-overview.md)
- [PanadapterStream reference](panadapter-stream-reference.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
