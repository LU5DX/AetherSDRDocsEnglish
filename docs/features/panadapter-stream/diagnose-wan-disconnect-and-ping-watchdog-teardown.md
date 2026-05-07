# Diagnose WAN disconnect and ping-watchdog teardown

`PanadapterStream::startWanUdpRegister` registers the client's UDP port with the radio over WAN by sending registration datagrams every 50 ms until the radio confirms receipt, then switches to a 5-second ping keepalive to maintain the NAT connection. Use the steps below to determine whether a WAN disconnect is caused by a failed registration, a dropped keepalive, or a data-path error.

## Before you start

- Confirm you are connected to the radio over WAN (not LAN).
- Enable the `lcVita49` debug log category so ping-keepalive and registration events are visible in the application log output.

## Steps

1. Attempt or re-attempt a WAN connection. Watch the log for the message `PanadapterStream: WAN ping keepalive` followed by a `totalRx` byte count. If this line never appears, registration did not complete — the radio did not confirm the UDP port within the 50 ms retry window.
2. If registration appeared to succeed but the stream later dropped, check the `totalRx` value reported in successive `WAN ping keepalive` log lines. A `totalRx` value that stops increasing while the connection appears open indicates no data is arriving from the radio — the NAT mapping has likely expired or the radio stopped responding to pings.
3. Call `packetErrorCount()` and `packetTotalCount()` from the diagnostics interface (or read them from the network quality monitor). A rising error count relative to the total count points to packet loss on the WAN path rather than a keepalive failure.
4. For per-category breakdown, call `categoryStats(cat)` for each `StreamCategory`. The returned `bytes`, `packets`, and `errors` fields show whether loss is concentrated in a specific stream category (for example, meter data versus FFT frames).

## What each control does

| Control | Behavior |
|---|---|
| WAN registration timer (50 ms) | Fires every 50 ms after `startWanUdpRegister` is called; sends `client udp_register handle=0x<handle>` to the radio until the radio acknowledges. Stops when acknowledgement is received. |
| WAN ping keepalive timer (5 s) | Fires every 5 seconds after successful registration; sends `client ping handle=0x<handle>` to keep the NAT mapping alive. Each firing logs the current `totalRx` byte count. |
| `packetErrorCount()` | Returns the total error count across all owned streams. Used by the network quality monitor to surface packet-loss conditions. |
| `packetTotalCount()` | Returns the total packet count across all owned streams. Compare against `packetErrorCount()` to calculate an error rate. |
| `categoryStats(StreamCategory cat)` | Returns a `CategoryStats` struct (`bytes`, `packets`, `errors`) for the specified stream category. Returns a zeroed struct for an out-of-range category. |

## Tips

- If `totalRx` is zero in the first few keepalive log lines, the radio received the registration but no VITA-49 data has arrived yet — check firewall rules and NAT port-forwarding for the UDP port the client bound to.
- A `totalRx` value that is non-zero but frozen across multiple 5-second keepalive cycles means data flow stopped after an initial burst; force a reconnect rather than waiting for a timeout.
- `categoryStats` is safe to call from any thread; it acquires an internal mutex before reading.

## Related

- [panadapter-stream-overview.md](panadapter-stream-overview.md)
- [wan-connection-setup.md](wan-connection-setup.md)
- [network-quality-monitor.md](network-quality-monitor.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
