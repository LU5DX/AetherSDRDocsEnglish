# Set a session-probed local bind address for multi-NIC routing

`RadioConnection` supports three tiers of local bind address selection for UDP streams. The session-probed tier (added in V0.9.5.1) sits between explicit and automatic: it reads the OS-observed source address of the established TCP control session and reuses that address when binding the UDP stream. Use this approach on multi-NIC hosts where the correct outbound interface is not known until the TCP connection is made.

## Before you start

- Your host must have more than one network interface (or a non-default routing table) that could cause UDP and TCP traffic to leave on different interfaces.
- The TCP control connection to the radio must be fully established before the bind address is probed.
- You must know which `RadioConnection` instance governs the session you want to configure.

## Steps

1. Establish the TCP control connection to the radio normally (LAN or WAN) using `RadioConnection`. Wait until the connection state reaches `Connected`.
2. After the TCP session is up, call `RadioConnection::localSessionAddress()` (or the equivalent property exposed by your binding) to retrieve the OS-observed source address of that TCP socket.
3. Pass the returned address as the `localBindAddress` argument when calling `PanadapterStream::start(conn)`. `RadioConnection` will use that address to bind the UDP port, keeping UDP and TCP on the same interface.
4. If the radio rejects the selected port/IP pair as already registered by another client, call `PanadapterStream::rebindToEphemeralPort(conn)` to fall back to an OS-assigned UDP port on the same address.

## What each control does

| Control | Behavior |
|---|---|
| Explicit bind address | A hard-coded local IP you supply before connecting. Highest priority. |
| Session-probed bind address | The source IP the OS assigned to the TCP control socket. Probed after `Connected` state is reached. Used when no explicit address is set. |
| Automatic (OS-assigned) bind address | Let the OS pick the interface and port freely. Used when neither explicit nor session-probed address is available, or after a call to `rebindToEphemeralPort`. |
| `rebindToEphemeralPort(conn)` | Releases the current UDP socket and rebinds to an OS-assigned port. Called automatically when the radio rejects the initial port/IP pair as already in use by another client. |

## Tips

- On a host with a VPN interface and a LAN interface, the session-probed tier prevents the UDP stream from routing over the VPN when the TCP session went over LAN, without requiring you to hard-code the LAN IP.
- If `localSessionAddress()` returns `0.0.0.0` or an unexpected loopback address, the TCP connection was routed by a proxy or local relay. Fall back to an explicit bind address in that case.
- The probed address is only valid for the lifetime of the current TCP session. Re-probe after any reconnect.

## Related

- [Connect to a radio over LAN](connect-lan.md)
- [Connect to a radio over WAN](connect-wan.md)
- [Configure UDP stream registration](udp-stream-registration.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
