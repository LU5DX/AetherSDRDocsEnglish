# Understand why slices and panadapters clear after a WAN disconnect

When AetherSDR loses a WAN (SmartLink) connection, it deliberately clears all panadapters, slices, and streams as part of a controlled teardown so stale data is never displayed.

## How the disconnect sequence works

1. The **Network Quality Monitor** sends a ping to the radio once per second over the WAN link. If five consecutive pings receive no reply, it calls `forceDisconnect()` exactly once — the watchdog fires only once per outage to prevent duplicate teardowns.
2. `forceDisconnect()` closes the TLS socket and triggers the normal `onDisconnected()` cleanup path. That path removes all panadapters, slices, and audio/IQ streams — the same cleanup that runs on any intentional disconnect.
3. After cleanup, MainWindow starts a WAN reconnect timer. It attempts to refresh Auth0 credentials using the saved refresh token and then re-establishes the radio link automatically.
4. If the Auth0 credential refresh fails, the retry loop stops and the UI shows a sign-in-required status. Sign in again to restore the connection.

## What the Network Quality indicator shows

| Control | Behavior |
|---|---|
| **Network Quality** — Off | Not connected. |
| **Network Quality** — Excellent | Ping RTT, packet loss, and audio jitter are all within optimal thresholds. |
| **Network Quality** — Very Good | Minor degradation; audio is unaffected. |
| **Network Quality** — Good | Noticeable degradation; audio is generally unaffected. |
| **Network Quality** — Fair | Moderate degradation; occasional audio artifacts possible. |
| **Network Quality** — Poor | Significant degradation; audio quality is likely impacted. |

The indicator drops to **Off** as soon as the disconnect fires, confirming the teardown has occurred.

## Tips

- Panadapters and slices reappear automatically after a successful reconnect — you do not need to recreate them manually.
- If the indicator stays **Off** and no reconnect occurs, check that your Auth0 session is still valid. The retry loop stops on auth failure and will not reconnect until you sign in again.
- A single missed ping does not trigger a disconnect; five consecutive unanswered pings are required, so brief network hiccups do not cause unnecessary teardowns.

## Related

- [network-quality-monitor.md](network-quality-monitor.md)
- [wan-smartlink-setup.md](wan-smartlink-setup.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
