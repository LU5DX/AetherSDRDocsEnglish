# Recover from a dropped WAN connection via auto-reconnect

`RadioConnection` manages the TCP control connection to the radio over LAN or WAN and coordinates UDP stream registration so data flows to the correct client port. When a WAN connection drops, the auto-reconnect mechanism re-establishes the TCP session and re-registers your UDP streams without manual intervention.

## Before you start

- Confirm the radio is reachable over the WAN (ping or equivalent).
- Ensure your AetherSDR client is running V0.9.5.1 or later, which includes improved disconnect sequencing and socket-error state recovery.

## Steps

1. Do nothing — when the TCP control connection drops, `RadioConnection` detects the socket error, transitions the connection state to `Disconnected`, and emits `errorOccurred` to signal the failure.
2. The auto-reconnect logic picks up the `Disconnected` state and initiates a new TCP connection to the radio's WAN address. UDP stream registration (`client udpport <port>`) is re-issued automatically once the TCP session is confirmed.
3. If the reconnect attempt finds that your previous UDP port/IP pair is already registered by another client, `RadioConnection` calls `rebindToEphemeralPort` to obtain a new OS-assigned UDP port before re-registering with the radio.
4. Monitor the connection state in the status area of the UI. A return to the **Connected** state confirms the session is fully restored.

## What each control does

| Control | Behavior |
|---|---|
| Auto-reconnect | Watches for `ConnectionState::Disconnected` (including after a socket error) and re-initiates the TCP handshake to the configured WAN address. |
| Ephemeral port rebind | If the radio rejects the previously used UDP port/IP pair as already registered, binds a new OS-assigned local UDP port and re-registers it via `client udpport`. |
| Graceful disconnect (on clean shutdown) | Sends a `stream remove` command and waits for acknowledgement (up to 2 s) before closing TCP, preventing stale session entries on the radio that could block reconnection. |
| Heartbeat | Sends a keepalive every 30 s. A missed heartbeat is one signal that the WAN connection has dropped and reconnect should be triggered. |

## Tips

- If reconnection succeeds but audio or panadapter data does not resume, the radio may still hold a stale UDP registration from the previous session. Disconnect cleanly using **File > Disconnect** and reconnect again so the full teardown sequence (stream remove → client disconnect) runs and clears the radio's session table.
- Check the application log for the `RadioConnection: disconnect summary` line (emitted at `INFO` level). The `streamAck` field tells you whether the previous session was torn down cleanly; `streamAck=no` on repeated attempts points to a WAN latency or firewall issue affecting the teardown handshake.

## Related

- [lan-connection-setup.md](lan-connection-setup.md)
- [udp-stream-registration.md](udp-stream-registration.md)
- [multi-nic-bind-address.md](multi-nic-bind-address.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
