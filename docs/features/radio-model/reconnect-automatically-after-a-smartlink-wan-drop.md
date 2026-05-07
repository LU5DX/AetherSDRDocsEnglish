# Reconnect automatically after a SmartLink WAN drop

AetherSDR monitors your SmartLink (WAN) connection in real time and, after five consecutive unanswered pings, automatically closes the stale connection and attempts to reconnect using your saved Auth0 credentials — no manual intervention required.

## Before you start

- You must have signed in to SmartLink at least once so that a refresh token is stored locally.
- Your machine must have internet access when the reconnect attempt fires.

## Steps

1. Watch the **Network Quality** indicator in the main toolbar. If the connection drops, it transitions to **Off** while AetherSDR tears down all panadapters, slices, and streams.
2. AetherSDR automatically refreshes your Auth0 credentials using the saved refresh token and re-establishes the radio link. No action is needed on your part unless the indicator shows a sign-in-required status (see Tips).

## What each control does

| Control | Behavior |
|---|---|
| **Network Quality** | Displays real-time connection health. **Off** — not connected. **Excellent** through **Poor** — assessed from ping round-trip time, packet loss, and audio jitter. **Poor** means audio quality is likely degraded. After five consecutive unanswered pings the watchdog fires once, closes the TLS socket, and starts the reconnect sequence. |

## Tips

- If **Network Quality** stays **Off** and a sign-in-required status appears, the Auth0 token refresh failed. Open the SmartLink sign-in screen, enter your credentials, and connect manually to reset the token.
- A **Poor** rating does not trigger a disconnect on its own — only five consecutive unanswered pings do. If audio is degraded but the connection stays open, check your WAN link quality.
- The ping watchdog fires exactly once per outage, so you will not see duplicate teardown events in the log.

## Related

- [smartlink-connect.md](smartlink-connect.md)
- [network-quality-monitor.md](network-quality-monitor.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
