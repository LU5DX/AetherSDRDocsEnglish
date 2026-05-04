# Force disconnect when radio stops responding to pings

AetherSDR monitors connection health in real time and automatically closes a stale connection after five consecutive unanswered pings, ensuring a dead radio link is never left open indefinitely.

## What each control does

| Control | Behavior |
|---|---|
| **Network Quality** — Off | Not connected. |
| **Network Quality** — Excellent | Ping RTT, packet loss, and audio jitter are all within ideal thresholds. |
| **Network Quality** — Very Good | Minor degradation; audio is unaffected. |
| **Network Quality** — Good | Moderate degradation; audio is unaffected. |
| **Network Quality** — Fair | Noticeable degradation; audio may be marginally affected. |
| **Network Quality** — Poor | Significant degradation; audio quality is likely degraded. |

## How the forced disconnect works

1. Watch the **Network Quality** indicator in the main toolbar. If the radio stops responding to pings, the indicator moves toward **Poor** and then drops to **Off** once five consecutive pings go unanswered.
2. AetherSDR fires the disconnect exactly once per outage — duplicate teardowns are prevented automatically. On a WAN (SmartLink) connection, the TLS socket is closed and all panadapters, slices, and streams are cleared through the normal cleanup path.
3. After a WAN forced disconnect, AetherSDR starts a reconnect timer automatically. It refreshes your Auth0 credentials using the saved refresh token and re-establishes the radio link. If the credential refresh fails, the retry loop stops and a sign-in-required status is shown — sign in again to reconnect.

## Tips

- A **Poor** reading is an early warning that a forced disconnect may be imminent; check your network path before the link drops entirely.
- On LAN connections the disconnect and cleanup happen immediately with no reconnect attempt — restart the connection manually from the radio list.
- If the sign-in-required status appears after a WAN outage, use File > Sign In to refresh your credentials and reconnect.

## Related

- [network-quality-monitor.md](network-quality-monitor.md)
- [wan-smartlink-connection.md](wan-smartlink-connection.md)
- [auth0-credentials.md](auth0-credentials.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
