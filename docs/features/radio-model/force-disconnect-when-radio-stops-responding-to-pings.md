# Force disconnect when radio stops responding to pings

AetherSDR monitors your connection health in real time and automatically closes a stale connection after five consecutive unanswered pings, so a dead link is never left open indefinitely.

## Before you start

- You must be connected to a radio (local or WAN/SmartLink).
- No manual configuration is required — the ping watchdog runs automatically while connected.

## Steps

1. Connect to your radio normally. AetherSDR begins pinging the radio immediately and displays the current link quality in the **Network Quality** indicator.
2. If the radio stops responding, AetherSDR counts consecutive missed pings. After five unanswered pings it calls `forceDisconnect()` exactly once, closes the connection (TLS socket on WAN), and triggers the normal disconnection cleanup — panadapters, slices, and streams are cleared automatically.
3. **WAN (SmartLink) connections only:** After a forced disconnect, MainWindow starts a reconnect timer that refreshes your Auth0 credentials using the saved refresh token and re-establishes the radio link. If the credential refresh fails, the retry loop stops and a sign-in-required status is shown. Sign in again via the SmartLink login flow to resume.

## What each control does

| Control | Behavior |
|---|---|
| **Network Quality** | Displays the real-time connection health assessment. States: **Off** (not connected), **Excellent**, **Very Good**, **Good**, **Fair**, **Poor**. Poor means audio quality is likely degraded. Based on ping round-trip time, packet-loss percentage, and audio jitter. |

## Tips

- The watchdog fires exactly once per outage — you will not see duplicate disconnect events even if the radio remains unreachable.
- On WAN connections, keep your Auth0 refresh token valid. An expired token prevents automatic reconnection after a forced disconnect.
- Watch the **Network Quality** indicator drop toward **Poor** as a leading warning before a forced disconnect occurs.

## Related

- [network-quality-monitor.md](network-quality-monitor.md)
- [smartlink-wan-connection.md](smartlink-wan-connection.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
