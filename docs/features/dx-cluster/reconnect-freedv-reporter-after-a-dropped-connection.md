# Reconnect FreeDV reporter after a dropped connection

The FreeDV tab in SpotHub connects to the qso.freedv.org WebSocket feed. If the connection drops unexpectedly, the client retries automatically using exponential backoff; you only need to act if you stopped it manually or want to force an immediate reconnect.

## Before you start

- Open SpotHub: **Settings > SpotHub...**
- Select the **FreeDV** tab.

## Steps

1. Check the status indicator below the **FreeDV** tab label. If it shows **Disconnected**, the auto-reconnect cycle has stopped (either you pressed **Stop** earlier, or all retries were exhausted).
2. Press **Start / Stop (FreeDV)** to initiate a new connection. The status changes to **Connecting...** while the handshake is in progress, then to **Connected** on success.

> **Auto-reconnect:** After any unexpected drop, the client automatically retries without user input. The status shows **Connecting...** during each attempt. Auto-reconnect stops only when you press **Stop** explicitly. If you need reconnection to happen on every launch without manual intervention, enable **Auto-Start: ON / OFF (FreeDV)**.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| **Start / Stop (FreeDV)** | Connects or disconnects the FreeDV WebSocket. During an unexpected drop, the client auto-reconnects with exponential backoff and the status shows **Connecting...** during each attempt. If reporting is active and credentials need refreshing (e.g. after a RADE mode toggle), the client transparently reconnects with updated credentials. |  |
| **Auto-Start: ON / OFF (FreeDV)** | When ON, automatically establishes the FreeDV WebSocket connection each time AetherSDR launches. Default: OFF. |  |
| **Status indicator** | Shows the current state: **Disconnected**, **Connecting...**, or **Connected**. Displays **Connecting...** during both the initial connect and every auto-reconnect attempt after an unexpected drop. |  |
| **FreeDV Spots** | Read-only console showing incoming FreeDV activity. Populates once the connection is established. |  |
## Tips

- If the status stays on **Connecting...** for an extended period, press **Start / Stop (FreeDV)** once to stop, then press it again to force a clean reconnect attempt.
- To avoid manual reconnects entirely, enable **Auto-Start: ON / OFF (FreeDV)**. The connection will be restored automatically on the next launch even if it was dropped in a previous session.
- If you have **Enable FreeDV Reporter reporting when RADE is active** checked, verify that **Callsign: (FreeDV Reporter)** and **Grid Square: (FreeDV Reporter)** are filled in — the reporter refuses to activate without both values, which can cause the session to appear connected but not reporting.

## Related

- [spothub-freedv-reporter-reporting.md](spothub-freedv-reporter-reporting.md)
- [spothub-overview.md](spothub-overview.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
