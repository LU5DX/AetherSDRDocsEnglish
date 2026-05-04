# Troubleshoot Multi-Flex UDP port conflicts

When multiple clients share a LAN, a second client attempting to connect may fail because the default UDP port is already held by the first client. The UDP Port Registration Policy detects this condition and retries the registration on a different port so the connection can proceed.

## Before you start

- Confirm that two or more AetherSDR clients are (or recently were) connected to the same radio on the same local network.
- Confirm you are running AetherSDR v0.9.5.1 or later.

## Steps

1. Attempt to connect to the radio as normal. If the connection stalls, AetherSDR automatically invokes the UDP Port Registration Policy to retry with an alternate port. No manual action is required for the retry itself.
2. If the connection remains stuck after the automatic retry, disconnect any other clients sharing the radio, then reconnect. The policy will succeed once the conflicting client releases the port.

## What each control does

| Control | Behavior |
|---|---|
| UDP Port Registration Policy | Monitors UDP port registration responses on LAN connections. If registration fails because another client already holds the default port, the policy selects an alternate port and retries the registration automatically. |

## Tips

- Only LAN connections are affected. Direct USB or WAN connections do not go through UDP port registration and will not encounter this conflict.
- If conflicts recur, check whether a previous AetherSDR session exited without cleanly disconnecting. A stale session can hold a port until the radio times it out (typically 30–60 seconds). Wait, then retry.
- To confirm the policy acted, check the application log for a message indicating a UDP port retry was attempted.

## Related

- [Connect to a radio over LAN](connect-lan.md)
- [Manage multiple simultaneous clients](multi-client.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
