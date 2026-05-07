# Recover from a dropped WAN connection via auto-reconnect

`RadioConnection` manages the TCP control connection to the radio over LAN or WAN and coordinates UDP stream registration so data flows to the correct client port. When a WAN connection drops, the auto-reconnect mechanism re-establishes the TCP link and re-registers all UDP streams automatically.

## Before you start

- Confirm the radio is reachable at the configured WAN address and port before relying on auto-reconnect.
- Ensure no firewall rule change has blocked the TCP control port or the UDP stream ports since the last successful connection.

## Steps

1. Open the **Connection** panel and verify the radio entry shows a WAN address (not a LAN/local address). If the connection status indicator shows disconnected, do not close the application — `RadioConnection` will attempt to reconnect on its own.
2. Wait for the reconnect cycle to complete. The status indicator returns to connected and the panadapter stream resumes automatically once the TCP handshake succeeds and UDP stream registration is re-sent to the correct client port.
3. If the connection does not recover after several cycles, select the radio entry and click **Disconnect**, then click **Connect** to force a clean reconnection attempt.

## What each control does

| Control | Behavior |
|---|---|
| Connection status indicator | Shows the current TCP link state: connecting, connected, or disconnected. Updates automatically as `RadioConnection` progresses through reconnect attempts. |
| **Disconnect** button | Tears down the TCP control connection and halts UDP stream registration immediately. |
| **Connect** button | Initiates a new TCP control connection to the configured address and port, then re-registers UDP streams once the link is established. |

## Tips

- Auto-reconnect runs silently in the background. You do not need to interact with the UI unless the indicator stays disconnected for an unusually long time (more than a few minutes).
- If you are behind NAT, confirm the WAN port forwarding rules are still active after a router reboot — `RadioConnection` cannot reconnect if the port mapping has expired.
- A brief audio or panadapter gap is expected during the reconnect window while UDP stream registration is re-sent.

## Related

- [connect-to-radio.md](connect-to-radio.md)
- [udp-stream-registration.md](udp-stream-registration.md)
- [network-diagnostics.md](network-diagnostics.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
