# Keep a SmartLink WAN session alive through NAT

`PanadapterStream::startWanUdpRegister` registers your local UDP port with the radio over a SmartLink WAN connection, then maintains the NAT mapping by sending periodic keepalive pings so the session does not drop.

## Before you start

- You must have a SmartLink (WAN) connection configured and the radio reachable through SmartLink.
- Ensure no local firewall rule blocks outbound UDP traffic on the port the SDK binds.

## Steps

1. Call `startWanUdpRegister` on your `PanadapterStream` instance after the stream has been started in WAN mode. The method immediately sends a registration datagram to the radio to announce the client's UDP port.
2. Wait for the radio to confirm receipt. While waiting, the method automatically retransmits the registration datagram every **50 ms**. No additional action is required from your application during this phase.
3. Once the radio acknowledges registration, the method switches automatically to a **5-second ping keepalive** cycle. The keepalive runs in the background and requires no further calls from your code.

## What each control does

| Control | Behavior |
|---|---|
| Initial registration datagram | Sent immediately on `startWanUdpRegister`; tells the radio which UDP port the client is listening on. |
| 50 ms retransmit interval | Repeats the registration datagram every 50 ms until the radio confirms receipt, compensating for packet loss across the WAN. |
| 5-second ping keepalive | After confirmation, sends a lightweight ping every 5 seconds to keep the NAT binding open on intermediate routers and firewalls. |

## Tips

- Do not call `startWanUdpRegister` on a LAN connection; it is intended exclusively for SmartLink WAN sessions. Use the standard VITA-49 UDP bind path for LAN.
- If your application needs to detect whether registration succeeded, poll `m_hasReceivedPacket` after a reasonable timeout (a few hundred milliseconds is typically sufficient over a healthy WAN link).
- Keep the `PanadapterStream` instance alive for the duration of the session. Destroying it stops the keepalive timer, which will cause the NAT mapping to expire and the stream to go silent.

## Related

- [start-wan-stream.md](start-wan-stream.md)
- [smartlink-connection-setup.md](smartlink-connection-setup.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
