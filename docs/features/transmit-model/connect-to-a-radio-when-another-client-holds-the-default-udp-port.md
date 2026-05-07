# Connect to a radio when another client holds the default UDP port

When you try to connect to a radio over a LAN and another client already holds the default UDP port, AetherSDR's UDP Port Registration Policy can automatically retry the connection on a different port instead of leaving the connection stuck.

## Before you start

- You must be connecting over a LAN (not WAN/internet) connection.
- Confirm that at least one other client is already connected to the radio and occupying the default UDP port.

## Steps

1. Attempt to connect to the radio as normal. If the default UDP port is already taken, the UDP Port Registration Policy detects the failed registration automatically.
2. AetherSDR retries the UDP port registration using an alternate port number. No additional action is required — the connection proceeds on the new port once a free one is found.

## What each control does

| Control | Behavior |
|---|---|
| UDP Port Registration Policy | Monitors the result of each UDP port registration attempt on a LAN connection. If registration fails because another client holds the port, it retries with a different port number rather than leaving the connection in a stuck state. |

## Tips

- This retry behavior applies to LAN connections only. WAN connections use a different connection path and are not affected.
- If the connection still fails after retries, check that the radio is reachable on the network and that no firewall is blocking the alternate UDP ports.

## Related

- [Connect to a radio](connect-to-radio.md)
- [LAN vs WAN connection modes](lan-wan-connection-modes.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
