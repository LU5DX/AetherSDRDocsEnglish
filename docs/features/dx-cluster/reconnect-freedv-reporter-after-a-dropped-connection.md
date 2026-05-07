# Reconnect FreeDV reporter after a dropped connection

The FreeDV tab in SpotHub connects to the public `qso.freedv.org` WebSocket feed. If the connection drops unexpectedly, the client automatically attempts to reconnect using exponential backoff and shows **Connecting...** in the status indicator during each attempt. You only need to act if you intentionally stopped the connection and want to restart it.

## Before you start

- Open SpotHub: **Settings > SpotHub...**
- Select the **FreeDV** tab.
- If you plan to report your station, ensure **Callsign: (FreeDV Reporter)** and **Grid Square: (FreeDV Reporter)** are filled in before connecting.

## Steps

1. Check the status indicator next to **Start / Stop (FreeDV)**. If it shows **Connecting...**, the client is already attempting to reconnect — no action is needed. Wait for it to reach **Connected**.
2. If the status shows **Disconnected** (meaning you previously pressed **Stop**), press **Start / Stop (FreeDV)** to reconnect. The status will move to **Connecting...** and then **Connected** once the WebSocket is established.

> **To prevent future manual restarts**, toggle **Auto-Start: ON / OFF (FreeDV)** to **ON**. The connection will be established automatically each time AetherSDR launches.

## What each control does

| Control | Behavior |
|---|---|
| **Start / Stop (FreeDV)** | Connects or disconnects the FreeDV WebSocket. After an unexpected drop the client auto-reconnects with exponential backoff; status shows **Connecting...** during each attempt. Auto-reconnect stops only when you press **Stop**. |
| **Auto-Start: ON / OFF (FreeDV)** | When **ON**, starts the FreeDV WebSocket connection automatically on launch. Default: **OFF**. |
| **FreeDV Spots** | Read-only console showing incoming FreeDV activity. |
| **Spot Color: (FreeDV)** | Opens a color picker for FreeDV spot labels on the panadapter. Default: dark orange (`#FF8C00`). |
| **Enable FreeDV Reporter reporting when RADE is active** | Broadcasts your station to the public FreeDV Reporter map when RADE mode is active. Requires **Callsign:** and **Grid Square:** to be set. |
| **Callsign: (FreeDV Reporter)** | Your callsign sent to FreeDV Reporter. Read-only when **Use radio (callsign)** is checked. |
| **Use radio (callsign)** | Populates the callsign field automatically from the connected radio. |
| **Grid Square: (FreeDV Reporter)** | Your Maidenhead grid square sent to FreeDV Reporter (up to 6 characters). Read-only when **Use GPS (grid)** is checked. |
| **Use GPS (grid)** | Populates the grid square from the radio's GPS hardware. Only shown on radios with GPS hardware (e.g. FLEX-8000 class, Aurora). |
| **Station Msg: (FreeDV Reporter)** | Optional free-text message shown next to your station on the FreeDV Reporter map. |

## Tips

- If the status stays on **Connecting...** for an extended time, check your network connection and confirm `qso.freedv.org` is reachable. Press **Stop** and then **Start** to force a fresh attempt.
- If you toggle RADE mode while reporting is active, the client transparently reconnects with updated credentials — you do not need to manually restart the connection.
- The FreeDV tab requires a build with WebSocket support (`HAVE_WEBSOCKETS`). If the tab is absent, your build does not include this feature.

## Related

- [spothub-overview.md](spothub-overview.md)
- [configure-freedv-reporter-reporting.md](configure-freedv-reporter-reporting.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
