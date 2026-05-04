# Diagnose WAN disconnect and ping-watchdog teardown

`PanadapterStream::startWanUdpRegister` maintains a WAN connection by sending UDP registration datagrams every 50 ms until the radio acknowledges, then switches to a 5-second ping keepalive to hold the NAT mapping open. When the connection drops or the watchdog tears down the session, the steps below help you identify where the failure occurred.

## Before you start

- Confirm you have access to the AetherSDR application log (debug logging must be enabled for the `lcVita49` category).
- Ensure you know whether the session was started in WAN mode or LAN mode — the bind behavior and log messages differ between the two.

## Steps

1. Open the application log and search for `PanadapterStream: LAN VITA UDP bind`. Confirm a line is present showing `addr=`, `port=`, `flags=DontShareAddress`, and `reason=`. If this line is absent, the UDP socket never bound and the session could not start.
2. If the bind line is present, search immediately after it for any `failed to bind UDP socket` warning. If found, note the error string — this indicates the OS rejected the bind before any registration attempt was made.
3. Search for `startWanUdpRegister` activity in the log. Verify the 50 ms registration datagrams appear and that a confirmation from the radio is logged. If the confirmation never appears, the radio did not acknowledge the client's UDP port — check NAT rules and firewall permissions for the ephemeral port shown in the bind line.
4. After confirmation, verify that 5-second ping keepalive entries appear at regular intervals. A gap longer than one ping interval indicates the NAT mapping may have expired or the radio became unreachable. Check the WAN path (router, ISP, VPN) for packet loss during that window.
5. If the session tears down, search for `rebindToEphemeralPort` or `routedPrimeTimer` stop events in the log. Their presence confirms the watchdog detected a dead connection and initiated teardown. Note the timestamp and correlate it with the last successful ping keepalive entry to measure how long the link was silent before teardown.

## What each control does

| Control | Behavior |
|---|---|
| Registration datagram (50 ms interval) | Sent immediately on WAN session start and repeated every 50 ms until the radio returns an acknowledgement confirming the client UDP port is registered. |
| Ping keepalive (5-second interval) | Replaces the registration loop after the radio acknowledges. Sends a lightweight datagram every 5 seconds to keep the NAT mapping alive. |
| `routedPrimeTimer` | Internal timer that drives the registration retry loop. Stopped when acknowledgement is received or when `rebindToEphemeralPort` is called during teardown. |
| UDP bind (`DontShareAddress`, OS-assigned port) | Binds the local VITA-49 socket to an OS-assigned ephemeral port on the resolved local address. The chosen address source (`explicit`, `probe-session`, `tcp-local`, or `auto`) is recorded in the log. |

## Tips

- The `reason=` field in the bind log line tells you which address-selection path was taken (`explicit` > `probe-session` > `tcp-local` > `auto`). If you see `auto`, no explicit or session address was resolved — verify the connection object provides a valid local address before the session starts.
- A WAN teardown with no preceding keepalive gap usually points to an abrupt radio reboot or a firewall rule dropping UDP silently. Compare radio-side logs against the client-side ping timestamps.
- Re-enabling the session after teardown triggers a fresh `startWanUdpRegister` cycle. Confirm a new bind line with a new port number appears; a repeated port from a previous session may indicate the socket was not fully closed before rebind.

## Related

- [wan-connection-setup.md](wan-connection-setup.md)
- [vita49-stream-diagnostics.md](vita49-stream-diagnostics.md)
- [panadapter-stream-overview.md](panadapter-stream-overview.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
