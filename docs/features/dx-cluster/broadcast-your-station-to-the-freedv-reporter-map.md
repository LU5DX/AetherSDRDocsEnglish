# Broadcast your station to the FreeDV Reporter map

When RADE mode is active, AetherSDR can send your callsign, grid square, and an optional message to the public FreeDV Reporter map so other operators can see your station.

## Before you start

- RADE mode must be available and active on your radio.
- You need a valid callsign and Maidenhead grid square. The reporter rejects submissions with either field empty.
- The FreeDV tab requires WebSocket support compiled into your build (`HAVE_WEBSOCKETS`).

## Steps

1. Open **Settings > SpotHub...** and select the **FreeDV** tab.
2. If you want to receive FreeDV spots as well, click **Start** to connect the WebSocket to `qso.freedv.org`. The status indicator changes from `Disconnected` to `Connected`.
3. In the **Callsign:** field, enter your callsign. To pull it from the connected radio automatically, check **Use radio (callsign)** — the field becomes read-only.
4. In the **Grid Square:** field, enter your Maidenhead grid square (up to 6 characters). On radios with GPS hardware (e.g. FLEX-8000 class, Aurora), check **Use GPS (grid)** instead — the field becomes read-only.
5. Optionally, type a short note in **Station Msg:** to display next to your station on the map.
6. Check **Enable FreeDV Reporter reporting when RADE is active**. AetherSDR immediately begins broadcasting your station to the FreeDV Reporter map whenever RADE mode is running.
7. To connect automatically on every launch, toggle **Auto-Start: ON / OFF** to `ON`.

## What each control does

| Control | Behavior |
|---|---|
| **Start / Stop** | Connects or disconnects the FreeDV WebSocket. After an unexpected drop, the client auto-reconnects with exponential backoff; the status shows `Connecting...` during each attempt. Auto-reconnect stops only when you press Stop. |
| **Auto-Start: ON / OFF** | When set to ON, automatically connects the FreeDV WebSocket when AetherSDR launches. |
| **Enable FreeDV Reporter reporting when RADE is active** | Broadcasts your station to the public FreeDV Reporter map whenever RADE mode is active. Requires a callsign and grid square. Refuses to enable if either field is empty. |
| **Callsign:** | Your callsign sent to FreeDV Reporter. Read-only when **Use radio (callsign)** is checked. |
| **Use radio (callsign)** | Populates the callsign field automatically from the connected radio. |
| **Grid Square:** | Your Maidenhead grid square sent to FreeDV Reporter (up to 6 characters). Read-only when **Use GPS (grid)** is checked. |
| **Use GPS (grid)** | Populates the grid square from the radio's GPS hardware automatically. Only shown on radios with GPS hardware. |
| **Station Msg:** | Optional free-text message displayed next to your station on the FreeDV Reporter map. |
| **Spot Color:** | Opens a color picker for FreeDV spot labels on the panadapter. Default color is dark orange (`#FF8C00`). |
| **FreeDV Spots** | Read-only console showing incoming FreeDV activity. |

## Tips

- If you toggle RADE mode while reporting is active, the client transparently reconnects with updated credentials — you do not need to stop and restart manually.
- Leave **Station Msg:** blank if you have nothing to communicate; the field is optional.
- Use **Auto-Start: ON / OFF** together with **Enable FreeDV Reporter reporting when RADE is active** so your station appears on the map immediately each time you launch without any manual steps.

## Related

- [spot-hub-overview.md](spot-hub-overview.md)
- [freedv-spots.md](freedv-spots.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
