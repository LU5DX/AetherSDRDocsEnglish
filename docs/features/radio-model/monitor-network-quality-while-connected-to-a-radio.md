# Monitor network quality while connected to a radio

The Network Quality Monitor tracks your connection health in real time using ping round-trip time, packet loss, and audio jitter. It assigns one of six quality levels and automatically disconnects a stale connection after five consecutive unanswered pings.

## Before you start

- Establish a connection to a radio (local or WAN/SmartLink).

## Steps

1. Look at the **Network Quality** indicator in the main window while connected to a radio.
2. Read the current quality level. If the indicator shows **Poor**, audio quality is likely degraded. If it shows **Off**, no connection is active.

## What each control does

| Control | Behavior |
|---|---|
| **Network Quality** — Off | No connection is active. |
| **Network Quality** — Excellent | Connection health is optimal; ping RTT, packet loss, and audio jitter are all very low. |
| **Network Quality** — Very Good | Connection health is high with minimal degradation. |
| **Network Quality** — Good | Connection health is acceptable; minor RTT or jitter may be present. |
| **Network Quality** — Fair | Noticeable RTT, packet loss, or jitter; audio may occasionally break up. |
| **Network Quality** — Poor | Significant degradation detected; audio quality is likely impaired. |

## Tips

- If the indicator reaches **Poor**, check your local network for congestion or packet loss before attempting to retransmit.
- On WAN (SmartLink) connections, after five consecutive unanswered pings the radio link is automatically closed. AetherSDR will attempt to reconnect by refreshing your Auth0 credentials using the saved refresh token. If the credential refresh fails, reconnection stops and you will need to sign in again.
- You do not need to manually disconnect a stale WAN session — the ping watchdog handles teardown once and cleans up panadapters, slices, and streams automatically.

## Related

- [Connect to a radio over WAN (SmartLink)](connect-smartlink.md)
- [Troubleshoot audio quality](troubleshoot-audio.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
