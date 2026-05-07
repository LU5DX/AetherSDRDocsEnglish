# Diagnose connection quality with ping RTT and packet-loss indicators

The Network Quality Monitor tracks your connection health in real time using ping round-trip time, packet-loss percentage, and audio jitter. It assigns one of six quality levels and automatically disconnects a stale connection after five consecutive unanswered pings.

## Steps

1. Connect to a radio (local or WAN/SmartLink). The **Network Quality** indicator appears in the main window status area and updates continuously.
2. Read the current quality level from the **Network Quality** indicator. If the level shows **Poor**, audio quality is likely degraded — check your network path or switch to a lower-bandwidth mode. If the indicator shows **Off**, no connection is active.

> **Note:** If five consecutive pings go unanswered, the software forces a disconnect automatically. On WAN (SmartLink) connections, MainWindow then attempts to refresh your Auth0 credentials and re-establish the link. If the credential refresh fails, the retry loop stops and you are prompted to sign in again.

## What each control does

| Control | Behavior |
|---|---|
| **Network Quality** | Displays one of six states — **Off**, **Excellent**, **Very Good**, **Good**, **Fair**, or **Poor** — based on real-time measurement of ping RTT, packet-loss percentage, and audio jitter. **Off** means no active connection. **Poor** means audio quality is likely degraded. The watchdog fires once per outage (not once per second) to avoid duplicate disconnects. |

## Tips

- If you see **Poor** intermittently, note whether it coincides with audio dropouts. Persistent **Poor** or repeated forced disconnects point to packet loss on the network path rather than a radio issue.
- On WAN connections, a forced disconnect triggers automatic credential refresh and reconnect. If reconnect fails repeatedly, select **Sign In** when prompted to re-enter your credentials.
- **Fair** or worse on a local network connection may indicate Wi-Fi interference; try a wired connection.

## Related

- [Connect via SmartLink (WAN)](connect-smartlink.md)
- [Audio troubleshooting](audio-troubleshooting.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
