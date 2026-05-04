# Diagnose radio disconnect and reconnect failures

`RadioConnection` manages the TCP control connection to the radio and coordinates UDP stream registration. When disconnect or reconnect attempts fail, the radio's session table can become stale, blocking future connections.

## Before you start

- Confirm the radio is reachable on the network (LAN or WAN).
- Note whether you are using a multi-NIC machine, as local bind address selection affects which interface is used.
- Have the AetherSDR application log accessible (enable the `lcConnection` log category if not already active).

## Steps

1. Attempt to connect to the radio normally. If the connection fails or drops, open the application log and locate the `RadioConnection: disconnect summary` entry. It contains the following fields:

   | Field | What it tells you |
   |---|---|
   | `handle` | The hex client handle used for this session. |
   | `streamId` | The stream that was being removed on teardown (`<none>` if no stream was active). |
   | `streamSeq` | The command sequence number sent for stream removal. |
   | `streamAck` | Whether the radio acknowledged the stream remove command (`yes` or `no`). |
   | `streamMs` | Milliseconds spent waiting for the stream remove acknowledgement. |
   | `closeMs` | Milliseconds spent closing the TCP socket. |
   | `totalMs` | Total disconnect duration in milliseconds. |

2. Use the log fields to identify the failure mode:

   - **`streamAck: no`** — The radio did not acknowledge the stream remove command within 2000 ms. The radio's session table may be stale. Wait 30–60 seconds before reconnecting so the radio can expire the previous session, then retry.
   - **`streamAck: yes` but reconnect still fails** — The TCP close took too long (`closeMs` is high). Check for network congestion or firewall rules blocking the TCP teardown on the control port.
   - **Socket error followed by `Disconnected` state** — The connection dropped unexpectedly. The log line `RadioConnection: socket error:` immediately before the disconnect summary contains the error string. Resolve the underlying network error before retrying.
   - **UDP stream not flowing after reconnect** — The previous port/IP pair may have been rejected as already registered. The SDK will attempt to rebind to an OS-assigned ephemeral UDP port automatically. If data still does not flow, restart the application to release the port reservation on the radio side.

## Tips

- If reconnect failures are intermittent on a multi-NIC machine, ensure the correct bind address is configured. Automatic local bind address selection may choose a different interface on each attempt, causing the radio to see requests from different source IPs.
- A `streamMs` value close to 2000 ms consistently indicates the radio is slow to process teardown. Avoid rapid disconnect/reconnect cycles in this case.
- On Linux, TCP keepalive options are applied automatically. If `closeMs` is consistently high, verify that no firewall is silently dropping FIN packets on the radio's control port.

## Related

- [connect-to-radio.md](connect-to-radio.md)
- [panadapter-stream-troubleshooting.md](panadapter-stream-troubleshooting.md)
- [multi-nic-bind-address.md](multi-nic-bind-address.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
