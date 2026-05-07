# Diagnose radio disconnect and reconnect failures

`RadioConnection` manages the TCP control connection to your radio (LAN or WAN) and coordinates UDP stream registration so data flows to the correct client port. Use these steps when the radio disconnects unexpectedly or fails to reconnect.

## Before you start

- Confirm the radio is powered on and reachable on the network (ping the radio's IP address from your machine).
- Note whether the failure is LAN or WAN — the diagnostic steps are the same, but firewall and port-forwarding rules differ for WAN connections.

## Steps

1. Open the connection panel and attempt to connect to the radio. Watch the status indicator for the point at which the connection attempt stops or drops.
2. Open **View > Network Diagnostics** to review the connection history logged by `NetworkDiagnosticsHistory`. Check the log for TCP handshake failures, UDP stream registration errors, and the timestamps of any disconnect events.
3. Check the packet error and total packet counts in the diagnostics view. A rising error count relative to total packets points to a network quality problem rather than a configuration problem.
4. If the connection drops after establishing successfully, compare `totalRxBytes` and `totalTxBytes` in the diagnostics view. A value that stops incrementing while the other continues indicates a one-way stream failure, which usually means a UDP port is blocked or the client port changed.
5. Disconnect, wait 10 seconds, then reconnect. If the reconnect succeeds, the previous session left a stale UDP registration on the radio. No further action is needed.
6. If reconnect still fails, verify that no firewall rule is blocking the TCP control port or the UDP stream port reported in the diagnostics log, then retry.

## What each control does

| Control | Behavior |
|---|---|
| Network Diagnostics view | Displays per-session connection history recorded by `NetworkDiagnosticsHistory`, including TCP connect/disconnect events and UDP stream registration results. |
| Packet error count | Running total of malformed or lost UDP packets across all streams. Use this to distinguish network degradation from a hard disconnect. |
| Total RX bytes | Cumulative bytes received over the UDP stream. Stops incrementing when inbound data is no longer arriving. |
| Total TX bytes | Cumulative bytes sent to the radio. Stops incrementing when outbound data is blocked. |
| Audio packet gap (ms) | Milliseconds between the two most recent audio packets. A large or growing value indicates jitter or packet loss on the audio stream. |
| Audio packet gap max (ms) | Largest audio packet gap observed in the current session. Useful for spotting intermittent network issues that have since recovered. |
| Audio packet jitter (ms) | Variation in audio packet arrival intervals. High jitter with low error count suggests router QoS or buffering problems. |

## Tips

- WAN connections require port forwarding for both the TCP control port and the UDP stream port. If only the TCP connection works, check that the UDP port is forwarded to the same host.
- Stale registrations are more common after an ungraceful shutdown (crash or power loss). Always use the disconnect button before closing the application when possible.
- If diagnostics show healthy packet counts but audio is silent, confirm the client UDP port has not changed — `RadioConnection` must re-register the stream when the local port changes.

## Related

- [Connect to a radio over LAN](connect-lan.md)
- [Connect to a radio over WAN](connect-wan.md)
- [Monitor network stream quality](network-stream-quality.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
