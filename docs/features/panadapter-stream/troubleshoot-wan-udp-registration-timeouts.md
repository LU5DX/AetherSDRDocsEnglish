# Troubleshoot WAN UDP registration timeouts

When connecting over WAN, AetherSDR sends a UDP registration datagram to the radio immediately, then repeats every 50 ms until the radio confirms receipt. Once confirmed, it switches to a 5-second ping keepalive to hold the NAT mapping open. If the radio never confirms, the registration loop stalls and no panadapter data arrives.

## Before you start

- Confirm your radio is reachable over TCP (the main control connection must be established before UDP registration begins).
- Know whether you are connecting over a VPN, a routed network, or a direct WAN path, as this affects which local bind address AetherSDR selects.

## Steps

1. Open the application log (Help > Diagnostic Log) and search for `PanadapterStream`. Confirm you see a line containing `LAN VITA UDP bind` with a non-zero port. If the line is absent or shows a bind failure, proceed to step 2.
2. If the bind failed, go to Settings > Radio Connection and set **Local Bind Address** to the explicit IPv4 address of the network interface facing the radio. This forces AetherSDR to use that address instead of relying on automatic detection. Restart the connection after saving.
3. If the bind succeeded but registration still times out (no panadapter data after 10–15 seconds), check that your firewall or NAT device allows inbound UDP on the port shown in the log line (`port=XXXXX`). The port is now assigned by the OS (ephemeral), so a fixed port rule such as 4991 is no longer sufficient.
4. If you are behind a NAT that drops idle UDP mappings in under 5 seconds, the keepalive ping interval may not be short enough to maintain the mapping. In this case, configure your router to extend the UDP timeout to at least 10 seconds, or enable a UDP keepalive/pinhole rule for the radio's public IP.

## What each control does

| Control | Behavior |
|---|---|
| Local Bind Address | Overrides automatic bind-address selection. When set, AetherSDR binds the UDP socket to this specific IPv4 address (`explicit` mode) instead of using the probe-session or TCP-local address. Leave blank for automatic selection. |
| WAN / LAN mode toggle | Switches the stream between LAN (VITA-49 direct) and WAN (registration + keepalive) paths. The registration retry loop (every 50 ms) and the 5-second ping keepalive only activate in WAN mode. |

## Tips

- The bind address selection priority is: **explicit** (user-set) → **probe-session** (from a pre-connection probe) → **tcp-local** (local side of the TCP control socket) → `0.0.0.0` (OS choice). If automatic selection picks the wrong interface on a multi-homed machine, set Local Bind Address explicitly.
- Each new connection attempt binds to an OS-assigned (ephemeral) port. If you have firewall rules that previously referenced port 4991, those rules no longer apply and must be updated to allow the dynamic port or the radio's IP without a port restriction.
- Use the diagnostic log `lcVita49` category to capture full bind and registration events.

## Related

- [configure-wan-connection.md](configure-wan-connection.md)
- [panadapter-stream-overview.md](panadapter-stream-overview.md)
- [network-firewall-requirements.md](network-firewall-requirements.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
