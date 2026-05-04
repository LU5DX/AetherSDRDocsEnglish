# Diagnose connection quality with ping RTT and packet-loss indicators

The Network Quality Monitor tracks your connection health in real time using ping round-trip time, packet-loss percentage, and audio jitter. It assigns one of six quality levels and automatically disconnects a stale connection after five consecutive unanswered pings.

## Steps

1. Connect to a radio (LAN or WAN/SmartLink). The **Network Quality** indicator appears in the status area once a connection is established.
2. Read the **Network Quality** indicator to assess current connection health. If the indicator shows **Poor**, expect degraded audio. If it shows **Off**, no connection is active.

## What each control does

| Control | Behavior |
|---|---|
| **Network Quality** | Displays a real-time quality level — **Off**, **Excellent**, **Very Good**, **Good**, **Fair**, or **Poor** — based on ping RTT, packet-loss percentage, and audio jitter. **Off** means not connected. **Poor** means audio quality is likely degraded. After five consecutive unanswered pings the software forces a disconnect so a stale connection is never left open. On WAN (SmartLink) connections, disconnect triggers normal cleanup of panadapters, slices, and streams, then starts a reconnect timer that refreshes Auth0 credentials automatically. If the credential refresh fails, the retry loop stops and a sign-in-required status is shown. |

## Tips

- Watch the indicator during a session — a drop from **Good** to **Fair** or **Poor** can indicate transient network congestion before audio artifacts become obvious.
- On WAN connections, an automatic reconnect attempt runs after a forced disconnect. If **Network Quality** stays **Off** after the retry, check your internet connection or sign in again if prompted.
- The ping watchdog fires once per outage, not once per second, so a single disconnect event in the log corresponds to exactly one lost-connection condition.

## Related

- [Connect over WAN with SmartLink](connect-wan-smartlink.md)
- [Troubleshoot audio issues](troubleshoot-audio.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
