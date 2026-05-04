# Reconnect automatically after a SmartLink WAN drop

AetherSDK monitors your SmartLink (WAN) connection in real time and, after five consecutive unanswered pings, closes the stale TLS socket and automatically attempts to re-establish the radio link using your saved Auth0 credentials.

## Before you start

- You must have signed in at least once so that a valid Auth0 refresh token is stored on your machine.
- If the refresh token has expired or is missing, the retry loop stops and you will see a sign-in-required status. Sign in again before proceeding.

## Steps

1. Do nothing — reconnection is automatic. When the Network Quality indicator drops to **Poor** and then five consecutive pings go unanswered, AetherSDK closes the connection, clears all panadapters, slices, and streams, and starts a WAN reconnect timer.
2. Watch the **Network Quality** indicator. Once the retry succeeds, the indicator returns to **Excellent**, **Very Good**, **Good**, or **Fair** and audio resumes.

## What each control does

| Control | Behavior |
|---|---|
| **Network Quality** | Displays the real-time connection health assessed from ping round-trip time, packet-loss percentage, and audio jitter. Possible states: **Off** (not connected), **Excellent**, **Very Good**, **Good**, **Fair**, **Poor** (audio quality likely degraded). After five consecutive unanswered pings the watchdog triggers exactly once, closes the WAN socket, and starts the reconnect sequence. |

## Tips

- If reconnection keeps failing, check that your Auth0 refresh token is still valid by signing out and signing back in — this stores a fresh token for future automatic reconnects.
- A persistent **Poor** reading before a full drop means your WAN link is degraded; consider switching to a better network before the watchdog fires.
- The ping watchdog fires only once per outage, so you will never see duplicate teardowns or double-reconnect attempts in the same drop event.

## Related

- [network-quality-monitor.md](network-quality-monitor.md)
- [smartlink-wan-setup.md](smartlink-wan-setup.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
