# Monitor network quality while connected to a radio

The Network Quality Monitor tracks your connection health in real time using ping round-trip time, packet-loss percentage, and audio jitter. It assigns one of six quality levels and automatically disconnects a stale connection after five consecutive unanswered pings.

## Steps

1. Connect to a radio. The **Network Quality** indicator becomes active once a connection is established.
2. Read the **Network Quality** indicator to assess your current connection health. If the indicator shows **Poor**, audio quality is likely degraded. If it shows **Off**, no connection is active.

## What each control does

| Control | Behavior |
|---|---|
| **Network Quality** | Displays one of six states — **Off**, **Excellent**, **Very Good**, **Good**, **Fair**, or **Poor** — based on live measurement of ping RTT, packet loss, and audio jitter. Updates continuously while connected. **Off** means no connection is active. **Poor** means audio quality is likely degraded. |

## Tips

- If the indicator drops to **Poor**, check your network path for congestion or high latency before adjusting radio settings.
- On WAN (SmartLink) connections, a forced disconnect after five missed pings triggers automatic reconnection. AetherSDR refreshes your Auth0 credentials using the saved refresh token and re-establishes the radio link. If credential refresh fails, the retry loop stops and you are prompted to sign in again.
- The disconnect watchdog fires only once per outage, so you will not see repeated disconnect events for a single network failure.

## Related

- [Connect to a radio over WAN (SmartLink)](connect-wan-smartlink.md)
- [Troubleshoot audio quality](troubleshoot-audio-quality.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
