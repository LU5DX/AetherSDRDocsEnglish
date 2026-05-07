# Troubleshoot WAN UDP registration timeouts

When connecting over WAN, AetherSDR sends a UDP registration datagram to the radio and retries every 50 ms until the radio confirms receipt. Once confirmed, it switches to a 5-second ping keepalive to hold the NAT mapping open. If registration never completes, the panadapter stream will not start.

## Before you start

- Confirm you have a working internet connection and that the radio's WAN address and port are correctly configured in your connection profile.
- Ensure no local firewall or NAT device is blocking outbound UDP traffic on the radio's control port.

## Steps

1. Open the connection log (View > Connection Log) and check for repeated `client udp_register` entries without a corresponding acknowledgement. If you see them, the radio is not responding to the registration datagrams.
2. Verify that your router is not blocking or rate-limiting outbound UDP. The registration datagrams are sent to the radio's configured port, and the keepalive pings are sent every 5 seconds to maintain the NAT mapping. If the NAT entry expires between pings, registration will appear to succeed but the stream will silently drop.
3. Check the Tx byte counter in the diagnostics panel. Each registration attempt and each keepalive ping increments the counter. If the counter is not increasing, the socket is not sending — rebind the connection (disconnect, then reconnect) to force a new ephemeral port assignment.
4. If the counter increases but registration still times out, the radio may be discarding the datagrams. Confirm the radio firmware is at the version required by your AetherSDR release and that no other client holds an active WAN session to the same radio.

## Tips

- The 50 ms retry interval means a single second of connectivity produces roughly 20 registration attempts. If the log shows fewer attempts than expected, a local firewall is likely dropping outbound packets before they leave the host.
- The 5-second keepalive is the minimum interval needed to hold most consumer NAT mappings open. If your router has an aggressive UDP timeout (under 30 seconds), contact your router vendor or increase the NAT idle timeout in the router's advanced settings.

## Related

- [Connect to a radio over WAN](connect-wan.md)
- [Configure UDP ports](configure-udp-ports.md)
- [Read connection diagnostics](connection-diagnostics.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
