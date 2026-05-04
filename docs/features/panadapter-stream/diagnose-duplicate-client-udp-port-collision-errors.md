# Diagnose duplicate-client UDP port collision errors

When two AetherSDR clients on the same host request the same UDP port, the radio rejects the initially chosen port. `PanadapterStream::rebindToEphemeralPort` recovers automatically by releasing the conflicting port, asking the OS to assign a new ephemeral port, and re-registering the stream with the radio.

## Before you start

- Run AetherSDR 0.9.5.1 or later.
- Have access to the application log output (console or log file) so you can confirm the port the OS assigns.

## Steps

1. Attempt to connect to the radio as normal. If a port collision occurs, AetherSDR detects the rejection and calls `rebindToEphemeralPort` automatically — no manual action is required.
2. Open the application log and search for the string `LAN VITA UDP bind`. Confirm the log entry shows `port=<number>` with a non-zero OS-assigned port and `flags=DontShareAddress`. This confirms the rebind succeeded and the stream is active on the new port.
3. If the log instead shows `failed to bind UDP socket`, note the error string that follows and check the steps under **Tips** below.

## What each control does

| Control | Behavior |
|---|---|
| `rebindToEphemeralPort` | Stops the routed-prime timer, closes the existing UDP socket binding, requests a new OS-assigned (ephemeral) port using `DontShareAddress` mode, logs the new address and port, and re-registers the data stream with the radio. |
| Bind address selection | Chooses the local IPv4 address in priority order: explicit override → probe-session address → TCP connection local address → any IPv4. |
| `DontShareAddress` flag | Prevents other sockets from sharing the port, which is the root cause of the original collision. |

## Tips

- If rebinding fails repeatedly, another process outside AetherSDR may be holding ports in the ephemeral range. Run `netstat -anup` (Linux) or `netstat -ano` (Windows) to identify the conflicting process and stop it.
- The log entry `reason=explicit` means an explicit local bind address is configured on the connection object. If you see an unexpected address, check your `RadioConnection` configuration for a hardcoded `explicitLocalBindAddress`.
- Running more than one AetherSDR instance against the same radio is supported; each instance will land on a different OS-assigned port after the automatic rebind.

## Related

- [panadapter-stream.md](panadapter-stream.md)
- [radio-connection.md](radio-connection.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
