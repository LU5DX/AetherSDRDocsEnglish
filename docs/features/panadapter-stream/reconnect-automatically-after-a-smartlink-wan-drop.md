# Reconnect automatically after a SmartLink WAN drop

`PanadapterStream::startWan` binds a local UDP port and registers it with the remote radio's UDP endpoint to begin receiving panadapter data over a SmartLink (WAN) connection. If the WAN link drops, you can trigger a clean reconnect by restarting the stream so the registration sequence runs again.

## Before you start

- Confirm that your SmartLink credentials are saved and that the remote radio is reachable.
- Note the radio's current connection state in the status bar — it must show **Disconnected** or an error before you attempt to reconnect.

## Steps

1. Open **Radio > SmartLink Connections** and select the affected radio in the list.
2. Click **Disconnect** to ensure the existing session is fully torn down (skipping this can leave a stale UDP registration on the radio side).
3. Click **Connect**. AetherSDR binds a new local UDP port, sends a `client udp_register` datagram to the radio, and starts the 5-second WAN ping keepalive. The status bar changes to **Connected** once the radio acknowledges registration.

## Tips

- If **Connect** does not succeed after 15–20 seconds, check whether your NAT or firewall is blocking the outbound UDP registration packet to port 4992 on the radio host.
- The WAN keepalive runs automatically every 5 seconds after a successful registration; you do not need to do anything to maintain the connection once it is established.
- If drops happen repeatedly, inspect the network quality monitor (packet error count and total count are tracked per stream) to determine whether packet loss is causing the keepalive to time out.

## Related

- [smartlink-setup.md](smartlink-setup.md)
- [panadapter-stream-diagnostics.md](panadapter-stream-diagnostics.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
