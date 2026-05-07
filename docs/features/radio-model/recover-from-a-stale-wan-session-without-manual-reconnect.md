# Recover from a stale WAN session without manual reconnect

AetherSDR's Network Quality Monitor detects a stale WAN (SmartLink) session automatically: after five consecutive unanswered pings it closes the TLS socket, clears all panadapters, slices, and streams, then starts a reconnect timer that refreshes your Auth0 credentials and re-establishes the radio link — no manual action required.

## Before you start

- You must have signed in with a SmartLink (WAN) connection at least once so a valid Auth0 refresh token is saved locally.
- Your internet connection must be capable of reaching the Auth0 authentication servers.

## Steps

1. Watch the **Network Quality** indicator in the main toolbar. When the session goes stale, the indicator transitions to **Off** briefly while the automatic teardown and cleanup occur.
2. Wait for the reconnect timer to complete. AetherSDR refreshes your credentials silently and restores the radio link. The **Network Quality** indicator will return to one of the active states (**Excellent**, **Very Good**, **Good**, **Fair**, or **Poor**) once the connection is re-established.
3. If the indicator remains **Off** and a sign-in-required message appears, your refresh token has expired or is invalid. Sign in again manually to restart the session.

## What each control does

| Control | Behavior |
|---|---|
| **Network Quality** — Off | Not connected. Shown during initial teardown of the stale session and while the reconnect timer is running. |
| **Network Quality** — Excellent | Connected. Ping RTT, packet loss, and audio jitter are all within optimal thresholds. |
| **Network Quality** — Very Good | Connected. Minor degradation in RTT, packet loss, or jitter; audio unaffected. |
| **Network Quality** — Good | Connected. Noticeable but acceptable degradation; audio quality is maintained. |
| **Network Quality** — Fair | Connected. Elevated RTT, packet loss, or jitter; audio may show minor artifacts. |
| **Network Quality** — Poor | Connected. Significant degradation across one or more metrics; audio quality is likely degraded. |

## Tips

- The ping watchdog fires exactly once per outage, so you will not see repeated disconnect/reconnect cycles from a single stale event.
- If you consistently see the session go stale and fail to reconnect automatically, check that your refresh token has not expired — sign out and sign back in to generate a fresh token.
- On LAN connections the automatic WAN reconnect timer does not apply; stale LAN sessions require a manual reconnect.

## Related

- [network-quality-monitor.md](network-quality-monitor.md)
- [smartlink-wan-setup.md](smartlink-wan-setup.md)
- [auth0-credentials.md](auth0-credentials.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
