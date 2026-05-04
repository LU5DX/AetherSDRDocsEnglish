# Recover from a stale WAN session without manual reconnect

AetherSDR automatically detects a stale WAN (SmartLink) session by sending periodic pings and forcing a clean disconnect after five consecutive unanswered pings, then immediately starts a reconnect sequence using your saved Auth0 credentials — no manual intervention required.

## Before you start

- You must have signed in to SmartLink at least once so a valid refresh token is saved on your device.
- Ensure your internet connection is active; the automatic retry cannot succeed without network access.

## Steps

1. Watch the **Network Quality** indicator. When a stale session is detected, it drops to **Off** as the connection is torn down.
2. Wait. AetherSDR closes the TLS socket, clears all panadapters, slices, and streams, then starts a reconnect timer that refreshes your Auth0 credentials and re-establishes the radio link automatically.
3. The **Network Quality** indicator returns to **Excellent**, **Very Good**, **Good**, **Fair**, or **Poor** once the session is restored. No further action is needed.

> **If the indicator stays Off and a sign-in-required status appears**, your saved refresh token has expired or is invalid. Open the SmartLink sign-in screen and authenticate again to restart the automatic retry loop.

## What each control does

| Control | Behavior |
|---|---|
| **Network Quality** | Displays real-time connection health based on ping round-trip time, packet-loss percentage, and audio jitter. Shows **Off** when not connected. Transitions through **Excellent**, **Very Good**, **Good**, **Fair**, and **Poor** as conditions change. **Poor** indicates likely audio degradation. After five consecutive unanswered pings the watchdog fires once, forces a disconnect, and triggers the WAN reconnect sequence. |

## Tips

- The ping watchdog fires exactly once per outage, not once per second, so you will not see repeated disconnect events for a single stale session.
- If your environment has a firewall that blocks ICMP, pings will always go unanswered and the watchdog will disconnect the session every cycle. Confirm that ping traffic is permitted to the radio's SmartLink endpoint.
- Auth-refresh failure stops the retry loop immediately. If automatic reconnect does not succeed, check that your device's system clock is correct, as a skewed clock can cause Auth0 token validation to fail.

## Related

- [monitor-network-quality.md](monitor-network-quality.md)
- [smartlink-sign-in.md](smartlink-sign-in.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
