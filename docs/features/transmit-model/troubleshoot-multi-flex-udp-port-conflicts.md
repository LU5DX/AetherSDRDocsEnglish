# Troubleshoot Multi-Flex UDP port conflicts

When multiple clients share a LAN and one already holds the default UDP port, AetherSDR's UDP Port Registration Policy can automatically retry with a different port number instead of leaving the connection stuck.

## Before you start

- Confirm you are using a LAN (not WAN) connection. The retry policy applies to LAN connections only.
- Identify whether another client instance is already connected to the same radio on the same network segment.

## Steps

1. Attempt to connect to the radio as normal. If the default UDP port is already held by another client, the UDP Port Registration Policy detects the failed registration automatically.
2. Wait for the automatic retry. AetherSDR reattempts registration using a different port number. No manual intervention is required if the policy is active.
3. If the connection remains stuck after the retry, check that no firewall rule is blocking the fallback port range, then disconnect and reconnect to trigger a fresh registration attempt.

## What each control does

| Control | Behavior |
|---|---|
| UDP Port Registration Policy | Monitors UDP port registration on LAN connections. When a registration failure is detected — typically because another client already holds the default port — it retries registration with an alternative port number, preventing a stuck connection. |

## Tips

- If you regularly run more than one client against the same radio, assign each client a distinct default UDP port in its settings to avoid relying on the automatic retry.
- The retry policy is LAN-specific. WAN connections use a separate port negotiation path and are not affected by this policy.

## Related

- [Connect to a radio over LAN](connect-lan.md)
- [Connect multiple clients to the same radio](multi-client.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
