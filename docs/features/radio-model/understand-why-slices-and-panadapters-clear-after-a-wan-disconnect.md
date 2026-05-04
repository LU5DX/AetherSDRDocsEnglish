# Understand why slices and panadapters clear after a WAN disconnect

When a WAN (SmartLink) connection drops, AetherSDR deliberately clears all panadapters, slices, and streams as part of a controlled teardown sequence — not as data loss. The Network Quality Monitor detects the outage, forces a disconnect, and then triggers reconnection automatically.

## Before you start

- You must be connected to a radio over a WAN (SmartLink) connection to observe this behavior.
- Confirm that the **Network Quality** indicator is visible in the main window.

## Steps

1. Watch the **Network Quality** indicator during a WAN connection. If the indicator reaches **Poor** and the radio stops responding to pings, the watchdog fires after five consecutive unanswered pings and calls `forceDisconnect()`.
2. When `forceDisconnect()` runs, it closes the TLS socket and routes through the normal `onDisconnected()` cleanup path — the same path used for a voluntary disconnect. This is why panadapters, slices, and streams are cleared: the cleanup is intentional and complete, not a crash or data corruption.
3. After the cleanup, MainWindow starts a WAN reconnect timer. It fetches fresh Auth0 credentials using the saved refresh token and re-establishes the radio link. When reconnection succeeds, panadapters and slices are rebuilt from the radio's current state.
4. If the auth-refresh fails (for example, the refresh token has expired), the retry loop stops and the status changes to sign-in required. In that case, sign in again manually to restore the connection.

## What each control does

| Control | Behavior |
|---|---|
| **Network Quality** | Displays real-time connection health based on ping round-trip time, packet-loss percentage, and audio jitter. **Off** means not connected. **Excellent** through **Poor** reflect increasing degradation — **Poor** means audio quality is likely affected. |

## Tips

- A single outage fires the ping watchdog exactly once, so you will not see repeated teardown attempts for the same drop. If reconnection fails at the auth step, check that your Auth0 session is still valid before assuming a radio or network fault.
- Panadapters and slices reappear automatically after a successful reconnect — you do not need to recreate them manually.

## Related

- [Network Quality Monitor](network-quality-monitor.md)
- [WAN (SmartLink) connection setup](wan-smartlink-setup.md)
- [Auth0 credential refresh](auth0-credential-refresh.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
